# Phase 7 — Control System Hardening and Independent Validation

This package contains a **proposed** additive lint v2 prototype, not an authorised chapter acceptance engine. It does not edit or replace frozen sources. Do not commit it to a protected publishing branch as an accepted gate without review.

Main report: `PHASE-7-CONTROL-HARDENING-AND-INDEPENDENT-VALIDATION-v1.0.md`. Trial protocol: `INDEPENDENT-AUTHOR-TRIAL-SPECIFICATION.md`.

To run from unpacked folder positioned beside `phase4_authoring`, `phase5_validation`, and `phase6_trial`:

```bash
python -m unittest discover -s phase7_hardening -p 'test_lint_v2.py' -v
python phase7_hardening/benchmark.py
python phase7_hardening/heldout_challenge.py
python phase7_hardening/lint_v2.py CH-013 manuscript.md
```

`lint_v2.py` accesses the existing Phase 4 chapter contract at `../phase4_authoring/CHAPTER-AUTHORING-CONTRACTS-58.csv`. If sharing just this folder, copy that **read-only** CSV beside the parent folder as expected, or adapt file location without changing its bytes. The package ZIP bundles this prerequisite into `phase4_authoring/` and the original 22-case source into `phase6_trial/reviewer/` so regression tests are reproducible.

Metrics: 18/18 known unsafe blocked, 4/4 known safe allowed; 0/8 novel unsafe blocked, 4/4 novel safe allowed; 6/6 focused test methods pass. **No independent author session performed and no human release acceptance obtained.**
