# Independent reviewer calibration — execution instructions

Use the existing Phase 7 review rules; this pack provides calibration cases and worksheets, not a new review authority.

**Answer-key separation:** `examiner/DEFECT-EXAMINER-KEY-RESTRICTED.csv` is NOT a participant resource, NOT a GitHub-public asset, and NOT a held-out benchmark. Examiner prepares blinded, shuffled cases with opaque IDs and controls; only the examiner retains the mapping and original unmodified snippets. The calibration set has seven Critical, seven Major and seven Minor deliberately unsafe claims, distributed across seven risk classes. Add at least seven independently sourced clean controls and a genuinely unseen holdout before relying on reviewer performance.

Reviewer sees pinned frozen source bundle, blinded excerpts, source citation requirements and `SEMANTIC-REVIEW-WORKSHEET.csv`; not earlier authors' outputs, the answer key or future holdout. Record per-case exact span, authoritative source, explanation, severity, corrected statement, confidence and active minutes. After all answers are locked, examiner reveals scores and preserves misses and false positives.

## Scoring
Five dimensions total 100: Atlas fidelity 25; ownership 25; evidence 25; chapter-contract scope 15; semantic correctness 10. Case detection requires identifying the real defect, citing the source, and assigning appropriate severity—not a vague “might be wrong.” Critical miss = calibration NO GO regardless of score. With seven Major cases, >=90% means 7/7; with seven Minor, >=80% means 6/7. Safe-case false positives must not exceed 10%; sample count and raw denominators must be reported.

No recoding after seeing the answer key counts as first-try success. A failed reviewer must practise on disclosed cases and then attempt fresh, independently constructed blinded material. Calibration demonstrates reviewer discrimination, not three-author reproducibility.
