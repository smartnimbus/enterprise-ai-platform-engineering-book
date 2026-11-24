# Programme Digital Twin — Derived Repository Model v1.0

**Classification:** implementation proposal and executable proof of concept — **NOT APPROVED CANONICAL CONTENT**  
**Date:** 24 November 2026  
**Repository:** `smartnimbus/enterprise-ai-platform-engineering-book`  
**Authority:** existing `REPOSITORY-GOVERNANCE.md`, frozen Atlas, chapters and Meridian, and existing Programme Operating System, Independent Validation Programme, and Multi-AI Contributor Operating Contract. No new governance, authorisation state, workflow or backlog is created here.  
**Scope:** content-indexing conventions, a derived graph schema and deterministic proof-of-concept data extraction. The repository's authoritative sources never derive authority from this index.

## Executive implementation decision

Build **a rebuildable dependency index and health report**, not a new database of record. Start with Git Markdown + JSON + CSV, git commit SHA, source file hash, explicit source-to-target crosswalk and Python validation. Store the *source facts* only in their approved upstream artefacts; store graph/index as disposable materialised output. Never allow human or AI editors to change a derived edge to 'fix' its source. A source discrepancy raises an issue in the existing operating system.

**Present verified GitHub boundary:** `main` has only `REPOSITORY-GOVERNANCE.md`, with no branch protection. Draft PR #1 (book and historical import), PR #2 (governance and execution), and PR #3 (deterministic-first research) remain open. This proof of concept indexes **provided local CSV sources**, *not the current approved remote GitHub tree*, and labels its outputs `LOCAL_INPUT_NOT_APPROVED_REPOSITORY`. The first authoritative CI run is blocked until the source manifest/import is approved; the present output must never be described as approved decision-implementation coverage.

## 1. Repository object model

An entity has a durable assigned `id`, `type`, `source_locator`, `source_revision` (Git commit or immutable published URI/version), content digest, status as reported by the owner, timestamp and optional evidence anchors. A derived index records observations about entities, not their legal or governance authority. Avoid conflating:

- **Decision** `D-01`–`D-30`: frozen general Atlas choice/default; **AppliedDecision** is a separate organisation-specific application/ADR with an owner, scope and its own ID; it can reference D-10 but not rewrite it.
- **Chapter** `CH-001`–`CH-058`: stable number; manuscript state and publication version must be sourced separately from the TOC. An outline entry does **not** mean the chapter is written.
- **Pattern** `EP-001`…: ranked *candidate*, until approved and tested. Do not infer implemented capability from a pattern description.
- **Article** `KA-001`…: ranked candidate, until reviewed and published. No AI-generated draft is silently promoted.
- **Claim**: one falsifiable assertion anchored to a citation span and to its source version; distinguish `ASSERTED`, `CONTESTED`, `WITHDRAWN`, `VERIFIED`. Claim status comes from reviewed claim record, **not AI confidence**.
- **Source**: RFC/standard/vendor documentation/book/research/incident etc., with version, copyright/rights, licence, retrieval date, canonical URL or internal custody pointer, evidence restriction, author and content digest. External sources are not authoritative for the frozen book merely because cited.
- **Evidence**: synthetic vs observed, environment and time, raw hash, collector, independence flag, retention and linkage to claim/test; synthetic Meridian fixture cannot prove production.
- **Test**: test definition distinct from **TestRun** with actual pinned commit, environment, runner, observed result, logs and approval.
- **Issue, PullRequest, Review**: identifiers are GitHub repository-qualified e.g. `github:smartnimbus/enterprise-ai-platform-engineering-book:pr:2`; review is an individual immutable GitHub review event, not a model opinion.
- **ValidationScenario**: `IV-01`–`IV-12`, definition only; **ValidationRun** is a distinct restricted participant event, including independence, score and source version.
- **LearningAsset**: role, prerequisites, competence and assessment; distinguishes planned syllabus from independently evaluated learning.
- **AIContribution**: agent registration + run ID + task, model/config revision, tool principal, exact base SHA, patch, scope, evidence, handover and human review. An AI identity is metadata, not a grant of permission.
- **WorkItem / Release / Repository**: scope and task status from existing work register; approved release provenance and repository identity; don't invent a second operating status.

