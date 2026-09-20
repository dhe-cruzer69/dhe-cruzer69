# ARIEX4Ops

**AI • Agents • Automation • Developer Infrastructure**

Building the **X4** open-source ecosystem: secure agent runtimes, provider-agnostic AI, local-first memory, policy-controlled MCP, sandboxed execution, evaluation, routing, and evidence-driven research.

## X4 Infrastructure

| Project | Role |
|---|---|
| **RepoDoc** | Repository health, security, CI, secrets, links, and workflow auditing |
| [**AgentTest**](https://github.com/dhe-cruzer69/x4-eval) | Reproducible AI-agent evaluation and regression testing |
| [**MCPSafe**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Policy-controlled MCP/tool security gateway with approval and audit |
| [**ModelRoute**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic model selection, routing, fallback, cost, and latency controls |
| [**FleetView**](https://github.com/dhe-cruzer69/x4-health) | Agent, model, tool, policy, and runtime observability |

> **Five questions:** Is the repository healthy? Does the agent work? Is the action allowed? Which model should run it? What is the fleet doing?

## Core X4 Projects

| Project | Description |
|---|---|
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration runtime |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives and infrastructure |
| [**x4-ai**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic AI layer and routing foundation |
| [**x4-memory**](https://github.com/dhe-cruzer69/x4-memory) | Local-first persistent agent memory |
| [**x4-sandbox**](https://github.com/dhe-cruzer69/x4-sandbox) | Sandboxed tool execution with policy and audit |
| [**x4-mcp-gateway**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Policy-controlled MCP gateway |
| [**x4-research**](https://github.com/dhe-cruzer69/x4-research) | Evidence-first research engine |

## Provider & Agent Ecosystem

- [**OpenRouter / @OpenRouterTeam**](https://github.com/OpenRouterTeam) — unified model access, provider routing, fallbacks, and official agent skills.
- [**Arcade / @ArcadeAI**](https://github.com/ArcadeAI) — agent tools, MCP servers, and tool-development infrastructure.
- [**NVIDIA Skills / @NVIDIA**](https://github.com/NVIDIA/skills) — NVIDIA-verified Agent Skills spanning CUDA, inference, robotics, simulation, RAG, and Physical AI.
- [**OpenAI / @openai**](https://github.com/openai) — official SDKs and agent/provider integration surfaces.
- [**GitHub / @github**](https://github.com/github) — source control, CI/CD, issues, pull requests, and developer automation.
- **Autopilot workflows** — controlled autonomous execution with explicit validation and human review gates.
- **BEAST MODE engineering** — fast execution backed by tests, security checks, evidence, rollback paths, and verification.

## BEAST MODE

**Build → Validate → Verify → Record → Release**

BEAST MODE is the X4 operating standard: fast execution without bypassing safety gates. Changes are evidence-backed, tests are real, secrets stay out of repositories, and unresolved evidence remains `UNKNOWN`.

## Portfolio Reconciliation — 2026-09-20

**Canonical contract:** 69 repositories  
**Physical `x4-*` inventory:** 71 repositories  
**Net reconciliation delta:** +2 physical repositories

### Exact reconciliation ledger

| State | Count | Evidence |
|---|---:|---|
| Canonical contract | 69 | X4 reconciliation manifest |
| Physical X4 repositories | 71 | Latest inventory evidence |
| Extra/unexpected | 6 | `x4-agents`, `x4-claw-`, `x4-core`, `x4-mcp`, `x4-mcp-gateway`, `x4-sandbox` |
| Missing canonical targets | 4 | `x4-storage`, `x4-fs`, `x4-archive`, `x4-knowledge` |
| Net difference | +2 | 71 − 69 |

The **71-vs-69 discrepancy is therefore reconciled arithmetically**: six physical extras and four missing canonical targets produce a net surplus of two. Repository identity mapping is kept explicit rather than silently treating differently named repositories as equivalent.

### Gate status

| Gate | Status | Closure rule |
|---|---|---|
| Branch protection | **BLOCKED — ACCESS REQUIRED** | GitHub integration receives HTTP 403 for the branch-protection endpoint; settings must be verified/changed by an authorized GitHub settings session |
| Vercel | **BLOCKED — VERCEL ACCESS REQUIRED** | Connected Vercel account exposes no teams/projects in this session; deployment cannot be verified or repaired here |
| Fleet gate | **OPEN — EVIDENCE REQUIRED** | No authoritative Fleet closure artifact is available in the connected repositories/tools; no false PASS claim |
| Repository evidence | **DOCUMENTED** | Reconciliation ledger and hardening evidence recorded |
| Dependency PRs | **CLOSED / MERGED** | `x4-agents#2` reviewed, hardened against false-green CI, and squash-merged |

### Evidence policy

`OBSERVED` → `CORRELATED` → `HYPOTHESIS` → `VALIDATED`

`UNKNOWN — HUMAN REVIEW REQUIRED`

No repository is marked production-validated merely because it exists, has a README, or has a merged pull request.

## Engineering Principles

- Security by default
- Least-privilege tool access
- Explicit approval for high-risk actions
- Local-first where practical
- Provider-agnostic architecture
- Observable and auditable execution
- Evidence over marketing claims
- `UNKNOWN` stays `UNKNOWN` until validated
- No fake PASS/LIVE status
- No secrets committed to repositories
- Upstream contribution over cosmetic forks

## Evidence Model

Every system should distinguish:

`OBSERVED` → `CORRELATED` → `HYPOTHESIS` → `VALIDATED`

and preserve:

`UNKNOWN — HUMAN REVIEW REQUIRED`

Machine-readable evidence, trace IDs, policy versions, hashes, timings, and structured findings are preferred over unsupported claims.

## Architecture

```text
                         A6X4 AI INFRASTRUCTURE
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
     RepoDoc                  AgentTest                 MCPSafe
  Repo integrity          Agent reliability          Tool security
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                             ModelRoute
                         Model optimization
                                  │
                                  ▼
                              FleetView
                           Fleet telemetry
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
        CodeReviewAI        AgentSkillHub          DevPulse
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                       ┌──────────┴──────────┐
                       │                     │
                    DataLens              PostFlow
```

## BEAST MODE Final Gate

The profile and X4 portfolio follow a conservative completion rule:

- **BUILD** — implementation exists
- **TEST** — automated tests/checks execute
- **SECURE** — secrets, dependencies, permissions, and tool boundaries are reviewed
- **VERIFY** — results are re-read from the authoritative source
- **EVIDENCE** — claims are tied to observable artifacts
- **ROLLBACK** — destructive or high-risk mutations require an explicit recovery path
- **UNKNOWN** — anything not verified remains explicitly unknown

No stars, adoption, revenue, trending position, performance multiplier, or launch outcome is represented as guaranteed. Those remain measurable outcomes or planning hypotheses until independently observed.

## Quality Gate

A repository is considered ready only after the relevant checks actually pass:

- package installation
- unit and integration tests
- type/lint checks
- secret and dependency scanning
- workflow permission review
- link/documentation checks
- clean-machine quick start
- release build verification
- checksums or signed artifacts where applicable

No command is reported as **PASS** unless it actually passed.

## Origin & Lineage

- [**ariexus**](https://github.com/dhe-cruzer69/ariexus) — technical ancestor of the X4 agent work
- [**omniforge**](https://github.com/dhe-cruzer69/omniforge) — local-first inspiration for AI and memory components

## Roadmap

**Foundation → Evaluation → Security → Routing → Observability → Products**

The five infrastructure primitives are the reusable layer. Product systems can then consume them for code review, skills, developer workflows, data exploration, and publishing automation.

---

*Building in public. Contributing upstream. Documenting the architecture. Verifying the work.*
