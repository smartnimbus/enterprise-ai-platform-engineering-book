# Master forensic review — historical architecture and intellectual capital

**Source:** Nine uploaded archives. **Date:** 24 November 2026. **Authority:** Research only, no change to frozen book.

**Navigation:** Nine source dossiers follow the synthesis and modernisation material; detailed source-level evidence, 86 concepts and the complete graph are provided as CSV/GraphML in the package.



---

## Scope, coverage and limitations

# Forensic method, coverage and limitations

**Assessment date:** 24 November 2026. **Input:** Nine uploaded archives. **Purpose:** Preserve historic intellectual capital without editing the frozen book. **No executable code was run from the user archives.**

## Coverage

1. Opened and inventoried all nine archives, including two 7z packages using libarchive; preserved original archive SHA-256 and per-member source SHA-256 for extracted text.
2. Enumerated every non-directory archive member and classified into extracted source/text, development metadata, binary, empty or oversize. All extracted text files were processed for content heading/link indices. No `.git` pack stores or binary libraries were treated as primary authored documents.
3. Examined engineering documents, ADRs, workshop materials, design specifications, code manifests, scripts, schema and high-value substantive notes; created 86 manually curated concept entries with an exact source-file, SHA-256, text anchor and line number, all successfully matched to their source files.
4. Compared duplicate/sibling archive file hashes; created explicit content-difference findings.
5. Parsed UAF draw.io source XML (ten first-party diagrams) and extracted labels and page/cell counts. Other diagram drawings exist in Markdown/Mermaid and have been indexed textually. AEGIS's 220-page PDF was rendered for visual inspection and extracted to searchable text; the PDF cover and representative content were examined. The full PDF text was indexed for term searches, not individually typeset-page-reviewed.
6. Opened the reference architecture's seventeen-sheet solution-selection workbook using the spreadsheet reader; checked dashboard, requirements, gate classifications, capability mappings, weights, scoring, example PoC and decision record. These are workbook examples, not independently evidenced product measurements.
7. Classified sources' claims as design, documented ADR, code-present, audit finding, historical reference, or scaffold. Source code presence was distinguished from tested or deployed status.
8. Built a graph of project→concept→pattern→Decision Atlas ID→architecture→chapter and publication mapping; the graph includes 86 extracted concepts, not every incidental term in the reference collection.

## Where the review is not exhaustive

- **Not every word of every document received a manual technical review.** Thousands of text/source files were systematically opened and indexed, but intensive human-style analysis was concentrated on representative, high-value first-party documents, AD​Rs, workshops, and relevant source code. Treat this as a substantial source-anchored first-pass forensic review rather than a certified line-by-line audit of every file.
- **Binary workbooks, images and PDF pages were not all manually inspected.** Four large workshop source-data workbooks were identified and classified as restricted potential enterprise data; they were not subjected to cell-by-cell analysis or copied into this deliverable. Third-party reference screenshots were not individually assessed for content ownership.
- **No compiled code, package install, integration service, cloud deployment or security control was executed.** Static source and audit claims do not establish operating readiness.
- **Archived Git internals were inventoried, not replayed as complete branch/commit histories.** UAF and MemOS contain substantial repository object material; extracted working trees and historical write-ups do not prove an exhaustive Git evolution chronology.
- **Internet-linked references were not recursively downloaded in bulk.** Local Markdown references were enumerated, with unresolved link targets retained for review. External links are outside the frozen archive evidence scope.
- **Automated link reports contain false positives**, including paths that point to GitHub, excluded dependencies, generated files, alternate export roots or renamed documents. Unresolved does not mean broken in the original workspace.
- **Authorship and copyright were not independently verified.** Source-internal names, copyright notices, dates and claims are evidence to investigate, not proof of ownership.
- **Claims that the archives represent multiple years cannot be independently validated from these files alone.** Most explicit dates visible in the analysed snapshots fall in April–August 2026; some work may have earlier provenance not included in these uploads.

## Traceability and confidence

- `archive_summary.json`: physical archive counts and SHA-256.
- `file_manifest.csv`: every archive file, size, extension, classification, per-text-member SHA-256.
- `Document_Headings_Index.csv`: all captured Markdown headings with source lines.
- `Reference_Link_Audit.csv`: relative Markdown links resolved against the extracted snapshot.
- `Intellectual_Asset_Register.csv`: 86 validated concept-to-source and book mappings with a specific evidence excerpt.
- `Visual_Artifact_Inspection.csv`: diagram names, XML structure and first-party labels; binary assets enumerated.
- `Knowledge_Graph_Nodes.csv`, `Knowledge_Graph_Edges.csv`, `.graphml`: attributed conceptual genealogy, with thematic links explicitly editorial rather than direct citations.

**Confidence scale:** `DIRECT SOURCE` = exact file/text content matched; `DESIGN CLAIM` = a design description without independent runtime proof; `CODE PRESENT` = implementation source found but not executed; `AUDIT CLAIM` = source report's finding, not independently re-tested; `INTERPRETATION` = editorial relevance or chronological extrapolation.

## Security and intellectual-property cautions

The workshop archive includes application/server mapping workbooks and the Estate Pulse documents mention real enterprise infrastructure. The MemOS reference tree includes third-party material. The AEGIS PDF expressly includes a copyright and publication disclaimer. The book repository is public; no original archive contents should be uploaded there without explicit security, confidentiality and intellectual-property review.



---

## Cross-project synthesis

# Cross-project synthesis — provenance-led intellectual history

## Executive methodology and boundary

Nine physical archives were inventoried; two are exact duplicates at the file level and two are closely related historical versions. The intellectual asset register contains 86 curated source-anchored concept entries; these are **not** claims that each idea was invented by the author. The full file inventory includes thousands of vendored references, configuration files and binary resources, which should not be confused with independently authored concepts.

No frozen architecture, chapters, Decision Atlas definitions or Meridian identifiers were changed. Historical architectural conflicts are recorded as lineage, not silently reconciled.

## What recurs across independent project families

| Cross-project pattern | Distinct project families | Why it matters |
|---|---:|---|
| evidence-lineage-continuity | 4 | AE;KO;ME;WS — corroborating concept IDs and file references are in the asset register |
| architecture-challenge-review | 3 | ME;UA;WS — corroborating concept IDs and file references are in the asset register |
| decision-to-evidence-chain | 3 | AE;UA;WS — corroborating concept IDs and file references are in the asset register |
| memory-isolation | 3 | KO;UA;WS — corroborating concept IDs and file references are in the asset register |
| multi-stage-data-protection | 3 | KO;ME;UA — corroborating concept IDs and file references are in the asset register |
| versioned-agent-contract | 3 | KO;ME;UA — corroborating concept IDs and file references are in the asset register |
| bounded-collaborative-deliberation | 2 | AE;KO — corroborating concept IDs and file references are in the asset register |
| cross-role-design-challenge | 2 | ME;WS — corroborating concept IDs and file references are in the asset register |
| declarative-tool-onboarding | 2 | EP;WS — corroborating concept IDs and file references are in the asset register |
| delegation-identity-chain | 2 | AE;RA — corroborating concept IDs and file references are in the asset register |
| durable-agent-execution | 2 | KO;UA — corroborating concept IDs and file references are in the asset register |
| evidence-claims-validation | 2 | ME;UA — corroborating concept IDs and file references are in the asset register |
| gated-authoring-execution | 2 | ME;RA — corroborating concept IDs and file references are in the asset register |
| identity-sovereignty | 2 | EP;WS — corroborating concept IDs and file references are in the asset register |
| policy-as-runtime-control | 2 | AE;WS — corroborating concept IDs and file references are in the asset register |
| pre-action-governance | 2 | AE;UA — corroborating concept IDs and file references are in the asset register |
| structured-unstructured-provenance | 2 | EP;WS — corroborating concept IDs and file references are in the asset register |
| team-boundary-operating-model | 2 | RA;WS — corroborating concept IDs and file references are in the asset register |

