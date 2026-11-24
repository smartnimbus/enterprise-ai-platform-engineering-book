# REPOSITORY-GOVERNANCE.md

**Programme:** *The Enterprise AI Agent Fabric: Designing, Governing and Operating AI Agents at Scale*  
**Repository:** `smartnimbus/enterprise-ai-platform-engineering-book`  
**Document ID:** `GOV-REPO-001`  
**Version:** `1.0.0` — proposed baseline, effective upon repository approval  
**Custodian:** Book Programme Manager / Configuration Manager  
**Approver:** Author / Editorial Director  
**Governing editorial authority:** `style-v1.2.md`  
**Classification:** Programme governance; not manuscript prose  
**Last verified:** 2026-11-24

> **Bootstrap status (verified).** At drafting time GitHub reports repository size `0`, default branch designation `main`, and no initial Git commit or tree. Consequently the manuscript, Style Bible and other book files are **not yet installed in the remote repository**. The file locations below are the required *target configuration*, not a claim about existing remote files. Existing conversation artefacts must be imported by an independently verified manifest, never inferred to be present because they were created earlier in a chat. The very first governance commit is a one-time repository bootstrap exception; after that, use pull requests for all controlled changes.

## 1. Mission, scope and non-negotiable boundaries

This document governs source control, provenance, authorship, reviews, evidence, editorial production, Apress submissions, releases, archival and recovery. It is the operating model of the **book project**, not an implementation of the fictional Meridian Financial enterprise.

The following are **frozen substantive baselines**: the canonical Enterprise AI Agent Fabric architecture (four Structural Layers and eight Control Planes), 58 chapter numbers and chapter structure, the 30 Decision Atlas IDs and defaults, the Meridian Evidence Fixture v1.0 and chronology, the Meridian identity registry and evidence dossier, Chapter 16 manuscript, D-10, D-18, and applicable approved authoring blueprints. "Frozen" means their protected meaning and identifiers cannot be changed by ordinary editorial approval. An editorial correction with no substantive change still requires impact analysis and the designated owner. A substantive amendment requires the exceptional process in §7; never silently reinterpret a frozen artefact.

This governance document neither retroactively approves previous drafts nor substitutes for a publisher contract. Style Bible v1.2 is binding for manuscript writing and illustration, including Parts C, E, F, H, K, M, N and O. Apress's actual contractual production requirements supersede repository production preferences where they legitimately conflict; such exceptions require a recorded decision and must not silently alter the book's frozen architecture.

**Mandatory operating principles:** (i) one authoritative editable source per artefact; (ii) provenance of every derived representation; (iii) no deletion or untracked rewriting of frozen artefacts; (iv) roles separated for authoring, review, approval and publication; (v) traceable changes through issues, pull requests and release manifests; (vi) zero invented Meridian IDs or observations; (vii) synthetic evidence labelled as synthetic; (viii) the book must remain complete without a companion site.

## 2. Verified starting position and bootstrap

| Item | Verified 2026-11-24 | Required target |
|---|---|---|
| GitHub repository | `smartnimbus/enterprise-ai-platform-engineering-book`, public, accessible | Authoritative working repository after controlled import |
| Default branch | `main` designated | Protected, releasable integration branch |
| Remote tree | None; GitHub returned `409 Git Repository is empty` | Manifest-controlled baseline files |
| Remote pull requests | None observed | Reviewable PR record |
| Historical book materials | Available as prior conversation artefacts; **not verified as committed to GitHub** | Imported with SHA-256 evidence and custodian confirmation |
| Branch protection, rulesets, CODEOWNERS, Actions | Not demonstrable on an empty repository | Configure and test after initial commit |

**Bootstrap sequence (one-time):** (B0) commit this `REPOSITORY-GOVERNANCE.md` as the initial `main` commit; (B1) inventory every supplied file with source name, checksum, edition/status, declared authority, owner and intended destination; (B2) compare content with frozen specifications and quarantine collisions or competing versions; (B3) create a `bootstrap/artefact-import` branch from `main`; (B4) import source files without rewriting their contents, accompanied by `governance/ARTEFACT-REGISTER.csv`, `governance/BASELINE-MANIFEST.yaml` and a migration log; (B5) request independent editorial/configuration review, merge by PR; (B6) set branch protection/rulesets, CODEOWNERS and required status checks; (B7) tag the first approved programme baseline only after full validation. **Do not treat B0 as approval of B1–B7.** If repository administration cannot configure protection, record the gap and withhold any publication release.

