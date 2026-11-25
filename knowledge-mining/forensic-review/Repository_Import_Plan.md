# Repository preservation and curated-import plan

**Target:** `smartnimbus/enterprise-ai-platform-engineering-book`  
**Governing source:** `REPOSITORY-GOVERNANCE.md`  
**Authority rule:** The book's ratified architecture, 58-chapter order, 30 fixed decisions, Style Bible v1.2 and Meridian Fixture v1.0 are not superseded by these historical archives.

## 1. Preservation is not publication

These ZIP and 7z files are evidence deposits. They contain proprietary architecture, internal workshop material, raw source inventories, third-party references, generated images, publication drafts and possibly personal/confidential data. The book repository is public. **Do not import raw archives, 7z contents, Git history packs, private chat files, operational secrets or asset-identifying datasets into it.** The analysis has not authorised publication of any original archive.

Use a **restricted preservation store** with immutable original bytes, SHA-256 per archive, access register and checksums. Use an **editorial source ledger** in the book repository containing non-sensitive metadata, a source identifier, rights status and curated findings. Keep a separate **publication working area** for approved excerpts and redrawn diagrams.

## 2. Provenance classes

| Class | Authority / treatment | Example |
|---|---|---|
| `CANONICAL-FROZEN` | Binding and change-controlled; cannot be overwritten by discovery | Style Bible, Meridian Fixture, D-10 and D-18 |
| `HISTORICAL-ORIGINAL` | Immutable restricted deposit | All nine uploaded packages |
| `HISTORICAL-VARIANT` | Separate version, explicit diff and provenance | Complete v2 versus Final V2 |
| `THIRD-PARTY-REFERENCE` | Do not claim authorship; licence/rights verification before use | `MemOS/ref/awesome-copilot` and linked web/image material |
| `INTERNAL-RESTRICTED` | No publication until explicit clearance | Workshop application inventory and internal infrastructure |
| `RESEARCH-EXTRACT` | Structured findings with source path, paragraph/line, hash, limitations | Concept IA-001 to IA-086 |
| `PUBLICATION-CANDIDATE` | Requires technical, editorial, privacy, attribution and rights gates | Redesigned figure, adapted example, comparison matrix |
| `DERIVED-GENERATED` | Rebuildable by script; never sole source of truth | CSV graph exports, PDFs and diagrams |
| `RETIRED-FOR-BOOK` | Historical retention, no case reuse | Helios narrative, prior layer taxonomies |

## 3. Recommended paths in book repository (once approved)

```text
research/
  historical-projects/
    source-register.csv            # safe provenance only
    archive-delta-register.csv     # hashes, no private paths beyond safe metadata
    intellectual-asset-register.csv
    book-relevance-matrix.csv
    modernisation-assessment.md
    cross-project-synthesis.md
    dossiers/                    # redacted/rights-reviewed versions only
    sources-and-rights.md
  knowledge-graph/
    graphml/
    nodes.csv
    edges.csv
  editorial-validation/
    claim-review-queue.csv
    author-rights-clearance.csv
    confidentiality-review.csv
```

Do not publish `extracted/`, `data/`, third-party `ref/`, `.git/objects/`, full workshop dumps, private real-company names, secret examples or proprietary workbooks.

## 4. Ingestion gates

| Gate | Input | Proof | Approver | Failure outcome |
|---|---|---|---|---|
| R0 custody | Original ZIP/7z | Full SHA-256, filename, size, date, restricted access | Configuration custodian | Quarantine |
| R1 inventory | Archive manifest | Every entry classified; binary/oversize omissions identified | Repository curator | Do not use unsupported content |
| R2 authorship/rights | Original works and assets | Ownership, licensing, company consent, generated-image provenance | Rights editor | Restrict use |
| R3 security/privacy | Internal code/data | Secret scan, personal data and topology review, redaction | Security reviewer | Quarantine |
| R4 relevance | Source-anchored concept | Evidence passage, maturity/claim status, book mapping | Development editor | Historical only |
| R5 architecture alignment | Research extract | No frozen taxonomy/Decision/fixture change | Architecture custodian | Escalate, do not rewrite |
| R6 technical validation | Claims and examples | Verified tests, primary-source references, or synthetic label | Technical editor | Flag as hypothetical |
| R7 editorial/publication | Adapted source | Style Bible, alt text, cross-reference, source credit | Editorial director | Reject from manuscript |

## 5. Recommended source import dispositions

