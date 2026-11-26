# Chapter 13 Editorial Upgrade Plan — 8.1 to 9.2+

Status: proposed final focused developmental revision, not manuscript approval. Baseline [79c550d3](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/commit/79c550d32f724a630bd507530190bb3e65792a81), [editable manuscript](manuscripts/chapter-13-context-acquisition-v1.md), preceding simulated independent-style acquisition assessment (8.1/10), BP13-v2 teaching overlay, [author self-review](chapter-13-editorial-self-review.md), [evidence crosswalk](evidence/ch13-claim-crosswalk.csv). The assessment and overlay were supplied in conversation; this plan does not assert their separate repository approval.

Preserve the architecture, F6, all four exact defaults, synthetic chronology, figure contracts, five artefacts, evidence limitations and 2,900–3,000 word acquisition target. No new controls, evidence, case studies or architecture. Do not edit the manuscript as part of this plan.

## Editorial strategy
Selective intervention: approximately 65% preserve, 25% substantive edit, 10% replace (planning estimate, not measured diff). Improve the practical judgement gained per paragraph. The prior review was simulated, not a publisher decision. Local gains are ordinal estimates and cannot be added to predict a total.

## Detailed intervention register
### EU13-01 — Adjacent-layer interfaces (Critical)
- Current / target / local gain: 6.5 / 9.0 / +2.5.
- Difficulty and effort: High; 45–60 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Coverage of owners drives the prose; responsibility recital duplicates the conclusion.
- Stronger teaching pattern: Organise the existing responsibilities around Tooling observations entering Context, the Harness receiving observations plus manifest and uncertainty, and the downstream precondition. Explain what information is lost if uncertainty is removed.
- Acceptance criterion: Reader can explain the significance of the exchanged information without reciting plane names.

### EU13-02 — Context schema (Critical)
- Current / target / local gain: 7.2 / 9.1 / +1.9.
- Difficulty and effort: Medium; 30–40 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Field inventory interrupts the opening; proposed schema is not a worked contract.
- Stronger teaching pattern: Group existing fields by reconstruction question: assembly/source version, tenant/subject/classification, effective versus observed time, authority versus confidence, integrity and retention. Keep the proposed-versus-fixture distinction.
- Acceptance criterion: Reader knows why the fields are needed and what they cannot prove.

### EU13-03 — Governed memory write (Critical)
- Current / target / local gain: 8.1 / 9.4 / +1.3.
- Difficulty and effort: High; 45–60 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Metadata enumeration displaces judgement about eligibility.
- Stronger teaching pattern: Evaluate the hypothetical eligibility assertion against the actual unresolved evidence and existing policy, grouping fields by accountability, justification, continuing validity. Distinguish blocked effect from performed transaction.
- Acceptance criterion: Reader can challenge a schema-valid but unjustified assertion.

### EU13-04 — Evidence interpretation (Critical)
- Current / target / local gain: 8.5 / 9.5 / +1.0.
- Difficulty and effort: Medium; 30–45 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Recorded denial risks being read as independently established non-disclosure.
- Stronger teaching pattern: Interpret manifest inclusion/exclusion, existing negative-test event, conflict reference and digest limitation; distinguish recorded outcome, intended control, and independently corroborated outcome. No new evidence.
- Acceptance criterion: Reader can state the limits of each existing artefact.

### EU13-05 — Design evaluation and practical decisions (Critical)
- Current / target / local gain: 7.4 (design evaluation); 8.4 (usefulness) / 9.3; 9.4 / +1.9; +1.0.
- Difficulty and effort: High; overlaps other tasks (indicative human editing effort, overlapping).
- Root cause and underperformance: Mechanisms named without a transferable assessment criterion.
- Stronger teaching pattern: For each major decision, replace generic conclusions with the existing design question, misleading shortcut, consequence, and evidence interpretation. Use D-11 admission, D-14 precedence, D-12 reuse, D-13 receiver authority and disposition.
- Acceptance criterion: Reader can identify an inadequate implementation without new controls or checklists.

### EU13-06 — Working context, memory, audit evidence (High)
- Current / target / local gain: 8.0 / 9.2 / +1.2.
- Difficulty and effort: Medium; 20–30 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Taxonomy obscures the consequences of survival beyond the task.
- Stronger teaching pattern: Contrast preserving current review inputs, progress for resumption, prior dispute experience, justified reusable assertions and investigation evidence. Keep all necessary distinctions without new tiers.
- Acceptance criterion: Reader distinguishes remembering a dispute from remembering eligibility.