## Six persistent architectural philosophies

### 1. Intent must not be confused with authority
The AEGIS interception concept, UAF GovernanceGuard, Kollab lifecycle hooks, and workshop workload-identity ADRs repeatedly separate a model’s proposed action from the privilege required to execute it. The convergence is stronger than any single product name; it supports frozen D-10, D-18 and D-20, provided actual enforcement tests are not inferred from design documents.

### 2. Enterprise truth requires provenance and tolerated disagreement
AEGIS explicitly treats durable disagreement as an asset. Kollab ties collective reasoning to evidence citation. MemOS specifies bitemporal memory and erasure. Estate Pulse processes heterogeneous source facts in an operational database. Together these offer a differentiated philosophical argument: retrieval relevance, entity identity, temporal validity and source authority are different questions. This informs Chapter 13, D-11/D-12/D-14 without adding new Context architecture.

### 3. An operating system is a governed continuity problem
Kollab long-running tasks, UAF One Thread, MemOS persistent state and Estate Pulse worker status all address work that spans independent executions. The unresolved engineering issue is not whether checkpoints exist, but whether state, permissions, policies and outstanding side effects can be reconstructed after interruption. This supports Chapters 14 and 36; formal replay claims must be tested.

### 4. Decisions should leave evidence rather than prose alone
Estate Pulse’s ADRs, Workshop’s 38 design ADRs, UAF audit and task-traceability matrices, and the reference architecture’s 17-sheet selection workbook all converge on explicit options, gates, proof and review. This is the most defensible lineage for the frozen 30-decision Atlas. It does not establish exclusive ownership of the general ADR method.

### 5. Bounded economics is part of safety
Kollab’s cost ledger and runtime budget circuit breakers, AEGIS economic governance, UAF model routing, and the agent selection workbook connect cost to autonomy and operational ownership. The reusable idea is measurable cost per successful outcome, not arbitrary token saving. This maps to D-26 and Chapters 20/38.

### 6. The lifecycle should include reversibility and retirement
The workshop enterprise lifecycle explicitly runs to decommission; the older selection reference asks if an agent is justified at all. Estate Pulse documents operational dependencies and ownership costs. The frozen book’s D-30 and Chapters 49–50 can be supported by this lineage without inventing a new decision.

## The negative evidence is unusually valuable
UAF’s independent remediation report documents why reported task completion cannot substitute for implementation readiness. MemOS’s audit distinguishes a largely completed GitHub-spec scaffolding from an unfinished product. AEGIS contains manuscript-ready prose but no verified runtime. These counterexamples are valuable to an honest technical author: do not assert successful production behaviour because a blueprint or diagram depicts it.

## Prior art and ownability
Neither “agent fabric,” “memory plane,” “gateway,” “identity chain,” nor “governance guard” should be represented as newly invented simply because they recur. Potentially ownable assets include a carefully selected and explained decision collection, original figures, original evidence cases, editorial synthesis and prose—subject to authorship verification. Distinctiveness is in the decision-to-evidence teaching method, not universal control-plane primitives.

## Fictional-world consistency
AEGIS contains an earlier Helios Financial Group narrative and a separate CommerceOps reference in its interior draft. They are historical evidence, not approved Meridian case material. No old person, transaction, incident or timestamp should be lifted into the frozen Meridian fixture without independent, explicit change authorisation.

## Duplication and version control
- Estate Pulse ZIP payloads are identical across 167 files. This is one content lineage represented by two packages.
- Complete-v2 and final-V2 reference archives share 371 common file paths but differ in ten paths, including the principal architecture document, manifest, runtime-layer files and installer. Keep both snapshots and a delta ledger; names are insufficient to establish authority.
- `Kollab/Notes/all/all.md` is a 1.43 MB aggregate and should not be counted as independent corroboration of smaller note files.
- MemOS contains a very large `ref/awesome-copilot` vendored library; it should be indexed for provenance but excluded from original authorship claims.

## Bottom-line editorial recommendation
Preserve all sources immutably. Publish no raw archive into the public book repo. Curate evidence-backed quotations, diagrams redrawn from approved source and rights-cleared extracts. The current frozen architecture, chapter map, decisions and Meridian fixture stay authoritative. The extracted intellectual history should act as a research genealogy, not a competing architecture baseline.



---

## Timeline and intellectual evolution

# Timeline and concept evolution

## Evidence-led chronology

**Important:** The uploaded snapshots are rich but do not establish the full years-long chronology asserted in the request. The file contents support dated snapshots mainly during 2026. Dates below are taken from source metadata or headings; they are not inferred creation dates of the ideas themselves.

| Period evidenced | Archive family | What the documents show | Status of chronology |
|---|---|---|---|
| April 2026 | UAF | Design documents dated 8 April, orchestration research and an independent remediation consolidation dated 22 April. One Thread, GovernanceGuard and gateway/control contracts are mature as design descriptions; audit reports severe code/config gaps. | Dated documentation and audit, not independently verified deployment |
| April–May 2026 | Workshop/UAF v4 | Enterprise lifecycle document reports draft v2.3 dated 15 April; workshop PRD and individual ADRs are dated 18 May. Agent-assisted discovery, challenged ADRs and decommission are already explicit. | Dated proposal/decision records |
| May 2026 | Kollab | Platform v2 and deep dives identify collaborative Mission Control, identity delegation, memory, long-running tasks, debate, cost and chaos testing. | Dated designs, no full implementation proof |
| 17–21 May 2026 | MemOS | Audit dated 17 May, workshop documents, ADR system and archived workspace on 21 May. The audit separates completed scaffolding from missing memory platform work. | Dated audit and archive snapshot |
| 2026, internally revised | AEGIS | v1–v3 folders, foundation packs, eight runtime sequences, v0.7 220-page interior PDF with 2026 copyright. Exact dates of earlier ideation are not proved by version labels. | Version lineage, incomplete dated history |
| 2026, v2 variants | Agentic Enterprise Reference Architecture | Complete-v2 and final-V2 share 371 paths; ten paths differ in hashes/additions/deletions. Selection framework and seventeen-sheet workbook document the evolution toward decision tooling. | Version difference verified, chronology order inferred only from naming |
| August 2026 | Estate Pulse | ADR-001 dated 5 August, context status 6 August and HLD draft 7 August. Code/worker manifests and CI files support a concrete infrastructure intelligence implementation baseline. | Dated engineering docs; live deployment unverified |
| November 2026 | Frozen book programme (not one of the nine historical archives) | Four Structural Layers, eight Control Planes, 58 chapters, 30 decisions and Meridian Fixture v1.0 are the ratified manuscript authority. | Supplied programme context; not overridden here |

