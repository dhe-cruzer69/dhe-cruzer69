#!/usr/bin/env python3
"""Update explicitly marked profile sections from public GitHub data."""
from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from ipaddress import ip_address
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import requests

GITHUB_API = "https://api.github.com"
README_PATH = Path("README.md")
ACTIVITY_START = "<!--START_SECTION:activity-->"
ACTIVITY_END = "<!--END_SECTION:activity-->"
DATA_START = "<!-- X4_PROFILE_DATA_START -->"
DATA_END = "<!-- X4_PROFILE_DATA_END -->"
TIMEOUT_SECONDS = 15

class GitHubAPIError(RuntimeError):
    """Unexpected GitHub API response."""

def github_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "x4-profile-updater",
    }

def get_json(url: str, token: str, *, not_found_ok: bool = False) -> Any:
    response = requests.get(url, headers=github_headers(token), timeout=TIMEOUT_SECONDS)
    if response.status_code == 404 and not_found_ok:
        return None
    if response.status_code == 404:
        raise GitHubAPIError(f"GitHub resource not found: {url}")
    response.raise_for_status()
    try:
        return response.json()
    except ValueError as exc:
        raise GitHubAPIError(f"GitHub returned invalid JSON for {url}") from exc

def fetch_user(token: str, username: str) -> dict[str, Any]:
    user = get_json(f"{GITHUB_API}/users/{username}", token)
    if not isinstance(user, dict) or user.get("login", "").lower() != username.lower():
        raise GitHubAPIError(f"GitHub user identity mismatch for {username!r}")
    return user

def fetch_repositories(token: str, username: str) -> list[dict[str, Any]]:
    """Fetch all public repositories owned by the user; never silently cap pages."""
    repositories: list[dict[str, Any]] = []
    page = 1
    while True:
        batch = get_json(
            f"{GITHUB_API}/users/{username}/repos?type=owner&per_page=100&page={page}&sort=pushed",
            token,
        )
        if not isinstance(batch, list):
            raise GitHubAPIError("GitHub repositories response was not a list")
        repositories.extend(item for item in batch if isinstance(item, dict))
        if len(batch) < 100:
            return repositories
        page += 1

def fetch_repository(token: str, username: str, repository: str) -> dict[str, Any]:
    result = get_json(f"{GITHUB_API}/repos/{username}/{repository}", token)
    if not isinstance(result, dict):
        raise GitHubAPIError(f"Invalid repository metadata for {repository}")
    return result

def fetch_workflow_status(token: str, username: str, repository: str, workflow_file: str = "ci.yml") -> str:
    metadata = fetch_repository(token, username, repository)
    default_branch = metadata.get("default_branch")
    if not isinstance(default_branch, str) or not default_branch:
        return "unknown (default branch unavailable)"
    url = (
        f"{GITHUB_API}/repos/{username}/{repository}/actions/workflows/"
        f"{workflow_file}/runs?branch={default_branch}&per_page=1"
    )
    try:
        runs = get_json(url, token, not_found_ok=True)
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code in (403, 429):
            return "unknown (API access/rate limit)"
        raise
    if not runs:
        return "not configured"
    workflow_runs = runs.get("workflow_runs", []) if isinstance(runs, dict) else []
    if not workflow_runs:
        return "no runs"
    latest = workflow_runs[0]
    if latest.get("status") != "completed":
        return str(latest.get("status") or "unknown")
    return str(latest.get("conclusion") or "unknown")

def fetch_latest_release(token: str, username: str, repository: str) -> dict[str, Any] | None:
    result = get_json(
        f"{GITHUB_API}/repos/{username}/{repository}/releases/latest",
        token,
        not_found_ok=True,
    )
    return result if isinstance(result, dict) else None

def fetch_public_events(token: str, username: str) -> list[dict[str, Any]]:
    events = get_json(f"{GITHUB_API}/users/{username}/events/public?per_page=10", token)
    return events if isinstance(events, list) else []

def _event_summary(event: dict[str, Any]) -> str:
    repo = event.get("repo", {}).get("name", "")
    if not isinstance(repo, str) or not repo or "/" not in repo:
        return ""
    summaries = {
        "PushEvent": "pushed commits to",
        "PullRequestEvent": "updated a pull request in",
        "IssuesEvent": "updated an issue in",
        "IssueCommentEvent": "commented on an issue in",
        "CreateEvent": "created a branch, tag, or repository in",
        "ReleaseEvent": "published a release in",
        "PublicEvent": "made a repository public:",
        "WatchEvent": "starred",
        "ForkEvent": "forked",
    }
    verb = summaries.get(event.get("type", ""))
    if not verb:
        return ""
    safe_repo = repo.replace("|", r"\|").replace("[", r"\[").replace("]", r"\]")
    return f"- {verb} [{safe_repo}](https://github.com/{repo})"

