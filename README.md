# ARIEX4Ops

**AI • Agents • Automation • Developer Infrastructure**

Building **local-first AI infrastructure and agent systems**: secure runtimes, tool-using agents, MCP integration, sandboxed execution, evaluation, model routing, observability, evidence-driven automation, and hybrid autofixing.

> Autonomous where authorized. Verifiable everywhere. Human-controlled when uncertain.

**Beast Mode active** — hybrid local/cloud, autofixing tools, policy-gated autonomy, evidence-first execution.

## Recent Activity

<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

---

## Ecosystem map

```mermaid
flowchart TB
  subgraph PROFILE["dhe-cruzer69"]
    README[Profile README]
  end

  subgraph CP["Control Plane"]
    BEAST[x4-beast]
    CORE[x4-core]
    APPROVAL[x4-approval]
    ACBEAST[ariexcore-beast-mode]
    CTRL[ariexcore-control-plane]
  end

  subgraph FLEET["Fleet & Healing"]
    FLEETR[x4-fleet]
    FOPS[ariexcore-fleet-ops]
    AUTOFIX[x4-autofix]
    AFIX[ariexcore-autofix-engine]
  end

  subgraph EV["Evidence & Eval"]
    EVID[x4-evidence]
    AEV[ariexcore-evidence]
    EVAL[x4-eval-harness]
    AEVAL[ariexcore-eval-suite]
  end

  subgraph AG["Agents"]
    AGENTS[x4-agents]
    HARNESS[x4-harness]
    AHARN[ariexcore-multi-agent-harness]
    ORCH[x4-orchestrator]
  end

  subgraph MEM["Memory & Context"]
    MEMR[x4-memory / x4-memory-core]
    AMEM[ariexcore-agent-memory]
    CTX[x4-context]
    ACTX[ariexcore-context-engine]
  end

  subgraph TOOLS["MCP • Skills • Router • Runtime"]
    MCP[x4-mcp / x4-mcp-prod]
    AMCP[ariexcore-mcp-gateway]
    SKILLS[x4-skills / x4-skills-hub]
    ASKILL[ariexcore-skill-registry]
    ROUTER[x4-router-score / x4-agent-router]
    AROUT[ariexcore-model-router]
    RUNTIME[x4-runtime]
    SAND[x4-sandbox]
    ASAND[ariexcore-sandbox-runtime]
  end

  subgraph SEC["Security & Observability"]
    SEC[x4-sec / x4-sec-action]
    ASEC[ariexcore-sec-action]
    OBS[x4-obs]
    AOBS[ariexcore-observability]
  end

  README --> CP
  CP --> FLEET
  CP --> AG
  FLEET --> EV
  FLEET --> AUTOFIX
  AG --> MEM
  AG --> TOOLS
  TOOLS --> SEC
  EV --> SEC
  APPROVAL --> CP
```

---

## Flagship (pin these)