## Concepts that appear forward-looking *within these sources*

The strongest forward-looking proposals address **institutional memory and accountability**, not merely adding agents: append-only provenance combined with explicit correction/erasure, preserving unresolved disagreement, linking an action's authorisation to a side-effect receipt, and constraining deliberation by budget. These would have demanded careful engineering before the corresponding product features were widely integrated; they are **not claimed to precede all industry prior art**.

## Concepts already mainstream or available in industry by late 2026

- Agent tool invocation and runtime orchestration, including checkpoint-capable workflow engines.
- MCP and Agent2Agent interoperability patterns, although security and adoption vary by version.
- Identity federation, OIDC, WIF, signed scopes and on-behalf-of concepts.
- Observability through OpenTelemetry and correlated traces.
- RAG/semantic retrieval, vector indexes and retrieval ACLs as standard design subjects.
- Cloud platform product catalogues and managed agent-runtime offerings.

The manuscripts should not present these primitives as new inventions. The potential originality is how the decision, evidence, ownership and lifecycle chain is taught.

## Ideas now questionable or obsolete as *defaults*

- **Original Kaniko upstream** as a default image builder without reviewing maintenance/security successors.
- Agent autonomy assessed by number of prompts/tools alone, without operational authority and outcome evidence.
- Protocol proliferation without explicit compatibility, versioning and identity boundaries.
- Directly copying hypothetical benchmark percentages as platform performance proof.
- Assuming generated architecture documentation or “spec complete” scores measure deployment readiness.
- Treating a vector-store result as verified enterprise truth or a stored memory as inherently permanent/accurate.
- Reusing earlier competing architectural taxonomies in the frozen current manuscript.

## Evolution that should be retained as intellectual history

1. **Agent anatomy → enterprise capability selection:** Early reference material enumerates capabilities and compares products; the later decision method insists on whether an agent is needed and evidence before procurement.
2. **Prompt instruction → interceptable control:** AEGIS and UAF/GovernanceGuard make the distinction between model intent and enforced admission increasingly explicit.
3. **Retrieved knowledge → governed institutional memory:** MemOS temporal schema, Kollab tenant memory and AEGIS disagreement preservation converge on source authority, provenance and retention.
4. **Individual orchestration → operational continuity:** UAF One Thread, Kollab durable work and Estate Pulse worker status support a richer discussion of resumption, replay and side effects.
5. **Cost dashboards → economic control:** Kollab budget circuit breakers and outcome attribution strengthen the idea that autonomy must be economically bounded.
6. **Architecture presentation → decision evidence:** ADR systems, audits and the seventeen-sheet selection workbook show a movement from descriptive diagrams toward falsifiable claims and review gates.
7. **Build → operate → retire:** The workshop’s concept-to-decommission lifecycle provides historical precedent for the frozen book’s retirement decision and playbooks.

## Editorial safeguards

- Do not attribute a 2026 first appearance date to an idea without earlier source proof.
- Distinguish “author mentioned in an earlier manuscript” from “author invented the industry concept.”
- Preserve prior fiction (Helios and CommerceOps) as historical rather than mixing it into Meridian.
- Use the current frozen decision IDs and chapter structure exclusively in new manuscript work.



---

## Modernisation assessment

# Modernisation Assessment — historical source versus 2026 applicability

**Status:** Research assessment, not an instruction to redesign the frozen book. **Cut-off:** 24 November 2026. Source paths and claim-status flags are in `Intellectual_Asset_Register.csv` and the nine dossiers. Current vendor-specific guidance is to be reverified at point of manuscript publication.

## Decision rule

A historical idea is **retain** when its mechanism survives a vendor or framework change; **reinterpret** when the requirement survives but its implementation or terminology has changed; **retire** when it conflicts with the book's frozen authority or has no credible application; and **verify** when the source makes a performance, product support, regulatory or deployment claim without a contemporaneous primary-source proof. An old technical choice is not automatically obsolete merely because a new cloud product exists.

## Estate Pulse

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| API-as-Runner launches Kubernetes Jobs on demand | **Retain pattern**, evaluate runtime constraints | Job-owner attribution, bounded execution, idempotency and recovery | Compare Jobs with durable workflow service if retries and process continuity become complex; keep project-specific workload separation |
| `worker.yaml` auto-discovery | **Retain pattern** | Declarative onboarding contract | Verify manifest signing, admission, schemas and dangerous worker privileges |
| GKE-managed PostgreSQL StatefulSet instead of Cloud SQL | **Conditional** | Operational-versus-managed ownership trade-off | Reassess backup, patching, SLA, PITR and recovery ownership rather than copying the old default |
| Kaniko image build (ADR-010) | **Review urgently** | Rootless/daemonless secure-build principle | Original upstream Kaniko was archived in 2025; reassess BuildKit/Buildah/maintained forks and signed release provenance |
| Keycloak identities and WIF-owned service accounts | **Retain boundary** | IdP authority, account ownership and workload provenance | Verify approved IdP versions, token audiences and federated IAM rules |
| vRLI and IPFIX ingestion | **Retain abstraction** | Source-specific ingestion, timestamps, raw observations and provenance | Verify vendor support, collection permissions and flow-data minimisation |
| Persistent logs in primary relational store | **Conditional** | Evidence correlation and operational access | Evaluate immutable retention, separation of duties and tamper-evident logs |

## AEGIS

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| Eight-plane cognitive architecture | **Historical only** | The underlying concern for authority and evidence | Do not introduce it as an alternate set of book Control Planes |
| “Cognition is not trusted by default” | **Retain claim only with mechanics** | Interception, bounded delegation, denial, observable consequence | Demonstrate with frozen Gateway events and negative tests |
| Append-only cognition spine | **Reinterpret** | Separate operational event log from tentative durable memory | Append-only evidence is not the same as immutable truth or erasable customer data |
| Replayable governance decisions | **Conditional** | Correlation, policy version and signed evidence concepts | Formal replay must account for external side effects and non-deterministic model responses |
| Formal debate/convergence | **Verify/limit** | Structured disagreement, citations, bounded deliberation | Do not claim safe consensus or quantitative uplift without verified experimental methods |
| Helios fictional storyline | **Retire from book** | Historical creative lineage | Meridian Financial remains frozen; preserve old manuscript only as dated history |
| Large multi-party sequence visuals | **Rework for accessibility before reuse** | Exact actor-and-evidence choreography | Split into diagram types/limits allowed by Style Bible v1.2; check rights and source fonts |