def format_recent_activity(events: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for event in events:
        summary = _event_summary(event)
        if summary and summary not in lines:
            lines.append(summary)
        if len(lines) == 10:
            break
    return "\n".join(lines) if lines else "_No recent public activity available._"

def replace_marked_section(readme: str, start_marker: str, end_marker: str, content: str) -> str:
    if readme.count(start_marker) != 1 or readme.count(end_marker) != 1:
        raise RuntimeError(f"README must contain exactly one {start_marker} and {end_marker}")
    start = readme.index(start_marker)
    end_start = readme.index(end_marker)
    if end_start < start + len(start_marker):
        raise RuntimeError(f"README markers are out of order: {start_marker}")
    return readme[:start] + f"{start_marker}\n{content}\n{end_marker}" + readme[end_start + len(end_marker):]

def _production_url_is_safe(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        return False
    hostname = parsed.hostname.rstrip(".").lower()
    if hostname in {"localhost", "localhost.localdomain"} or "." not in hostname:
        return False
    try:
        address = ip_address(hostname)
        if address.is_private or address.is_loopback or address.is_link_local or address.is_reserved:
            return False
    except ValueError:
        pass
    return True

def check_production(url: str) -> tuple[str, str]:
    if not url:
        return "Not configured", ""
    if not _production_url_is_safe(url):
        return "Invalid URL configuration", ""
    try:
        response = requests.get(
            f"{url.rstrip('/')}/healthz/ready",
            timeout=TIMEOUT_SECONDS,
            allow_redirects=False,
        )
        if response.status_code != 200:
            return f"Unhealthy (HTTP {response.status_code})", ""
        body = response.json()
        if not isinstance(body, dict) or body.get("status") != "ready":
            return "Unhealthy (invalid readiness response)", ""
        version = str(body.get("version", "")).strip()
        return ("Live and ready", version) if version else ("Unhealthy (version missing)", "")
    except (requests.RequestException, ValueError):
        return "Unreachable or invalid response", ""

def format_number(value: Any) -> str:
    return f"{value:,}" if isinstance(value, int) and value >= 0 else "unknown"

def build_profile_section(token: str, username: str, user: dict[str, Any], repositories: list[dict[str, Any]], production_url: str) -> str:
    owned_originals = [
        repo for repo in repositories
        if not repo.get("fork", False)
        and repo.get("owner", {}).get("login", "").lower() == username.lower()
    ]
    x4_repos = [repo for repo in owned_originals if repo.get("name", "").startswith("x4-")]
    active_x4 = [repo for repo in x4_repos if not repo.get("archived", False)]
    stars = sum(int(repo.get("stargazers_count", 0) or 0) for repo in owned_originals)
    forks = sum(int(repo.get("forks_count", 0) or 0) for repo in owned_originals)
    core_ci = fetch_workflow_status(token, username, "x4-core")
    sandbox_ci = fetch_workflow_status(token, username, "x4-sandbox")
    release = fetch_latest_release(token, username, "x4-sandbox")
    release_tag = str(release.get("tag_name", "unknown")) if release else "No published release"
    release_url = str(release.get("html_url", "")) if release else ""
    release_display = f"[{release_tag}]({release_url})" if release_url.startswith("https://github.com/") else release_tag
    production_status, production_version = check_production(production_url)
    production_detail = production_status + (f" — version {production_version}" if production_version else "")
    production_url_display = production_url if production_status != "Invalid URL configuration" else "Invalid URL configuration"
    refreshed = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""## Real-Time X4 Portfolio

| Metric | Current Value |
|---|---:|
| Public repositories reported by GitHub | {format_number(user.get("public_repos"))} |
| Original public repositories in fetched inventory | {format_number(len(owned_originals))} |
| X4 repositories | {format_number(len(x4_repos))} |
| Active X4 repositories | {format_number(len(active_x4))} |
| Stars across original public repositories | {format_number(stars)} |
| Forks across original public repositories | {format_number(forks)} |
| Followers | {format_number(user.get("followers"))} |

## X4 CI and Release Evidence

| Project | Default-branch CI | Latest stable release |
|---|---|---|
| [x4-core](https://github.com/{username}/x4-core) | {core_ci} | — |
| [x4-sandbox](https://github.com/{username}/x4-sandbox) | {sandbox_ci} | {release_display} |

## Production Readiness

- Status: {production_detail}
- Configured URL: {production_url_display or "Not configured"}
- Checked endpoint: {production_url.rstrip("/") + "/healthz/ready" if production_url and production_status != "Invalid URL configuration" else "Not checked"}
- Refreshed: {refreshed}

_These values reflect public GitHub API responses and one readiness probe; they do not prove security isolation or validate every production subsystem._"""

def main() -> int:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    username = os.getenv("GITHUB_USERNAME", "dhe-cruzer69").strip()
    production_url = os.getenv("X4_PRODUCTION_URL", "").strip()
    if not token:
        print("ERROR: GITHUB_TOKEN is required.", file=sys.stderr)
        return 2
    if not username or any(ch.isspace() for ch in username):
        print("ERROR: GITHUB_USERNAME is invalid.", file=sys.stderr)
        return 2
    if not README_PATH.is_file():
        print("ERROR: README.md not found.", file=sys.stderr)
        return 2
    try:
        user = fetch_user(token, username)
        repositories = fetch_repositories(token, username)
        events = fetch_public_events(token, username)
        section = build_profile_section(token, username, user, repositories, production_url)
        original = README_PATH.read_text(encoding="utf-8")
        updated = replace_marked_section(original, ACTIVITY_START, ACTIVITY_END, format_recent_activity(events))
        updated = replace_marked_section(updated, DATA_START, DATA_END, section)
        if updated == original:
            print("No profile changes required.")
            return 0
        README_PATH.write_text(updated, encoding="utf-8")
        print("README updated with public GitHub metrics and activity.")
        if production_url:
            status, version = check_production(production_url)
            print(f"Production readiness: {status}" + (f" (version {version})" if version else ""))
        else:
            print("Production readiness: not checked (X4_PRODUCTION_URL is not configured).")
        return 0
    except (GitHubAPIError, requests.RequestException, RuntimeError, OSError) as exc:
        print(f"ERROR: profile update failed: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
