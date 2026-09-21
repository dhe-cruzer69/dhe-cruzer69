# ARIEX4Ops

**AI • Agents • Automation • Developer Infrastructure**

Building **local-first AI infrastructure and agent systems**: secure runtimes, tool-using agents, MCP integration, sandboxed execution, evaluation, model routing, observability, and evidence-driven automation.

## Architecture at a Glance

```text
LOCAL / EDGE AI
      │
   Edge0* / Ollama
      │
      ▼
   X4 AGENTS
      │
 ┌────┼───────────────┐
 ▼    ▼               ▼
Test MCP            Route
 │    │               │
 └────┼───────────────┘
      ▼
   FleetView
      │
      ▼
Agentic workflows + developer automation
```

\* **Edge0 is used here as the local/edge runtime concept, not as an external repository claim.**

### Agent Engineering Layer

The X4 architecture follows the same progression used in modern agent engineering:

**Model → Agent → Tools/MCP → Policy → Evaluation → Routing → Observability → Workflow**

MCP provides a standardized interface for exposing tools and context to AI applications. Security controls such as authentication, authorization, approval, sandboxing, rate limiting, and audit logging are enforced by the surrounding system rather than assumed to come from MCP alone.

## The 7-Capability Autonomous Agent Architecture

A stronger definition of a genuinely useful autonomous agent:

| # | Capability | Core mechanism | Success criterion |
|---|---|---|---|
| 1 | Reliable autonomous execution | Planner + executor + retry/recovery loop | Goal completed across multiple tools |
| 2 | Verification before success | Tests + output inspection + evidence ledger | No PASS without evidence |
| 3 | Secure tools & credentials | Sandbox + least privilege + secret isolation + policy gates | Unsafe actions blocked |
| 4 | Persistent context & memory | State store + project memory + task history | Agent resumes work correctly |
| 5 | Multi-agent orchestration | Delegation + specialist agents + coordinator | Complex tasks decomposed effectively |
| 6 | Intelligent routing | Capability/cost/latency/reliability router | Best available model/tool selected dynamically |
| 7 | Human-in-the-loop control | Approval gates + uncertainty states + escalation | High-impact actions require human approval |

**Key principle:** The system should never equate execution with success.

```
INTENT → PLAN → EXECUTE → OBSERVE → VERIFY → EVIDENCE → SUCCESS

If verification fails: FAIL → DIAGNOSE → RECOVER → RETRY → VERIFY AGAIN
If confidence cannot be established: UNKNOWN → HUMAN REVIEW REQUIRED
```

## New X4 Capability Repos (2026-09-21)

| Project | Capability | Description |
|---|---|---|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Full stack | Local-first provider-agnostic agent runtime with MCP, policy, routing, audit |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | #2 Verification | Evidence ledger — OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED / UNKNOWN |
| [**x4-orchestrator**](https://github.com/dhe-cruzer69/x4-orchestrator) | #5 Orchestration | Multi-agent coordinator that validates specialist outputs |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | #7 Human control | Risk-based approval gates and autonomy controls |
| [**x4-router-score**](https://github.com/dhe-cruzer69/x4-router-score) | #6 Routing | Capability / cost / latency / reliability scoring router |

These five repositories implement the missing engineering needed for dependable autonomy beyond “agents + MCP”.

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

- [**OpenRouter / @OpenRouterTeam**](https://github.com/OpenRouterTeam) — unified model access, provider routing, fallbacks, and model access, routing, and agent integrations.
- [**Arcade / @ArcadeAI**](https://github.com/ArcadeAI) — agent tools, MCP servers, and tool-development infrastructure.
- [**NVIDIA Skills / @NVIDIA**](https://github.com/NVIDIA/skills) — NVIDIA-verified Agent Skills spanning CUDA, inference, robotics, simulation, RAG, and Physical AI.
- [**OpenAI / @openai**](https://github.com/openai) — official SDKs and agent/provider integration surfaces.
- [**GitHub / @github**](https://github.com/github) — source control, CI/CD, issues, pull requests, and developer automation.
- **Autopilot workflows** — controlled autonomous execution with explicit validation and human review gates.
- **BEAST MODE engineering** — fast execution backed by tests, security checks, evidence, rollback paths, and verification.

These references are ecosystem/tooling references only; they do not imply affiliation, endorsement, sponsorship, or partnership.

## BEAST MODE

**Build → Validate → Verify → Record → Release**

BEAST MODE is the X4 operating standard: fast execution without bypassing safety gates. Changes are evidence-backed, tests are real, secrets stay out of repositories, and unresolved evidence remains `UNKNOWN`.

## Portfolio Reconciliation — 2026-09-21

**Canonical contract:** 69 repositories  
**Physical `x4-*` inventory:** 76 repositories (previous 71 + 5 new capability repos)  
**Net reconciliation delta:** +7 physical repositories

### Exact reconciliation ledger

| State | Count | Evidence |
|---|---:|---|
| Canonical contract | 69 | X4 reconciliation manifest |
| Physical X4 repositories | 76 | Latest inventory + 5 new capability repos |
| Extra/unexpected | 11 | previous extras + `x4-beast`, `x4-evidence`, `x4-orchestrator`, `x4-approval`, `x4-router-score` |
| Missing canonical targets | 4 | `x4-storage`, `x4-fs`, `x4-archive`, `x4-knowledge` |
| Net difference | +7 | 76 − 69 |

The discrepancy is kept explicit. Repository identity mapping is not silently collapsed.

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

**Local AI → Agents → Evaluation → MCP/Tool Security → Routing → Observability → Products**

The five infrastructure primitives are the reusable layer. Product systems can then consume them for code review, skills, developer workflows, data exploration, and publishing automation.

---

*Building in public. Contributing upstream. Documenting the architecture. Verifying the work.*