## Kollab

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| Proprietary DAAP manifest/protocol proposal | **Reinterpret** | Versioned role and handoff contracts | Check current MCP/A2A/AG-UI conventions; no assertion DAAP is adopted standard |
| 27 lifecycle interception events | **Verify** | Pre- and post-action trust boundaries | Count represents specification, not independently verified runtime hook completeness |
| Collaborative debates and convergence | **Conditional** | Counterargument and dissent ledger | Demonstrate stopping, provenance, selection bias and budget; avoid unverified speed/accuracy percentages |
| Multi-tenant shared memory | **Retain boundary** | Principal/tenant ACL, provenance, minimisation | Require separate consent, deletion and cross-tenant negative tests |
| Layered token and tool budgets | **Retain principle** | Cost-per-outcome and per-tenant guardrails | Integrate caching/routing rules only when policy and outcome metrics support them |
| Long-running Mission Control tasks | **Retain principle** | Durable checkpoints and human intervention | Compare with supported workflow engines and current SDK checkpoint semantics |

## Unified Agent Fabric (UAF)

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| GovernanceGuard as mandatory non-bypassable pipeline | **Evidence-first verification** | Policy enforcement boundary | Audit reports serious implementation gaps; do not claim design equals deployed control |
| `One Thread` custom persistence | **Retain concept, evaluate implementation** | State, authority, resumption, expiry and external side effects | Supported durable execution/checkpoint options may reduce custom code; validate lifecycle invariants |
| Cached PII masking/tokenisation | **Retain with constraints** | Classified data fencing and token map access | Compare current cryptographic/privacy requirements; avoid reversible token claims without key custody proof |
| LLM Gateway provider routing | **Reinterpret** | Model admission, rate/cost controls, provider failure isolation | Do not confuse model gateway with Gateway admission of mutable external actions |
| Multi-agent A2A and MCP adapters | **Verify current protocols** | Typed versioned interface contracts | Pin protocol versions and supported scopes, fail-open/fail-closed behaviours |
| Reported 93% task completion | **Do not reuse as readiness proof** | Separate task, epic, test and operational denominators | Audit explicitly contrasted 106/113 tasks with 4/35 epics and serious remaining defects |
| Production-ready posture in conceptual docs | **Not demonstrated** | Design-to-evidence discipline | Require runtime negative tests, persistent state and secret/key reviews |

## MemOS

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| Bitemporal memory schema | **Retain** | Effective/observation times and provenance | Verify temporal queries, correction semantics and immutable audit versions |
| SQLite+FTS5+vector locally; PostgreSQL+pgvector in cloud | **Conditional** | Portable data model and sync strategy | Synchronisation, encryption, vector extension support and conflict resolution remain substantial engineering work |
| MCP memory service | **Revalidate interface** | Controlled memory access with caller identity | Confirm MCP version and authorisation at boundaries |
| Cryptographic erasure of memory | **Verify strictly** | Data deletion evidence and key lifecycle | Backups, replicas, embeddings and third-party copies affect outcome; do not claim universal deletion |
| AI-driven multi-role workshop and `/fleet` | **Reinterpret as facilitation** | Independent reviews and challenge roles | Autogenerated deliverables need accountable human acceptance and evidence checks |
| Audit reports 85% completeness | **Restrict claim** | Scaffolding progress | Not evidence of 85% finished operational memory platform |

## Workshop/UAF v4

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| Enterprise workshop in 2–3 hours replacing 6–12 weeks | **Unsupported impact claim** | Structured intake and question sequencing | Conduct representative before/after studies before citing time saving |
| Agent team challenges and standards cascade | **Retain** | Cross-role review/ownership/approval | Clearly distinguish machine-proposed findings from approved architecture |
| Cloud-native GCP, model/orchestration stack | **Review dependencies** | Workload identity, lifecycle and source contracts | Update SDK/platform names/versions and assess vendor maturity |
| Real enterprise asset workbooks | **Research, restricted** | Provenance and data-quality questions | No identifiable records, IPs or internal estate exports in public manuscript repository |
| Draft architecture and accepted ADRs | **Retain provenance** | Choice and alternatives with timestamp | “Accepted” does not equal “deployed”; source assumptions must be dated |

## Agentic reference architecture — complete-v2 and final-V2

| Historical design/assumption | Current assessment | Preserve | Revalidation or replacement |
|---|---|---|---|
| -1 to 13+ runtime layer numbering | **Historical** | Atomic capability taxonomy | Must not overwrite frozen four Structural Layers/eight Control Planes |
| Weighted solution selection workbook | **Retain methodology** | Hard gates, weighting, penalties, PoC results, decision record | Validate formulas, illustrative data and bias in criteria before public templates |
| Product capability matrices | **Update before publication** | Question vocabulary and requirements mapping | Vendor names, product support and pricing change rapidly; dated citations essential |
| Security/identity/trust chain | **Retain design lineage** | Delegation constraints and threat questions | Apply current standards and frozen decisions rather than historical taxonomy |
| Final-v2 variant | **Preserve as explicit delta** | Example of source reconciliation | Ten changed/added/removed paths require version-specific references |

## Externally checked developments (November 2026)

- Google Cloud introduced **Gemini Enterprise Agent Platform** in 2026, superseding many former Vertex AI product labels. This affects historical vendor terminology, not the book's architectural model. Primary source: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
- The original GoogleContainerTools Kaniko repository was archived in 2025; maintained successors and alternative builders have different support/patch profiles. Primary source: https://github.com/chainguard-forks/kaniko
- LangGraph includes checkpointer/durable state primitives, useful as a comparator for historical custom flow runtimes. Primary source: https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint
- Current Google agent-platform documentation supports MCP/A2A integration patterns, but **current protocol compatibility and security behaviours must still be independently verified**: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent

**Modernisation does not imply an architecture change.** These findings are time-stamped editorial notes for checking statements during manuscript development.



---

## Knowledge graph

# Master Knowledge Graph — how to read and use it

The source-derived register contains **86 curated concepts**, distributed across eight distinct project identifiers plus one intentionally duplicated Estate Pulse package. The graph contains **255 nodes and 1,009 directed edges**; these are relationships for editorial traceability, not evidence that historical diagrams themselves were implemented.

## Graph schema

```text
Project (source family)
  └─contains→ Concept (IA-###)
       └─instantiates→ Pattern (controlled thematic label)
            └─informs→ Decision (existing D-01..D-30)
                 └─governed_area→ Architecture (frozen 4L or 8P)
                      └─context_for→ Chapter (frozen 1..58)
                           └─cross_references→ AtlasPage (existing D-###)
```

Additional `Pattern → Chapter`, `Pattern → Architecture`, and `Decision → Chapter` links preserve direct mappings. `Decision → AtlasPage` is one-to-one and does not create a decision or alter its default. Every `Concept` source, line and SHA-256 is in the Intellectual Asset Register; direct source links were not copied as graph nodes to keep the GraphML manageable.

## Three important traversals

**Security enforcement lineage:** `AEGIS → Interceptable cognition → pre-action-governance → D-10 / D-18 → Eight Control Planes → Chapter 16 → D-10/D-18 AtlasPage`. Similar paths exist from UAF GovernanceGuard, Kollab hooks and workshop identity ADR.

