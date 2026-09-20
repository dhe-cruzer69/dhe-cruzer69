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
| [**x4-local-ai-runtime**](https://github.com/dhe-cruzer69/x4-local-ai-runtime) | Local AI runtime infrastructure |
| [**x4-mcp**](https://github.com/dhe-cruzer69/x4-mcp) | X4 MCP integration layer |

## Provider & Agent Ecosystem

- [**OpenRouter / @OpenRouterTeam**](https://github.com/OpenRouterTeam) — unified model access, provider routing, fallbacks, and agent tooling.
- [**Arcade / @ArcadeAI**](https://github.com/ArcadeAI) — agent tools, MCP servers, and tool-development infrastructure.
- [**NVIDIA Skills / @NVIDIA**](https://github.com/NVIDIA/skills) — NVIDIA-verified Agent Skills spanning CUDA, inference, robotics, simulation, RAG, and Physical AI. citeturn0search0
- [**OpenAI / @openai**](https://github.com/openai) — official SDKs and agent/provider integration surfaces.
- [**GitHub / @github**](https://github.com/github) — source control, CI/CD, issues, pull requests, and developer automation.
- **Autopilot workflows** — controlled autonomous execution with explicit validation and human review gates.
- **BEAST MODE engineering** — fast execution backed by tests, security checks, evidence, rollback paths, and verification.

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

## Support X4

If these projects save you time or become part of your stack, consider supporting continued open-source development.

**[GitHub Sponsors → dhe-cruzer69](https://github.com/sponsors/dhe-cruzer69)**

---

*Building in public. Contributing upstream. Documenting the architecture. Verifying the work.*
