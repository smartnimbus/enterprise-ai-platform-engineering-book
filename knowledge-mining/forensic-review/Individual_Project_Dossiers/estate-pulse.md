## Dossier — estate-pulse

# Project dossier: Estate Pulse — estate-pulse.zip

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
GKE-native estate intelligence and multi-source infrastructure ingestion; not an AI-agent platform. Its direct relevance is the discipline of evidence provenance, source adapters, recoverable worker execution, and platform ownership.

## 2. Maturity and evidence boundary
Implementation evidence exists: Python workers, API/UI, SQL migrations, Helm/Terraform and GitLab CI files. The 2026-08-07 HLD is explicitly a draft. Source presence does not prove deployed health, current coverage or test pass.

- Archive entries (non-directory): **167**; captured text/source files: **155**; recognised code/config source files (approximate): **107**.
- **Reported status:** Code-present but unexecuted in this review; design status varies by file.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Kubernetes API-as-Runner pattern, ephemeral Jobs and persistent collectors, PostgreSQL/JSONB data model and manifest-described workers.

## 4. Distinctive strengths
Fifteen named ADRs with context, decisions and consequences; worker manifests and code support real engineering review rather than purely conceptual description. Normalisation and run-status patterns are transferable.

## 5. Weaknesses, contradictions and failure modes
Some implementation decisions favour self-hosted state and a single worker image, creating rollback, patching and backup obligations. The source design references a real organisation; raw datasets, credentials and internal topology are not safe book inputs.

## 6. Thematic contribution to the book
Source-of-truth separation; declarative adapters; job/identity provenance; code-to-evidence traceability; bounded operational ownership.

## 7. Modernisation and technical debt review
Do not reuse Kaniko from ADR-010 without supply-chain review: the original project was archived in 2025. Compare actively maintained image-build options. Reassess self-managed PostgreSQL, IPFIX ingestion security, job persistence and asset data privacy against current cloud and internal policy.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-001 — API-as-Runner Kubernetes Jobs | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:74 | ## ADR-004 — API-as-Runner (direct K8s Jobs) over Argo/Celery/KEDA for worker orchestration | ephemeral-worker-execution | **B** | Ch 11, 14, 36; D-08, D-15 |
| IA-002 — Manifest auto-discovery of workers | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:221 | ## ADR-009 — Worker plugin pattern: worker.yaml auto-discovery | declarative-tool-onboarding | **B** | Ch 12, 29, 44; D-09, D-29 |
| IA-003 — Hybrid SQL plus JSONB lineage | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:116 | ## ADR-005 — Hybrid SQL + JSONB over pure relational or pure document model | structured-unstructured-provenance | **B** | Ch 13, 17, 57; D-14, D-24 |
| IA-004 — Federated workload identity ownership | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:296 | ## ADR-011 — create_gsa: false for GSAs owned by jlp-jvp-wif (ADR-031 federated pattern) | identity-sovereignty | **B** | Ch 15, 27, 35; D-19, D-20 |
| IA-005 — Infrastructure and platform authority split | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:328 | ## ADR-012 — Infra Terraform lives in estate-pulse/infra/, not jlp-jvp-wif | control-ownership-boundaries | **B** | Ch 6, 35, 39; D-06, D-29 |
| IA-006 — RVTools and vRLI heterogeneous ingestion | `estate-pulse-main.zip/estate-pulse-main/docs/WORKERS.md`:16 | ## RVTools ingest — ephemeral storage Q&A | heterogeneous-data-ingestion | **B** | Ch 13, 28, 57; D-11, D-14 |
| IA-007 — IPFIX direct collection alternative | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:142 | ## ADR-006 — IPFIX over vRLI-only for flow collection | source-capability-selection | **D** | Ch 5, 13; D-02, D-14 |
| IA-008 — SSE rather than WebSockets for logs | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:379 | ## ADR-014 — SSE over WebSocket for log streaming | right-sized-streaming-contract | **E** | Ch 17, 36; D-17, D-24 |
| IA-009 — GKE stateful database over Cloud SQL | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:6 | ## ADR-001 — GKE Autopilot over Cloud SQL for PostgreSQL | ownership-vs-managed-services | **D** | Ch 5, 36; D-02, D-27 |
| IA-010 — Log retention in relational store | `estate-pulse-main.zip/estate-pulse-main/docs/DECISIONS.md`:355 | ## ADR-013 — Log persistence in PostgreSQL over external log aggregation | operational-evidence-retention | **B** | Ch 17, 40; D-24, D-25 |
| IA-011 — Worker execution RBAC and status | `estate-pulse-main.zip/estate-pulse-main/CONTEXT.md`:197 | ### Job status model (tbl_script_runs) | workload-identity-traceability | **B** | Ch 15, 17, 35; D-19, D-24 |
| IA-012 — Self-contained operational context document | `estate-pulse-main.zip/estate-pulse-main/CONTEXT.md`:3 | > Machine + human readable technical state document. | repository-continuity | **E** | Ch 39, 52; D-29 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Keep both ZIP original hashes in the preservation ledger. `estate-pulse.zip` and `estate-pulse-main.zip` have **identical 167 non-directory file payload hashes**, therefore choose one archival content copy with two source-package references.
- Curate source ingestion, job lineage and ADR case extracts as **supporting examples** after confidentiality review. Do not publish real customer, organisation, IP, credential or server data.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?



---