**Recommended technical types** in the graph: `decision`, `applied_decision`, `chapter`, `pattern`, `article`, `claim`, `source`, `evidence`, `test_definition`, `test_run`, `issue`, `pull_request`, `review`, `validation_scenario`, `validation_run`, `learning_asset`, `ai_contribution`, `work_item`, `release`, `repository`, `glossary_term`. Types outside this list require a versioned schema migration, not ad hoc node keys.

### Distinct state axes (never collapsed)

- **Authority tier**: as defined by existing Knowledge System Blueprint (T1 frozen; T2 approved derived; T3 work; T4 experimental; T5 external reference). This must be read from authoritative data, or `UNKNOWN`.
- **Workflow state**: existing Programme Operating System state, sourced from its work item; never computed from a file being present.
- **Evidence grade**: `SPECIFIED`, `IMPLEMENTED`, `REPRODUCED`, `INDEPENDENTLY_VALIDATED` only if supported by review and test records. No 'best guess'.
- **Publication state**: explicit publisher/release record, otherwise `NOT_VERIFIED`.
- **Graph materialisation status**: `EXTRACTED`, `STALE`, `UNRESOLVED`, `EXCLUDED`; these labels describe graph mechanics, not project approval.

## 2. Relationship model, direction and semantics

Canonical direction: **subject -> object**. Every edge has `source_anchor`, `source_sha256`, `observed_at`, `assertion_kind`, and optionally `review_event_id`; avoid anonymous inferred facts.

| Type | Domain -> range | Precise meaning | Do not infer |
|---|---|---|---|
| `references` | any -> any | source explicitly names target | approval or implementation |
| `depends_on` | any -> any | source declares prerequisite | runtime call graph |
| `implements` | code/config -> decision/pattern | explicitly mapped working implementation | from a proposal or design prose |
| `validates` | test_run/validation_run -> claim/asset | actual executed test result with evidence | from test definition or scenario |
| `tested_by` | asset -> test_run | corroborated executed test | from test name alone |
| `challenges` | claim/review -> claim/decision | recorded reasoned challenge | rewriting frozen decision |
| `supersedes` | new_version -> old_version | explicit approved replacement | rename/similarity alone |
| `approved_by` | asset/revision -> human_review | recorded human approval | AI reviewer, merged-looking prose |
| `published_in` | asset_version -> release/book | release manifest enumerates it | file path includes `manuscript` |
| `retired_by` | retired_asset -> work_item/change | explicit retirement event | deleted/missing file alone |
| `derived_from` | generated_asset -> source | recorded transformation | source similarity |
| `teaches` | learning_asset -> concept/pattern | declared learning outcome | topic in passing |
| `uses_evidence` | claim/decision -> evidence | explicitly cited evidence record | same lexical string |
| `produced_by` | change/asset -> ai_contribution | recorded provenance | commit author is an AI nickname |
| `reviews` | review -> change | reviewer evaluated exact version | comment without review event |
| `blocks` | evidence/failed_test -> release/PR | negative gate actively enforced | test suggested but not executed |
| `affects` | issue -> asset | explicit impact scope | same repo folder |

Additional typed relationship semantics may be stored as properties (scope, direction, validity interval) rather than creating unrelated edge names. Never compute `approved_by` or `validated` using text extraction.

### Temporal semantics

Every edge can have **observed_at**, **effective_from**, **effective_to**, and **source_version**. A later edge does not delete a historic edge. Render current/as-of views by filtering effective ranges and approved source versions; report unknown effective dates. Release snapshots pin exact Git SHAs and schema version. Audit logs preserve previous derived graph hashes, without making the index immutable authority.