## 3. Repository topology — target hierarchy

```text
/
├── README.md
├── REPOSITORY-GOVERNANCE.md
├── CONTRIBUTING.md
├── CODEOWNERS
├── .editorconfig
├── .gitignore
├── .gitattributes
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── ISSUE_TEMPLATE/{editorial,technical,change-request,erratum}.md
│   └── workflows/{validate,build-preview,release-check}.yml
├── governance/
│   ├── ARTEFACT-REGISTER.csv
│   ├── BASELINE-MANIFEST.yaml
│   ├── AUTHORITY-MATRIX.md
│   ├── CHANGE-REGISTER.md
│   ├── DECISION-LOG.md
│   ├── REVIEW-REGISTER.csv
│   ├── EXCEPTION-REGISTER.md
│   ├── RELEASE-REGISTER.md
│   ├── SOURCE-AND-RIGHTS-LEDGER.csv
│   └── migration/
├── editorial/
│   ├── style/style-v1.2.md
│   ├── standards/
│   ├── outlines/
│   ├── authoring-blueprints/
│   ├── reviews/
│   └── production-roadmap/
├── architecture/
│   ├── canonical/
│   ├── crosswalks/
│   └── references/
├── decisions/
│   ├── catalogue/
│   ├── pages/D-01.md ... D-30.md
│   ├── template/
│   └── reviews/
├── meridian/
│   ├── fixture/v1.0/
│   ├── evidence/
│   ├── scenarios/
│   ├── narrative/
│   └── validations/
├── manuscript/
│   ├── part-01/chapter-01/
│   ├── part-01/chapter-02/
│   ├── ...
│   ├── part-03/chapter-13/
│   │   ├── chapter-13.md
│   │   └── evidence-map.yaml
│   ├── part-03/chapter-16/
│   │   ├── chapter-16.md
│   │   └── evidence-map.yaml
│   └── part-08/chapter-58/
├── figures/
│   ├── source/chapter-13/
│   ├── source/chapter-16/
│   ├── rendered/
│   └── FIGURE-REGISTER.csv
├── playbooks/
│   ├── source/
│   └── evidence/
├── references/
│   ├── citations.bib
│   ├── standards-version-register.csv
│   └── research-notes/
├── publishing/
│   ├── apress/proposal/
│   ├── apress/submissions/
│   ├── permissions/
│   ├── proofs/
│   └── release-manifests/
├── automation/
│   ├── validators/
│   ├── tests/
│   └── build/
├── generated/                 # ignored; reproducible build products only
└── archive/                   # retained source history, explicit retirement records
```

These locations define **logical ownership**, not instructions to mass-move imported files. During B1–B4 choose a canonical location for each physical source and register old paths as aliases; never keep editable duplicates. The 58 chapters are numbered exactly as in the frozen TOC. The ellipsis above is a pattern description, not an instruction to omit chapter folders; materialise all 58 from the approved chapter inventory during the controlled import. The Mermaid and SVG figure files remain separate from chapters, with stable references. An explicit chapter evidence map links claims to fixture and decision records.

### 3.1 Source-of-truth versus generated output

| Artefact class | Editable master | Generated/derived artefacts | Rule |
|---|---|---|---|
| Editorial rules | `editorial/style/style-v1.2.md` | Compliance reports, checklists | Never edit generated reports as the source |
| Architecture | `architecture/canonical/` | Rendered figures, summary extracts | Master frozen; exceptions require escalation |
| TOC and production briefs | `editorial/outlines/`, `editorial/authoring-blueprints/` | Work trackers and chapter previews | Chapter ID and sequence frozen |
| Decisions | `decisions/catalogue/` and approved `decisions/pages/` with explicit master field in register | Typeset Atlas PDF, sample extracts | Catalogue owns ID/default; pages own approved explanatory prose |
| Meridian | `meridian/fixture/v1.0/` | Evidence tables, narrative excerpts, diagram labels | Fixture owns identifiers and outcomes; immutable v1.0 |
| Chapters | `manuscript/part-XX/chapter-YY/chapter-YY.md` | PDF/EPUB/HTML and publisher Word exports | Markdown is editable master until mutually approved editorial handoff |
| Diagrams | `figures/source/` | SVG and print PNG under build output | Source is editable, render is derivative |
| Publisher proposal | `publishing/apress/proposal/` | Submitted PDF/DOCX | Submission copies immutable and checksum-registered |
| Reviews | `editorial/reviews/`, PR reviews | Status dashboards | Immutable decisions and reviewer attribution |

