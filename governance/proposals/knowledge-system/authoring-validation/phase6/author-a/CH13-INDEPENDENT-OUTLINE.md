# Author A — Chapter 13: Context (F6 authoring outline)

**Trial assignment:** Chapter 13; D-11, D-12, D-13, D-14. **Input boundary:** frozen Chapter 13 blueprint, frozen decision catalogue, Style Bible v1.2, Meridian v1.0 and frozen chapter structure. No Author B or C material is a source. **Status:** independently scoped simulation, not a chapter manuscript or independent human authorship.

## Unique reader outcome
The reader can specify an access-aware, provenance-carrying context contract, explain why a retrieval hit is not an admissible claim, keep contradictory source records unresolved, gate durable memory writes and distinguish bounded inter-agent context exchange from authorisation to mutate. Context does not own Gateway enforcement, delegated privilege or behavioural release evaluation.

## Required F6 structure and section specification

### Opening hook (unheaded; ~115 words)
Start with the two source-authorised retail records at Week 8. Explain that two retrieval results describe the same synthetic product at the same effective time yet disagree: Registry `MF-REC-A-001` says `ACTIVE`, CRM `MF-REC-B-001` says `CLOSED`. The observed state is `MF-EVD-RC-001.status=UNRESOLVED`. Introduce why a context system must retain disagreement instead of allowing a model to choose a convenient answer. Do not invent a subsequent steward decision.

### What this layer decides (~35 words)
Context owns governed retrieval, admissible evidence assembly, semantic identity, unresolved conflict signalling and memory boundary contracts. It does not authorise a side effect or settle a domain owner's business decision.

### The mechanism (~1,640 words)
1. **13.1 Context contract and terms (~180).** Define index hit, source record, source-authorised result, context manifest, semantic identity, working context, durable memory and audit evidence. Proposed fields are illustrative schema, not asserted Meridian JSON fields. Diagram the trust boundary from candidate to admitted context.
2. **13.2 Retrieval checks and manifest (~250).** Use `MF-EVT-002`–`004` to show the wrongly retail-tagged insurance record `MF-REC-INS-LEAK-001` being quarantined before consumption. Use `MF-EVT-005`/`006` to show the two retail sources allowed following ACL and consumer rechecks. Refer to `MF-EVD-CM-001` and show provenance, tenant, classification and inclusion decisions. **Figure 13-1:** source ACL → consumer recheck → manifest; visibly separate index result from admitted context.
3. **13.3 Semantic identity and conflict (~310).** Compare canonical referent, tenant, product ID, effective time, recorded time, claimed value and source. `ACTIVE` and `CLOSED` are incompatible. No effective precedence rule is defined. `MF-EVT-007` is blocked conflict; `MF-EVT-008` routes to domain data owner `MF-HUM-RET-OWN-001`. **Figure 13-2:** two evidence arrows into `UNRESOLVED`, with escalation; no asserted resolution.
4. **13.4 Memory tiers (~230).** Distinguish transient context, governed durable assertion, audit event. A context read neither proves source truth nor constitutes a durable write. Retention and deletion obligations are policy inputs.
5. **13.5 Governed durable-memory write (~280).** D-12's exact default controls provenance, classification, owner, retention, verification. An unresolved eligibility assertion is not persisted as verified fact. Provide an illustrative write-decision contract and negative test; explicitly state no memory-write event appears in frozen Meridian. **Figure 13-3:** proposed write gate, with observed fixture hold/deny path clearly marked.
6. **13.6 Cross-agent context transfer (~170).** D-13 requires signed, policy-brokered handoff, bounded audience, tenant, provenance, retention and receiving-side validation. This is normative guidance; Meridian does not contain an executed signed Context handoff. Do not interpret delegation record `MF-EVD-DG-001` as a context handoff receipt.
7. **13.7 Deletion/correction and proof limits (~220).** Correction must preserve original observation and audit provenance; deletion must respect governance and retention rules. Neither completed deletion nor production erasure is demonstrated by the refund fixture.

