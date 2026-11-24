# Programme Digital Twin — Offline Demonstration

This is a **derived, non-authoritative** machine-readable view of six local source CSVs. The design does not change the architecture, Atlas, Meridian, chapter plan, Programme Operating System, backlog or review rules.

**Source authority warning:** Inputs are available as local files in the conversation environment, not yet merged/approved in GitHub `main`. All graph entries are `OBSERVED_LOCAL_CANDIDATE`, and all crosswalks are `EXPLICIT_SOURCE_MAPPING`. No implemented control, passed test, reviewer approval or publication claim is inferred.

## Files
- `PROGRAMME-DIGITAL-TWIN-DESIGN-v1.0.md`: ten-part technical specification and limitations.
- `build_twin.py`: stdlib-only deterministic extraction and impact traversal.
- `twin-schema-v1.json`: JSON Schema for emitted six-type proof-of-concept subset.
- `test_twin.py`: thirteen negative/positive offline tests.
- `generated/twin.json`: disposable derived graph; absolute paths are local to this demonstration.
- `generated/nodes.csv`, `edges.csv`: machine-readable inventory.
- `generated/impact-D-10.json`: explicit reverse-reference impact candidates.
- `generated/coverage-report.json`: source-dependent diagnostics with unknown validation/review coverage.
- `PROTOTYPE-TEST-REPORT.json`: local structural and reproducibility test evidence.

## Reproduce

```bash
python3 build_twin.py --source /mnt/data --output generated
python3 -m unittest -v test_twin.py
```

To use an approved checkout in future, the source path mapping must first be updated to match that checkout and its authoritative manifest, then checked at a pinned commit. The sample's `/mnt/data` path must not be considered a GitHub repository path.

## Safety & governance

Never promote a derived graph edge to authority; edit the owning source under existing review rules. Public repository output must exclude restricted sources and private participant evidence. Frozen D-IDs and Meridian records are read-only. No graph database, vector runtime, autonomous write access, or new approval chain is implied.