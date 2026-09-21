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

\* **Edge0** is used here as the local/edge runtime concept, not as an external repository claim.

### Agent Engineering Layer

**Model → Agent → Tools/MCP → Policy → Evaluation → Routing → Observability → Workflow**

MCP provides a standardized interface for tools and context. Security (authentication, authorization, approval, sandboxing, rate limits, auditing) is enforced by the surrounding system.

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

**Key principle:** Never equate execution with success.

```
INTENT → PLAN → EXECUTE → OBSERVE → VERIFY → EVIDENCE → SUCCESS

If verification fails → FAIL → DIAGNOSE → RECOVER → RETRY → VERIFY AGAIN
If confidence cannot be established → UNKNOWN → HUMAN REVIEW REQUIRED
```

## Capability Repos (2026-09-21)

| Project | Capability | Description |
|---|---|---|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Full stack (v0.1.1) | Local-first provider-agnostic agent runtime — MCP, policy, routing, audit |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | #2 Verification (v0.1.1) | Evidence ledger — OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED / UNKNOWN |
| [**x4-orchestrator**](https://github.com/dhe-cruzer69/x4-orchestrator) | #5 Orchestration (v0.1.1) | Multi-agent coordinator that validates specialist outputs |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | #7 Human control (v0.1.1) | Risk-based approval gates and autonomy controls |
| [**x4-router-score**](https://github.com/dhe-cruzer69/x4-router-score) | #6 Routing (v0.1.1) | Capability / cost / latency / reliability scoring router |

These implement the engineering needed for dependable autonomy beyond “agents + MCP”.

## X4 Infrastructure

| Project | Role |
|---|---|
| **RepoDoc** | Repository health, security, CI, secrets, links, workflow auditing |
| [**AgentTest**](https://github.com/dhe-cruzer69/x4-eval) | Reproducible AI-agent evaluation and regression testing |
| [**MCPSafe**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Policy-controlled MCP/tool security gateway |
| [**ModelRoute**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic model selection, routing, fallback |
| [**FleetView**](https://github.com/dhe-cruzer69/x4-health) | Agent, model, tool, policy, runtime observability |

> **Five questions:** Is the repository healthy? Does the agent work? Is the action allowed? Which model should run it? What is the fleet doing?

## Core X4 Projects

| Project | Description |
|---|---|
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration runtime |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives |
| [**x4-ai**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic AI layer |
| [**x4-memory**](https://github.com/dhe-cruzer69/x4-memory) | Local-first persistent agent memory |
| [**x4-sandbox**](https://github.com/dhe-cruzer69/x4-sandbox) | Sandboxed tool execution |
| [**x4-mcp-gateway**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Policy-controlled MCP gateway |
| [**x4-research**](https://github.com/dhe-cruzer69/x4-research) | Evidence-first research engine |

## Provider & Agent Ecosystem

- [**OpenRouter**](https://github.com/OpenRouterTeam) — unified model access and routing
- [**Arcade**](https://github.com/ArcadeAI) — agent tools and MCP infrastructure
- [**NVIDIA Skills**](https://github.com/NVIDIA/skills) — verified agent skills
- [**OpenAI**](https://github.com/openai) — official SDKs and agent surfaces
- [**GitHub**](https://github.com/github) — source control, CI/CD, developer automation
- **BEAST MODE** — fast execution backed by tests, security checks, evidence, and verification

*These are ecosystem references only; no affiliation or endorsement is claimed.*

## BEAST MODE

**Build → Validate → Verify → Record → Release**

Fast execution without bypassing safety gates. Changes are evidence-backed. Secrets stay out of repositories. Unresolved evidence remains `UNKNOWN`.

## Portfolio Reconciliation — 2026-09-21

| Metric | Value |
|---|---:|
| Canonical contract | 69 |
| Physical `x4-*` inventory | 76 |
| Net delta | +7 |
| Missing canonical targets | 4 (`x4-storage`, `x4-fs`, `x4-archive`, `x4-knowledge`) |

Discrepancy is kept explicit. Identity mapping is never silently collapsed.

### Gate status

| Gate | Status |
|---|---|
| Branch protection | **BLOCKED — ACCESS REQUIRED** |
| Vercel | **BLOCKED — VERCEL ACCESS REQUIRED** |
| Fleet gate | **OPEN — EVIDENCE REQUIRED** |
| Repository evidence | **DOCUMENTED** |
| Dependency PRs | **CLOSED / MERGED** |

### Evidence policy

`OBSERVED` → `CORRELATED` → `HYPOTHESIS` → `VALIDATED`  
`UNKNOWN — HUMAN REVIEW REQUIRED`

No repository is marked production-validated merely because it exists or has a README.

## Engineering Principles

- Security by default • Least-privilege tool access
- Explicit approval for high-risk actions
- Local-first where practical • Provider-agnostic
- Observable and auditable execution
- Evidence over marketing claims
- `UNKNOWN` stays `UNKNOWN` until validated
- No fake PASS/LIVE status • No secrets in repositories
- Upstream contribution over cosmetic forks

## Quality Gate

A repository is ready only after relevant checks actually pass:

- package installation • unit/integration tests • type/lint
- secret & dependency scanning • workflow permissions
- documentation & link checks • clean-machine quick start
- release build verification

No command is reported as **PASS** unless it actually passed.

## Origin & Lineage

- [**ariexus**](https://github.com/dhe-cruzer69/ariexus) — technical ancestor
- [**omniforge**](https://github.com/dhe-cruzer69/omniforge) — local-first inspiration

## Roadmap

**Local AI → Agents → Evaluation → MCP/Tool Security → Routing → Observability → Products**

---

*Building in public. Contributing upstream. Documenting the architecture. Verifying the work.*