**Authority is determined by artefact ID, approved baseline manifest and precedence below, not by folder names, date modified or the newest file.** If an old document contradicts a newer approved canonical source, quarantine it, cite both versions and raise a controlled change. Never resolve a conflict by silently choosing the newer file.

## 4. Configuration and naming standards

- Directory names: lowercase `kebab-case`; stable two-digit part/chapter numbers (`part-03/chapter-16`) and exact `D-XX` decision IDs in filenames.
- Primary chapter filename: `chapter-16.md`; blueprint: `chapter-16-authoring-blueprint-v1.0.md`; decision: `D-10.md`; figure source: `fig-16-01.mmd` or `.drawio`; derived figure: `fig-16-01.svg`; synthetic fixture evidence: preserve original exact IDs such as `MF-EVD-AU-001` in record names/metadata.
- Governance filenames: capitalised canonical root files (`REPOSITORY-GOVERNANCE.md`, `CONTRIBUTING.md`, `CODEOWNERS`) and explicit registered filenames for ledgers; do not case-fold frozen identifiers.
- UTF-8 text, LF line endings, final newline, no trailing whitespace, no mutable timestamps as identity. British spelling in manuscript. No secrets, real customer records, access tokens or unlicensed proprietary excerpts.
- One file = one defined artefact/authority. Use relative Markdown links to the canonical path, not duplication of content. All artefacts contain metadata in a header or catalogue: `artifact_id`, `title`, `owner`, `state`, `version`, `source_ref`, `approved_commit`, `dependencies`, `rights_status`.
- Do not rename existing frozen artefacts merely to satisfy a convention. If a rename is necessary for import, preserve bytes and map old filename → new path in migration log with checksums.
- Decision IDs and Meridian IDs are **never regenerated**, even if an entry retires. Figure numbers `13-1`, `16-1` etc. are fixed within a chapter. Reference IDs use `REF-0001` once assigned; issue, review and release IDs remain globally unique.
- Use `git-lfs` only for non-reproducible large binary source assets with a documented retention need. Do not use it for core Markdown, YAML, JSON, CSV, Mermaid or SVG.

## 5. Artefact authority and status model

**Precedence:** (A0) external law and signed publisher agreement for permitted use and output formats; (A1) approved frozen architecture and Meridian fixture for their respective technical claims, together with Style Bible v1.2 for editorial form; (A2) frozen chapter numbering and Decision Atlas catalogue for structure, IDs and defaults; (A3) approved chapter authoring blueprints and decision-page production template; (A4) reviewed chapter manuscripts, approved Atlas pages and diagrams; (A5) Apress proposal and delivery roadmap (commercial intentions, not technical authority); (A6) commentary, drafts, discovery notes and retired material. A0 does not silently override technical facts; a conflict triggers hold and formal reconciliation. No single authority outranks another outside its domain.

| State | Meaning | Read/write rule |
|---|---|---|
| `IMPORTED_UNVERIFIED` | Provenance, completeness or equivalence not validated | Read-only quarantine; cannot cite as canon |
| `DRAFT` | Authoring in progress | Editable through review branch |
| `IN_REVIEW` | Submitted to named reviewers | Material changes reset approvals |
| `APPROVED` | Accepted at an editorial gate | May change via normal change control if not frozen |
| `FROZEN` | Approved substantive baseline | No ordinary content edits |
| `SUBMITTED` | Immutable publisher handoff | Retain exact submission payload/hash |
| `PUBLISHED` | Released immutable version | Amend only through erratum/new edition |
| `SUPERSEDED` | Replaced by specifically approved successor | Keep reference and provenance, no new citations |
| `RETIRED` | Withdrawn; retained for audit/history | Excluded from builds; do not delete history |

A record may be `APPROVED` but not `FROZEN`; it may be `FROZEN` but not yet in a published edition. These are separate gates. State changes require issue/PR/review records, never just changing a CSV value.