| Project | Role | Status |
|---------|------|--------|
| [**x4-beast**](https://github.com/dhe-cruzer69/x4-beast) | Control plane — local-first, provider-agnostic agent runtime with policy, MCP, routing, audit, autofix | Active |
| [**x4-fleet**](https://github.com/dhe-cruzer69/x4-fleet) | Self-healing fleet: inventory, nightly audit, evidence ledger, auto-issue on staleness/CI fail | **Live + CI** |
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration — task graphs, sandboxed tools, approvals, memory | Active |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | Human-in-the-loop approval gates & risk-based autonomy controls for high-impact actions | Active |
| [**x4-evidence**](https://github.com/dhe-cruzer69/x4-evidence) | Evidence ledger (`OBSERVED` → `VALIDATED` / `UNKNOWN`) — no PASS without evidence | Active |
| [**x4-autofix**](https://github.com/dhe-cruzer69/x4-autofix) | Policy-gated autofix and recovery loops (Level 0–3) | Live |
| [**x4-sec-action**](https://github.com/dhe-cruzer69/x4-sec-action) | GitHub Action for agent security scanner (SARIF) | Live |

---

## Evidence ledger (explained)

The evidence ledger is the single source of truth for **whether a claim is actually true**.

```text
OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED
                              ↓
                           UNKNOWN / FAIL
```

| State | Meaning |
|-------|---------|
| **OBSERVED** | Raw fact recorded (log line, API response, test output, inventory row) |
| **CORRELATED** | Multiple observations linked to the same claim |
| **HYPOTHESIS** | Proposed explanation or fix; not yet proven |
| **VALIDATED** | Claim backed by sufficient evidence; may PASS |
| **UNKNOWN** | Evidence missing or incomplete — **never treated as green** |
| **FAIL** | Evidence contradicts the claim |

**Rules**
- Execution ≠ success. A green CI run is only VALIDATED if the checks that matter actually ran and passed.
- Fleet inventory writes OBSERVED entries every night (`x4-fleet`).
- Autofix may only act on VALIDATED findings inside policy Level 0–2.
- Level 3 actions (delete, secrets, force-push) always require human approval via **x4-approval**.

Primary repos: [x4-evidence](https://github.com/dhe-cruzer69/x4-evidence) · [ariexcore-evidence](https://github.com/dhe-cruzer69/ariexcore-evidence) · schema in [x4-fleet/data/evidence](https://github.com/dhe-cruzer69/x4-fleet).

---

## Full polished catalog (detailed)

### Control plane
| Repo | Description |
|------|-------------|
| [x4-beast](https://github.com/dhe-cruzer69/x4-beast) | Flagship local-first, provider-agnostic AI agent infrastructure with policy controls, MCP, model routing, audit, and the 7-capability autonomous architecture. |
| [ariexcore-beast-mode](https://github.com/dhe-cruzer69/ariexcore-beast-mode) | Org-branded Beast Mode control-plane scaffold for ARIEXCORE-69X transfer. |
| [ariexcore-control-plane](https://github.com/dhe-cruzer69/ariexcore-control-plane) | Policy engine, autonomy levels 0–3, fleet contract schema, evidence gates. |
| [x4-core](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives: config, logging, events, telemetry, plugin system. |
| [**x4-approval**](https://github.com/dhe-cruzer69/x4-approval) | **Human-in-the-loop approval gates and risk-based autonomy controls.** High-impact actions (deletes, secrets, production changes, merges) must pass an approval gate before execution. Implements Level 3 “Never autonomous” enforcement and escalates UNKNOWN decisions to a human. |

### Fleet & self-healing
| Repo | Description |
|------|-------------|
| [x4-fleet](https://github.com/dhe-cruzer69/x4-fleet) | Self-healing fleet core: GitHub inventory collector, Actions health, nightly audit (02:00 IST), weekly report, evidence snapshots, CI (pytest/ruff/mypy), autonomy policies. |
| [ariexcore-fleet-ops](https://github.com/dhe-cruzer69/ariexcore-fleet-ops) | Organization-level fleet operations twin (inventory, audit, reconciliation). |
| [x4-autofix](https://github.com/dhe-cruzer69/x4-autofix) | Policy-gated autofix: detect failures, propose repairs, apply trivial fixes only when Level 2 is authorized. |
| [ariexcore-autofix-engine](https://github.com/dhe-cruzer69/ariexcore-autofix-engine) | Org autofix engine with sample findings and level gates. |

### Evidence & evaluation
| Repo | Description |
|------|-------------|
| [x4-evidence](https://github.com/dhe-cruzer69/x4-evidence) | Evidence ledger and verification engine. No PASS without evidence. |
| [ariexcore-evidence](https://github.com/dhe-cruzer69/ariexcore-evidence) | Canonical ARIEXCORE evidence ledger. |
| [x4-eval-harness](https://github.com/dhe-cruzer69/x4-eval-harness) | Evidence-first evaluation harness for agents (claim graphs, scoring). |
| [ariexcore-eval-suite](https://github.com/dhe-cruzer69/ariexcore-eval-suite) | Org evaluation suite with sample claims. |

### Agents & orchestration
| Repo | Description |
|------|-------------|
| [x4-agents](https://github.com/dhe-cruzer69/x4-agents) | Secure multi-agent orchestration runtime — task graphs, sandboxed tools, approvals, memory. |
| [x4-harness](https://github.com/dhe-cruzer69/x4-harness) | Multi-agent harness with shared context, role assignment, adaptive memory. |
| [ariexcore-multi-agent-harness](https://github.com/dhe-cruzer69/ariexcore-multi-agent-harness) | Org multi-agent harness (planner / implementer / reviewer / security roles). |
| [x4-orchestrator](https://github.com/dhe-cruzer69/x4-orchestrator) | Multi-agent coordinator with specialist delegation, validation, recovery loops. |

### Memory & context
| Repo | Description |
|------|-------------|
| [x4-memory](https://github.com/dhe-cruzer69/x4-memory) / [x4-memory-core](https://github.com/dhe-cruzer69/x4-memory-core) | Multi-layer persistent agent memory (working, episodic, semantic). |
| [ariexcore-agent-memory](https://github.com/dhe-cruzer69/ariexcore-agent-memory) | Org memory store with sample trajectories. |
| [x4-context](https://github.com/dhe-cruzer69/x4-context) | Context compression and session memory for long-horizon agents. |
| [ariexcore-context-engine](https://github.com/dhe-cruzer69/ariexcore-context-engine) | Org context engine with compression metrics. |

### MCP, skills, routing, runtime
| Repo | Description |
|------|-------------|
| [x4-mcp](https://github.com/dhe-cruzer69/x4-mcp) / [x4-mcp-prod](https://github.com/dhe-cruzer69/x4-mcp-prod) | Production MCP gateway: registry, auth, permissions, schema validation, rate limits. |
| [ariexcore-mcp-gateway](https://github.com/dhe-cruzer69/ariexcore-mcp-gateway) | Org production MCP gateway. |
| [x4-mcpgen](https://github.com/dhe-cruzer69/x4-mcpgen) | Generate tested, secure-by-default MCP server scaffolds. |
| [x4-skills](https://github.com/dhe-cruzer69/x4-skills) / [x4-skills-hub](https://github.com/dhe-cruzer69/x4-skills-hub) | Verified AI agent skills registry + seed MCP skills. |
| [ariexcore-skill-registry](https://github.com/dhe-cruzer69/ariexcore-skill-registry) | Org skill registry with 5 seed skills. |
| [x4-router-score](https://github.com/dhe-cruzer69/x4-router-score) / [x4-agent-router](https://github.com/dhe-cruzer69/x4-agent-router) | Intelligent model & tool router (capability / cost / latency / reliability). |
| [ariexcore-model-router](https://github.com/dhe-cruzer69/ariexcore-model-router) | Org model router with sample scores. |
| [x4-runtime](https://github.com/dhe-cruzer69/x4-runtime) | Local-first model runtime with hardware-aware routing. |
| [x4-sandbox](https://github.com/dhe-cruzer69/x4-sandbox) / [ariexcore-sandbox-runtime](https://github.com/dhe-cruzer69/ariexcore-sandbox-runtime) | Secure sandboxed tool execution (least privilege, audit). |

### Security & observability
| Repo | Description |
|------|-------------|
| [x4-sec](https://github.com/dhe-cruzer69/x4-sec) | AI agent security scanner — skills, hooks, MCP, SARIF. |
| [x4-sec-action](https://github.com/dhe-cruzer69/x4-sec-action) | GitHub Action packaging for the scanner (Marketplace-ready). |
| [ariexcore-sec-action](https://github.com/dhe-cruzer69/ariexcore-sec-action) | Org security Action. |
| [x4-obs](https://github.com/dhe-cruzer69/x4-obs) | Agent telemetry and evidence receipts (local-first). |
| [ariexcore-observability](https://github.com/dhe-cruzer69/ariexcore-observability) | Org observability + sample receipts. |

### Other active short names
| Repo | Description |
|------|-------------|
| [x4-ai](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic AI / model abstraction layer. |
| [x4-research](https://github.com/dhe-cruzer69/x4-research) | Evidence-first research agent (claim graphs, source ranking). |

---

## Autonomy levels

| Level | Name | Allowed |
|-------|------|---------|
| 0 | Observe | Read → inspect → report |
| 1 | Assist | Read → plan → patch → open PR |
| 2 | Governed Autopilot | Plan → policy → execute → verify → recover / autofix (hard limits) |
| 3 | Never autonomous | Delete, secrets, production destructive, unapproved merge, financial — **gated by x4-approval** |

Default: **Observe / Assist**. Autopilot only inside explicit policy bounds.

---

## Quality gate

A change is ready only when required checks pass: install • unit • integration • lint • typecheck • secret scan • permissions • docs • clean-machine start • release build.

**One unresolved required gate → UNKNOWN, not green.**

---

## Automation status

| Step | Status |
|------|--------|
| Inventory + classification | ✅ |
| Polished public repos (x4-* + ariexcore-*) | ✅ Live |
| x4-fleet CI + collectors + evidence schema | ✅ |
| Profile README (this file) | ✅ |
| Org transfer (ARIEXCORE-69X) | ⏳ Manual (token lacks org admin) |
| Archive empty stubs | ⏳ Pending your approval |
| Twin-pair merges | ⏳ Pending |
| Pin flagship repos | ⏳ GitHub UI |

---

## Org note

[ARIEXCORE-69X](https://github.com/ARIEXCORE-69X) currently holds `literate-spoon` only. Polished `ariexcore-*` repos live under the personal account and are ready to **Transfer** into the org once ownership/admin is confirmed.

---

*Building in public. Documenting the architecture. Verifying the work. Keeping the profile clean and high-signal only.*
