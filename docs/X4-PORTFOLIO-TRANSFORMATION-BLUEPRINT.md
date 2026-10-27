# X4 portfolio transformation blueprint

**Planning snapshot: 27 October 2026 · Status: proposed architecture, not a product-release claim**

The objective is a smaller, coherent portfolio of independently useful security-first developer products. Repository names, architecture diagrams and planned integrations are not proof of implementation. The labels below distinguish strategy from verified state.

## Ten proposed Apex products

| Product | Intended responsibility | First proof required |
|---|---|---|
| **architect-x4** | Local-first engineering workbench: repository context, reviewed patches, tests and local model selection | End-to-end edit proposal, explicit diff approval, test execution receipt and rollback |
| **swarm-x4** | Durable agent task graphs, bounded retries, cancellation, budgets and approval checkpoints | Deterministic recovery tests and capability-limited tool execution |
| **nexus-x4** | MCP gateway with identity, per-tool authorization, quotas and redacted audit events | Real protocol integration tests, negative authorization tests and session lifecycle coverage |
| **sentinel-x4** | Secret, dependency, license and static checks with policy-driven SARIF output | Reproducible fixtures, low-noise findings, correct file/line locations and fail-closed exit codes |
| **vault-x4** | Controlled execution for untrusted workloads | Demonstrated isolation boundary, resource limits, network policy and cleanup tests; a container alone is not automatically a complete boundary |
| **ledger-x4** | Hash-linked audit records and signed release evidence | Canonical event format, integrity verification and documented key/retention model |
| **prism-x4** | Local and hosted model routing with explicit privacy, timeout and cost policies | Tests proving private prompts are never routed externally without explicit policy permission |
| **oracle-x4** | Source-grounded retrieval and private knowledge workflows | Citation correctness, provenance, deletion propagation and retention tests |
| **crucible-x4** | Versioned model/agent evaluation and regression testing | Repeatable datasets, baseline comparisons and quality/cost/latency reports |
| **x4-fleet** | Read-only portfolio inventory, CI evidence, dependency mapping and reviewed disposition proposals | Pagination completeness, immutable evidence receipts and human-reviewed decisions |

These are product proposals. They do not imply that each repository exists, is available under that name, or already implements the listed behavior.

## Shared platform contract

The proposed parent repository is **x4-platform**. It should share contracts and engineering policy without forcing every product to run as one coupled service.

- **Contracts:** versioned JSON Schema and typed interfaces with compatibility tests.
- **Policy:** deny-by-default for unknown or unavailable required controls; explicit capabilities and human approval for high-impact actions.
- **Local-first:** local model and storage paths where practical; external routing must be explicit and observable.
- **Storage:** SQLite for single-user/local deployments; PostgreSQL only where multi-user concurrency and operational needs justify it.
- **Execution:** separate the control plane from untrusted workloads; document the actual threat boundary and test it.
- **Evidence:** structured logs, correlation IDs, redaction, reproducible test output and tamper-evident records. A hash chain detects changes to recorded data; it does not prove the original event was truthful.
- **CI:** lockfiles, lint/type checks, unit and integration tests, secret/dependency/license checks, reproducible builds where practical, and retained evidence artifacts.
- **Release:** least-privilege workflow permissions, actions pinned to verified full commit SHAs, protected branches, human review and explicit release verification.
- **Dependency discipline:** add Redis, Kubernetes, cloud services or additional databases only when a documented requirement justifies their operational and security cost.

## Existing repository migration policy

Existing repositories remain the source of truth until each migration is reviewed and approved. Similar names are not proof of duplicate functionality.

For every candidate, record: stable repository identity, default branch and baseline commit SHA; source/test/workflow inventory; license and fork provenance; dependencies and downstream consumers; unique functionality; migration and rollback plan; evidence links and check date; proposed disposition; reviewer; and individual approval state.

Allowed planning dispositions:

- **KEEP** — retain as an independent product or shared component.
- **MERGE_CANDIDATE** — consider migration only after source, license, history and consumer analysis.
- **ARCHIVE_CANDIDATE** — candidate for later review, not an archive instruction.
- **REVIEW** — evidence is incomplete or conflicting.
- **UNKNOWN — HUMAN REVIEW REQUIRED** — identity or required evidence is unresolved.

Default state is **REVIEW**. No repository is to be deleted, archived, renamed, made public/private, or have history rewritten based only on size, stars, names, README claims or an automated score. Require explicit individual approval for each high-impact repository action. Preserve source history and retain a rollback path for approved migrations.

