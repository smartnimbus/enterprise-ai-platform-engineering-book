# Phase 7 — Control System Hardening and Independent Validation

**Date:** 24 November 2026  
**Status:** Offline controls hardened and executed; genuine independent validation **NOT RUN**  
**Verdict:** NO GO for unattended semantic approval or full-manuscript release; CONDITIONAL GO to a *controlled independent two-chapter trial* with mandatory manual review. **NO GO** for 5 or 10 concurrent full chapters.

## 0. Scope and evidence basis

This is a control-system evaluation. It does not assess or revise frozen architecture, Atlas defaults, Meridian, Style Bible, Chapter contracts, Phase 4 crosswalk or lifecycle stages. The assessed baseline is the actual Phase 5 `lint_manuscript.py`, `CHAPTER-VALIDATION-GATES.csv`, the Phase 6 source `run_review.py` that defines 22 mutation cases, and the resulting Phase 6 case-by-case benchmark. The frozen Phase 4 contract CSV was read for exact chapter identity and authority lanes.

**Three evidence categories must never be conflated:** a documented check; a check implemented and locally tested; a check that independently detects novel unsafe prose from real authors. Only the first two categories have evidence here. All proposed human approvals in this report remain explicitly pending.

The key falsification result: Phase 5 v1 caught 11/18 deliberately unsafe statements and allowed 4/4 known safe statements. Phase 7 v2, built with those cases visible, now catches 18/18 and allows 4/4. A further challenge set, created after v2 implementation, included eight different unsafe paraphrases and four safe statements; v2 caught **0/8 unsafe** while allowing **4/4 safe**. Thus the repaired regex helps known examples but fails to establish general semantic drift prevention. These percentages are on tiny adversarial curated sets, not measured field error rates.

## 1. Part 1 — Lint v2 specification and seven missed mutations

The companion **MISSED-MUTATION-ROOT-CAUSE-7.csv** provides explicit root cause, original failure mode, replacement rule, required metadata, automation mode and expected false-positive risk for T10, T11, T12, T14, T15, T16 and T17.

| ID | Source fault | Why Phase 5 missed it | V2 rule | Residual limitation |
|---|---|---|---|---|
| **T10** | Gateway approved payout/released funds | Checked limited refund-posted phrase | `V2-OUTCOME`: payout/transfer synonyms | Indirect paraphrase, generic true positive workflows |
| **T11** | Latest CRM record wins | Required named evidence/reconciliation verb | `V2-CONFLICT`: known recency-to-canonical language | “Prefer most recent” still escaped in H01 |
| **T12** | Context automatically resolves conflicting product states | No implicit state-transition recognition | `V2-CONFLICT`: Context + automatic resolution | Other implicit truth changes still escaped in H03/H08 |
| **T14** | Cryptographically signed permission token | Detected fixture-as-production proof, not fabricated issuance | `V2-EVIDENCE`: signature/permit assertion | A “valid signed JWT” assertion escaped in H04 |
| **T15** | Ninth invented plane | Regex only identified legacy named plane | `V2-PLANE`: frozen eight-plane allowlist | Loose noun-boundary parser; must validate typed component identity |
| **T16** | Chapter 13 specifies Gateway credentials | No contextual chapter ownership assertions | `V2-SCOPE`: per-chapter forbidden implementation zone | Indirect ownership changes and legitimate citations require review |
| **T17** | Chapter 13 wrong title | Checked presence, not exact title | `V2-TITLE`: canonical title and chapter number | Generic pilot headings warn; strict release rejects them |

**Required metadata for reliable checks:** exact source/TOC/Atlas hashes, chapter ID/title, typed `claim_id`, subject/component, action or property, factual/normative modality, decision ID and source-exact default span, Meridian event and candidate identity, claimed evidence class, source URI/hash, claimed signature/key evidence, owner chapter and reviewer record. Text-only regex cannot supply the missing facts.

V2 is additive to (and intended to preserve) Phase 5's source-provenance rules. It has draft mode and a strict release mode. **Strict mode intentionally rejects missing source hashes, crosswalk ratification, errata approval, claim evidence and qualified human approval.** This is a negative gate, not a way for an AI to grant approval. V2 has **no external API/model dependency**; all tests run offline. The tool does not amend source files or apply a waiver.

### Executed test results

