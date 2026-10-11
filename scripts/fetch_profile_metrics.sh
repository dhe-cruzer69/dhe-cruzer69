#!/usr/bin/env bash
#
# Fetch live GitHub repository metrics for the X4 profile.
# Requirements: GitHub CLI (gh), jq, and an authenticated gh session.
# Usage: bash scripts/fetch_profile_metrics.sh
#
set -euo pipefail

OWNER="dhe-cruzer69"
REPOS=(
  "x4-core"
  "x4-agents"
  "x4-sandbox"
  "x4-router"
  "x4-mcp"
)

for command in gh jq; do
  if ! command -v "$command" >/dev/null 2>&1; then
    printf 'ERROR: required command not found: %s\n' "$command" >&2
    exit 2
  fi
done

gh auth status >/dev/null

printf '==============================================\n'
printf 'X4 Profile Repository Metrics\n'
printf 'Generated: %s\n' "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
printf '==============================================\n\n'

for REPO in "${REPOS[@]}"; do
  FULL="$OWNER/$REPO"
  printf '→ %s\n' "$FULL"

  if ! REPO_JSON="$(gh api "repos/$FULL" 2>/dev/null)"; then
    printf '  ERROR        : repository unavailable or access denied\n\n'
    continue
  fi

  DEFAULT_BRANCH="$(jq -r '.default_branch // empty' <<<"$REPO_JSON")"
  STARS="$(jq -r '.stargazers_count // 0' <<<"$REPO_JSON")"

  LATEST_RELEASE="none"
  if RELEASE_JSON="$(gh api "repos/$FULL/releases/latest" 2>/dev/null)"; then
    LATEST_RELEASE="$(jq -r '.tag_name // "none"' <<<"$RELEASE_JSON")"
  fi

  OPEN_PRS="$(gh api search/issues -f "q=repo:$FULL is:pr is:open" --jq '.total_count // 0' 2>/dev/null || printf 'unknown')"

  CI_STATUS="unknown"
  if [[ -n "$DEFAULT_BRANCH" ]]; then
    if RUNS_JSON="$(gh api "repos/$FULL/actions/runs" -f "branch=$DEFAULT_BRANCH" -F per_page=1 2>/dev/null)"; then
      CI_STATUS="$(jq -r '
        if (.workflow_runs | length) == 0 then "no-runs"
        else (.workflow_runs[0].conclusion // .workflow_runs[0].status // "unknown")
        end
      ' <<<"$RUNS_JSON")"
    fi
  fi

  printf '  Default branch: %s\n' "${DEFAULT_BRANCH:-unknown}"
  printf '  Latest release : %s\n' "$LATEST_RELEASE"
  printf '  Open PRs       : %s\n' "$OPEN_PRS"
  printf '  Latest CI      : %s\n' "$CI_STATUS"
  printf '  Stars          : %s\n' "$STARS"
  printf '\n'
done

printf '==============================================\n'
printf 'Done (values are live API observations, not health guarantees).\n'
printf '==============================================\n'