## 3. Identifier durability and canonical path mapping

The identifier registry is **owned by the canonical source**; the graph stores read-only lookup tables `id -> (current path, anchors, revision, previous paths, status)`.

- **Rename/move:** preserve canonical ID, update the source path and add a redirect alias; checksums change when content changes, not necessarily for a pure move; a rename is verified from Git provenance and ID, not guessed by fuzzy name match.
- **Revision:** preserve ID for the same logical asset; capture source revision and digest. Frozen records follow existing exceptional review rules. The graph can hold historical versions by `(id, revision)` keys without minting new Atlas IDs.
- **Split:** original ID remains an archived or parent historical referent; new assets receive *their owning registry's* IDs, each `derived_from` original; relationships are reviewed, not copied blindly.
- **Merge:** surviving approved ID chosen by owner; others receive explicit `supersedes`/redirect mapping. Never choose 'first file wins'.
- **Retirement:** ID stays a permanent tombstone with retired date and successor/reason, pending legal retention. Search excludes retired recommendations by default but can find history.
- **Duplicates:** same canonical ID in two active source records is a *hard error*. Same title in two domains is a warning, not automatic equivalence.
- **Namespace collision:** prefixes are registry-defined and domain-scoped. Existing `D-`, `KA-`, `EP-`, `IV-` and `MF-` IDs remain unchanged. A new claim/run needs registration in its already approved owning system before an index can reference it.

## 4. Machine-readable contract and repository layout

Do not create a manually edited graph alongside source documents. The proposal fits under a future `tooling/digital-twin/` directory after adoption; for review, keep it in the existing governance PR proposal area.

```text
<approved-repo>/
  [existing canonical Markdown, CSV, JSON and release manifests]
  tooling/digital-twin/                # proposed implementation location, non-authoritative
    build_twin.py                      # deterministic extractor
    twin-schema-v1.json               # output contract
    test_twin.py                       # fixtures and negative tests
    README.md                          # operating limits
  .generated/digital-twin/            # gitignored, disposable CI output
    twin.json
    nodes.csv
    edges.csv
    impact-D-10.json
    coverage-report.json
    build-provenance.json
```

**No separate graph file should be hand-maintained.** For current proof, the builder accepts explicit paths to six *local* CSVs: decisions, chapters, articles, patterns, validation scenarios and Meridian event ledger. This avoids silently inventing GitHub approval status. It emits materialised `twin.json`, node/edge CSVs, D-10 transitive impact and a coverage diagnostics report.

The graph carries:

```json
{
  "schema_version": "1.0",
  "generation_mode": "offline_explicit_crosswalk",
  "authority": "DERIVED_NON_AUTHORITATIVE",
  "snapshot_scope": "LOCAL_PROVIDED_FILES_NOT_GITHUB_MAIN",
  "sources": {"decision": {"path":"...","sha256":"...","authority":"LOCAL_INPUT_NOT_APPROVED_REPOSITORY"}},
  "nodes": [{"id":"D-10","type":"decision","title":"...","status":"OBSERVED_LOCAL_CANDIDATE","source_path":"...","source_sha256":"...","metadata":{}}],
  "edges": [{"from":"KA-013","to":"D-10","type":"references","source_path":"...","source_sha256":"...","basis":"frozen_decisions","evidence_state":"EXPLICIT_SOURCE_MAPPING","review_state":"UNREVIEWED_DERIVATION"}]
}
```

This is intentionally smaller than an ontology platform. A later explicit authoritative repository manifest can add commit SHA, source anchors, owner and approval record. Unverified fields stay `UNKNOWN`, not default `Approved`.

**Schema tests** must reject missing IDs, unknown relationships, duplicate canonical IDs, missing targets, duplicate relationship triples, invalid SHA, self-dependency, unsafe path, improper evidence elevation and illegal cross-domain authority. Coverage queries must never count a `references` link as a completed `validates` link. Graph schema version and extractor hash must be pinned in release snapshots.