### EU13-07 — Conditional commitment and idempotency (High)
- Current / target / local gain: 7.8 / 9.2 / +1.4.
- Difficulty and effort: Medium; 20–30 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Solution names precede sufficient explanation of the failure sequence.
- Stronger teaching pattern: Use existing hypothetical sequence: validate against a reconciliation version, relevant change before commitment, attempted write, conditional validation or equivalent existing option. Contrast retry identity with validity; no new mandatory consistency architecture.
- Acceptance criterion: Reader recognises an idempotent but unjustified write.

### EU13-08 — Cross-agent sharing (High)
- Current / target / local gain: 7.6 / 9.1 / +1.5.
- Difficulty and effort: Medium; 30–40 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Packet attributes obscure the receiver's independent authority.
- Stronger teaching pattern: Organise around intended audience, current permission, origin/integrity, claim meaning, expiry/retention. Explain repeated acceptance only where relevant; retain replay controls as options. Explain validation and retrieval cost.
- Acceptance criterion: Reader explains why a signed packet may be rejected; no fictional handoff.

### EU13-09 — Retention and deletion (High)
- Current / target / local gain: 7.8 / 9.0 / +1.2.
- Difficulty and effort: Medium; 20–30 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Lifecycle definitions obscure continuing justification.
- Stronger teaching pattern: Follow existing hypothetical assertion through changed justification; distinguish refresh, expiry, invalidation, correction and disposition by effect on consumption. Contrast receipt scope with negative retrieval test. Preserve lawful exceptions and restoration limits.
- Acceptance criterion: Reader distinguishes removal from one store and exclusion from later Context.

### EU13-10 — Trade-offs and architectural judgement (High)
- Current / target / local gain: 7.6 / 9.2 / +1.6.
- Difficulty and effort: Medium; 25–35 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Costs named but not justified.
- Stronger teaching pattern: For D-11, D-12, D-13 and D-14 connect existing cost to avoided consequence: unauthorised recall, propagation, authority confusion, hidden disputes. Preserve defaults and deviation conditions.
- Acceptance criterion: Reader explains why the cost is justified without inventing quantitative results.

### EU13-11 — Cognitive transitions (High)
- Current / target / local gain: 7.6 / 9.2 / +1.6.
- Difficulty and effort: Low–medium; 15–20 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Topic order replaces intellectual dependency.
- Stronger teaching pattern: Repair opening to schema, schema to admission, memory to sharing, sharing to retention, evidence to interfaces. Preserve reconciliation-to-memory transition. No repetitive rhetorical questions.
- Acceptance criterion: Each subsection addresses a limitation raised previously.

### EU13-12 — Terminology and density (Medium)
- Current / target / local gain: 8.0 / 9.2 / +1.2.
- Difficulty and effort: Low; 15–25 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Abstract expressions consume attention without improving precision.
- Stronger teaching pattern: Scrutinise conceptual hot/working tier, bounded read-time inputs, writer actor chain, applicable trust assumptions, downstream precondition, disposition restrictions, release suitability, owner-specific limits and verification capacity. Preserve controlled vocabulary and literal evidence fields.
- Acceptance criterion: Every retained term earns its place.

### EU13-13 — Scaling, failures and anti-patterns (Medium)
- Current / target / local gain: 7.9 (combined estimate); scaling 8.1 / 9.0 / +1.1 combined; +0.9 scaling.
- Difficulty and effort: Medium; 20–30 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Repeated principles consume budget; metrics become inventory.
- Stronger teaching pattern: Mechanism teaches operation, failures diagnose, scaling distinguishes bottlenecks, anti-patterns explain shortcuts. Keep 800/200 ms illustrative example and existing failures; distinguish worker saturation from source capacity.
- Acceptance criterion: Each closing section adds a separate reader outcome.

### EU13-14 — Closing artefacts (Medium)
- Current / target / local gain: 7.5 / 9.1 / +1.6.
- Difficulty and effort: Medium; 15–20 min (indicative human editing effort, overlapping).
- Root cause and underperformance: Artefact names are not consistently earned by the teaching.
- Stronger teaching pattern: Connect existing manifest schema, write contract, reconciliation, negative tests and deletion receipts to the investigation or design question in body prose. Preserve exact list.
- Acceptance criterion: Reader can explain the use of each artefact.

### EU13-15 — Originality and central argument (High)
- Current / target / local gain: 7.5 / 8.8–9.1 / +1.3–1.6.
- Difficulty and effort: Cross-cutting; overlaps other tasks (indicative human editing effort, overlapping).
- Root cause and underperformance: Established mechanisms are taught separately, weakening their integration.
- Stronger teaching pattern: Maintain the distinction between admission, business authority, reuse, sharing, continuing justification, Gateway admission and Verification. Demonstrate synthesis, not new terminology or novelty claims.
- Acceptance criterion: Reader can explain the central argument without naming subsection headings.

