## Dossier — agentic-enterprise-reference-architecture-complete-v2

# Project dossier: Agentic Enterprise Reference Architecture — complete v2 — agentic-enterprise-reference-architecture-complete-v2.zip

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
Complete-v2 agent capability atlas, layered runtime anatomy, trust-chain framing, platform/solution selection workbook, technology comparison and operational readiness guidance.

## 2. Maturity and evidence boundary
371 files including 331 Markdown documents and 36 CSVs, plus spreadsheet workbooks. Largely research/reference design; product comparisons are snapshots requiring date and source checks.

- Archive entries (non-directory): **373**; captured text/source files: **370**; recognised code/config source files (approximate): **0**.
- **Reported status:** Reference design and candidate-selection artefacts; no full platform implementation.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Broad atomised capability taxonomy: user intent, identity, retrieval, planning, tools, memory, evaluation, governance, selection, operating model.

## 4. Distinctive strengths
Direct prior work on option appraisal, explicit when-not-to-use-agents decisions, weighted gates and PoC evidence. The selection workbook is a genuine structured artefact with seventeen sheets.

## 5. Weaknesses, contradictions and failure modes
Historical layer numbering is not the frozen E/T/C/L taxonomy; large product matrix can date quickly. Workbook sample uses illustrative Candidate A/B and must not be cited as field evidence.

## 6. Thematic contribution to the book
Capability-driven selection, must-pass gates, evidence-based weighting, build/buy choices, user and workflow segmentation.

## 7. Modernisation and technical debt review
Retain the process and decision rationale while refreshing vendor/protocol status before publication. Treat the workbook as companion research, never as a source for new frozen architecture rules.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-076 — Decision tree: whether an agent is needed | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/09-solution-selection-framework/selection-framework-complete.md`:8 | 2. Is an AI agent actually required? | adopt-or-decline | **A** | Ch 4, 5, 23; D-01, D-02 |
| IA-077 — Weighted platform selection method | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/09-solution-selection-framework/selection-framework-complete.md`:245 | ## 55. Weighted Platform Evaluation | weighted-option-appraisal | **A** | Ch 5, 23, 54; D-02, D-03 |
| IA-078 — Agent capability atlas | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/02-agent-capability-atlas/04-master-layer-matrices/README.md`:3 | \| Appendix \| Matrix \| Purpose \| | capability-to-requirement-mapping | **B** | Ch 5, 22, 54; D-02, D-21 |
| IA-079 — Agent autonomy spectrum | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/01-foundations/06-agent-autonomy-spectrum.md`:1 | ## 6. Agent Autonomy Spectrum | earned-autonomy | **A** | Ch 2, 9, 18; D-05, D-23 |
| IA-080 — Layered runtime anatomy | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/02-agent-runtime-anatomy/00-runtime-anatomy-overview.md`:3 | \| Layer \| Name \| Responsibility \| | layer-and-control-taxonomy | **B** | Ch 10, 11, 14; D-07, D-15 |
| IA-081 — AI Agent Trust Chain | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/05-ai-agent-trust-chain/threat-model.md`:1 | ## 35. Threat Model | delegation-identity-chain | **B** | Ch 15, 16; D-19, D-20 |
| IA-082 — Digital worker operating model | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/07-digital-worker-operating-model/incident-response.md`:1 | # Incident Response | team-boundary-operating-model | **A** | Ch 35, 37; D-06, D-28 |
| IA-083 — Decision playbooks | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/10-decision-playbooks/README.md`:14 | \| HR \| Policy Q&A with escalation \| Automated employment decisions \| | reusable-decision-playbooks | **A** | Ch 23, 41, 42; D-01, D-02 |
| IA-084 — Production readiness checklist | `agentic-enterprise-reference-architecture-complete-v2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/11-production-readiness/production-readiness-checklist.md`:1 | ## 52. Production Readiness Checklist | gated-authoring-execution | **B** | Ch 18, 33; D-22, D-23 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Preserve the original complete-v2 as historical source and the 17-sheet workbook as a derived selection research artefact.
- Do not copy historical layer numbering, unreviewed product ratings or stylised vendor details into frozen book decisions.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?



---