**Context and memory lineage:** `MemOS → Bitemporal persistent memory → temporal-memory-provenance → D-12/D-14 → Four Structural Layers → Chapter 13 → D-12/D-14 AtlasPage`, complemented by AEGIS persistent disagreement, Estate Pulse source provenance, and Kollab memory boundaries.

**Decision evidence lineage:** `Reference architecture complete-v2 → Weighted platform selection method → weighted-option-appraisal → D-02/D-03 → Eight Control Planes → Chapter 5/23/54`; separately, workshop quality gates and UAF implementation audit point to D-22/D-23/D-24.

## Data boundaries

- The graph supports **historical evidence discovery**; it does not supersede the binding book architecture.
- A `supports` edge means an editor found a topical connection, not that the decision quotes or depends upon the prior source.
- The 86 concepts map to **43 frozen chapters** and **29 distinct frozen decisions**. Other book chapters/decisions remain authoritative and are simply not mapped by the selected historical source material.
- The complete-v2 and final-V2 snapshots are separate project IDs to preserve variant history. Estate Pulse duplicate package is preserved in original custody, with concepts counted only once under EP.

## Graph files

- `Master_Knowledge_Graph.graphml` for Gephi/NetworkX/yEd-compatible import.
- `Knowledge_Graph_Nodes.csv` and `Knowledge_Graph_Edges.csv` for spreadsheet/SQL ingestion.
- `Book_Relevance_Matrix.csv` expands 86 concept records into source→chapter→Decision combinations.
- `Cross_Project_Patterns.csv` lists repeated controlled patterns across multiple project families.

**Before using any graph edge in a manuscript:** open the source file shown in the Intellectual Asset Register and verify wording, applicability, rights, date and claim status.



---

## Repository import strategy

# Repository preservation and curated-import plan

**Target:** `smartnimbus/enterprise-ai-platform-engineering-book`  
**Governing source:** `REPOSITORY-GOVERNANCE.md`  
**Authority rule:** The book's ratified architecture, 58-chapter order, 30 fixed decisions, Style Bible v1.2 and Meridian Fixture v1.0 are not superseded by these historical archives.

## 1. Preservation is not publication

These ZIP and 7z files are evidence deposits. They contain proprietary architecture, internal workshop material, raw source inventories, third-party references, generated images, publication drafts and possibly personal/confidential data. The book repository is public. **Do not import raw archives, 7z contents, Git history packs, private chat files, operational secrets or asset-identifying datasets into it.** The analysis has not authorised publication of any original archive.

Use a **restricted preservation store** with immutable original bytes, SHA-256 per archive, access register and checksums. Use an **editorial source ledger** in the book repository containing non-sensitive metadata, a source identifier, rights status and curated findings. Keep a separate **publication working area** for approved excerpts and redrawn diagrams.

## 2. Provenance classes

| Class | Authority / treatment | Example |
|---|---|---|
| `CANONICAL-FROZEN` | Binding and change-controlled; cannot be overwritten by discovery | Style Bible, Meridian Fixture, D-10 and D-18 |
| `HISTORICAL-ORIGINAL` | Immutable restricted deposit | All nine uploaded packages |
| `HISTORICAL-VARIANT` | Separate version, explicit diff and provenance | Complete v2 versus Final V2 |
| `THIRD-PARTY-REFERENCE` | Do not claim authorship; licence/rights verification before use | `MemOS/ref/awesome-copilot` and linked web/image material |
| `INTERNAL-RESTRICTED` | No publication until explicit clearance | Workshop application inventory and internal infrastructure |
| `RESEARCH-EXTRACT` | Structured findings with source path, paragraph/line, hash, limitations | Concept IA-001 to IA-086 |
| `PUBLICATION-CANDIDATE` | Requires technical, editorial, privacy, attribution and rights gates | Redesigned figure, adapted example, comparison matrix |
| `DERIVED-GENERATED` | Rebuildable by script; never sole source of truth | CSV graph exports, PDFs and diagrams |
| `RETIRED-FOR-BOOK` | Historical retention, no case reuse | Helios narrative, prior layer taxonomies |

## 3. Recommended paths in book repository (once approved)

```text
research/
  historical-projects/
    source-register.csv            # safe provenance only
    archive-delta-register.csv     # hashes, no private paths beyond safe metadata
    intellectual-asset-register.csv
    book-relevance-matrix.csv
    modernisation-assessment.md
    cross-project-synthesis.md
    dossiers/                    # redacted/rights-reviewed versions only
    sources-and-rights.md
  knowledge-graph/
    graphml/
    nodes.csv
    edges.csv
  editorial-validation/
    claim-review-queue.csv
    author-rights-clearance.csv
    confidentiality-review.csv
```

Do not publish `extracted/`, `data/`, third-party `ref/`, `.git/objects/`, full workshop dumps, private real-company names, secret examples or proprietary workbooks.

## 4. Ingestion gates

| Gate | Input | Proof | Approver | Failure outcome |
|---|---|---|---|---|
| R0 custody | Original ZIP/7z | Full SHA-256, filename, size, date, restricted access | Configuration custodian | Quarantine |
| R1 inventory | Archive manifest | Every entry classified; binary/oversize omissions identified | Repository curator | Do not use unsupported content |
| R2 authorship/rights | Original works and assets | Ownership, licensing, company consent, generated-image provenance | Rights editor | Restrict use |
| R3 security/privacy | Internal code/data | Secret scan, personal data and topology review, redaction | Security reviewer | Quarantine |
| R4 relevance | Source-anchored concept | Evidence passage, maturity/claim status, book mapping | Development editor | Historical only |
| R5 architecture alignment | Research extract | No frozen taxonomy/Decision/fixture change | Architecture custodian | Escalate, do not rewrite |
| R6 technical validation | Claims and examples | Verified tests, primary-source references, or synthetic label | Technical editor | Flag as hypothetical |
| R7 editorial/publication | Adapted source | Style Bible, alt text, cross-reference, source credit | Editorial director | Reject from manuscript |

## 5. Recommended source import dispositions

| Archive | Custody | Research | Suitable publication use | Exclude from public repository |
|---|---|---|---|---|
| `estate-pulse-main.zip` | Retain canonical content copy | Ingestion/worker/ADR case | Redacted supporting case methodology | Real infrastructure and identities |
| `estate-pulse.zip` | Retain duplicate-package hash and reference | No redundant concept ingestion | None additional | Duplicate whole archive |
| `AEGIS.zip` | Retain full lineage and PDF | Cognition, policy, evidence, narrative history | New attribution-cleared prose/diagram inspiration | Historical Helios case, unlicensed artwork |
| `Kollab.zip` | Retain design docs | Collaborative memory, runtime hooks, FinOps, convergence | Select conceptual illustrations with claim caveats | Third-party reference images, unverified benchmark claims |
| `uaf.zip` | Retain design and adverse audit | Gateway/identity/memory, failed security-control evidence | Carefully anonymised design-vs-evidence contrast | Private chats, hardcoded test secrets, unauthorised config |
| `MemOS...7z` | Retain first-party + third-party provenance separately | Bitemporality, retention, workshop governance | Memory provenance discussion, after citations | Vendor reference tree and copied skill content |
| `workshop...7z` | Restrict whole package | Human challenge, gated ADRs, lifecycle-to-exit | Redacted facilitated-review method | Internal source spreadsheets/data |
| `...complete-v2.zip` | Retain historical baseline | Selection workbook/agent taxonomy | Decision method explanation, after review | Historical competing layer model as new canon |
| `...final-V2.zip` | Retain delta baseline | Historical source diff | No duplicate content | Unreviewed installer/product extracts |