## 6. Branching, commits, PRs and versioning

### 6.1 Git workflow

- `main`: protected baseline integration branch; no direct pushes after B0, no force pushes, no deletion, no automatic merging without required checks and reviews.
- `feature/chapter-13-context`, `editorial/chapter-16-peer-review`, `decision/D-10-copyedit`, `figure/16-01`, `governance/GOV-REPO-001`, `fix/erratum-...`, `bootstrap/artefact-import`: short-lived topic branches from current `main`.
- No permanent `develop` or per-chapter long-lived branches; milestone releases are annotated protected tags, not work branches. Rebase/update before merge, never rewrite a signed approved release tag.
- Use squash merge for routine editorial changes where available; merge commits are permitted for auditable multi-commit imports with clear provenance. Each PR changes one primary artefact family and its linked evidence/diagrams, avoiding unrelated changes.
- Commit syntax: `<type>(<scope>): <specific action>`; types `docs`, `editorial`, `decision`, `fixture`, `figure`, `governance`, `fix`, `build`, `release`; e.g. `editorial(chapter-16): clarify PEP denial receipt`.
- PR title: `[chapter-16] editorial: clarify action authorisation`; PR body: purpose, affected IDs, source hashes, freeze-impact check, validation results, reviewer roles, figure preview, rights confirmation, rollback path and links to issues.
- Block self-approval for protected content. At least two independent reviewers for architecture/security/fixture/decision baseline changes, one technical and one editorial reviewer for a chapter; a separate publication approver for submitted releases. The same person may hold roles in a small programme but cannot approve their own change as the only reviewer.

### 6.2 Versioning and releases

- **Programme baseline tags:** annotated `book-baseline-v1.0.0`, `book-baseline-v1.0.1`, etc.; each tag binds approved source files, fixture version, Style Bible version and an SHA-256 manifest.
- **Manuscript internal milestones:** `ms-draft-v0.1.0`, `ms-techreview-v0.2.0`, `ms-editorial-v0.3.0`, `ms-submission-v1.0.0`. These are examples of naming patterns, not assertions that releases exist.
- **Fixture:** `meridian/fixture/v1.0` is immutable. Any validated change is a separately approved `v1.1` directory with explicit compatibility and a migration report; no reusing v1.0 IDs for changed meanings.
- **Style Bible:** `style-v1.2.md` remains authoritative; v1.3 would require the book's style decision procedure and an impact assessment. Publisher-only formatting changes should be implemented as build profiles where possible.
- **Chapter revision:** use Git commit SHA as exact version; editorial stage as status, not proliferation of `final-final2.md` files.
- **Atlas pages:** individual prose revisions are tracked by Git, but the frozen defaults, IDs and reversibility require formal change authority. No page may exceed F1 one-page limit.
- **Publisher submissions:** immutable `apress-submission-YYYY-MM-DD-rN` tags and a payload manifest recording exact files, formats, approvals and sha256; rejected submissions remain archived, never overwritten.

## 7. Change control, exceptions and freeze protection

Every change begins with an issue and an **impact classification**:

| Class | Example | Approval route |
|---|---|---|
| `C0-METADATA` | Link or typo without semantic effect | Editorial review + automated checks |
| `C1-EDITORIAL` | Mechanism wording, non-substantive chapter revision | Technical/editorial reviewers; programme manager confirms frozen invariants |
| `C2-EVIDENCE` | Incorrect field citation, missing diagram source, cross-reference repair | Evidence custodian + relevant technical reviewer; fixture remains untouched |
| `C3-FROZEN-EXCEPTION` | New Meridian value, changed D-10 default, revised 4×8 model, reordered chapter | **Reject by default**; require documented defect, source proof, scope/impact, independent technical challenge, editorial director sign-off, new versioned baseline and publisher notification if applicable |
| `C4-PUBLISHER-PRODUCTION` | Trim, typography or format requirement | Production editor and rights owner; no silent semantic alterations |

The change request must capture `CR-ID`, problem, affected artefacts/IDs and chapters, existing approved value, proposed change, why a correction is unavoidable, alternatives, tests, reversibility, owner, approvers, effective baseline, migration work and downstream impact. A C3 request cannot proceed as a routine PR; first obtain an explicit decision in `governance/DECISION-LOG.md`, then implement through an independently reviewed PR. Emergency correction uses a temporary hold/erratum, **not** an unreviewed force push.

