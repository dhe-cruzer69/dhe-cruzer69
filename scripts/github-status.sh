#!/usr/bin/env bash
# Read-only GitHub account status. Requires gh, jq and curl.
set -euo pipefail

OWNER="${1:-dhe-cruzer69}"
command -v gh >/dev/null || { echo "ERROR: GitHub CLI (gh) is required." >&2; exit 127; }
command -v jq >/dev/null || { echo "ERROR: jq is required." >&2; exit 127; }

gh auth status >/dev/null
LOGIN="$(gh api user --jq '.login')"
if [[ "$LOGIN" != "$OWNER" ]]; then
  echo "ERROR: authenticated as '$LOGIN', expected '$OWNER'. No checks performed." >&2
  exit 2
fi

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

# --slurp groups all paginated API pages; filter owner explicitly.
gh api --paginate --slurp "/user/repos?per_page=100&affiliation=owner&visibility=all" > "$TMP"
jq -e 'type == "array"' "$TMP" >/dev/null
TOTAL="$(jq --arg owner "$OWNER" '[.[][] | select(.owner.login == $owner)] | length' "$TMP")"
PUBLIC="$(jq --arg owner "$OWNER" '[.[][] | select(.owner.login == $owner and .private == false)] | length' "$TMP")"
PRIVATE="$(jq --arg owner "$OWNER" '[.[][] | select(.owner.login == $owner and .private == true)] | length' "$TMP")"
ARCHIVED="$(jq --arg owner "$OWNER" '[.[][] | select(.owner.login == $owner and .archived == true)] | length' "$TMP")"
ACTIVE="$(jq --arg owner "$OWNER" '[.[][] | select(.owner.login == $owner and .archived == false)] | length' "$TMP")"

echo "GitHub status — $(date -u +%FT%TZ)"
echo "Authenticated user: $LOGIN"
echo "Owned repositories visible to this token: $TOTAL"
echo "  Public:   $PUBLIC"
echo "  Private:  $PRIVATE"
echo "  Archived: $ARCHIVED"
echo "  Active:   $ACTIVE"
echo
echo "Hub check:"
if gh api "repos/$OWNER/x4-spec" --jq '.full_name' >/dev/null 2>&1; then
  echo "  x4-spec: repository visible"
else
  echo "  x4-spec: NOT FOUND or not accessible to this token"
fi
if gh api "repos/$OWNER/x4-spec/contents/.github/workflows/reusable-python-ci.yml?ref=v1" >/dev/null 2>&1; then
  echo "  x4-spec reusable Python workflow at tag v1: resolvable"
else
  echo "  x4-spec reusable Python workflow at tag v1: NOT resolvable"
fi
echo
echo "Latest CI evidence (most recent run shown; this does not trigger workflows):"
for R in x4-core x4-beast x4-fleet x4-sandbox x4-agents x4-agent-skills-hub x4-ai-security-scanner x4-agent-observability; do
  if VALUE="$(gh run list -R "$OWNER/$R" --limit 1 --json conclusion,headBranch,createdAt,url --jq '.[0] // empty' 2>/dev/null)" && [[ -n "$VALUE" ]]; then
    printf '  %-28s %s
' "$R" "$(jq -r '[.conclusion // "in_progress", .headBranch // "unknown", .createdAt // "unknown", .url // "no-url"] | join(" | ")' <<< "$VALUE")"
  else
    printf '  %-28s %s
' "$R" "no visible workflow run or workflow unavailable"
  fi
done

echo
echo "Read-only script: no commits, repository settings, deployments, archives, or deletions performed."