## 6. Version and duplicate procedure

- The two Estate Pulse archives contain identical 167 non-directory files by content SHA-256. Record two original archive packages but one conceptual source lineage.
- The two v2 architecture archives have 371 common file paths and ten differing/added/removed paths. Produce a minimal textual diff and annotate any reference to the main architecture document as **complete-v2** or **final-V2**; never rely on a bare “v2” label.
- Maintain a source hash alongside every concept record. If source files change, mark the record for re-review rather than silently updating historical claims.
- The author's existing published/rights-controlled materials must remain under their own separate licence status until verified.

## 7. Change control and decision governance

The 86 historic concept records are research inputs **only**. None creates D-31, alters D-10/D-18, changes a chapter number, or modifies the Meridian fixture. New evidence can enter the manuscript only by a normal reviewed editorial pull request, citing the exact research source. A perceived critical architecture defect follows the existing exceptional-change escalation rather than automatic rewriting.

## 8. Import order

1. Preserve archive checksums and file manifest in the restricted custody store; deduplicate concept processing, not original package evidence.
2. Screen confidential data, IP provenance and third-party reference materials; quarantine anything not cleared.
3. Review and import `Cross_Project_Synthesis.md`, `Modernisation_Assessment.md`, and the 86-entry safe concept ledger as **research**, not governing architecture.
4. Import individual dossiers only when identifiers/company-specific details are approved for the public repository.
5. Add knowledge graph and reproducible mapping scripts; link node evidence back to the restricted source store through opaque IDs where necessary.
6. Create PR containing the curated research, with separate sign-offs from editorial, rights, security, and architecture custodians.
7. After merge, run the frozen Chapter 13/16/Decision Atlas baseline integrity checks. If any frozen artefact changed, block publication.

## 9. Publication red flags requiring explicit resolution

- The AEGIS interior PDF contains a copyright statement with a named author and says legal/confidentiality review remains necessary. Confirm ownership and attribution before incorporating wording or images.
- Workshop workbooks and Estate Pulse source describe actual enterprise systems. This is not safe synthetic Meridian evidence.
- The MemOS `ref` tree is a massive third-party reference collection. Presence in a ZIP does not grant republication rights.
- Several diagrams use older architectural plane and layer taxonomies or are too dense for the Style Bible diagram limits.
- UAF audit findings and MemOS scaffolding reports contradict superficial “production-ready” readings of the design claims.

## 10. Definition of done

The research import is ready only when the source-to-claim chain is replayable, all rights/security gates have documented outcomes, every extracted concept has a frozen chapter/decision mapping or an explicit exclusion, and no original archive or sensitive content is on public `main`.

**Current status:** Analysis complete at a curated conceptual level; **no GitHub import performed**. This document is a recommendation, not an approval to publish raw evidence.



---

## Dossier — AEGIS

# Project dossier: AEGIS — AEGIS.zip

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
Multi-generation authorial programme for governed cognitive infrastructure: AEGIS reference systems, runtime sequence packs, memory/governance/collaboration designs, narrative books and illustration standards.

## 2. Maturity and evidence boundary
Substantial authored textual intellectual capital and a 220-page interior PDF draft. No independently verified running AEGIS system was found in this archive. Several files are blank or earlier versions.

- Archive entries (non-directory): **194**; captured text/source files: **65**; recognised code/config source files (approximate): **0**.
- **Reported status:** Historical concepts and manuscript work; execution remains unverified.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Conceptual control-plane architecture, sequenced operational traces, governed cognition, evidence-centric memory, debate and convergence; repeated revisions v1–v3.

## 4. Distinctive strengths
Strong through-line: intent does not imply authority; cognition should be intercepted, attributed and replayed; disagreements persist as evidence. The runtime sequence designs can inspire demonstrable diagrams.

## 5. Weaknesses, contradictions and failure modes
Repeated grand originality claims are not evidence of invention. Earlier fictional Helios Financial world conflicts with frozen Meridian. The image-generation assets and PDF carry separate rights, source and style obligations. Sequence diagrams are dense.

## 6. Thematic contribution to the book
Executable accountability, append-only evidence, institutional disagreement, bounded autonomy, replay, economic and reliability governance.

## 7. Modernisation and technical debt review
Preserve the mechanism, not legacy competing taxonomies such as “eight-plane cognitive architecture” that differ from the frozen book. Convert long cross-plane sequence diagrams into smaller approved figures only through editorial adaptation. Audit model/provider citations and generated artwork rights.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-013 — Interceptable cognition | `AEGIS.zip/AEGIS/Governance Plane Deep Dive.md`:223 | ## Interceptable Cognition | pre-action-governance | **A** | Ch 16, 19, 48; D-10, D-18 |
| IA-014 — Executable governance semantics | `AEGIS.zip/AEGIS/Governance Plane Deep Dive.md`:253 | ## Executable Governance | policy-as-runtime-control | **A** | Ch 16, 19, 40; D-10, D-19 |
| IA-015 — Append-only cognition spine | `AEGIS.zip/AEGIS/Build the Memory Plane Deep Dive.md`:217 | ## The Append-Only Cognition Spine | evidence-lineage-continuity | **A** | Ch 13, 17, 40, 57; D-12, D-24 |
| IA-016 — Persistent disagreement | `AEGIS.zip/AEGIS/Build the Memory Plane Deep Dive.md`:481 | ## Persistent Disagreement Infrastructure | non-silent-reconciliation | **A** | Ch 13, 57; D-14 |
| IA-017 — Policy-bounded recall | `AEGIS.zip/AEGIS/Build the Memory Plane Deep Dive.md`:434 | ## Policy-Bounded Recall | retrieval-access-governance | **A** | Ch 13, 21; D-11, D-12 |
| IA-018 — Replayable governance evidence | `AEGIS.zip/AEGIS/Governance Plane Deep Dive.md`:329 | ## Replayable Governance Evidence | decision-to-evidence-chain | **A** | Ch 16, 17, 40, 57; D-18, D-24 |
| IA-019 — Identity continuity through cognitive handoffs | `AEGIS.zip/AEGIS/AEGIS Foundation Pack.md`:67 | * identity continuity, | delegation-identity-chain | **A** | Ch 15, 16; D-19, D-20 |
| IA-020 — Debate and convergence as bounded reasoning | `AEGIS.zip/AEGIS/Runtime Sequence Pack — Sequence 4.md`:7 | # Debate & Convergence Flow | bounded-collaborative-deliberation | **C** | Ch 14, 18; D-13, D-22 |
| IA-021 — AEGIS trust and failure narrative | `AEGIS.zip/AEGIS/AEGIS Foundation Pack.md`:958 | Helios Financial Group is one of the first enterprises attempting to operationalize governed cognition at scale. | fictional-case-literacy | **F** | Ch 9, 18, 57; D-23 |
| IA-022 — Multi-volume cognitive architecture programme | `AEGIS.zip/AEGIS/v2/Books Blueprint.md`:45 | Volume 1 — Building Governed Agentic AI Systems | editorial-modularisation | **E** | Ch 39, 52; D-29 |
| IA-023 — Cost and reliability as governance constraints | `AEGIS.zip/AEGIS/AEGIS Foundation Pack.md`:453 | FinOps["FinOps Engine"] | economic-reliability-governance | **B** | Ch 20, 36, 38; D-26, D-27 |
| IA-024 — Canonical runtime sequence templates | `AEGIS.zip/AEGIS/The Canonical Runtime Sequence Pack.md`:5 | # The Canonical Runtime Sequence Pack | trajectory-as-teaching-evidence | **E** | Ch 17, 57; D-24 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Preserve conceptual and manuscript lineage with explicit attribution and rights clearance.
- Retire Helios as a book case source; it must not silently replace the frozen fictional Meridian Financial scenario.
- The 220-page PDF is a prior interior draft, not proof of a published or legally cleared book.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?