### The interface with adjacent layers (~205 words)
Lifecycle requests context and manages workflow/checkpoint state; Tooling mediates invoked tools; Execution isolates runtime; Identity establishes principals and delegated scope; Data Protection supplies classification and retention rules; Governance owns policy/accountability; Gateway admits or rejects mutable actions using context state as an input. **Handoff to Chapter 16:** `UNRESOLVED` is data-quality state, not a granted `refund:execute` permission. **Handoff to Chapter 18:** a subsequent release gate is not a Context decision.

### Failure modes (~245 words)
Table with: tenant index mislabel → source recheck/quarantine; stale source → expiry/re-fetch; alias collision → canonical ID and provenance; source contradiction → `UNRESOLVED` and steward; prompt/context poisoning → boundary-labelled citation; replay/stale memory → version/retention check; incomplete deletion → control evidence and outstanding obligation. Columns: trigger, symptom, observed vs hypothetical, detection, prevention, owner.

### Scaling signal (~140 words)
Specify proposed signals (ACL recheck failures, contradiction backlog age, unreviewed memory writes, stale source rate) and accountable response. Do not invent production SLO values or observed latency benchmarks.

### Anti-patterns (~240 words)
Three F4 cards: (1) vector similarity equated with ACL; (2) newest-wins reconciliation; (3) unbounded shared memory. Each states trigger, failed boundary, detection signal, corrective contract and Meridian citation if observed.

### Decisions to make (~65 words)
D-11 Control retrieval access; D-12 Govern durable memory; D-13 Enable cross-agent memory; D-14 Reconcile semantic identities. State decisions without amending Atlas.

### Defaults (~105 words)
Quote each frozen default exactly from the catalogue, separately from narrative examples. Automatic comparison against source is required before publication.

### Artefacts to produce (~35 words)
Context contract and manifest; reconciliation record and steward escalation; illustrative durable-memory write contract and bounded handoff contract. Mark the last two proposed, not executed fixture observations.

### See also (~25 words)
Chapter 7 for evidence boundaries, Chapter 14 for Lifecycle, Chapter 15 for Identity, Chapter 16 for Gateway and Chapter 18 for Verification; link to Chapter 57 for full specimen.

## Evidence usage plan
| Claim | Frozen evidence | Permitted inference | Explicit exclusion |
|---|---|---|---|
| Cross-tenant indexing is unsafe without source recheck | `MF-REC-INS-LEAK-001`, `MF-EVT-002`–`004`, `MF-EVD-CM-001` | Synthetic quarantine result | Universal deployed ACL proof |
| Two retail records conflict | `MF-REC-A-001`, `MF-REC-B-001`, `MF-EVD-RC-001`, `MF-EVT-005`–`008` | Unresolved, steward escalation | `ACTIVE` or `CLOSED` selected as truth |
| Durable memory requires policy gate | D-12, Ch13 authoring blueprint | Design-time requirement | Executed write/deletion receipt |
| Cross-agent handoff is bounded | D-13 | Normative contract | Signed handoff observed in Meridian |
| Authorisation delegated elsewhere | D-10, D-14; Ch16 as cross-reference | Gateway uses Context conflict as input | Context grants mutable action |

## Lifecycle and playbook references
Primarily lifecycle Stage 4/5 first-case Context onboarding and evidence acceptance, with application in Stage 9 ongoing evaluation and Stage 11 retirement; these are **editorial learning mappings, not Meridian completed stage evidence**. Link to tenant and Context playbook (Ch43) and memory/governance playbook (Ch49), without reproducing their execution instructions. Use actual stage titles from the frozen TOC at typesetting.

## Author A self-check before comparison
D-11 ACL and provenance; D-12 no ungoverned memory; D-13 bounded signed policy-brokered handoff is a requirement not observed; D-14 canonical identifiers and explicit unresolved states. No altered Atlas default; no ninth plane; no simulated outcome promoted to production; no case resolution invented.
