# Phase 7 — Independent Author Trial Specification

**Execution status:** NOT RUN. This is an operationally executable experiment specification, not proof that independent authors took part. Scope is frozen Chapter 13, Chapter 16 and D-10/D-14/D-18 F1 authoring; do not modify frozen materials.

## 1. Trial hypothesis and falsification

H0 (unsafe): given identical approved sources, uncoached and genuinely independent authors make material differences in ownership, Atlas meaning, Meridian outcomes, or evidence grade. H1 (reproducible within tested scope): independent authors produce compatible source-supported claims despite different prose. The protocol is designed to find H0, not reward polished writing.

One reviewer is blind to participant identity and drafts' provenance until individual scoring is locked. Human reviewer must be different from all authors and from prompt administrator where feasible. An LLM reviewer may assist but cannot approve.

## 2. Personnel and independence

- **Administrator:** prepares pinned manifest, seals source bundle, assigns anonymous IDs, retains access logs, accepts original uploads. Cannot edit submissions.
- **Author A:** writes full Chapter 13 under frozen F6, taking D-11–D-14 into account. No access to B/C workspaces or responses.
- **Author B:** writes full Chapter 16 under frozen F7, taking D-10 and D-18 into account. No access to A/C outputs.
- **Author C:** writes candidate F1 exemplars for D-10, D-14, D-18 without altering originals. Cannot access A/B drafts.
- **Independent reviewer:** independently checks each against signed source packet before pairwise comparison. Reviewer cannot use their own earlier generated solution as answer key.
- **Technical adjudicator (if available):** resolves appealed findings; cannot be an author of the disputed item.

For a **real** trial, use separate humans or independently configured systems with isolated context and tools; identity/independence must be evidenced rather than assumed from role names. AI-generated output is permitted as an additional test stratum but not a replacement for independent practitioners.

## 3. Source manifest and sealed packets

Administrator creates a content-addressed read-only bundle containing Style Bible v1.2, frozen TOC, source Atlas records and complete Decision Catalogue, Meridian v1.0 evidence ledger/JSON and validator, approved Phase 4 chapter contracts and typed crosswalk, Phase 5 gate baseline and lint release hash. Create separate A/B/C task instruction PDFs or text documents with only the role's mission, allowed sources, expected output form, prohibited outputs and deadline. Record SHA-256 for every source, prompt and packet; freeze at one source commit/tag. The hash must refer to bytes participants actually receive, not to a filename or GitHub ref alone.

**Important gating:** Phase 4 crosswalk and Style Bible errata are still candidate/unratified in observed history. If they have not subsequently been approved, the trial may be run as an explicitly labelled *candidate-baseline experiment*, but it may not certify production readiness or claim approved source custody.

Deliver permissions: Author A can read the common frozen source pack but writes only `A/CH13-draft.md` plus `A/claims.csv`. B analogously writes `B/CH16-draft.md`; C writes F1 specimen drafts and claim table only. All participants are prohibited from viewing previous AI chat history, other submissions, reviewer key, or historical Phase 6 suggested prose. Monitor workspace access. Do not let the administrator write any content into author submission folders.

## 4. Sealed author assignments

### A sealed task (not an answer key)

Produce complete Chapter 13 with the exact frozen F6 section structure and the chapter's unique teaching outcome. Cite all material source decisions, preserve source-level entitlements and unresolved business-record distinctions. For each material claim, submit `claim_id, passage_span, component, decision_id, evidence_id, evidence_grade, normative_or_observed, source_sha`. Clearly identify descriptions of required design versus an observed fixture result. Do not add to or edit any frozen source.

### B sealed task

Produce complete Chapter 16 under F7 section structure and teaching outcome. Describe authority admission and enforcement boundaries, including distinctions between normative requirements and Meridian observations. Submit identical claim metadata. Never infer a production security property from a synthetic test. Do not add to or edit any frozen source.

### C sealed task

Produce unapproved candidate F1 specimens for D-10, D-14 and D-18 using the exact frozen fields and source-exact default excerpts. Supply citation and evidence class for each material statement. Do not claim human approval or modify the frozen decision source.

Each prompt excludes the auditor's canonical answer, prior participant results, the Phase 6 author specimens, and any anticipated mutation patterns; prompt tests are not a writing tutorial.

## 5. Raw first-submission capture