## 5. Impact analysis and invalidation

For a changed source `X`, calculate reverse reachability along explicitly dependency-bearing edge types. Return the **candidate impact set**, not an automatic approval decision. Classify:

- `DIRECT`: references X directly;
- `TRANSITIVE`: depends on items referencing X;
- `TEST_STALE_CANDIDATE`: a test run is tied to a superseded input hash (requires test-run evidence);
- `REVIEW_REQUIRED`: an approved output is dependent on an amended source;
- `NO_KNOWN_LINK`: could be an indexing gap, not proof of safety.

**D-10:** list Atlas-linked articles/patterns/chapters and validation scenarios by exact ID. The book's D-10 remains frozen; a change request triggers existing exceptional governance. The demo impact output is advisory because it indexes proposals and cannot know implemented assets or historical human reviews.

**KA-001:** reverse traversal of `references` and `depends_on`; do not infer every glossary or chapter with related prose is affected. If a candidate article isn't in approved main, report that fact prominently.

**Stale validation:** only an executed `ValidationRun` with input hashes can become stale by hash mismatch. Scenario definitions alone can be flagged `REVIEW_REQUIRED` but never `previously_passed_test_stale`.

**AI-generated output:** match recorded `produced_by` edges and work-item scope; include base SHA, changed files and reviewer status. Without a provenance ledger return `UNKNOWN_AI_ANCESTRY`, never invent output ownership.

## 6. Coverage diagnostics

| Indicator | Required denominator | Numerator | Missing evidence behaviour |
|---|---|---|---|
| Traceability completeness | in-scope canonical published assets | assets with required explicit source/owner/decision links | Not measurable if approved baseline absent |
| Validation coverage | assets requiring applicable executed tests | assets with eligible **passed** test runs and pinned versions | `UNKNOWN`; never count scenario definitions |
| Independent validation | claims eligible for review | claims with recorded independent qualified approvals | `UNKNOWN`; AI peer not independent |
| Orphan rate | active approved assets | assets with no required explicit relationships | For candidate set, report diagnostic *isolated candidates* |
| Duplicate rate | active canonical IDs | duplicated active IDs | Reject build for duplicate ID |
| Review coverage | changes requiring review | changes with qualified approved human review record | Unknown without reviewer records |
| Staleness | tracked source-bound claims/tests | claims/tests whose version expiry/anchors changed | Unknown without pinned release and source checks |
| Dependency density | active nodes | number of explicit edges / active nodes | Distinguish observed from inferred edge counts |
| Broken-link rate | explicit edges | unresolved target IDs | Fail build; cannot silently create target |
| AI contribution coverage | AI-authored changed assets | records with sponsor, run, scope, SHA and human review | Unknown without run ledger |

Quality gates are deterministic checks, not a new approval process. Severity: missing ID, duplicate ID and incorrect authority elevation **BLOCK** the derived graph; missing optional relationships and isolated candidates **WARN** with accountable follow-up; absent approved baseline gives `NOT_MEASURABLE`, not zero and not a pass.

## 7. AI integration boundary

Any provider (GPT, Claude, Claude Code, Codex, Copilot or successor) receives:

1. Source/target exact SHA and declared authority tier.
2. A read-only generated graph for discovery and candidate impacts.
3. The relevant canonical file and exact provenance spans for decisions.
4. Existing assigned work-item scope and active ownership lease.

AI may *query* the twin, explain impacts with citations, propose missing links as a patch to the **owning canonical source**, challenge an apparent contradiction in an issue and run the local checker. AI must not approve, suppress blocking warnings, directly edit derived edges as authoritative, change frozen records or infer a successful test from its definition. Every agent must pin the index generation digest and check whether source HEAD has moved. Cross-agent disagreement becomes a source-anchored challenge under the existing Multi-AI contract.

