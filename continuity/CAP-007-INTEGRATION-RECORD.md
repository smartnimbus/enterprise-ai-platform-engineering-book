# CAP-007 — Working integration record

26 November 2026. Author explicitly requested integration of all existing committed book assets. Working baseline amendment v1.1.0 effective; independent technical/editorial acceptance, rights and strict release gates unchanged. No new acquisition assessment.

Initial main: cc728dbec56190276eb3f25b5f10729c9959ab95. Verified integrated asset revision: 6272044e2b4e4d1dd110cda0f1a48e1aec30f4f6. This record precedes its own closure-only PR and does not predict that PR's commit SHA.

| PR | Original head | Merge into main |
|---|---|---|
| 22 | f71d431fcf6a5e4034f8d0e361dbafa4ae443f2a | b0bcac176f270a39ac6a5739a8c99c978ab3f2e2 |
| 19 | 1a932ea3125c548ae3238e3a653bbc1159d27e22 | f4bdc4524096520193eafbee7b13cd3548d4288e |
| 21 | 2316e582f48ba3ecb0726bb892da8ae85cb0a38f | ed70cac10ba049e86bb8a71230ab89ca77583c6c |
| 11 | 1d7699d1b3f4abc8fe8c2d8e477697c8be2ecc3e | 602f9c2c74f3dbe70b500cc999e088f07c8e769d |
| 7 | 22ecbf572e885cad992b261fc0b3181c01e654ed | f1833b574193136e994602bf8279419b11da3a5f |
| 9 | 441dc92902ba26666ba6615af8ae9343baf45322 | 28090bbf2a039a937ee43294afb4c1cdfa584b3b |
| 13 | dec94ae45dbbb7ada8e67571549224952fc018ea | 925aabd9a1620b4bfab1a5e814592ad40364a1c4 |
| 17 | a1b5416801baaf740abe6c1e08adb5734d432621 | 09106de2a644f7749026fcf2b86b088cf51ae315 |
| 15 | 8a8fa0962a765fb8558d065e349eec9ec92b8c4e | 6272044e2b4e4d1dd110cda0f1a48e1aec30f4f6 |

PR21 retargeted to main after PR19. Four topic reconciliation merge commits: PR9 b7e07d2a5fc54ccefdbc813f0e8a3957d756c0c7; PR13 e8dd4ad4f7cce42ab65066135317c641267d7db5; PR17 8f5feabc4f546d199838553641fbdd727ed49caf; PR15 497fb318891c4a58c57ba15d4cbe5982a00d1e74. Initial PR9/17 merge attempts returned HTTP 405 conflict, resolved on topic branches with both parents and original non-overlap blobs. No force/direct push to main.

## Executed verification

Compared recursive original topic trees against initial and integrated main. 295 baseline blobs, 416 integrated blobs; 131 unique changed paths, 129 exact source blob matches, two explicitly reconciled paths (root README and production-plan README), zero mismatches outside those, zero baseline paths missing, zero unexpected changed paths. 24 baseline blobs in Meridian fixture, decision catalogue, outlines, Style Bible and frozen TOC unchanged. All 50 historical acquisition manifest paths match recorded Git blob and size in integrated tree; pinned source manifest not rewritten. All nine PRs reported merged, zero open PRs before closure. All 13 non-main branch heads compared against integrated main with ahead_by=0, including four historical branches. All original topic heads retained via merge ancestry. Branch refs retained; no branch deletion, tags or releases.

## Prior validation, not newly executed

Historical [mechanical results](../publishing/apress/submissions/validation/acquisition-mechanical-results.json) and [proof preflight](../publishing/apress/submissions/validation/acquisition-proof-preflight-results.json) integrated verbatim. Pinned mechanical checks previously passed; strict release lint still blocked. Historical render results do not establish correct typography, tagged PDFs, page fit, human visual inspection or independent acceptance. No fresh integrated CI run claimed; source identity comparison is the current integration check. No external publication/rights approval.

CAP-006 remains partial (original later responses unavailable). CAP-008 not started. Author facts, genuine reviewer evidence, rights and delivery commitments still outstanding. Administrative branch protection/cleanup separate; no destructive changes.
