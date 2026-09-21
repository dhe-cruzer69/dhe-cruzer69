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

\* **Edge0** is the local/edge runtime *concept* used in this portfolio — not an external repository claim.

### Agent Engineering Progression

**Model → Agent → Tools/MCP → Policy → Evaluation → Routing → Observability → Workflow**

MCP standardizes tool and context interfaces. Authentication, authorization, approval, sandboxing, rate limits, and auditing are enforced by the surrounding system.

## 7-Capability Autonomous Agent Architecture

| # | Capability | Core mechanism | Success criterion |
|---|---|---|---|
| 1 | Reliable autonomous execution | Planner + executor + retry/recovery | Goal completed across tools |
| 2 | Verification before success | Tests + inspection + evidence ledger | No PASS without evidence |
| 3 | Secure tools & credentials | Sandbox + least privilege + policy gates | Unsafe actions blocked |
| 4 | Persistent context & memory | State store + project memory + history | Correct resume of work |
| 5 | Multi-agent orchestration | Delegation + specialists + coordinator | Effective decomposition |
| 6 | Intelligent routing | Capability / cost / latency / reliability | Best option selected dynamically |
| 7 | Human-in-the-loop control | Approval gates + uncertainty + escalation | High-impact actions gated |

**Key principle:** Never equate execution with success.

```
INTENT → PLAN → EXECUTE → OBSERVE → VERIFY → EVIDENCE → SUCCESS

FAIL → DIAGNOSE → RECOVER → RETRY → VERIFY AGAIN
UNKNOWN → HUMAN REVIEW REQUIRED
```

## Capability Repos

| Project | Maps to | Description |
|---|---|---|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Full stack | Local-first provider-agnostic runtime (MCP, policy, routing, audit) — v0.1.1 |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | #2 | Evidence ledger (`OBSERVED` → `VALIDATED` / `UNKNOWN`) — v0.1.1 |
| [**x4-orchestrator**](https://github.com/dhe-cruzer69/x4-orchestrator) | #5 | Multi-agent coordinator with output validation — v0.1.1 |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | #7 | Risk-based approval gates & autonomy controls — v0.1.1 |
| [**x4-router-score**](https://github.com/dhe-cruzer69/x4-router-score) | #6 | Scoring router (capability / cost / latency / reliability) — v0.1.1 |

## Infrastructure Layer

| Project | Role |
|---|---|
| **RepoDoc** | Repo health, security, CI, secrets, links, workflow auditing |
| [**AgentTest**](https://github.com/dhe-cruzer69/x4-eval) | Reproducible agent evaluation & regression testing |
| [**MCPSafe**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Policy-controlled MCP / tool security gateway |
| [**ModelRoute**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic model selection & fallback |
| [**FleetView**](https://github.com/dhe-cruzer69/x4-health) | Fleet-level observability |

> Five questions every system must answer: *Is the repo healthy? Does the agent work? Is the action allowed? Which model should run it? What is the fleet doing?*

## Core Projects

| Project | Description |
|---|---|
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration runtime |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives |
| [**x4-ai**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic AI layer |
| [**x4-memory**](https://github.com/dhe-cruzer69/x4-memory) | Local-first persistent agent memory |
| [**x4-sandbox**](https://github.com/dhe-cruzer69/x4-sandbox) | Sandboxed tool execution |
| [**x4-mcp-gateway**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Policy-controlled MCP gateway |
| [**x4-research**](https://github.com/dhe-cruzer69/x4-research) | Evidence-first research engine |

## Ecosystem References

OpenRouter • Arcade • NVIDIA Skills • OpenAI • GitHub  
*Ecosystem tooling references only — no affiliation or endorsement claimed.*

## BEAST MODE

**Build → Validate → Verify → Record → Release**

Fast execution that never bypasses safety gates. Evidence-backed changes. Secrets never committed. `UNKNOWN` remains `UNKNOWN` until validated.

## Portfolio Snapshot — 2026-09-21

| Metric | Value |
|---|---:|
| Canonical contract | 69 |
| Physical `x4-*` inventory | 76 |
| Net delta | +7 |
| Missing targets | 4 |

Discrepancy is documented, not hidden.

### Operational Gates

| Gate | Status |
|---|---|
| Branch protection | BLOCKED — ACCESS REQUIRED |
| Vercel | BLOCKED — VERCEL ACCESS REQUIRED |
| Fleet | OPEN — EVIDENCE REQUIRED |
| Evidence | DOCUMENTED |
| Dependency PRs | CLOSED / MERGED |

## Engineering Principles

Security by default • Least privilege • Explicit high-risk approval  
Local-first • Provider-agnostic • Observable & auditable  
Evidence over claims • `UNKNOWN` stays `UNKNOWN`  
No fake PASS • No secrets in repos • Prefer upstream contribution

## Quality Gate

Ready only when checks actually pass: install, tests, lint, secrets scan, permissions, docs, clean-machine start, release build.  
No command is reported **PASS** unless it passed.

## Lineage

[ariexus](https://github.com/dhe-cruzer69/ariexus) • [omniforge](https://github.com/dhe-cruzer69/omniforge)

## Roadmap

Local AI → Agents → Evaluation → MCP/Tool Security → Routing → Observability → Products

---

*Building in public. Contributing upstream. Documenting the architecture. Verifying the work.*
