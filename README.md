# ARIEX4Ops

**AI • Agents • Automation • Developer Infrastructure**

Building the **X4** open-source ecosystem — secure agent runtimes, local-first memory, MCP infrastructure, sandboxed tool execution, evidence-driven research, and developer tooling.

---

## Featured Projects

| Project | Description | Status |
|---------|-------------|--------|
| [**x4-agents**](https://github.com/dhe-cruzer69/x4-agents) | Flagship secure multi-agent orchestration (task graphs, approvals, audit) | Active |
| [**x4-core**](https://github.com/dhe-cruzer69/x4-core) | Shared runtime primitives (config, logging, events, permissions) | **v0.1.0** |
| [**x4-ai**](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic AI layer (OpenAI / Anthropic / Gemini / local) | Active |
| [**x4-memory**](https://github.com/dhe-cruzer69/x4-memory) | Local-first persistent agent memory | Active |
| [**x4-sandbox**](https://github.com/dhe-cruzer69/x4-sandbox) | Sandboxed tool execution with policy & audit | Active |
| [**x4-mcp-gateway**](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Secure MCP gateway (auth, policy, rate-limit, audit) | Active |
| [**x4-research**](https://github.com/dhe-cruzer69/x4-research) | Evidence-first research agent (claim graphs, citations) | Active |

---

## Engineering Principles

- **Security by default** — policy, risk, permission, approval, audit
- **Explicit permissions** — no unrestricted production credentials for agents
- **Local-first** where practical
- **Observable & auditable** execution
- **Evidence over marketing claims**
- **Upstream contribution** over cosmetic forks

---

## Quick Start

```bash
git clone https://github.com/dhe-cruzer69/x4-core.git
cd x4-core
pip install -e ".[dev]"
python examples/hello_x4_core.py
pytest -q
```

---

## Origin Projects

- [ariexus](https://github.com/dhe-cruzer69/ariexus) — technical ancestor of x4-agents
- [omniforge](https://github.com/dhe-cruzer69/omniforge) — local-first workbench inspiration

---

## Support X4

If these projects save you time or become part of your stack, consider supporting continued open-source development:

**[Sponsor ARIEX4Ops](https://github.com/sponsors/dhe-cruzer69)**

---

*Building in public. Contributing upstream. Documenting the architecture.*