| Test | Unsafe caught | Safe allowed | Interpretation |
|---|---:|---:|---|
| Phase 5 earlier baseline | 11/18 | 4/4 | Documented original weakness |
| Phase 7 v2 on known Phase 6 cases | **18/18** | **4/4** | Regression repair: known-data fit |
| Phase 7 v2 additional adversarial challenge | **0/8** | **4/4** | Strong evidence of semantic generalisation failure |
| Phase 7 focused unit tests | **6 test methods passed** | — | Known constraints and strict-mode negative controls |

Run `python lint_v2.py CH-013 draft.md`; use `--strict --metadata claims.json` to test release prerequisites; run `python -m unittest discover -s . -p 'test_lint_v2.py' -v` and `python benchmark.py` / `python heldout_challenge.py` to reproduce sample diagnostics.

**Do not advertise 100% lint accuracy.** The known-case result is in-sample. The additional challenge result is a constructed diagnostic, not external blind evaluation; the failure itself is valuable evidence that semantic review remains essential.

## 2. Part 2 — Semantic Validation Framework

The **SEMANTIC-VALIDATION-CONTROL-MATRIX.csv** defines fourteen controls mapped to the *existing* gates G0–G6, including required metadata, permitted automation and expected blocking behaviour.

- **Fully deterministic where properly represented:** SHA checks, known chapter/decision IDs, exact chapter title, source-exact quoted defaults, enumerated components, declared evidence IDs, JSON/CSV contract structure, and frozen-source byte comparison.
- **Reviewer-assisted:** claims of ownership or scope, paraphrased Atlas meaning, cross-chapter claim alignment, event/state reconstruction, whether a denied action is misrepresented through indirect language, and whether narrative implies an unsupported implementation.
- **Human-only:** resolving contested business truth, accepting evidence as sufficiently independent, assigning risk and release approval, accepting source-rights obligations, adjudicating ambiguous negation/context and certifying real human-independent authoring. AI-to-AI consensus cannot serve as an approval record.

The recommended next implementation is not to add more regex variations. Use **typed claim cards** for all high-impact manuscript statements (`subject`, `predicate`, `object`, `modality`, `owner_chapter`, `decision`, `event`, `evidence_grade`, `source_hash`). Apply deterministic fact/state constraints to those cards, then have qualified reviewers compare the natural-language claims to the cards and source. No NLP can guarantee faithfulness of this extraction without human sampling and challenge testing.

**Blocking semantic invariants:** no Context-initiated external refund authorisation, no Gateway business-source reconciliation, no widening of delegation, no admission without required decision/receipt, no assertion of successful denied refund, no treating retail contradictions as resolved, no simulated egress test turned into deployed enforcement, no invented signed execution permit, no fabricated durability receipt, no release result attributed to the wrong candidate, and no architecture ownership change through a secondary chapter.

Warnings are not approvals: waive a warning only with an exact-line scope/rationale, evidence URI, authorised reviewer, date and immutable document hash. Critical or major factual contradictions are non-waivable editorial failures until corrected or formal pre-existing exception adjudication applies.

## 3. Part 3 — Real independent author trial

A complete executable protocol is in **INDEPENDENT-AUTHOR-TRIAL-SPECIFICATION.md**. It names administrator, isolated Author A (full Chapter 13), Author B (full Chapter 16), Author C (unapproved F1 D-10/D-14/D-18 candidate specimens), and a separate blinded qualified reviewer. It defines sealed prompts, read-only source packet, SHA-256 manifest, isolation evidence, unedited first-submission archive, typed evidence-claim tables, pairwise claim comparisons, active reviewer labour measurement, contradiction thresholds and restricted custody.

**This trial has not occurred.** A single assistant producing multiple drafts is only a role simulation; it cannot establish external independent author reliability. If the accepted Phase 4 crosswalk or Style Bible errata remain unratified, the trial can evaluate the candidate authoring baseline but cannot certify approved production operation.

Trial pass requires: actual isolated authors, first-submission hashes, exact Atlas defaults, no material authority/evidence contradiction, mandatory reviewer-signature on exact bytes, and no resulting drift of frozen sources. Failures are kept in raw evidence without rewriting the original submission. All participant/coaching/reviewer-time data must be captured; a quality gate based only on a post-edited clean final manuscript is invalid.

## 4. Part 4 — Harden existing G0–G6, do not create new governance

**HARDENED-G0-G6-QUALITY-GATES.csv** preserves exactly G0–G6. No new top-level gate or approval hierarchy is invented.

