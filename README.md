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
| [**x4-fleet**](https://github.com/dhe-cruzer69/x4-fleet) | Self-healing fleet: inventory, nightly audit, evidence ledger, auto-issue on staleness/CI fail | **New — Live** |
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration — task graphs, sandboxed tools, approvals, memory | Active |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives, config, logging, events, telemetry, plugin system | Active |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | Evidence ledger and verification engine (`OBSERVED` → `VALIDATED` / `UNKNOWN`) | Active |
| [**x4-autofix**](https://github.com/dhe-cruzer69/x4-autofix) | Policy-gated autofix and recovery loops (Level 0–3) | **New — Live** |

---

## New Public Repos (Oct 2026)

High-signal, polished scaffolds aligned with current trending agent infrastructure:

| Repo | Purpose |
|------|---------|
| [**x4-fleet**](https://github.com/dhe-cruzer69/x4-fleet) | Self-healing fleet inventory + nightly audit + metrics |
| [**x4-context**](https://github.com/dhe-cruzer69/x4-context) | Context compression & persistent session memory |
| [**x4-harness**](https://github.com/dhe-cruzer69/x4-harness) | Multi-agent harness (shared context, roles, adaptive memory) |
| [**x4-autofix**](https://github.com/dhe-cruzer69/x4-autofix) | Policy-gated autofix & recovery loops |
| [**x4-sec-action**](https://github.com/dhe-cruzer69/x4-sec-action) | GitHub Action for agent security scanner (SARIF) |
| [**x4-skills-hub**](https://github.com/dhe-cruzer69/x4-skills-hub) | Verified skills registry + 5 seed MCP skills |
| [**x4-memory-core**](https://github.com/dhe-cruzer69/x4-memory-core) | Multi-layer persistent agent memory (working / episodic / semantic) |
| [**x4-mcp-prod**](https://github.com/dhe-cruzer69/x4-mcp-prod) | Production MCP gateway (auth, rate limits, audit) |
| [**x4-eval-harness**](https://github.com/dhe-cruzer69/x4-eval-harness) | Evidence-first evaluation harness |
| [**x4-agent-router**](https://github.com/dhe-cruzer69/x4-agent-router) | Intelligent model & tool router with multi-dimension scoring |

---

## Clean X4 Short-Name Family

Canonical short names only. No multi-word bloat.

| Repo | Purpose |
|------|---------|
| **x4-beast** | Flagship control plane + autonomous runtime |
| **x4-fleet** | Self-healing data-collection & fleet core |
| **x4-core** | Invariant runtime / foundation |
| **x4-ai** | Provider-agnostic AI/model layer |
| **x4-agents** | Agent runtime & multi-agent orchestration |
| **x4-mcp** / **x4-mcp-prod** | MCP / tool integration gateway |
| **x4-skills** / **x4-skills-hub** | SkillHub / verified skill contracts |
| **x4-runtime** | Local-first model runtime (hardware-aware) |
| **x4-router-score** / **x4-agent-router** | Intelligent model & tool router |
| **x4-orchestrator** | Multi-agent coordinator |
| **x4-approval** | Policy / approval gates |
| **x4-evidence** | Evidence & verification |
| **x4-obs** | Telemetry & observability |
| **x4-sec** / **x4-sec-action** | Security scanner (skills, hooks, MCP, SARIF) |
| **x4-sandbox** | Secure sandboxed tool execution |
| **x4-memory** / **x4-memory-core** | Persistent multi-layer agent memory |
| **x4-research** | Evidence-first research agent |
| **x4-context** | Context compression |
| **x4-harness** | Multi-agent harness |
| **x4-autofix** | Recovery & autofix |
| **x4-eval-harness** | Evaluation harness |

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
- **Self-healing fleet** — `x4-fleet` nightly inventory + auto-issue on staleness
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
| Read-only inventory | ✅ Complete (130 repos) |
| Classification (KEEP / RENAME / MERGE / DELETE) | ✅ Complete |
| DELETE_CANDIDATES list generated | ✅ ~55–85 empty/failed stubs identified |
| 10 new high-quality public repos created | ✅ Live (Oct 3 2026) |
| x4-fleet self-healing core | ✅ Scaffold + workflows pushed |
| Profile README updated | ✅ This commit |
| Human review of delete/archive list | ⏳ Pending your approval |
| Pin powerful repos | ⏳ Manual (GitHub UI) — recommend: x4-beast, x4-fleet, x4-agents, x4-evidence, x4-autofix, x4-sec-action |
| Twin-pair merges | ⏳ Pending |
| Final verification + receipt | ⏳ After deletions |

---

## Roadmap

```text
Local AI → Agents → Evaluation → MCP / Tool Security → Routing → Observability → Autofix → Fleet → Products
```

**Build order**  
`x4-beast` (control plane) → `x4-fleet` (inventory + self-heal) → Evidence Ledger → Policy Engine → Verification → Autopilot + Autofix → selective consolidation of stubs.

---

*Building in public. Documenting the architecture. Verifying the work. Keeping the profile clean and high-signal only.*
