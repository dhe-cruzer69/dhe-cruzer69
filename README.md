# ARIEX4Ops

**AI • Agents • Automation • Developer Infrastructure**

Building **local-first AI infrastructure and agent systems**: secure runtimes, tool-using agents, MCP integration, sandboxed execution, evaluation, model routing, observability, and evidence-driven automation.

> Autonomous where authorized. Verifiable everywhere. Human-controlled when uncertain.

---

## Flagship

| Project | Role |
|---------|------|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Control plane — local-first, provider-agnostic agent runtime with policy, MCP, routing, audit |
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration — task graphs, sandboxed tools, approvals, memory |
| [**x4-mcp**](https://github.com/dhe-cruzer69/x4-mcp) | Production MCP gateway — registry, auth, permissions, schema validation, rate limits |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives, config, logging, events, telemetry, plugin system |

---

## 7-Capability Autonomous Agent Architecture

| # | Capability | Core mechanism | Success criterion |
|---|------------|----------------|-------------------|
| 1 | Reliable autonomous execution | Planner + executor + retry/recovery | Goal completed across tools |
| 2 | Verification before success | Tests + inspection + evidence ledger | No PASS without evidence |
| 3 | Secure tools & credentials | Sandbox + least privilege + policy gates | Unsafe actions blocked |
| 4 | Persistent context & memory | State store + project memory + history | Correct resume of work |
| 5 | Multi-agent orchestration | Delegation + specialists + coordinator | Effective decomposition |
| 6 | Intelligent routing | Capability / cost / latency / reliability | Best option selected dynamically |
| 7 | Human-in-the-loop control | Approval gates + uncertainty + escalation | High-impact actions gated |

**Key principle:** Never equate execution with success.

```text
INTENT → PLAN → POLICY → EXECUTE → OBSERVE → VERIFY → EVIDENCE
                                                      │
                                         ┌────────────┼────────────┐
                                         ▼            ▼            ▼
                                       PASS        UNKNOWN        FAIL
                                         │            │            │
                                      RELEASE    HUMAN REVIEW   RECOVER
```

---

## Capability Layer

| Project | Maps to | Description |
|---------|---------|-------------|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Full stack | Control plane + runtime |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | #2 | Evidence ledger (`OBSERVED` → `VALIDATED` / `UNKNOWN`) |
| [**x4-orchestrator**](https://github.com/dhe-cruzer69/x4-orchestrator) | #5 | Multi-agent coordinator with output validation |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | #7 | Risk-based approval gates & autonomy controls |
| [**x4-router-score**](https://github.com/dhe-cruzer69/x4-router-score) | #6 | Scoring router (capability / cost / latency / reliability) |
| [**x4-runtime**](https://github.com/dhe-cruzer69/x4-runtime) | Local AI | Hardware-aware local model runtime |
| [**x4-skills**](https://github.com/dhe-cruzer69/x4-skills) | Skills | Verified, security-aware agent skills registry |
| [**x4-sec**](https://github.com/dhe-cruzer69/x4-sec) | Security | Agent security scanner (skills, hooks, MCP, SARIF) |
| [**x4-obs**](https://github.com/dhe-cruzer69/x4-obs) | Observability | Telemetry and evidence receipts |

---

## Engineering Principles

- Security by default • Least privilege • Explicit high-risk approval  
- Local-first • Provider-agnostic • Observable & auditable  
- Evidence over claims • `UNKNOWN` stays `UNKNOWN`  
- No fake PASS • No secrets in repos • Prefer upstream contribution  
- Modules first. New repositories only when justified.

## Quality Gate

A change is ready only when the required checks actually pass:  
install • unit tests • integration tests • lint • typecheck • secret scan • permissions • documentation • clean-machine start • release build.

One unresolved required gate → **UNKNOWN**, not green.

## Autonomy Levels

| Level | Name | Allowed |
|-------|------|---------|
| 0 | Observe | Read → inspect → report |
| 1 | Assist | Read → plan → patch → open PR |
| 2 | Governed Autopilot | Plan → policy → execute → verify → recover (hard limits) |
| 3 | Never autonomous | Delete, credential exposure, production destructive, unapproved merge, financial, policy bypass |

Default mode: **Observe / Assist**. Autopilot only inside explicit policy bounds.

---

## Roadmap

```text
Local AI → Agents → Evaluation → MCP / Tool Security → Routing → Observability → Products
```

**Build order**  
`x4-beast` (control plane) → Fleet Contract → Evidence Ledger → Policy Engine → Verification → Autopilot → FleetView → selective consolidation.

---

*Building in public. Documenting the architecture. Verifying the work.*