Conflicting sources are recorded in `EXCEPTION-REGISTER.md` with links and hashes. `SUPERSEDED` and `RETIRED` material remains readable in archive or Git history; removal from current builds is explicit in the artefact register. Do not rewrite history or destroy legal/source evidence.

## 8. Review and publication gates

| Gate | Name | Entry evidence | Exit evidence / decision |
|---|---|---|---|
| G0 | Source intake | Inventory, checksum, source, rights | Provenance validated; canonical owner designated |
| G1 | Pre-writing | Approved brief, type F6/F7/F1/F2, source map | Style Bible M1 signed off |
| G2 | Author draft | Complete Markdown and refs | Mechanical checks; no unknown/fabricated IDs |
| G3 | Technical review | Mechanisms, scope, evidence, figure sources | Independent architecture/security/data reviewer approval |
| G4 | Developmental edit | Full chapter plus comments | Reader journey, depth, anti-slop, narrative and E4 validated |
| G5 | Copyedit and accessibility | Text, diagrams, references | M2, K1/K2, H2, alt text, greyscale and link checks pass |
| G6 | Production integration | Approved chapter/decision/figure | PDF/EPUB layout, one-page F1, print legibility, index/xrefs |
| G7 | Apress submission | Proposal/manuscript and permissions | Named approver signs submission manifest; immutable handoff |
| G8 | Publication/errata | Publisher proofs and legal approvals | Publisher-approved final payload tagged; corrections tracked |

No claim of completion of G3–G8 is valid without reviewer identity, date, reviewed commit SHA, findings and closure evidence. The current Chapter 16 draft and D-10/D-18 previews are **not automatically publication-approved** because they existed before remote import. A prior 27/27 fixture consistency run is evidence for a particular local version, not proof that the later repository files match those bytes.

### 8.1 Chapter workflow

1. Open issue with chapter number, type, versioned authoring blueprint and cross-reference list; verify chapter ID against frozen 58-row TOC.
2. Run M1, establish `manuscript/.../evidence-map.yaml` with cited source/fixture IDs; note source and claim-level uncertainty.
3. Write only on short-lived branch; preserve E1/E4/F6/F7, C2 vocabulary, C7 claim provenance, C10/O anti-slop and E5 narrative limits.
4. Supply tables with captions/source, diagrams by figure IDs, and synthetic case evidence that matches fixture chronology.
5. Run local tests; open PR with word/page estimate and required reviewer assignments.
6. Technical review, developmental edit and Style Bible M2 checks; resolve all critical/major findings before approval.
7. Integrate to `main`; produce reproducible preview; store status, reviewers and approved commit in register.
8. After publisher acceptance, lock edition content and route later fixes through errata/new-edition control.

### 8.2 Decision Atlas workflow

- The **catalogue** owns decision ID/title/context/default/trade-off/deviation/reversibility/artefact; the approved one-page page may supply worked evidence in `Why` and editorial cross-references without changing those fields.
- Import decisions D-01 to D-30 with stable IDs. Draft in `decisions/pages/D-XX.md` using F1 **exactly**: `Context`, `Default`, `Why`, `Trade-off`, `When to deviate`, `Reversibility`, `Artefact`, `See also`.
- Validate frozen-value equality, evidence IDs, one-page print preview, change rationale and no invented approval/receipt. D-10 and D-18 remain frozen as existing samples; edits require their custodian approval.
- Obtain decision custodian + technical + editorial reviews. Release PDF only as a derived, traceable preview of an approved source commit.

### 8.3 Diagram workflow

- Open figure issue including `fig-13-01` / `fig-16-01`, chapter, diagram type, frozen inputs, approved claims and source refs.
- Use only H1's eight types; restricted H3 notation, no more than 12 nodes/20 edges, one main point per diagram, meaningful directional edges and verb-labelled relationships.
- Keep Mermaid/draw.io/Excalidraw **source** in `figures/source/`; generate SVG and 300-dpi print raster as needed. Do not hand-edit exports independently.
- Require figure title, ID, version, source note, legend when needed, one-sentence caption, 2–3 sentence alt text, greyscale legibility, WCAG-related contrast and a prose/table equivalent.
- Verify specific negative claims: a denied refund **must not** be pictured as an executed ledger call; the Week 11 release failure must not be confused with Week 9 policy denial.
- Reviewer: chapter technical owner plus diagram/accessibility reviewer. Record source SHA and render tool version.