Record start and finish UTC, active working minutes (with interruptions), tool/system versions, full prompt SHA and source bytes. On first submission, copy output **without edits** to append-only examiner custody, compute SHA-256, record upload and administrator receipt; preserve subsequent edits as separately hashed versions. Capture retrieval/source-reference logs and any coaching; coaching is disqualifying for an unassisted score. No silently edited answer or post-hoc correction may replace first submission.

## 6. Blind review phases

1. **Eligibility:** check source/prompt hash, role isolation, output completeness and evidence availability before looking at answer correctness; reject cross-contaminated tests as INELIGIBLE, not PASS.
2. **Individual review:** reviewer evaluates A, B and C independently against frozen source (accuracy, decision default, owner, evidence grade, lifecycle claims, citations, F6/F7/F1 structure). Redact identity and do not share reviewer worksheet back during this phase.
3. **Claim extraction and pairwise join:** compare A–B at Context/Gateway boundary; A–C on D-14; B–C on D-10/D-18; three-way overlap on Meridian outcomes and evidence grading. Classify `AGREE`, `COMPATIBLE_NONIDENTICAL`, `CONTRADICTORY`, `UNSUPPORTED`, `NOT_COMPARABLE`.
4. **Severity:** CRITICAL for false external authorisation, fabricated signed permit, changed Atlas default, silent merger of unresolved fixture records, or evidence inflation to production assurance; MAJOR for responsibility relocation or false candidate/release timeline; MINOR for wording or navigation without behavioural effect.
5. **Time accounting:** measure independent reading, semantic check, overlap reconciliation, request for evidence, defect retest and final acceptance separately. Record both elapsed and active person-hours. Report whether reviewer had known likely failure locations before review (bias indicator).
6. **Disposition:** independent reviewer signs a specific submitted SHA and dates, records defect log with quotes, source citations and reproduction evidence. Failed first submissions stay failed even after rework; retests are a new outcome with linkage.

## 7. Proposed thresholds and decision rules

- **Critical defects:** zero in first submissions for a trial GO; one immediately causes NO GO for authoring reproducibility within this cohort.
- **Major contradictory claims:** zero unresolved in pairwise review. Resolved defects require complete re-review; first-submission score is preserved.
- **Atlas default fidelity:** 100% exact quotations in C when quoting defaults. A/B paraphrases checked manually against the same pinned source, without allowing semantic expansion.
- **Evidence:** 100% of consequential observed claims carry a source/event/candidate and correct evidence grade. Missing evidence on a consequential claim is NO GO.
- **Independence:** 100% of participants confirmed isolated; independent human review evidenced by a real reviewer with no conflicting author role.
- **Reviewer burden:** not an arbitrary hard time threshold for first pilot; record actual hours and use measured 2-chapter effort to accept/reject a 5-chapter capacity model. Targets proposed for progression: <= 5 total qualified reviewer hours per finished chapter, <= 20% of accepted claims needing substantive correction, and no latent critical findings in independent audit sample. These are planning gates and must be ratified by programme owner.
- **Reproducibility:** all three author outputs must make correct decisions for D-10, D-14, D-18 and respect the frozen event sequence. Report pairwise raw and adjudicated agreements, with per-claim denominators; do not report statistical reliability from three handpicked decisions as a population estimate.

## 8. Required examiner evidence pack

`trial-manifest.json`, `A-prompt.sha256`, `B-prompt.sha256`, `C-prompt.sha256`, source manifest, original SHA-attested drafts/claims, participant role/independence records, reviewer raw worksheets, contradiction register, timed-review log, lint v1/v2 diagnostics, code/config hashes, waiver register, and final reviewer-authorised verdict. Participant identity and confidential materials must be retained in restricted custody under existing information policy; publish only redacted aggregate conclusions.

Use `SEALED-TRIAL-RUN-RECORD-TEMPLATE.json` for initial recording. Its blank fields demonstrate NOT RUN. A synthetic role simulation does not satisfy this protocol.

## 9. Invalid runs and escalation

Mark trial INVALID / NO CLAIM if two agents share prior conversation state, authors receive reference answers, source files change mid-trial, reviewer wrote an author draft, first submissions are unavailable, evidence rights are missing, or the same model context is reused while claiming independence. Fail-closed when any condition is ambiguous; gather new evidence, do not promote an assumption into pass.