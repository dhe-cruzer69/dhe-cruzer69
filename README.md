# Abhishek — AI Automation & Developer Infrastructure

**ARIEX4Ops / X4**

I build local-first AI agent systems, policy-gated automation, and developer tools. I care about reproducible verification, clear security boundaries, and keeping high-impact actions under human control.

## Featured projects

### [X4 BEAST](https://github.com/dhe-cruzer69/x4-beast)
Local-first, provider-agnostic agent runtime with model routing, MCP/tool integration, policy controls, audit trails, and repair workflows.

[Source & setup](https://github.com/dhe-cruzer69/x4-beast#quick-start) · [Development quality gates](https://github.com/dhe-cruzer69/x4-beast#development--quality-gates)

### [X4 Fleet](https://github.com/dhe-cruzer69/x4-fleet)
GitHub fleet inventory, Actions health checks, scheduled audits, evidence reporting, and issue generation.

[Source & setup](https://github.com/dhe-cruzer69/x4-fleet#quick-start) · [CI workflow](https://github.com/dhe-cruzer69/x4-fleet/blob/main/.github/workflows/ci.yml)

### [X4 Sandbox](https://github.com/dhe-cruzer69/x4-sandbox)
Policy-gated process execution with executable allow-lists, timeouts, bounded output, approval tokens, and a SHA-256-linked JSONL audit log.

**Security boundary:** its current process mode is not an OS-enforced sandbox and is not suitable for hostile code. The README documents what is and is not implemented.

[Source & verification steps](https://github.com/dhe-cruzer69/x4-sandbox#install-and-verify) · [Tests](https://github.com/dhe-cruzer69/x4-sandbox/blob/main/tests/test_core.py) · [Security limitations](https://github.com/dhe-cruzer69/x4-sandbox#not-implemented)

### [X4 Core](https://github.com/dhe-cruzer69/x4-core)
Shared Python runtime primitives for configuration, logging, events, telemetry, permissions, and plugins, with a minimal usage example.

[Source & architecture](https://github.com/dhe-cruzer69/x4-core#architecture) · [CI workflow](https://github.com/dhe-cruzer69/x4-core/blob/main/.github/workflows/ci.yml)

## Engineering principles

- **Evidence before claims:** distinguish observed behavior from hypotheses and validated results.
- **Fail closed:** unsupported security guarantees remain explicit; they are not implied by configuration.
- **Human control:** high-impact operations require deliberate approval.
- **Reproducibility:** document setup and verification commands so work can be checked independently.

## Tools

Python · Docker · GitHub Actions · pytest · Ruff · mypy · MCP · local LLM tooling

---

I add hosted demos and deployment badges only when the deployment and its health checks can be independently verified. The featured repositories above are code-first developer tools; their READMEs link to setup, tests, or CI evidence rather than claiming an unverified live UI.