Security: knowledge graph may reveal restricted relationships even if source text is redacted. Build separate views according to source licences and the user's effective access; never merge private archive nodes into the public repository's graph or leak protected evidence through search snippets. Secret scanning and output sanitisation apply to generated files, not only checked-in originals.

## 8. Repository health and operating checks

For 1 architect: a single Python script reads CSVs, outputs reports, and tests explicit data integrity. Every run records file digests. No service to operate.

For 10 contributors: run a single reproducible CI job per PR, with graph comparison to an approved protected baseline, impact diff, check for duplicate IDs and broken explicit links. Human reviewers use the report; no agent writes to main.

For 100 contributors: shard extraction by domain but **merge deterministically by canonical ID and pinned source revisions**, with a global schema check and append-only record of imports/releases. Use dependency-index cache and incremental rebuild only when results match a full cold rebuild. Strong ownership and ID registry matter more than a graph engine.

At 10,000+ assets: CSV/JSON remains authoritative where practical; replace the derived index implementation with SQLite/FTS, DuckDB or a graph query engine **only if** observed query latency/size/scope justifies it. The backing graph is a cache, and a clean rebuild from Git must reproduce the same logical nodes and edges. Evaluate storage, provenance filtering and access-control leak risks before introducing a server database. No vector similarity edge becomes an explicit `depends_on` or `approved_by` without reviewed source evidence.

Suggested measurable health thresholds are targets for later ratification, not existing governance controls: 0 duplicate IDs, 0 broken explicit references, 0 false authority elevations, 100% source hashes recorded in derived nodes, and no published coverage figure where test evidence is absent. Review the observed trends in the existing programme metrics without adding a competing scoreboard.

## 9. Proof run: inputs and observed limitations

From the provided local files, deterministic extraction currently yields:

- 30 decision nodes, 58 chapter nodes, 100 article candidates, 100 pattern candidates, 12 scenario definitions and 15 synthetic Meridian events = **315 nodes**.
- **2,013** cross-reference edges, each grounded in an explicit source CSV field.
- 25 isolated candidates in the current local input graph (this is **not** an orphan rate for approved production knowledge).
- No broken explicit links or repeated `(from,to,type)` links in this local build.

**It is not possible to calculate** actual deployment `implements` links, completed validation coverage, independent approval coverage, claim withdrawal, staleness by executed test, or AI provenance from the six CSVs. Those are recorded `NOT_MEASURABLE`. The current `main` branch has not imported these source catalogues. This demonstrator does not establish an approved digital twin of main.

### Reproduce

```bash
python3 build_twin.py --source /mnt/data --output /mnt/data/programme-digital-twin/generated
python3 -m unittest -v test_twin.py
```

In a clean future checkout, replace `/mnt/data` with the **approved local checkout root containing the six canonical CSV files**, and update path bindings through a reviewed configuration file if approved repository paths differ. Never make the sample's container paths into assumed permanent GitHub paths.

## 10. Acceptance, dependencies and strict non-goals

**Minimum acceptance:** two fresh deterministic builds match after normalisation of machine-local source paths, 0 duplicated IDs, 0 broken links, predictable D-10 and KA-001 impact traversal, explicit missing-evidence indications, and a simulated rename/split/retirement test showing ID continuity without updating frozen Atlas records.

**Blocked integration:** approved canonical input file import; controlled source manifest; protected main and CI rights; validated test-run evidence and human review records; restricted-source ACL design. Implement through existing EX backlog and validation programme. Do not create a new backlog or gate.

**Never do:** auto-approve decisions, treat a GitHub PR as a human approval, promote AI confidence to an evidence grade, silently rewrite Meridian, ingest licensed books to a public graph, publish assessor keys, invent new Atlas IDs, replace source markdown with graph-only edits, infer relationships from embedding similarity as authority, or use a graph database as an excuse to bypass source control.

**Final disposition:** the digital twin is a source-indexed, queryable, disposable reflection of approved Git revisions. Its value is to make missing relationships and stale evidence visible—not to make decisions for the programme.