---

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

## Dossier — MemOS-2026-05-21-09-53-51

# Project dossier: MemOS — MemOS-2026-05-21-09-53-51.7z

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
Agent-aware developer memory and coding-assistant support concept with bitemporal storage, provenance, MCP interfaces, cloud/local deployment profiles and facilitated multi-agent architecture workshops.

## 2. Maturity and evidence boundary
Much of the 7z contains a vendored third-party awesome-copilot reference collection. First-party MemOS material is largely specs, templates, agent instructions, workshop output and a limited workshop_main.py; May 17 audit itself distinguishes scaffolding from missing implementation.

- Archive entries (non-directory): **3,119**; captured text/source files: **2,551**; recognised code/config source files (approximate): **158**.
- **Reported status:** Design/scaffolding and workshop artefacts, not verified operating memory platform.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Layered memory/data/agent/security/observability architecture with SQLite-local/PostgreSQL-cloud design, GitHub-spec and test-gated developer workflow.

## 4. Distinctive strengths
Bitemporal concepts, provenance and erasure ADRs provide concrete questions for Chapter 13. Workshop outputs expose cross-role reviews and explicit unresolved items rather than a single agent viewpoint.

## 5. Weaknesses, contradictions and failure modes
An “85% complete” audit is for workspace scaffolding; it is not proof of durable, secure memory persistence. The 7z mixes first-party work with extensive third-party repository content; copying references into the book raises IP/licence problems.

## 6. Thematic contribution to the book
Temporal knowledge, policy-bounded recall, memory erasure, spec-driven engineering, multi-persona challenge.

