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
