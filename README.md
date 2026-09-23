# ARIEX4Ops

**AI • Agents • Automation • Developer Infrastructure**

Building **local-first AI infrastructure and agent systems**: secure runtimes, tool-using agents, MCP integration, sandboxed execution, evaluation, model routing, observability, evidence-driven automation, and hybrid autofixing.

> Autonomous where authorized. Verifiable everywhere. Human-controlled when uncertain.

**Beast Mode active** — hybrid local/cloud, autofixing tools, policy-gated autonomy, evidence-first execution.

---

## Flagship (Pin These)

| Project | Role | Status |
|---------|------|--------|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Control plane — local-first, provider-agnostic agent runtime with policy, MCP, routing, audit, autofix | Active |
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration — task graphs, sandboxed tools, approvals, memory | Active |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives, config, logging, events, telemetry, plugin system | Active |
| [**x4-mcp**](https://github.com/dhe-cruzer69/x4-mcp) | Production MCP gateway — registry, auth, permissions, schema validation, rate limits | Active |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | Human-in-the-loop approval gates & risk-based autonomy controls | Active |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | Evidence ledger and verification engine (`OBSERVED` → `VALIDATED` / `UNKNOWN`) | Active |

---

## Clean X4 Short-Name Family

Canonical short names only. No multi-word bloat.

| Repo | Purpose |
|------|---------|
| **x4-beast** | Flagship control plane + autonomous runtime |
| **x4-core** | Invariant runtime / foundation |
| **x4-ai** | Provider-agnostic AI/model layer |
| **x4-agents** | Agent runtime & multi-agent orchestration |
| **x4-mcp** | MCP / tool integration gateway |
| **x4-skills** | SkillHub / verified skill contracts |
| **x4-runtime** | Local-first model runtime (hardware-aware) |
| **x4-router-score** | Intelligent model & tool router |
| **x4-orchestrator** | Multi-agent coordinator |
| **x4-approval** | Policy / approval gates |
| **x4-evidence** | Evidence & verification |
| **x4-obs** | Telemetry & observability |
| **x4-sec** | Security scanner (skills, hooks, MCP, SARIF) |
| **x4-sandbox** | Secure sandboxed tool execution |
| **x4-memory** | Persistent multi-layer agent memory |
| **x4-research** | Evidence-first research agent |

All other empty `x4-*` stubs and failed experiments are scheduled for removal.

---

## 7-Capability Autonomous Agent Architecture

| # | Capability | Core mechanism | Success criterion |
|---|------------|----------------|-------------------|
| 1 | Reliable autonomous execution | Planner + executor + retry/recovery + autofix | Goal completed across tools |
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
                                      RELEASE    HUMAN REVIEW   RECOVER / AUTOFIX
```

---

## Beast Mode Features (Current)

- **Hybrid local/cloud** — run fully local or fall back to cloud providers with policy control
- **Autofixing tools** — detect, propose, and (when authorized) apply repairs
- **Evidence-first** — every claim must be backed by observed evidence
- **Policy-gated autonomy** — Level 0–3 controls (Observe → Assist → Governed Autopilot → Never)
- **MCP-native** — first-class Model Context Protocol support
- **Security by default** — sandbox, least privilege, secret scanning, SARIF output
- **Short-name namespace** — clean `x4-*` family only

---

## Engineering Principles

- Security by default • Least privilege • Explicit high-risk approval  
- Local-first • Provider-agnostic • Observable & auditable  
- Evidence over claims • `UNKNOWN` stays `UNKNOWN`  
- No fake PASS • No secrets in repos • Prefer upstream contribution  
- Modules first. New repositories only when justified.  
- Eco-friendly profile: only completed, high-quality, integrated repos remain.

## Quality Gate

A change is ready only when the required checks actually pass:  
install • unit tests • integration tests • lint • typecheck • secret scan • permissions • documentation • clean-machine start • release build.

One unresolved required gate → **UNKNOWN**, not green.

## Autonomy Levels

| Level | Name | Allowed |
|-------|------|---------|
| 0 | Observe | Read → inspect → report |
| 1 | Assist | Read → plan → patch → open PR |
| 2 | Governed Autopilot | Plan → policy → execute → verify → recover / autofix (hard limits) |
| 3 | Never autonomous | Delete, credential exposure, production destructive, unapproved merge, financial, policy bypass |

Default mode: **Observe / Assist**. Autopilot only inside explicit policy bounds.

---

## Automation Status (Profile Cleanup)

| Step | Status |
|------|--------|
| Read-only inventory | ✅ Complete |
| Classification (KEEP / RENAME / MERGE / DELETE) | ✅ Complete |
| DELETE_CANDIDATES list generated | ✅ 85 empty/failed repos identified |
| Profile README updated (Beast Mode) | ✅ This commit |
| x4-beast enrichment | 🔄 In progress |
| Human review of delete list | ⏳ Pending your approval |
| Pin powerful repos | ⏳ Manual (GitHub UI) |
| Final verification + receipt | ⏳ After deletions |

---

## Roadmap

```text
Local AI → Agents → Evaluation → MCP / Tool Security → Routing → Observability → Autofix → Products
```

**Build order**  
`x4-beast` (control plane) → Fleet Contract → Evidence Ledger → Policy Engine → Verification → Autopilot + Autofix → FleetView → selective consolidation.

---

*Building in public. Documenting the architecture. Verifying the work. Keeping the profile clean and high-signal only.*