The working Keep-30 proposal previously matched 23 names in a historical metadata snapshot; seven proposed names remained unresolved. That snapshot is not a completed code audit or an authorization to archive anything. Refresh the inventory and reconcile the seven names before treating the Keep-30 set as final.

## Engineering investment order

1. **Inventory and evidence:** reconcile the exact Keep-30 set; capture repository IDs, default-branch SHAs, licenses, source trees, workflows and consumers.
2. **Shared contracts and policy:** define API/schema versions, error semantics, permissions and audit event formats.
3. **sentinel-x4:** implement a deterministic scanner with fixtures, safe traversal, SARIF validation and fail-closed exit codes.
4. **nexus-x4:** implement real MCP protocol handling, identity/authorization, rate limits, audit redaction and protocol-level tests.
5. **vault-x4:** prove the execution boundary before marketing it as secure isolation.
6. **crucible-x4 and ledger-x4:** make quality and security claims reproducible with test/evidence artifacts.
7. **Remaining products:** integrate only through tested contracts; keep each product independently testable.
8. **Migration and releases:** migrate in small reviewed batches, validate behavior and licenses, preserve rollback, then request individual approval for any archival action.

## Quality rubric — not yet scored

| Dimension | Weight |
|---|---:|
| Working functionality and reproducible demos | 20 |
| Meaningful tests and correctness | 15 |
| Security and supply-chain controls | 15 |
| Documentation and onboarding | 10 |
| Distinct product value | 10 |
| Maintenance and release discipline | 10 |
| License and contribution governance | 5 |
| Adoption and independent usage evidence | 10 |
| Profile clarity and discoverability | 5 |
| **Total** | **100** |

**Portfolio score: NOT ESTABLISHED.** Do not infer a numeric score from repository count, stars, file size, or architecture diagrams. Award credit only when the relevant evidence is inspected and dated. A score is not a security certification.

## Adoption, research and commercial hypotheses

Security-governed agent execution, MCP gateways, evaluation/observability, local-first AI and actionable DevSecOps are areas worth investigating—not guaranteed growth markets. Projects such as OpenSandbox, AgentGateway, AgentScope, Langfuse and MLflow are reference points for studying architecture, developer experience, governance and integration quality, not templates to copy.

Star counts from different research snapshots can disagree and change quickly; this document intentionally does not present them as a current ranking. Before making comparative claims, record the source URL, observation date, stars/forks, release activity, license, integrations and signs of real usage. Popularity does not establish profitability.

Potential commercial paths include paid support, team governance, managed evaluations, compliance evidence, hosted orchestration and enterprise integrations. These remain hypotheses until validated through user interviews, working demos, adoption, willingness-to-pay evidence and support-cost estimates. No stars, sponsorship income or profitability are promised.

## Evidence and status vocabulary

- **OBSERVED** — directly visible in source, configuration or recorded output.
- **CORRELATED** — multiple signals agree but do not establish causality.
- **HYPOTHESIS** — a proposal to test, not an implementation claim.
- **VALIDATED** — the specified check actually passed and its evidence is linked.
- **UNKNOWN — HUMAN REVIEW REQUIRED** — evidence is absent, conflicting or access-limited.

Never suppress failing tests with `|| true`; a skipped security check is not a pass. Do not claim a build, test, deployment, isolation guarantee or live service unless the relevant run or verification exists.

*Strategy note added 27 October 2026. Product scopes and migration relationships are proposals until supported by implementation evidence.*

## Mythos × Fable: the intelligence and trust layer

**Positioning:** Mythos proposes and explains engineering changes; Fable independently evaluates evidence and policy; X4 coordinates tools and enforces authorization. These are complementary roles, not three names for the same agent.

### Mythos — repository understanding and controlled recoding

Mythos should turn a real repository problem into an inspectable engineering decision:
1. **Understand:** map files, entry points, dependencies, tests, configuration, workflows and documented behavior. Mark inaccessible or unparsed areas as unknown.
2. **Diagnose:** tie every finding to a file/line, reproducible command, test result or explicit hypothesis. Rank by impact, confidence and remediation cost.
3. **Design:** produce a short decision record with alternatives, trade-offs, compatibility impact and a rollback path.
4. **Propose:** generate the smallest coherent patch on a review branch. Show the diff before any write and never silently rewrite a user's working tree or default branch.
5. **Prove:** propose regression tests, run only in an authorized environment, and attach actual command output and commit identity. A generated test is not a passed test.

