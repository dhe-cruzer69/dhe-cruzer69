# X4 Spec — Proposed Architecture Blueprint

> **Status: PROPOSED — the `dhe-cruzer69/x4-spec` repository was not found in the live GitHub inventory checked on 2026-10-18. This document is a blueprint, not a deployed workflow hub.**

## Unique architecture diagram

```mermaid
flowchart TB
    AUTHOR[Maintainer] --> SPEC[Workflow and Policy Specification]
    SPEC --> REVIEW[Human Review]
    REVIEW -->|approved| TAG[Versioned Immutable Tag]
    REVIEW -->|changes requested| EDIT[Revise and Re-review]
    EDIT --> REVIEW
    TAG --> PY[Reusable Python CI]
    TAG --> NODE[Reusable Node CI]
    TAG --> SECURITY[Security and Dependency Checks]
    TAG --> RELEASE[Release and Provenance Workflow]
    TAG --> DEPLOY[Deploy and Health-check Workflow]
    PY --> CONSUMERS[Consumer Repositories]
    NODE --> CONSUMERS
    SECURITY --> CONSUMERS
    RELEASE --> CONSUMERS
    DEPLOY --> CONSUMERS
    CONSUMERS --> EVIDENCE[Workflow Run and Artifact Evidence]
    EVIDENCE --> SCORE[Portfolio Evidence Scorecard]
    SCORE --> MAINTAINER[Maintainer Review]
    NOTE[No consumer should label itself APEX without real evidence] -. gate .-> SCORE
```

## Intended responsibilities

- Versioned reusable workflows for language-specific CI, security scanning, releases, and deployment.
- Explicit consumer inputs and least-privilege permissions.
- A human review gate before changing shared workflows used by multiple repositories.
- Evidence links to workflow runs, artifacts, and live health checks.
- A read-only fleet scorecard; no repository deletion or archival from scheduled automation.

## Bootstrap acceptance criteria

1. Repository exists and its default branch is known.
2. All workflow files parse and pass actionlint or equivalent validation.
3. Consumer test repositories exercise each reusable workflow.
4. Each consumer has a pinned version reference rather than an unreviewed mutable branch.
5. A tagged release has a successful consumer run and a rollback procedure.

No workflow, tag, release, or deployment is claimed to exist until those checks pass.
