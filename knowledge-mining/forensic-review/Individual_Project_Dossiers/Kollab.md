## Dossier — Kollab

# Project dossier: Kollab — Kollab.zip

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
Cloud-agnostic, multi-user collaboration environment where domain experts and specialist agents form Mission Control workspaces, debate, perform long tasks and share governed memory.

## 2. Maturity and evidence boundary
Detailed design collection with v2 platform specification and deep dives, not accompanied by substantive runnable platform source in the archive. Feasibility and performance claims are proposed, not demonstrated.

- Archive entries (non-directory): **136**; captured text/source files: **80**; recognised code/config source files (approximate): **0**.
- **Reported status:** Design/reference; production status unverified.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Collaborative agent workspaces, multi-hop identity, interception hooks, memory tiers, event protocol manifests, budget guards, chaos/recovery testing.

## 4. Distinctive strengths
Clear connection between human/team ownership, long-running tasks, agent contracts, budget circuit breakers and operational resilience. The protocol and FinOps chapters address practical integration concerns.

## 5. Weaknesses, contradictions and failure modes
Formal convergence guarantees and numerical efficiency claims depend on external research and cannot be transferred as author-proven results. “27-event hook system” is a design count, not validated implementation. Large Notes/all compilation may duplicate smaller notes.

## 6. Thematic contribution to the book
Mission control, bounded deliberation, tenant/agent memory isolation, action interception, cost-attributed reasoning.

## 7. Modernisation and technical debt review
Assess DAAP against current MCP/A2A/AG-UI/OpenAPI contracts before recommending it as an interoperability standard. Prefer proven orchestration and checkpoint primitives when implementation requirements match, while retaining protocol-agnostic contracts.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-025 — Mission Control collaborative workspace | `Kollab.zip/Kollab/docs/architecture/kollab-platform-spec-v2.md`:5 | > **Abstract:** This document specifies the complete architecture for Kollab—a cloud-agnostic, open-source platform where specialized AI agents assemble with human experts in collaborative "Mission Control" workspac | human-agent-shared-workspace | **B** | Ch 6, 14, 35; D-06, D-15 |
| IA-026 — Domain-Agnostic Agent Protocol | `Kollab.zip/Kollab/docs/architecture/domain-agnostic-protocol.md`:1 | # Kollab Domain-Agnostic Agent Protocol (DAAP) | versioned-agent-contract | **B** | Ch 22, 53; D-21 |
| IA-027 — Dynamic agent marketplace provisioning | `Kollab.zip/Kollab/docs/architecture/dynamic-agents-marketplace.md`:1 | # Kollab Dynamic Agents & Marketplace | controlled-agent-provisioning | **B** | Ch 12, 29; D-09, D-29 |
| IA-028 — Long-running requests and checkpoints | `Kollab.zip/Kollab/docs/architecture/long-running-requests.md`:25 | ### Pattern 1: Checkpoint-and-Resume | durable-agent-execution | **A** | Ch 14, 36; D-15, D-27 |
| IA-029 — Lifecycle hooks for agent interception | `Kollab.zip/Kollab/docs/architecture/agent-runtime-security.md`:5 | > **Abstract:** This document specifies the complete security architecture for the Kollab agent runtime—the foundation upon which the platform’s governance, identity, and compliance controls depend. Before guardrail | deterministic-interception | **A** | Ch 16, 21; D-10, D-18 |
| IA-030 — Four-point sensitive data pipeline | `Kollab.zip/Kollab/docs/architecture/agent-runtime-security.md`:5 | > **Abstract:** This document specifies the complete security architecture for the Kollab agent runtime—the foundation upon which the platform’s governance, identity, and compliance controls depend. Before guardrail | multi-stage-data-protection | **B** | Ch 13, 21; D-11, D-25 |
| IA-031 — Multi-hop on-behalf-of identity | `Kollab.zip/Kollab/docs/architecture/agent-runtime-security.md`:5 | > **Abstract:** This document specifies the complete security architecture for the Kollab agent runtime—the foundation upon which the platform’s governance, identity, and compliance controls depend. Before guardrail | scope-attenuated-delegation | **A** | Ch 15, 16; D-19, D-20 |
| IA-032 — Debate convergence engine | `Kollab.zip/Kollab/docs/deep-dives/debate-convergence-engine.md`:1 | # Kollab Debate & Convergence Engine | bounded-collaborative-deliberation | **C** | Ch 14, 18; D-13, D-22 |
| IA-033 — Evidence citation protocol | `Kollab.zip/Kollab/docs/deep-dives/debate-convergence-engine.md`:5 | > **Abstract:** This document provides the formal specification for the Kollab Debate Engine—the architectural centerpiece that transforms a Mission Control from a collection of independent agents into a collaborati | evidence-lineage-continuity | **B** | Ch 13, 17; D-14, D-24 |
| IA-034 — Agent cost attribution ledger | `Kollab.zip/Kollab/docs/deep-dives/cost-billing.md`:5 | > **Abstract:** This document specifies the complete cost optimization and billing architecture for Kollab. Agentic AI has fundamentally broken traditional pricing models: where a single LLM call has predictable cos | cost-per-task-attribution | **A** | Ch 20, 38, 57; D-26 |
| IA-035 — Cost-based runtime circuit breakers | `Kollab.zip/Kollab/docs/deep-dives/cost-billing.md`:5 | > **Abstract:** This document specifies the complete cost optimization and billing architecture for Kollab. Agentic AI has fundamentally broken traditional pricing models: where a single LLM call has predictable cos | economic-admission-control | **A** | Ch 20, 38; D-26 |
| IA-036 — Chaos testing for multi-agent systems | `Kollab.zip/Kollab/docs/deep-dives/chaos-engineering.md`:1 | # Kollab Chaos Engineering & Agent Reliability Testing | failure-injection-verification | **B** | Ch 18, 36, 47; D-22, D-27 |
| IA-037 — Multi-user tenant memory boundaries | `Kollab.zip/Kollab/docs/architecture/memory-architecture.md`:5 | > **Abstract:** This document specifies the complete memory architecture for Kollab. Memory is not an afterthought—it is the foundation that enables Mission Control sessions to maintain coherent context, share knowl | memory-isolation | **A** | Ch 13, 21; D-12, D-13 |
| IA-038 — FinOps outcome unit economics | `Kollab.zip/Kollab/docs/deep-dives/finops.md`:232 | The council operates on a publish‑and‑track cadence: every new agent persona deployed to production publishes its cost profile (expected CPT, expected cost per task, budget per session) and the council reviews actua | cost-per-task-attribution | **B** | Ch 20, 38; D-26 |
| IA-039 — Deployment profiles and data recovery | `Kollab.zip/Kollab/docs/supporting/deployment-profiles.md`:1 | # Kollab Deployment Profiles | deployment-sovereignty | **B** | Ch 7, 36; D-04, D-27 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Preserve original design documents with archival status and add book-specific extract records, rather than copying wholesale into the governing manuscript repository.
- Require verification before claiming hook counts, performance savings, safe convergence or deployed security.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?



---