| Archive | Custody | Research | Suitable publication use | Exclude from public repository |
|---|---|---|---|---|
| `estate-pulse-main.zip` | Retain canonical content copy | Ingestion/worker/ADR case | Redacted supporting case methodology | Real infrastructure and identities |
| `estate-pulse.zip` | Retain duplicate-package hash and reference | No redundant concept ingestion | None additional | Duplicate whole archive |
| `AEGIS.zip` | Retain full lineage and PDF | Cognition, policy, evidence, narrative history | New attribution-cleared prose/diagram inspiration | Historical Helios case, unlicensed artwork |
| `Kollab.zip` | Retain design docs | Collaborative memory, runtime hooks, FinOps, convergence | Select conceptual illustrations with claim caveats | Third-party reference images, unverified benchmark claims |
| `uaf.zip` | Retain design and adverse audit | Gateway/identity/memory, failed security-control evidence | Carefully anonymised design-vs-evidence contrast | Private chats, hardcoded test secrets, unauthorised config |
| `MemOS...7z` | Retain first-party + third-party provenance separately | Bitemporality, retention, workshop governance | Memory provenance discussion, after citations | Vendor reference tree and copied skill content |
| `workshop...7z` | Restrict whole package | Human challenge, gated ADRs, lifecycle-to-exit | Redacted facilitated-review method | Internal source spreadsheets/data |
| `...complete-v2.zip` | Retain historical baseline | Selection workbook/agent taxonomy | Decision method explanation, after review | Historical competing layer model as new canon |
| `...final-V2.zip` | Retain delta baseline | Historical source diff | No duplicate content | Unreviewed installer/product extracts |

## 6. Version and duplicate procedure

- The two Estate Pulse archives contain identical 167 non-directory files by content SHA-256. Record two original archive packages but one conceptual source lineage.
- The two v2 architecture archives have 371 common file paths and ten differing/added/removed paths. Produce a minimal textual diff and annotate any reference to the main architecture document as **complete-v2** or **final-V2**; never rely on a bare “v2” label.
- Maintain a source hash alongside every concept record. If source files change, mark the record for re-review rather than silently updating historical claims.
- The author's existing published/rights-controlled materials must remain under their own separate licence status until verified.

## 7. Change control and decision governance

The 86 historic concept records are research inputs **only**. None creates D-31, alters D-10/D-18, changes a chapter number, or modifies the Meridian fixture. New evidence can enter the manuscript only by a normal reviewed editorial pull request, citing the exact research source. A perceived critical architecture defect follows the existing exceptional-change escalation rather than automatic rewriting.

## 8. Import order

1. Preserve archive checksums and file manifest in the restricted custody store; deduplicate concept processing, not original package evidence.
2. Screen confidential data, IP provenance and third-party reference materials; quarantine anything not cleared.
3. Review and import `Cross_Project_Synthesis.md`, `Modernisation_Assessment.md`, and the 86-entry safe concept ledger as **research**, not governing architecture.
4. Import individual dossiers only when identifiers/company-specific details are approved for the public repository.
5. Add knowledge graph and reproducible mapping scripts; link node evidence back to the restricted source store through opaque IDs where necessary.
6. Create PR containing the curated research, with separate sign-offs from editorial, rights, security, and architecture custodians.
7. After merge, run the frozen Chapter 13/16/Decision Atlas baseline integrity checks. If any frozen artefact changed, block publication.

## 9. Publication red flags requiring explicit resolution

- The AEGIS interior PDF contains a copyright statement with a named author and says legal/confidentiality review remains necessary. Confirm ownership and attribution before incorporating wording or images.
- Workshop workbooks and Estate Pulse source describe actual enterprise systems. This is not safe synthetic Meridian evidence.
- The MemOS `ref` tree is a massive third-party reference collection. Presence in a ZIP does not grant republication rights.
- Several diagrams use older architectural plane and layer taxonomies or are too dense for the Style Bible diagram limits.
- UAF audit findings and MemOS scaffolding reports contradict superficial “production-ready” readings of the design claims.

## 10. Definition of done

The research import is ready only when the source-to-claim chain is replayable, all rights/security gates have documented outcomes, every extracted concept has a frozen chapter/decision mapping or an explicit exclusion, and no original archive or sensitive content is on public `main`.

**Current status:** Analysis complete at a curated conceptual level; **no GitHub import performed**. This document is a recommendation, not an approval to publish raw evidence.