| Gate | Enhanced requirement | Cannot be satisfied solely by |
|---|---|---|
| **G0 — Source pin** | Frozen SHA manifest; editorial baseline actually ratified | Names/branch labels |
| **G1 — Scope** | Exact heading, chapter authority, typed claim owner | Generic scope prose |
| **G2 — Automated lint** | v1+v2 regression, source-backed structured checks, severity and signed waivers | 22 hand-built examples passing |
| **G3 — Semantic review** | Independent qualified examiner for ownership, Atlas equivalence, event/claim grades | AI output or regex |
| **G4 — Cross-chapter** | Compare A↔B, A↔C, B↔C first submissions and record material divergences | One model inventing three role voices |
| **G5 — Editorial** | Exact SHA-bound human acceptance, F6/F7/F1 teaching scope, rights/citations | “Lint passed” label |
| **G6 — Publication** | Immutable release package tied to G0–G5 and no silent source drift | Merge event alone |

Do not treat checks added to G0–G6 as a newly approved operating model. These changes are **proposed acceptance strengthening** subject to existing programme governance.

## 5. Part 5 — Scaled authoring readiness

Scenario A is the Phase 5 observed control suite: seven critical/major misses in its 18-case mutation sample. Scenario B is Phase 7 v2: zero misses on the same known sample, but eight misses on eight new unsafe paraphrases. **Neither state can reliably prevent semantic drift in full independent manuscripts.** The difference is useful automated detection of known errors, not validated semantic equivalence.

| Active chapters | Existing controls | Hardened v2 prototype | Human review consequence |
|---|---|---|---|
| **2** | CONDITIONAL GO only for isolated trial | CONDITIONAL GO for a real supervised pilot; not publication | All substantive claims checked manually |
| **5** | NO GO | NO GO | Requires completed two-chapter independent pass and measured capacity |
| **10** | NO GO | NO GO | Requires five-chapter demonstrated review throughput, drift and rework rates |

The Phase 6 planning model (not observed): 14.25 reviewer-hours for two completed chapters; 33 hours for five; 67 hours for ten. At five available reviewer-hours/week, these correspond to ~2.9, 6.6 and 13.4 weeks before exceptional rework. Validation must measure actual durations, not use these forecasts as evidence of capacity.

A five-chapter GO cannot be derived from successful local lint; it requires *real* independence, no critical defects, complete source/claim linkage, independent human approval, and demonstrated ability to work through review queues without growing critical WIP. A ten-chapter GO requires repeatable positive cohort evidence, not extrapolation from manuscript-generation speed.

## 6. Defect Prevention Matrix and Automation Sequence

**DEFECT-PREVENTION-MATRIX.csv** links all seven known misses and eight new challenge misses to detection layer, essential metadata, gate and observed limitation. **CONTROL-AUTOMATION-IMPLEMENTATION-SEQUENCE.csv** prioritises source pinning and title/ID checks, claim cards and isolated human trial before adding paraphrase-detection machinery. It avoids a new product/platform or artificial AI governance layer.

Required acceptance before any increased scale:

1. Ratify baseline source custody and candidate editorial exceptions under pre-existing approval authority.
2. Implement typed evidence/authority claim cards; validate them against frozen source events and Atlas exact text, fail on missing consequential evidence.
3. Extend v2 to block at least the eight novel challenge examples **without sacrificing clean-case handling**, then evaluate on a separate genuinely unseen set authored by a different reviewer (no tuning on test cases).
4. Execute full Chapter 13/16 + F1 A/B/C independent human or separate-system cohort with sealed prompts and preserved first submissions.
5. Record reviewer-hours, contradictions, claim-level evidence precision and escaped defects, and obtain qualified human review of exact revisions.
6. Only then consider a five-chapter cohort; permit ten only after five has independently passed. G6 publication release remains separately subject to rights and editorial acceptance.

## 7. Final verdict

**Question: Can the control system reliably prevent semantic drift in independently authored manuscripts?** **NO, not based on available evidence.** There are two decisive reasons: it has never been evaluated on real independently authored full chapters, and the newly challenged deterministic lint still misses eight meaningful paraphrases.

**GO**: none for unattended acceptance or scaled release. **CONDITIONAL GO**: two isolated full-chapter human-supervised reproducibility experiments (no publication claims). **NO GO**: five and ten parallel full manuscripts under both currently observed and newly hardened prototype controls. Keep frozen architecture, Atlas, Meridian, chapter contracts and lifecycle unchanged.

The Phase 7 outcome is therefore *successful regression hardening of specific weaknesses* and *negative validation of general semantic coverage*. Preserving that negative evidence is more useful than declaring a false authoring system GO.
