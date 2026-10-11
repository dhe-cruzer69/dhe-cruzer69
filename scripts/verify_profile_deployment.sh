#!/usr/bin/env bash
# Verifies the profile pipeline, default-branch CI, stable release, and production endpoints.
set -euo pipefail

PROFILE_REPO="${PROFILE_REPO:-dhe-cruzer69/dhe-cruzer69}"
X4_CORE_REPO="${X4_CORE_REPO:-dhe-cruzer69/x4-core}"
X4_SANDBOX_REPO="${X4_SANDBOX_REPO:-dhe-cruzer69/x4-sandbox}"
RELEASE_TAG="${X4_RELEASE_TAG:-v0.3.0}"
PRODUCTION_URL="${X4_PRODUCTION_URL:-}"
FAILURES=0

check() {
  local name="$1"; shift
  printf '\n==> %s\n' "$name"
  if "$@"; then
    printf 'PASS: %s\n' "$name"
  else
    printf 'FAIL: %s\n' "$name"
    FAILURES=$((FAILURES + 1))
  fi
}

check_profile_public() {
  gh repo view "$PROFILE_REPO" --json visibility,url \
    --jq '.visibility == "PUBLIC" and (.url | startswith("https://github.com/"))' | grep -qx true
}
check_profile_workflow_exists() {
  gh workflow view update-profile.yml --repo "$PROFILE_REPO" >/dev/null
}
check_latest_profile_run() {
  gh run list --repo "$PROFILE_REPO" --workflow update-profile.yml --branch main --limit 1 \
    --json status,conclusion --jq '.[0] | .status == "completed" and .conclusion == "success"' | grep -qx true
}
check_repo_ci() {
  local repo="$1" default_branch
  default_branch="$(gh repo view "$repo" --json defaultBranchRef --jq '.defaultBranchRef.name')"
  [[ -n "$default_branch" ]] || return 1
  gh run list --repo "$repo" --workflow ci.yml --branch "$default_branch" --limit 1 \
    --json status,conclusion --jq '.[0] | .status == "completed" and .conclusion == "success"' | grep -qx true
}
check_stable_latest_release() {
  gh release view "$RELEASE_TAG" --repo "$X4_SANDBOX_REPO" \
    --json tagName,isDraft,isPrerelease,isLatest \
    --jq --arg tag "$RELEASE_TAG" '.tagName == $tag and (.isDraft | not) and (.isPrerelease | not) and .isLatest' | grep -qx true
}
check_http_200() {
  local path="$1"
  [[ -n "$PRODUCTION_URL" ]] || return 1
  curl --fail --silent --show-error --max-time 10 -o /dev/null -w '%{http_code}' \
    "${PRODUCTION_URL%/}$path" | grep -qx 200
}
check_ready_payload() {
  [[ -n "$PRODUCTION_URL" ]] || return 1
  local body
  body="$(curl --fail --silent --show-error --max-time 10 "${PRODUCTION_URL%/}/healthz/ready")" || return 1
  printf '%s' "$body" | jq -e '.status == "ready" and (.version | type == "string" and length > 0)' >/dev/null
}
check_metrics_payload() {
  [[ -n "$PRODUCTION_URL" ]] || return 1
  local body
  body="$(curl --fail --silent --show-error --max-time 10 "${PRODUCTION_URL%/}/metrics")" || return 1
  grep -qE '^# (HELP|TYPE) ' <<< "$body"
}
check_https_headers() {
  [[ -n "$PRODUCTION_URL" && "$PRODUCTION_URL" == https://* ]] || return 1
  curl --fail --silent --show-error --max-time 10 -I "${PRODUCTION_URL%/}/" >/dev/null
}

echo "X4 profile/deployment verification"
check "GitHub authentication" gh auth status
check "Profile repository is public" check_profile_public
check "Profile workflow exists" check_profile_workflow_exists
check "Latest profile workflow on main succeeded" check_latest_profile_run
check "Latest x4-core default-branch CI succeeded" check_repo_ci "$X4_CORE_REPO"
check "Latest x4-sandbox default-branch CI succeeded" check_repo_ci "$X4_SANDBOX_REPO"
check "Requested release is published, stable, and latest" check_stable_latest_release
check "Production live endpoint returns HTTP 200" check_http_200 "/healthz/live"
check "Production ready endpoint returns ready JSON" check_ready_payload
check "Production metrics endpoint returns Prometheus text" check_metrics_payload
check "Production HTTPS endpoint responds" check_https_headers

printf '\n==================================\nVerification failures: %s\n' "$FAILURES"
if (( FAILURES == 0 )); then
  echo "VERDICT: ALL CHECKS PASSED"
  exit 0
fi
echo "VERDICT: DEPLOYMENT NOT VERIFIED"
exit 1
