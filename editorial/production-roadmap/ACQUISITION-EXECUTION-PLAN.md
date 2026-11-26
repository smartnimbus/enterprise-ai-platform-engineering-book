# Acquisition Execution Plan
2026-11-25. Execution companion to [Master Publishing Roadmap](MASTER-PUBLISHING-ROADMAP.md), not a replacement roadmap. Baseline main cc728dbe; PR7 ce295338 (Ch13 manuscript 79c550d3), PR9 02a2ab7d, PR11 eec11f44. Existing G0–G6; no new governance. All effort estimates indicative qualified human hours, overlapping, not measured. Do not claim approval.

## Work packages
### W1 Chapter 13 (PR7)
W1.01 one bounded EU13-01–15 edit, 2900–3000 words, F6, exact D11–14, protected passages, unchanged synthetic facts/figure refs/artefacts. W1.02 reconcile evidence/ch13-claim-crosswalk.csv and run actual lint, update existing self-review. W1.03 figure-13-{1,2,3}.mmd/.svg. W1.04 proofs/chapter-13.pdf. W1.05 independent Context/data architect and developmental editor review, correct material findings and rebuild. W1.06 named author approval, integrate exact accepted master. Existing manuscript path unchanged.
### W2 Chapter 16 (PR9)
W2.01 targeted copy only, 2300–2500 words, F7, D10/D18 verbatim, D20 supporting; W2.02 evidence/ch16-claim-crosswalk.csv and chapter-16-editorial-self-review.md actual check log. W2.03 figure-16-{1,2,3}.mmd/.svg. W2.04 proofs/chapter-16.pdf. W2.05 independent security/identity reviewer and technical editor; W2.06 cross-sample consistency and integration. Preserve DENY, null token, NOT_ISSUED_DENIED, no call, zero mutation, separate synthetic bypass, blocked release. Original frozen draft untouched. Can start before W1 closes; cross-sample acceptance requires both.
### W3 Atlas (dedicated PR)
W3.01 D14; W3.02 D10/D18; W3.03 D01; W3.04 D26; W3.05 D30. Canonical decisions/pages/D-XX.md, four new/two updated. Exact seven F1 labels/defaults/rationale/deviation/reversibility/artefact. Use six production specs; D01/26/30 hypothetical, no new fixture. W3.06 six one-page PDFs and combined atlas-six-page-sampler.pdf; W3.07 independent domain/editor review. All proofs under publishing/apress/acquisition-samples/proofs/. Do not write other 24.
### W4 submission
W4.01 publishing/apress/submissions/acquisition-submission-index.md and working source manifest, Proposal v2, pitch, dossier and frozen synopsis linked. W4.02 author-supplied official form, CV/bio, rights/AI-use statement, permissions, delivery commitment and reviewer availability; keep sensitive data outside public repo. W4.03 independent cross-sample and proof acceptance, G0–G6; W4.04 integrate accepted PRs, pin exact SHAs and checksum actual files in submission manifest; W4.05 author-approved external submission and receipt recorded, no invented publisher response. Optional Ch1 only if requested. Preliminary package can be prepared earlier but not labelled approved.
### W5 Chapter 14
W5.01 short pinned source pack editorial/authoring-blueprints/chapter-14-source-pack.md: CH014 F6 contract, D15/D16, canonical glossary, Harness and trajectory scope, fixture limits, references, owner/reviewer. Contract CSV row status PROPOSED_EDITORIAL_CONTRACT_NOT_RATIFIED; obtain author/editorial ratification and pilot acceptance before manuscript drafting. Register BP13 overlay if exact source available; do not reconstruct and call approved. W5.02 one complete reviewable manuscript at manuscript/part-03/chapter-14/chapter-14.md after pilot gate. No five-way drafting; no need to wait for publisher response after pilot gate.
## Next ten deliverables
| Rank | Deliverable | Effort | Dependency | Done |
|---|---|---|---|---|
| 1 | Chapter 13 author-final manuscript | 4–6 h | EU13 plan | PR7 revised, F6 and exact sources retained; author checks executed |
| 2 | Six Atlas editable masters | 8–12 h | Six F1 specs, catalogue | Four new, two edited; defaults exact |
| 3 | Chapter 16 evidence crosswalk and final copy | 3–5 h | PR9, receipts/ledger | Mapped claims, actual lint, author-final F7 |
| 4 | Six editable figures and SVG exports | 6–10 h | Frozen figure contracts | All six rendered, checked, linked |
| 5 | Eight proofs + combined Atlas PDF | 4–6 h | 1–4 | Readable chapter proofs and six one-page proofs, no overflow |
| 6 | Independent technical/editorial acceptance | 8–12 h | 1–5 | Named reviewers, exact accepted SHAs, corrections and reproof |
| 7 | Author form, bio/CV, rights and capacity | 3–5 h author time | Author input | Verified fields, author declarations, delivery commitment; private information kept private |
| 8 | Integrated submission manifest and approved sample package | 2–4 h | 5–7 | G0–G6, accepted revisions, checksums, author approval |
| 9 | Chapter 14 pinned source pack | 1–2 h | Existing contract and source authority | Ratified scope, D15/D16, reviewer, WIP=1; prep can overlap |
| 10 | Publisher submission and first Wave 1 draft | Submission 0.5–1 h; Ch14 per existing ~15h estimate | 8; pilot acceptance + 9 for Ch14 | Author sends and records submission; separately Ch14 full reviewable draft |
## Execution order
Start W1/W2/W3 and author administration immediately in separate branches; figure work can begin from frozen contracts. Proof only from pinned current text. Request qualified reviewers now; independent review of candidates then corrections/reproof, cross-sample consistency, author acceptance and integration. Package index can be prepared before approvals; immutable submission release only after actual acceptance and author details. W5 source prep overlaps; first Chapter 14 draft after pilot acceptance and contract ratification. Existing G0 source pin, G1 contract, G2 mechanical, G3 technical, G4 cross-sample, G5 editorial proof, G6 custody apply. A green lint does not prove semantic correctness. No actual review, submission or manuscript creation is claimed by this execution plan.
## AI authoring queue
[Five executable prompts](IMMEDIATE-AI-AUTHORING-QUEUE.md). Prompt 1 and 2 may run independently; 3 independent; 4 depends on final candidate manuscripts; 5 prepares package and handoff, final release depends on human approvals. No download-only deliverables.