**MVP acceptance gate:** on one selected repository, Mythos can explain a defect with source evidence, create a minimal reviewable patch, add a regression test, and report honestly what was and was not executed. No broad autonomous refactor is required for the first release.

### Fable — evidence graph and policy gate

Fable should evaluate claims independently of the agent that made them:
- Represent a claim as **claim → evidence → method/version → timestamp → result → reviewer**.
- Use explicit states: **OBSERVED**, **CORRELATED**, **HYPOTHESIS**, **VALIDATED**, and **UNKNOWN — HUMAN REVIEW REQUIRED**.
- Treat missing, stale, contradictory, skipped or inaccessible evidence as unknown or failing according to the declared policy—not as green.
- Validate CI conclusions against the exact head SHA; distinguish workflow completion, individual check outcomes, required-check configuration and merge authorization.
- Preserve evidence provenance and redaction rules. A hash chain can detect alteration of recorded events; it cannot prove the events were truthful when created.
- Keep scoring explainable. Publish rubric, weights, evidence links, check dates and uncertainty; do not turn an unvalidated score into a security certification.

**MVP acceptance gate:** seeded fixtures prove Fable catches a suppressed linter failure, a skipped required check, stale evidence, an absent test suite and a claim with no supporting artifact. Negative tests must demonstrate that each case cannot be reported as PASS.

### The separation of duties

| Component | May do | Must not do |
|---|---|---|
| Mythos | Inspect authorized source; explain findings; propose diffs and tests | Approve its own patch or claim unrun tests passed |
| Fable | Evaluate evidence, policy and confidence; emit a reasoned gate result | Invent evidence, repair its own failed gate silently or infer authorization from a green check |
| X4 control plane | Enforce capability grants, approvals, budgets, timeouts, sandbox routing and audit receipts | Treat model output as policy; bypass denied or unknown controls |
| Human maintainer | Approve high-impact changes, resolve ambiguity, accept risk and authorize merge/release | Be pressured by opaque scores or fabricated urgency |

Use versioned, typed contracts between components. A proposed finding should include a stable finding ID, repository identity, commit SHA, location, severity, confidence, evidence references, suggested remediation and policy version. A proposed change should include a patch digest, affected paths, test plan, risk summary and required approvals. Reject malformed or unknown schema versions.

### Authentic connection: build trust with users, not just features

- **Show the work:** every important conclusion links to evidence, a diff, or a reproducible command.
- **Respect user intent:** explain what will change and why; offer a small reversible step before a broad migration.
- **Make uncertainty legible:** use plain-language limitations, confidence rationale and clear next steps instead of inflated claims.
- **Invite correction:** provide issue templates for expected behavior, reproduction steps, environment, redacted logs and acceptance criteria. Treat maintainer feedback as evidence, not an interruption.
- **Close the loop:** link reports to fixes, regression tests and release notes so users can verify that their reported problem was addressed.
- **Protect privacy:** local-first by default where practical; disclose every external model/provider boundary and what data crosses it. Redact secrets and personal data from logs and issue reports.
- **Measure value honestly:** track time-to-reproduce, accepted-fix rate, regression rate, false-positive rate, evidence completeness and onboarding success. Do not optimize for stars or activity counts alone.

### Delivery sequence

1. **Foundation:** define finding/evidence schemas, status vocabulary, threat model, data-retention rules and review-branch workflow.
2. **Fable first:** implement deterministic evidence parsing and negative fixtures so the governance gate is testable before it is trusted.
3. **Mythos read-only:** add repository mapping and evidence-linked diagnosis without write access.
4. **Mythos patch proposals:** generate small diffs and tests on a non-default branch; require explicit approval before applying changes.
5. **X4 orchestration:** add least-privilege tool grants, bounded execution, cancellation, audit receipts and policy-enforced approvals.
6. **Pilot:** test on one maintained repository with known defects and seeded false-green cases; publish results, failures and limitations.
7. **Expand carefully:** add repositories only after owner consent, license/provenance checks, baseline snapshots and a rollback plan.

### Release gate

Do not label Mythos or Fable production-ready until the relevant implementation exists and evidence shows: unit and integration tests pass on the exact commit; negative authorization and false-green tests pass; secrets are not exposed; dependencies and actions are pinned/checked; clean-environment setup is documented; and limitations are disclosed. A skipped, missing or unobservable required check remains **UNKNOWN — HUMAN REVIEW REQUIRED**.

*Mythos × Fable is a proposed product direction. This section does not assert that these components are implemented or validated today.*

