# Forensic method, coverage and limitations

**Assessment date:** 24 November 2026. **Input:** Nine uploaded archives. **Purpose:** Preserve historic intellectual capital without editing the frozen book. **No executable code was run from the user archives.**

## Coverage

1. Opened and inventoried all nine archives, including two 7z packages using libarchive; preserved original archive SHA-256 and per-member source SHA-256 for extracted text.
2. Enumerated every non-directory archive member and classified into extracted source/text, development metadata, binary, empty or oversize. All extracted text files were processed for content heading/link indices. No `.git` pack stores or binary libraries were treated as primary authored documents.
3. Examined engineering documents, ADRs, workshop materials, design specifications, code manifests, scripts, schema and high-value substantive notes; created 86 manually curated concept entries with an exact source-file, SHA-256, text anchor and line number, all successfully matched to their source files.
4. Compared duplicate/sibling archive file hashes; created explicit content-difference findings.
5. Parsed UAF draw.io source XML (ten first-party diagrams) and extracted labels and page/cell counts. Other diagram drawings exist in Markdown/Mermaid and have been indexed textually. AEGIS's 220-page PDF was rendered for visual inspection and extracted to searchable text; the PDF cover and representative content were examined. The full PDF text was indexed for term searches, not individually typeset-page-reviewed.
6. Opened the reference architecture's seventeen-sheet solution-selection workbook using the spreadsheet reader; checked dashboard, requirements, gate classifications, capability mappings, weights, scoring, example PoC and decision record. These are workbook examples, not independently evidenced product measurements.
7. Classified sources' claims as design, documented ADR, code-present, audit finding, historical reference, or scaffold. Source code presence was distinguished from tested or deployed status.
8. Built a graph of project→concept→pattern→Decision Atlas ID→architecture→chapter and publication mapping; the graph includes 86 extracted concepts, not every incidental term in the reference collection.

## Where the review is not exhaustive

- **Not every word of every document received a manual technical review.** Thousands of text/source files were systematically opened and indexed, but intensive human-style analysis was concentrated on representative, high-value first-party documents, AD​Rs, workshops, and relevant source code. Treat this as a substantial source-anchored first-pass forensic review rather than a certified line-by-line audit of every file.
- **Binary workbooks, images and PDF pages were not all manually inspected.** Four large workshop source-data workbooks were identified and classified as restricted potential enterprise data; they were not subjected to cell-by-cell analysis or copied into this deliverable. Third-party reference screenshots were not individually assessed for content ownership.
- **No compiled code, package install, integration service, cloud deployment or security control was executed.** Static source and audit claims do not establish operating readiness.
- **Archived Git internals were inventoried, not replayed as complete branch/commit histories.** UAF and MemOS contain substantial repository object material; extracted working trees and historical write-ups do not prove an exhaustive Git evolution chronology.
- **Internet-linked references were not recursively downloaded in bulk.** Local Markdown references were enumerated, with unresolved link targets retained for review. External links are outside the frozen archive evidence scope.
- **Automated link reports contain false positives**, including paths that point to GitHub, excluded dependencies, generated files, alternate export roots or renamed documents. Unresolved does not mean broken in the original workspace.
- **Authorship and copyright were not independently verified.** Source-internal names, copyright notices, dates and claims are evidence to investigate, not proof of ownership.
- **Claims that the archives represent multiple years cannot be independently validated from these files alone.** Most explicit dates visible in the analysed snapshots fall in April–August 2026; some work may have earlier provenance not included in these uploads.

## Traceability and confidence

- `archive_summary.json`: physical archive counts and SHA-256.
- `file_manifest.csv`: every archive file, size, extension, classification, per-text-member SHA-256.
- `Document_Headings_Index.csv`: all captured Markdown headings with source lines.
- `Reference_Link_Audit.csv`: relative Markdown links resolved against the extracted snapshot.
- `Intellectual_Asset_Register.csv`: 86 validated concept-to-source and book mappings with a specific evidence excerpt.
- `Visual_Artifact_Inspection.csv`: diagram names, XML structure and first-party labels; binary assets enumerated.
- `Knowledge_Graph_Nodes.csv`, `Knowledge_Graph_Edges.csv`, `.graphml`: attributed conceptual genealogy, with thematic links explicitly editorial rather than direct citations.

**Confidence scale:** `DIRECT SOURCE` = exact file/text content matched; `DESIGN CLAIM` = a design description without independent runtime proof; `CODE PRESENT` = implementation source found but not executed; `AUDIT CLAIM` = source report's finding, not independently re-tested; `INTERPRETATION` = editorial relevance or chronological extrapolation.

## Security and intellectual-property cautions

The workshop archive includes application/server mapping workbooks and the Estate Pulse documents mention real enterprise infrastructure. The MemOS reference tree includes third-party material. The AEGIS PDF expressly includes a copyright and publication disclaimer. The book repository is public; no original archive contents should be uploaded there without explicit security, confidentiality and intellectual-property review.