### 8.4 Review and issue workflow

Review findings have stable `REV-` IDs, severity (`BLOCKER`, `MAJOR`, `MINOR`), owner, source span, suggested correction, reviewer, closure proof and disposition. Blocking defects prevent merge; unresolved major defects need explicit editor disposition and cannot be hidden in comments. Every PR identifies whether a technical peer review was independent. A publisher proof correction is linked back to the exact approved source revision and reruns affected checks.

## 9. Apress proposal and submission workflow

The manuscript and proposal are separate release products. `publishing/apress/proposal/` contains the editable proposal, annotated frozen TOC, six-comparator matrix, audience/market evidence and sample list. The reviewer assembles a release manifest listing title/subtitle, rights, author biography, figures, accessibility, complete chapter synopses, sample chapters 13 and 16, Decision Atlas samples and evidence designation. Obtain editor approval and author approval; verify the current publisher form and any sole-consideration/exclusivity requirements **at submission time**. Do not record an exclusivity promise without the author's confirmation. Export a dated immutable handoff; record recipient, submission time, means, response, rights issues, edition, hashes, and subsequent revision requests. Apress requests cannot implicitly rewrite Style Bible or frozen technical sources; use C4 or escalate C3.

**Publication gates:** a proposal may be `SUBMITTED` without a finished book; individual chapters must be G5/G6-approved before representing them as production-ready. No publisher version may have unresolved critical technical, rights, fabricated evidence or accessibility defects. A release checklist must include agreement on fonts/trim/figure licensing and final indexing. Release artefacts are generated from an approved tag rather than local unstaged files.

## 10. Roles, authority matrix and separation of duties

| Role | Writes | Reviews | Approves/owns |
|---|---|---|---|
| Author | Manuscript, sample prose, original arguments | Responses to reviews | Intellectual responsibility, rights statements |
| Book Programme Manager | Register, roadmap, PR coordination | Milestone and completeness | Programme status; cannot self-certify content |
| Configuration Manager | Baselines, manifests, releases | Cross-file and change impact | Git integrity, frozen-artefact preservation |
| Developmental Editor | Editorial changes and briefs | Teaching flow, chapters, narrative | Editorial readiness; not technical truth alone |
| Technical Architecture Reviewer | Technical findings | Architecture and engineering mechanisms | Technical review disposition |
| Security/Data Reviewer | Risk/evidence findings | Security, delegation, provenance, privacy | Specific domain verification |
| Decision Atlas Custodian | Decision change requests | Frozen values and F1 compliance | Decision-page acceptance within authorised baseline |
| Meridian Fixture Custodian | Fixture intake and migration report | Identifier/chronology integrity | Fixture baseline, C3 escalations |
| Diagram/Accessibility Editor | Figures and proofs | H/K rules, formats | Visual and accessibility approval |
| Publisher Liaison/Editorial Director | Proposal and handoff | Contract, market, rights, production | Release authorisation for publisher submission |

For a single-person team, designate a named external or independent reviewer at each high-risk gate. Absence of a reviewer means `BLOCKED`, not implied approval. Actual GitHub CODEOWNERS entries must use accounts/teams confirmed to exist and have review access; **do not invent handles**. Keep the initial role mapping in `governance/AUTHORITY-MATRIX.md` and update it through review.

## 11. Validation and CI policy

Mandatory checks for PRs touching controlled artefacts:

1. Inventory schema and no duplicate `artifact_id`, decision ID, chapter ID, figure ID or Meridian identifier.
2. Verify 58 frozen chapter numbers/part assignments and 30 exact decision IDs/defaults by hashing approved canonical data fields, not by relying on source file names.
3. Re-run Meridian fixture integrity and cross-reference tests on the **imported bytes**; ensure contextual conflict remains `UNRESOLVED`, Week 7/8/9/11 events remain ordered, `MF-EVD-AU-001` is a DENY and financial mutation count remains zero.
4. Verify Markdown links, citations/source ledger, evidence-map references, reference standards dates and figure registry consistency.
5. Scan for secrets, sensitive personal data, unlicensed images, inappropriate pasted copyrighted material and ambiguous synthetic/real evidence claims.
6. Check F1 page count, F6/F7 required headings, chapter E4 closing blocks, text anti-slop checks, spelling, and one-page decision exports. Automated word/rhythm checks are advisory unless an explicit Style Bible rule is mechanically enforceable.
7. Build diagrams, validate Mermaid syntax, inspect human-readable negative flows, alt text and greyscale; image accuracy needs human review even if rendering succeeds.
8. Record exact test command, tool version, inputs, source SHA and pass/fail report. No fabricated green checks when runners or scripts have not yet been installed.

CI checks are **proposed** until the repository has workflows, branch rules and a successful run. A later migration must preserve existing manual review evidence. A build failure blocks publication rather than causing the author to quietly delete evidence fields.

## 12. Contributor guide and conduct

Before contributing, read `REPOSITORY-GOVERNANCE.md`, the ratified Style Bible, the approved canonical architecture, the frozen TOC and decision catalogue, the Meridian fixture relevant to your work, and the relevant authoring blueprint. Ask the programme manager for the latest `BASELINE-MANIFEST.yaml`; avoid citing loose chat files as canonical. Contributors do not create new Meridian identifiers, alter published decision defaults, renumber chapters, replace source material with generated text, or add new architecture models. All factual claims require a source reference or explicit `synthetic/illustrative` designation. Personal data and third-party material require rights review before commit. AI-assisted prose, figures and technical checks are declared in the source ledger per relevant publisher policy; AI output is never treated as independent evidence. Contributor statements of expertise must be verifiable.

Submission procedure: claim a labelled issue; branch from `main`; edit only identified files; run checks; open a linked PR with before/after and evidence; request required roles; address findings; record decision and status; merge only after gates. External contributions need contributor rights/permissions approval and editorial acceptance before integration. Comments remain professional and evidence-based; disagreements are resolved by source authority and change control, not editor seniority alone.

## 13. Recovery, audit and archival

Weekly verify that the baseline manifest resolves to current `main` and that the last approved tag is retrievable. Monthly export a read-only repository mirror and signed/hashed release manifests to a separately controlled location, subject to rights and publisher contracts. A restore drill must reproduce the canonical Markdown, fixture validation, decisions and figure renders from a tagged commit; record outcome and any unavailable binary dependencies. Git history is a traceability aid but not an independent backup. Do not depend on generated build artefacts or one individual's local machine for recovery.

Do not erase retired artefacts; relocate only when a migration map and preserved Git history support traceability. Restrict access to unreleased commercial proposals, private contact information, customer evidence and publisher correspondence; the verified repository is **public**, so do not upload any confidential contractual or personal material there. If confidential materials are required, use an approved separate private location with a controlled reference in the register.

## 14. Operational reporting and enforcement

At each monthly book programme review publish: baseline tag/SHA, authoritative artefact coverage, number of imported/unverified sources, chapters by G0–G8 stage, decisions completed and one-page checked, diagrams rendered/reviewed, Meridian test status, open blockers/major findings, submissions and responses, release risks, and next milestone. Never report an artefact as committed or approved unless the source URL, exact SHA and named approval are recorded.

**Go/no-go conditions:** no fabricated source provenance; no unresolved frozen-content changes; no ghost approvals; no unreadable decision page; no omitted reviewer; no synthetic evidence claimed as production proof; no publication from a working tree; no missing publisher rights approval. Any violation blocks the relevant gate and creates an issue.

## 15. Adoption decision and initial tasks

This document becomes binding after approval by the Author/Editorial Director and configuration custodian. Its first remote commit, if used to initialise the otherwise-empty repository, is **bootstrap only**. Required immediate tasks are: import and reconcile frozen artefacts; create and sign the artefact register and baseline manifest; establish roles and CODEOWNERS; activate repository rules and CI; complete a dry-run chapter/Atlas/figure PR; tag an initial authoritative baseline after tests and approvals.

**Out of scope for this governance change:** writing Chapter 13, altering Chapter 16, modifying D-10/D-18 or other frozen decisions, revising the Meridian fixture, reshaping the book or creating an unapproved publisher submission.