## A. Minimum coherent intervention toward 9.0
Complete EU13-01–05 and the essential transitions in EU13-11 within the edited passages. These five packages address the weakest section, specification prose, evidence limitations and transfer to design evaluation. EU13-05 is a lens for the other four, not an additional chapter subsection. Protect existing successful evidence and reconciliation material. Target 8.7–9.1, central 9.0 subject to fresh independent assessment; no guarantee.

## B. From 9.0 toward 9.3
After the first pass, complete EU13-06–10, the remaining transitions in EU13-11, and integrate EU13-15 across those changes. Apply EU13-12–14 as the final compression and reference-function edit, not a new authoring cycle. Target 9.0–9.3, central 9.2 if execution is consistently strong. Stop if changes add terminology, repeat the case or dilute the strongest passages.

## C. Protected passages
Preserve the 105-word opening's facts and restrained stakes, the exact F6 framing and closing defaults, record A/B comparison and chronology, digest limitation, no performed durable write/no signed handoff/no deletion limitations, and all figure placements/captions/alt text. Preserve substantially the recording-time paragraph, the retrieval recall judgement, the reconciliation-to-memory transition, schema-valid/write-policy distinction, investigator opening, backup restoration sentence, scaling backlog distinction and behavioural conclusion. Only local connective edits where necessary. Do not expand semantic reconciliation (9.2) merely to balance subsection lengths.

## D. Style benchmark for Chapters 14–18
Use existing Chapter 13 sentences as teaching examples, not mandatory slogans:
- Ch14: "An unresolved claim does not acquire authority when the task ends." Teach continuation and checkpoint consequences.
- Ch15: "Its credential cannot answer the consumer's permission question." Teach identity versus actual authority.
- Ch16: "A correctly recorded conflict grants neither execution permission nor release approval." Teach independent admission.
- Ch17: "An investigator starts with the Context Manifest, not the generated answer." Teach investigation through evidence.
- Ch18: "Zero side effects do not make that behaviour acceptable." Teach behavioural evaluation independent of runtime denial.
- Across chapters: preserve the CRM recording-time paragraph as the model of evidence, competing interpretations and judgement; preserve "A higher recall score achieved by exposing another tenant's documents measures the wrong outcome." as trade-off model. Use analogous chapter-specific reasoning rather than copying language.

## E. Ranked final backlog
1. EU13-01 — Adjacent-layer interfaces (Critical)
2. EU13-03 — Governed memory write (Critical)
3. EU13-04 — Evidence interpretation (Critical)
4. EU13-02 — Context schema (Critical)
5. EU13-05 — Design evaluation and practical decisions (Critical)
6. EU13-06 — Working context, memory, audit evidence (High)
7. EU13-08 — Cross-agent sharing (High)
8. EU13-07 — Conditional commitment and idempotency (High)
9. EU13-10 — Trade-offs and architectural judgement (High)
10. EU13-09 — Retention and deletion (High)
11. EU13-11 — Cognitive transitions (High)
12. EU13-15 — Originality and central argument (High)
13. EU13-13 — Scaling, failures and anti-patterns (Medium)
14. EU13-12 — Terminology and density (Medium)
15. EU13-14 — Closing artefacts (Medium)

## One-cycle execution and stop conditions
1. Lock strong passages and evidence; edit the five critical packages first.
2. Integrate supporting memory, sharing, lifecycle and trade-off edits; repair transitions as part of those paragraphs.
3. Compress duplication and terminology; retain closing contracts and references. Aim to exchange roughly 700–1,000 words of weaker prose rather than add length; the exact allocation depends on the edit.
4. Run a fresh manuscript-only developmental review, O3 test, Style Bible lint and evidence/chronology comparison; check actual word count and F6. Test whether an independent reader can reconstruct admission, explain why neither status wins, reject an unjustified memory assertion, challenge receiving authority, and distinguish deletion receipt from retrieval evidence. These are editorial reader tests, not new platform controls or observed outcomes.
5. Stop after one focused pass if substantive concerns have been addressed. Escalate any genuine remaining defect rather than generate another unrestricted revision. Independent acceptance and finished publishing assets remain separate.

## Predicted quality and limitations
Current 8.1 (simulated manuscript-only assessment); first-pass 8.7–9.1; full focused cycle 9.0–9.3 (central 9.2). No numerical improvement is guaranteed. Reader transfer, authorial execution, independent editorial judgement, actual market demand and final artwork cannot be established by this plan. The chapter is already an acquisition candidate; the aim is consistency and practical usefulness, not additional architectural coverage.
