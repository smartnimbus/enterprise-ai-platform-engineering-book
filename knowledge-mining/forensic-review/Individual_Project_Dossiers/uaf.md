## Dossier — uaf

# Project dossier: Unified Agent Fabric (UAF) — uaf.zip

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
Unified Agent Fabric engineering design repository covering an agent runtime, One Thread state, GovernanceGuard, LLM and connector gateways, observability, marketplace and orchestration.

## 2. Maturity and evidence boundary
Rich technical design and ADR corpus plus project orchestration scripts and audit documents. The exported archive contains little of the claimed core src/uaf runtime; crucial internal audit reports serious deficiencies. No deployment assurance is possible from it.

- Archive entries (non-directory): **467**; captured text/source files: **346**; recognised code/config source files (approximate): **25**.
- **Reported status:** Mixed design, scripts and negative audit evidence; runtime deployment unverified.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Plugin-extensible Python/async service contracts, Pydantic models, flow orchestration, governance before model/action paths, multi-tenancy and explicit recovery contracts.

## 4. Distinctive strengths
Precise low-level documents, ADRs, test traceability matrices, dependency plans and independent challenge reports. The audit creates a rare counterexample to confusing a mature design library with a secure platform.

## 5. Weaknesses, contradictions and failure modes
April 22 remediation report lists critical JWT/config/persistence issues and inconsistent completeness denominators; copying “non-bypassable” claims without deployed negative-test results would be misleading. Some docs are marked draft while executive summaries sound complete.

## 6. Thematic contribution to the book
Mandatory admission, policy-aware caching, multi-tenant state, orchestrator continuity, verification before claims, audit-based remediation.

## 7. Modernisation and technical debt review
Reassess LiteLLM/SDK/Gateway and protocol choices for current supported versions; require credentials and K8s policy tests before representing an implementation as secure. Contrast durable-framework capabilities with custom orchestration but do not retrofit frozen book architecture.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-040 — One Thread state manager | `uaf.zip/uaf/docs/architecture/design-doc-uaf-one-thread.md`:2 | id: design-doc-uaf-one-thread | durable-agent-execution | **A** | Ch 14, 36; D-15, D-27 |
| IA-041 — GovernanceGuard mandatory path | `uaf.zip/uaf/docs/architecture/design-doc-uaf-governance-guard.md`:235 | ### Scenario C: "GovernanceGuard Mandatory Pipeline" — UAF Approach | pre-action-governance | **A** | Ch 16, 19; D-10, D-18 |
| IA-042 — PII classification and tokenisation | `uaf.zip/uaf/docs/architecture/design-doc-uaf-governance-guard.md`:33 | \| **Tokenisation** \| Replacing a sensitive value with a non-reversible surrogate token (e.g., '"John Smith"' → '<name:a1b2c3d4>'). The token map is stored separately. \| | multi-stage-data-protection | **B** | Ch 13, 21; D-11, D-25 |
| IA-043 — Cache fencing by classification | `uaf.zip/uaf/docs/architecture/design-doc-uaf-governance-guard.md`:44 | \| **Cache Fencing** \| ADR-012 enforcement — L2/L3 classified data bypasses the semantic cache entirely. L0 is cached globally, L1 per-tenant. \| | memory-isolation | **A** | Ch 13, 21; D-11, D-25 |
| IA-044 — LLM Gateway routing and costs | `uaf.zip/uaf/docs/architecture/design-doc-uaf-llm-gateway.md`:2 | id: design-doc-uaf-llm-gateway | model-routing-admission | **B** | Ch 16, 20; D-17, D-26 |
| IA-045 — Task graph orchestration | `uaf.zip/uaf/docs/specs/task-graph-orchestration-spec.md`:2 | title: "Agent Orchestration Spec: Task Graph — UAF" | dependency-based-work-execution | **B** | Ch 14, 39; D-15, D-29 |
| IA-046 — Super-agent worker orchestration | `uaf.zip/uaf/docs/specs/super-agent-orchestration-spec.md`:2 | title: "Super-Agent Orchestration Spec — Autonomous UAF Development Pipeline" | bounded-agent-delegation | **B** | Ch 14, 15; D-15, D-20 |
| IA-047 — Connector framework contracts | `uaf.zip/uaf/docs/architecture/design-doc-uaf-connector-framework.md`:2 | id: design-doc-uaf-connector-framework | versioned-agent-contract | **B** | Ch 12, 22; D-09, D-21 |
| IA-048 — Governed lifecycle flow engine | `uaf.zip/uaf/docs/architecture/design-doc-uaf-flow-engine.md`:2 | id: design-doc-uaf-flow-engine | durable-agent-execution | **B** | Ch 14, 18; D-15, D-22 |
| IA-049 — Tenant separation design | `uaf.zip/uaf/docs/architecture/design-doc-uaf-multi-tenancy.md`:11 | - ADR-010 (Multi-Tenant Data Isolation) | memory-isolation | **A** | Ch 7, 13, 21; D-04, D-11 |
| IA-050 — Admin API test traceability | `uaf.zip/uaf/docs/project/test-traceability-matrix.md`:1 | # UAF Test Traceability Matrix | decision-to-evidence-chain | **B** | Ch 18, 39, 40; D-22, D-23 |
| IA-051 — Restart versus remediate adjudication | `uaf.zip/uaf/docs/research/audits/Restart_Or_Remediate_FINAL_Consolidated_Plan.md`:1 | # Restart or Remediate — FINAL Consolidated Report & Execution Plan | architecture-challenge-review | **D** | Ch 39, 40; D-29 |
| IA-052 — Implementation completeness denominator conflict | `uaf.zip/uaf/docs/research/audits/Restart_Or_Remediate_FINAL_Consolidated_Plan.md`:83 | \| 25 \| **HIGH (Process)** \| **The "93% done" headline is the wrong denominator.** Task-graph shows 106/113 tasks done (93%) — but only **4 of 35 epics done (11.4%)**. 'gen_dashboard.py' is computing right-ratio-o | evidence-claims-validation | **A** | Ch 18, 40; D-22, D-24 |
| IA-053 — Runtime security fallback findings | `uaf.zip/uaf/docs/research/audits/Restart_Or_Remediate_FINAL_Consolidated_Plan.md`:34 | The remediation path is **objectively cheaper** because every Critical/High finding is a bounded, file-locatable, single-edit fix. None require re-architecting Thread, Governance, Flow, LLM, Agent, or Gateway. | security-review-negative-evidence | **D** | Ch 16, 36, 48; D-18, D-27 |
| IA-054 — Design-coded tool and model contracts | `uaf.zip/uaf/docs/architecture/design-doc-uaf-agent-framework.md`:2 | id: design-doc-uaf-agent-framework | typed-agent-contract | **B** | Ch 12, 22; D-09, D-21 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Place independent audit findings beside design claims, so the reader can compare intent and implementation risk.
- Do not import possible credentials, internal chat logs, external service configurations or unsupported “production ready” assertions into public book sources.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?


---

