# GitHub repository file-integrity validation — 24 November 2026

**Scope:** `smartnimbus/enterprise-ai-platform-engineering-book` · All four branch trees inspected · Non-truncated GitHub tree responses · No PR merges or deletions.

## Verified outcomes

- Governance review branch: **190/190** explicitly mapped local programme artefacts match GitHub blob SHA and byte length exactly (Phase 1–8 reports, registers, lint/test code, generated graphs/heatmaps, book completion, and the XLSX workbook).
- Research/book-import branch: **18/18** original Meridian v1.0 fixture files exact; **48/48** total mapped fixture, book source, non-restricted forensic and Atlas preview files exact.
- Remaining research local-vs-curated comparisons: **13** differ in content/bytes, and are held for editorial/source-rights reconciliation; these are not automatically stale or corrupt.
- All branch trees: **4** branches, **263** tracked branch-file occurrences at this snapshot. No tree reports truncation.

## Branch state

| Branch | Head SHA | Files | Protected | Recommendation |
|---|---|---:|---|---|
| `governance/knowledge-system-v1-2026-11-24` | `30a27cc4991f` | 192 | No | Review and converge PR #2 |
| `main` | `b38854ba1386` | 1 | No | Keep baseline unchanged; approved merges still required |
| `research/deterministic-first-patterns-2026-11-24` | `47559b53bbda` | 3 | No | Review and converge PR #3 |
| `research/industry-lineage-and-book-baseline-2026-11-24` | `dc00c6a7a8e0` | 67 | No | Review curated differences then converge PR #1 |

## Open PR status

- PR #3: open; draft=true; head=`research/deterministic-first-patterns-2026-11-24`; merged=false.
- PR #2: open; draft=true; head=`governance/knowledge-system-v1-2026-11-24`; merged=false.
- PR #1: open; draft=true; head=`research/industry-lineage-and-book-baseline-2026-11-24`; merged=false.
- Repository rulesets reported: **0**. Branch protection flags are false. File presence and exact hashes do not establish merge approval or CI enforcement.

## Research differences held for review

These are comparisons with a local historical source; different bytes may reflect deliberate public curation, research rewrite, or line-ending differences. Do not overwrite without inspecting provenance and rights.

| GitHub path | Local bytes | GitHub bytes |
|---|---:|---:|
| `REPOSITORY-GOVERNANCE.md` | 33073 | 33072 |
| `archive/historical/Agentic-Enterprise-Reference-Architecture.md` | 144408 | 142164 |
| `archive/historical/The-Enterprise-AI-Agent-Fabric-Blueprint.md` | 14764 | 14134 |
| `knowledge-mining/cross-project-analysis/fabric-industry-comparison-v2.md` | 57991 | 27428 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/AEGIS.md` | 6334 | 6364 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/Kollab.md` | 8563 | 8594 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/MemOS-2026-05-21-09-53-51.md` | 6459 | 6509 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/agentic-enterprise-reference-architecture-complete-v2.md` | 6552 | 6630 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/agentic-enterprise-reference-architecture-final-V2.md` | 3990 | 4065 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/estate-pulse-main.md` | 6980 | 7022 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/estate-pulse.md` | 6975 | 7012 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/uaf.md` | 7874 | 7901 |
| `knowledge-mining/forensic-review/Individual_Project_Dossiers/workshop-2026-05-21-09-50-32.md` | 7027 | 7072 |

## Checks performed

- GitHub Git-tree enumeration and blob SHA/size comparison against pinned local bytes.
- Phase 5 lint: 18/18 unit tests pass locally; Phase 7 lint-v2: 6/6 pass locally.
- Digital twin: 13/13 tests; Programme Operating System: 11 checks; Multi-AI contributor validator: 11/11 tests.
- Meridian v1.0: 27/27 fixture checks; independent-validation pack: 12 unique scenarios and static pack checks pass.
- Tests are offline results from the matching local source files, not evidence of GitHub Actions execution or human approval.

## Deliberately excluded from blind publishing

- Protected source ZIPs, historical client archives, restricted examiner answer key, unpublished participant submissions, scratch transfers, `__pycache__`, and generated duplicate archive ZIPs.
- The uploaded generic document template library has not been declared part of the book's canonical programme sources.
- Research dossiers and historical source assets with unreviewed content or usage-rights differences remain untouched.

## Current conclusion

**The mapped, owned programme output is synchronised and byte-identical on its draft review branch. The repository is not yet converged or approved on `main`.** Review the thirteen research exceptions and merge the three existing PRs through authorised gates. Do not call the work publication-ready merely because SHA checks pass.

See `GITHUB-FILE-VALIDATION-MANIFEST-2026-11-24.csv` for a per-file branch snapshot and status.