## 7. Modernisation and technical debt review
Evaluate available managed vector/search, durable execution, retention and MCP capabilities against cost and compliance. Require direct verification of cryptographic erasure, secondary copies and backup retention before claiming deletion guarantees.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-055 — Bitemporal persistent memory | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/context/memos-context.md`:6 | (Claude Code, Cursor, Copilot, Codex CLI) with persistent bitemporal memory, multi-language | temporal-memory-provenance | **A** | Ch 13, 57; D-12, D-14 |
| IA-056 — Local and cloud memory portability | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/context/memos-context.md`:15 | - **Portable:** Single SQLite file ('memos.db') with sqlite-vec (vector) + FTS5 (keyword). | memory-portability | **B** | Ch 13, 36; D-12, D-27 |
| IA-057 — MCP-based memory service interface | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/context/memos-context.md`:7 | code intelligence, and multi-agent orchestration — all accessible through the MCP protocol. | versioned-agent-contract | **B** | Ch 22, 53; D-21 |
| IA-058 — Memory provenance and temporal recall | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/AUDIT.md`:148 | 8. Provenance for Every Memory | evidence-lineage-continuity | **A** | Ch 13, 17; D-12, D-14 |
| IA-059 — Multi-agent architecture workshop | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/docs/workshops/HOW-IT-WORKS.md`:1 | # MemOS AI Agent Workshop System — How It Works | cross-role-design-challenge | **C** | Ch 35, 41, 42; D-06, D-29 |
| IA-060 — Architecture challenger personas | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/docs/workshops/WORKSHOP-FACILITATOR-HANDBOOK.md`:151 | **If someone challenges a decision**: | architecture-challenge-review | **D** | Ch 35, 40; D-06, D-22 |
| IA-061 — Spec-driven TDD and approval gates | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/docs/start.md`:17 | │ ├── tdd-engineer.agent.md ← TDD-first implementation agent | gated-authoring-execution | **E** | Ch 18, 39; D-22, D-29 |
| IA-062 — GDPR erasure and key destruction | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/docs/adr/ADR-0008-GDPR-Erasure-Cryptographic-Key-Destruction.md`:1 | # ADR-0008: GDPR Erasure via Cryptographic Key Destruction | memory-erasure-evidence | **A** | Ch 13, 21, 49; D-12, D-25 |
| IA-063 — Memory security mesh | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/.github/context/memos-context.md`:42 | ### Layer 4: Security Mesh | multi-stage-data-protection | **B** | Ch 13, 21; D-11, D-25 |
| IA-064 — Scaffold completeness versus product readiness | `MemOS-2026-05-21-09-53-51.7z/MemOS-2026-05-21-09-53-51/AUDIT.md`:4 | **Overall Status:** ✅ **85% Complete** — Excellent foundation, some tooling gaps | evidence-claims-validation | **D** | Ch 18, 40; D-22, D-24 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Preserve first-party memory/ADR/workshop assets separately from the vendored `ref/awesome-copilot` tree.
- Treat outside reference content as third-party material until individual licences and permissions are documented.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?



---

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

## Dossier — agentic-enterprise-reference-architecture-final-V2

# Project dossier: Agentic Enterprise Reference Architecture — final V2 — agentic-enterprise-reference-architecture-final-V2.zip

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
Final-v2 variant of the same agentic enterprise reference architecture, with changed manifest and runtime-layer map plus one installer variation.

## 2. Maturity and evidence boundary
371 common files with complete v2 and only ten path/content differences. Not an independent project or second source of truth. Version labels must not override file hash comparison.

- Archive entries (non-directory): **373**; captured text/source files: **370**; recognised code/config source files (approximate): **0**.
- **Reported status:** Alternative historical snapshot, not an independently validated deployment.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Same reference anatomy, decision/selection workbook, and capability atlas; limited delta in runtime map and export/installer metadata.

## 4. Distinctive strengths
A useful provenance example demonstrating why named “final” packages must be diffed before authority designation.

## 5. Weaknesses, contradictions and failure modes
Competing runtime-layer map filenames and changed canonical large document can create accidental mixed-version citations. “Final” is not the frozen 58-chapter baseline.

## 6. Thematic contribution to the book
Versioned intellectual capital, reconciliation, source registry, decision evolution.

## 7. Modernisation and technical debt review
Import only the historically distinct changed material and an explicit delta manifest. Do not select either archive as the book’s canonical architecture without authority crosswalk.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-085 — Final-v2 changed runtime layer mapping | `agentic-enterprise-reference-architecture-final-V2.zip/agentic-enterprise-reference-architecture/01-reference-architecture/02-agent-runtime-anatomy/01-enhanced-runtime-layer-map.md`:1 | ## 9. Enhanced Agent Runtime Layers | historical-model-reconciliation | **E** | Ch 10, 11; D-07 |
| IA-086 — Final-v2 source manifest | `agentic-enterprise-reference-architecture-final-V2.zip/agentic-enterprise-reference-architecture/MANIFEST.md`:1 | # Repository Manifest | source-provenance-registry | **E** | Ch 40, 52; D-24, D-29 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Retain this archive as a historical variant with a change register; the two v2 archives share 371 common files and have ten changed/added/removed paths.
- Do not overwrite the frozen manuscript architecture or previous reference snapshots.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?



---

## Dossier — estate-pulse-main

# Project dossier: Estate Pulse — estate-pulse-main.zip

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

## Dossier — workshop-2026-05-21-09-50-32

# Project dossier: Architecture Workshop / UAF v4 — workshop-2026-05-21-09-50-32.7z

**Review basis:** Original uploaded archive; full path/size/type/sha256 index in `file_manifest.csv`. The extracts below refer to exact archived source files and line numbers; descriptions distinguish design intent from executed evidence.

## 1. Purpose and problem being solved
May 2026 UAF v4 project-discovery workshop design; accelerates enterprise discovery through specialised agents, architecture challenge, specification generation and design approvals.

## 2. Maturity and evidence boundary
Product requirements, 38 ADR files, engineering specifications, and long enterprise lifecycle research. Also includes real-world application inventory workbooks. Little executable workshop runtime code in the exported archive.

- Archive entries (non-directory): **464**; captured text/source files: **134**; recognised code/config source files (approximate): **0**.
- **Reported status:** Research and draft/accepted ADRs; deployment claims unverified.
- The archive itself is a snapshot; this review did not authenticate deployment endpoints, execute the application, or inspect external systems.

## 3. Architectural style and technology boundary
Agent-assisted collaborative requirements capture, standard cascade, human review, governed evidence pipelines and end-to-end project lifecycle models.

## 4. Distinctive strengths
Complete decision record sequence and surprisingly broad lifecycle coverage including decommission; good example of turning complex discovery sessions into inspectable decisions.

## 5. Weaknesses, contradictions and failure modes
2–3 hour workshop replacing 6–12 weeks of discovery is an unverified promotional estimate. Source workbooks contain potentially confidential enterprise inventories and must never become public example fixtures. Several engineering docs are draft versus claimed approvals.

## 6. Thematic contribution to the book
Multi-persona challenge, decision gates, human sign-off, source provenance, workload identity, concept-to-retirement.

## 7. Modernisation and technical debt review
Assess current agent-framework/transport options before treating May 2026 names as canonical. Treat agent-synthesised output as proposed findings until SMEs validate source and assumptions. Separate input data retention from public research excerpts.

## 8. Concept-level forensic evidence

| Concept ID | Document and line | Extracted evidence | Pattern | Classification | Frozen book mapping |
|---|---|---|---|:---:|---|
| IA-065 — Multi-persona four-hour architecture workshop | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/product/prd.md`:4 | tags: [prd, requirements, product, ai, workshop] | cross-role-design-challenge | **C** | Ch 6, 35, 42; D-06, D-29 |
| IA-066 — Challenger agent to challenge consensus | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/research/enterprise-lifecycle-spec.md`:17 | - [3B. Challenger & Consultant Personas](#3b-challenger--consultant-personas) | architecture-challenge-review | **C** | Ch 18, 35; D-22, D-23 |
| IA-067 — Lifecycle from concept to decommission | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/research/enterprise-lifecycle-spec.md`:1 | # Enterprise Project Lifecycle — Concept to Decommission | lifecycle-to-exit | **A** | Ch 24, 34, 49, 50; D-29, D-30 |
| IA-068 — Standards cascade and review gates | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/research/enterprise-lifecycle-spec.md`:226 | Enterprise projects don't just have *one* set of standards. Standards cascade from global corporate policy down to individual code commits. Most projects fail the standards game because nobody maps which layer appli | policy-as-runtime-control | **B** | Ch 19, 33, 39; D-19, D-23 |
| IA-069 — Declarative agent profile registry | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/engineering/agent-orchestration-spec.md`:18 | 4. [Agent Profile Registry](#4-agent-profile-registry) | declarative-tool-onboarding | **B** | Ch 12, 29; D-09, D-29 |
| IA-070 — Evidence-backed quality gates | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/engineering/agent-orchestration-spec.md`:21 | 7. [Validation and Quality Gates](#7-validation-and-quality-gates) | decision-to-evidence-chain | **A** | Ch 18, 40; D-22, D-23 |
| IA-071 — Workload identity without static keys | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/engineering/adr/adr-012-workload-identity.md`:2 | title: "ADR-012: Workload Identity — No Static Service Account Keys" | identity-sovereignty | **A** | Ch 15, 16; D-19, D-20 |
| IA-072 — Three-tier file pipeline | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/engineering/adr/adr-032-three-tier-file-pipeline.md`:2 | title: "ADR-032: Three-Tier File Pipeline — Raw → Wiki → Outputs in GCS" | evidence-lineage-continuity | **B** | Ch 13, 17, 57; D-11, D-24 |
| IA-073 — Multi-tenant auth model | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/engineering/design-multitenant-auth.md`:2 | title: "Design: Multi-Tenant Auth & Workspace Isolation" | memory-isolation | **A** | Ch 7, 15, 21; D-04, D-19 |
| IA-074 — Enterprise support skills model | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/research/enterprise-support-skills-model.md`:1 | # Enterprise Support & Skills Model — Full-Stack Technology Competency Framework | team-boundary-operating-model | **C** | Ch 6, 35; D-06 |
| IA-075 — Real-world application data sources | `workshop-2026-05-21-09-50-32.7z/workshop-2026-05-21-09-50-32/docs/engineering/data-model.md`:2 | title: "Data Model: Unified Agent Fabric v4.0" | structured-unstructured-provenance | **F** | Ch 13, 57; D-11, D-14 |

## 9. Implementation versus concept classification

The register records file-level conceptual evidence. “Code-present” means that relevant source or execution configuration exists in the archive, **not** that a production implementation passed an independent test. “Accepted ADR” means a recorded choice, **not** that every dependent control was implemented. For book use, verified vendor/standards claims need separate dated citations.

## 10. Preservation and import decision

- Quarantine raw business workbooks and internal enterprise identifiers. Import only approved, redacted research interpretations.
- Curate ADR and workshop methodology as research inputs; never relabel them as frozen Decision Atlas IDs.

## 11. Open validation questions

- Who holds rights to the complete source, including images, reference libraries and company materials?
- Which design assertions have corroborating runtime tests and operational records?
- Does the cited architecture source remain applicable to the frozen book decision, or is it an earlier exploratory taxonomy?
- What must be independently sourced from primary standards before publication?

