# Acquisition and Developmental Editorial Review

**Work assessed:** *The Enterprise AI Agent Fabric: Reference Architecture and Playbook*  
**Binding authority:** `style-v1.2.md`, version 1.2  
**Assessment date:** 9 November 2026  
**Outcome:** **NOT READY FOR ACQUISITION AS A FINISHED MANUSCRIPT**  
**Review posture:** editorial compliance first; technical and market judgments second.

## Evidence and scoring protocol

The submitted package does **not** contain five completed manuscript files. Four files were available:

| File | Extent | Editorial treatment |
|---|---:|---|
| `The-Enterprise-AI-Agent-Fabric-Blueprint.md` | 629 lines; ~2,000 whitespace-separated words | The intended 53-chapter/8-part table of contents and skeleton. The official chapter numbering used throughout this review. |
| `Agentic-Enterprise-Reference-Architecture.md` | 2,241 lines; ~17,300 words | A parallel technical source draft. Its §1–§59 and §25A–C are source sections, **not** finished chapters of the canonical book. |
| `transcript.md` | 1,241 lines; ~13,680 words | A conversational source transcript about **CoLab**, not book text and not the **Meridian Financial** narrative. Assessed for source fitness and factual risk, **excluded** from book-prose compliance denominators. |
| `style-v1.2.md` | 1,239 lines; ~11,900 words | The governing editorial specification, not scored as manuscript prose. |

Word counts are approximate; Markdown tables and punctuation change the result depending on tokenisation. The two book drafts total only ~19,300 whitespace-separated words, with substantial conceptual overlap. They cannot be added together and called 19,300 finished book words. The Style Bible specifies approximately **490 designed pages** (`style-v1.2.md`, E2, lines 405–418). Page-equivalent completion cannot be computed accurately without layout; it is unquestionably far below target.

**Evidence convention:** `B:nn` refers to the blueprint's physical line `nn`; `R:nn` to the long reference architecture draft; `T:nn` to the transcript; `S:nn` to the Style Bible. Where a range is given it contains the relevant passage or missing expected structure. Section numbers alone are ambiguous because the two drafts employ conflicting numbering. Quotation marks indicate source text, not reviewer-invented text. Editorial score percentages are explicitly **rubric judgments**, not statistical estimates of author identity or AI involvement. The language audit and chapter inventory CSV files accompany this report.

### Methodological hard stops

- **No complete sample chapter is present.** Selecting a publisher-ready chapter today would misrepresent what was supplied.
- **No Meridian Financial vignette exists** in either manuscript draft. A genuine before/after rewrite of a current vignette is impossible; this report provides an original proposed replacement, clearly marked as new text.
- The Style Bible has **some internally stale chapter references**. An editor must reconcile them in a new style decision. They are not grounds for silently ignoring the Bible: see A2 references to Chapters 23 and 29 (`S:27–36`) versus blueprint Ch.23 (tenant substrate, `B:367`) and Ch.29 (decommission, `B:418`).
- Publisher verdicts are **editorial fit estimates**; no publisher's acquisitions board was consulted. A proposal may be solicited before a manuscript is finished, but this submission is not a finished book or a suitable sample.

---

# Stage 1 — Executive assessment

## Scores

| Category | Score /10 | Evidence and explanation |
|---|---:|---|
| Originality | **5.5** | The package integrates familiar runtime, governance, evaluation, and operations themes. Its decision-centric proposition could be differentiating, but the text does not substantiate a novel method or prior-art comparison (`R:58–112`; `B:273–314`). |
| Technical credibility | **5.5** | Relevant security/memory/availability concepts appear in `R:654–980` and `R:1876–1981`; the normative models clash, and contracts are not executable or tested. |
| Architectural rigour | **4.0** | Four structural layers, a 15-position runtime inventory, six named second-tier planes, and three third-tier planes have no definitive ownership and enforcement crosswalk (`B:150–175`; `R:256–317`). |
| Editorial quality | **2.5** | Most blueprint chapters are stubs, and the reference source is dominated by tables rather than integrated explanatory prose. |
| Readability | **4.5** | Tables support lookup but cannot explain causal reasoning, trade-offs, and failure stories. The architecture keeps switching altitude and taxonomy. |
| Narrative strength | **0.5** | No Meridian running scenario, character incidents, scenes, or narrative-to-artefact transitions (`S:J1–J5`; `B:21–570`). |
| Marketability | **5.0** | A vendor-neutral decision/reference book for enterprise architects has a plausible audience. No market comparison, reader testing, or differentiated sample demonstrates demand. |
| Publisher readiness | **1.0** | The core book has not been written to the governing chapter templates; ten playbooks are essentially blank (`B:510–530`). |
| Long-term relevance | **6.5** | The durable concepts are identity, authority, source provenance, isolation, decision records, reliability, and lifecycle; product/protocol predictions need versioned caveats. |
| **Overall** | **3.9** | Equal-weight mean rounded to one decimal. Editorial classification: **Early Draft / Not Ready**. |

**One-sentence acquisition judgment:** Credible material for a differentiated technical reference book exists, but the submission is an advanced outline with inconsistent architecture governance, not a manuscript.

## Editorial identity, argument, and narrative spine

The governing reader promise is **(1) a decision surface, (2) a reference architecture, (3) a practitioner's journey**, in that priority order (`S:17–25`). The actual drafts reverse the first two: inventories and layered taxonomies dominate; decision pages and worked examples are absent. The narrative spine is entirely absent. The core argument worth retaining is: **shared agent execution is defensible when several use cases need the same policy-enforced tool, identity, evidence, operational, and cost services, and when its aggregate benefit exceeds the cost and isolation risks of a common fabric**. This proposition needs quantified counterexamples and explicit cases in which **not** to build a shared fabric.

**Single biggest strength:** enterprise-level breadth, especially the strong source notes on memory write governance, sandbox isolation, tool controls, evaluation, and per-layer HA/DR (`R:654–980`; `R:1876–1981`).  
**Single biggest weakness:** no canonical, decision-driven, fully worked chapter that proves the concepts through a mechanism, failure, deviation, and artefact.  
**Commercial diagnosis:** the book does not yet deliver its own declared product, the one-page decision surface.

---

# Stage 2 — Publisher acquisition review

The answers below mean **as a finished manuscript today**, not whether a future proposal might be considered.

| Publisher | Would publish as submitted? | Fit if rebuilt | Acquisition concerns and required improvements |
|---|---|---|---|
| **O'Reilly** | **No** | Possible after substantial development | Needs a distinctive technical thesis, authoritative architecture examples, readable conceptual explanation, competing-title analysis, independently reviewed diagrams, genuine experienced-practitioner voice, and a complete sample. Clarify authorship and provenance of any AI-assisted material in any actual proposal. |
| **Manning** | **No** | Possible, weaker fit without exercises | Manning foregrounds teachability and what readers can accomplish. Add stepwise scenarios, progressive artefacts, real worked decisions, exercises, and measurable checkpoints; reduce encyclopaedic inventory (`R:258–274`, `R:1807–1981`). |
| **Apress** | **No** | Plausible after rewrite | The enterprise architecture topic fits a professional technology list; needs several complete substantial chapters, implementation-level contracts, technically defensible claims, coherent scope, and a credible use-case progression. |
| **Packt** | **No** | Plausible, if made more hands-on | A purely conceptual reference may underdeliver for task-focused readers. Introduce executable decision worksheets, reproducible diagrams, test evidence, and a concrete onboarding playbook without abandoning vendor neutrality. |
| **Wiley** | **No** | Plausible as professional/enterprise reference | Needs strong positioning beyond technical readers, defensible financial and operational models, market analysis, and evidence-based case material. Reference breadth alone is insufficient. |

Publisher-policy anchors: [O'Reilly author resources](https://www.oreilly.com/about/resources); [Manning's published proposal criteria](https://www.manning.com/write-for-us); [Apress subject and author programme](https://link.springer.com/brands/apress); [Wiley's acquisition and proposal process](https://www.wiley.com/publishing/book/steps/submit-proposal). These sources establish broad publisher positioning, **not** predictions about an individual acquisition decision.

**Proposal decision:** Do **not** present the current package as a completed book. A concept proposal may be worth developing, but first complete one differentiated sample and one genuine one-page decision template, then conduct competing-title and sample-reader tests.

---

# Dedicated Style Bible audit — calculated before final conclusions

## Calculation method

The five requested compliance values use a **20-point editorial gate rubric per dimension**: five subtests, scored 0–4 each. This is a declared, auditable editorial judgment; it is **not** a mechanically extracted percentage of compliant sentences. A score is `earned / 20 × 100`. The machine-counted language occurrences and all numbered section extents are provided separately. **To exceed 95% on this rubric requires 20/20**, because 19/20 is exactly 95%.

| Metric | Five subtests (0–4 each, listed in order) | Earned | Compliance |
|---|---|---:|---:|
| **Anti-Slop** | Specific mechanism 1; human-plausible tone 3; information density 1; authorial judgment 2; C10 mechanical hygiene 4 | 11/20 | **55%** |
| **Controlled vocabulary** | Defined terms 3; persona/archetype distinction 1; structural-layer distinction 0; control-plane consistency 0; terminology and cross-reference hygiene 1 | 5/20 | **25%** |
| **Narrative quality** | Meridian through-line 0; recognisable stakes 0; incident consequence 0; E5 dose 0; narrative-to-artefact handoff 0 | 0/20 | **0%** |
| **Reference architecture** | Component boundaries 3; failure-mode reasoning 2; scaling signal 1; enforcement/evidence contract 1; repeatable F6/F7 chapters 0 | 7/20 | **35%** |
| **Decision-centricity** | Declared defaults 2; trade-offs/deviation 1; reversibility 1; supporting evidence 0; completed F1 decision pages 0 | 4/20 | **20%** |

Low **Anti-Slop** is driven mainly by insufficient substance, not a large number of banned buzzwords. A 20-word checklist does not become high-quality prose by avoiding 'pivotal'. Controlled-vocabulary and architecture scores are reduced by **conflicting canonical models**. Narrative is zero because the required narrative does not exist, not because the transcript is conversational. Narrative-exempt Parts IV and VIII do not count against narrative scoring.

## Exactly which chapters reduce each sub-85% score, and what raises it beyond 95%

| Metric | Chapter groups responsible (canonical blueprint numbering) | Required repair to reach 20/20 |
|---|---|---|
| **Anti-Slop 55%** | Ch. **1–4** are mainly definitions/lists; **5–9** assert defaults without defense; **10–15** label mechanisms but seldom prove them; **16–18** are enumerations; **19–35** are one-line stage/function lists; **36–45** lack playbook body; **46–53** are reference placeholders. Supporting `R:58–112`, `R:1197–1304`, `R:1566–1785`, `R:2139–2241` compound catalogue prose. | For **each Ch.1–53**, require a concrete governing question, a failure/consequence or meaningful decision, an explicit output, and an O1 pass. Remove redundant taxonomies. Rebuild source-list sections as mechanisms and examples, not prose expansion. Cut C10 violations and perform read-aloud rhythm review only on actual prose. |
| **Vocabulary 25%** | Ch. **1, 3, 10–15** conflate 'platform' with fabric and add planes outside C2; **16–18** cannot reference a stable vocabulary; **23–24, 30–35** blur substrate/platform/runtime ownership; **46, 48, 51** do not define the final glossary or protocol taxonomy. Source conflicts occur especially in `R:256–317`, `R:561–608`, `R:981–1020`, and `R:1145–1395`. | Establish the **four structural layers and eight C2 control planes** as binding. Place semantic entity resolution *inside a named existing plane* unless a formal new style decision is ratified. Define persona/archetype/agent/use case in Ch.2/Glossary and refactor every source table and diagram to that contract. Add vocabulary lint and an I1 cross-reference audit. |
| **Narrative 0%** | Mandatory narrative is absent throughout Ch. **1–9** (Parts I–II), **19–29** (Part V), **30–35** (Part VI), and **36–45** (Part VII). Part III Ch. **10–15** also lacks required failure opening hooks, though its narrative allocation is only 5%. Ch.16–18 and Ch.46–53 are narrative-exempt. | Create a Meridian case ledger and one causal decision sequence spanning the parts. Add E5-length vignettes with real stakes and specific artefacts, in B1/B4 register; introduce no invented *real* cases. Close each with a named decision record or operational artefact. Check ratios and J5 individually. |
| **Reference architecture 35%** | Ch. **10–15** lack F6/F7 depth, failure tables, enforcement points, and adjacency contracts; Ch. **19–29** lack entry/exit gates; **30–35** lack SLO and RACI contracts; **46–50, 52–53** lack the promised reference entries. Source `R:318–1144` is detailed inventory without specification-level interactions, while `R:1876–1981` offers useful but unvalidated HA/DR patterns. | Freeze the canonical topology. Complete F6/F7 for each layer/plane with input, owner, policy check, output, failure mode, scaling signal, evidence record, and non-bypassability proof. Add 3 sequence diagrams and a per-tenant fault scenario. Make each stage reproducible without another chapter. |
| **Decision-centricity 20%** | Ch. **4–9** name decisions without complete rationale; **16–17** promise 15+ decision pages but contain only a list; **18** has unnamed anti-pattern bullets; **19–29** name stages rather than gates; **36–45** have no decision/artefact contracts; **49** is an empty technology matrix. | Produce F1 one-page records for **every decision named in Ch.16**, plus explicit build/buy, tenancy, autonomy, memory, gateway, risk, FinOps, and decommission decisions. Each needs default, why, trade-off, deviation, reversibility, artefact, and cross-reference; evidence and thresholds must be tested or labelled assumptions. |

**Gate to >95%:** Each of the five rubrics must score **20/20**, supported by full chapter templates and sampled QA sign-offs. Word-search cleaning alone will never do this.

---

# Stage 3 — Section-by-section Style Bible compliance

| Style section | Compliance /100 | Compliant areas | Violations with locations | Risk | Required edit |
|---|---:|---|---|---|---|
| **A — Editorial identity** | **30%** | Explicit audience and three reading modes (`B:9–17`); partially vendor-neutral argument (`B:73–84`). | The prioritised decision surface is absent (`S:A1`, `B:273–314`); no Meridian journey (`S:A1–A4`); reference-versus-source document identity not resolved. | **Critical** | Write signed one-page book charter, unique promise, TOC, and positioning; build narrative ledger. |
| **B — Voice** | **25%** | Technical inventory is generally restrained in the long source. | B1's five registers and B4's scene-to-analysis mechanics cannot be found; blueprint is bullet notes throughout (`B:21–570`). | **High** | Draft sample from every part; compare each against register and sentence constraints. |
| **C — Language** | **57%** | Few occurrences of the specified buzzword group inside the two drafts; British terms appear frequently. | Six 'not only/not just' constructions in reference (`R:91,112,1069,1494,2229,2231`); `R:1494` uses 'just' and curly quotes; 34 curly quote characters and two ellipses; controlled vocabulary conflict. | **High** | C10 phrase sweep, quote normalisation, sentence/colon pass, and C2 whole-book linter. |
| **D — Depth** | **15%** | Memory (`R:870–980`) and per-layer resilience (`R:1876–1981`) provide usable source substance. | 48/53 blueprint chapters have fewer than 50 words. F6/F7 chapters nowhere meet depth floor (`S:D1–D3`, `B:150–268`). | **Critical** | Author complete mechanisms; add rather than pad. Delete catalogues that do not change a decision. |
| **E — Chapter structure** | **5%** | Eight-part organisation exists. | No complete E1 chapter, no E4 mandatory closings, no E5 narrative dose, and multiple forbidden dictionary/definition openings (`B:23–37`; `R:116–124`). | **Critical** | Enforce E1/E3/E4/E5 as a pre-merge checklist for each chapter. |
| **F — Templates** | **10%** | Ch.17 lists plausible decision-record fields (`B:300–313`). | F1 decision page never instantiated; Ch.36–45 playbooks lack F2; Ch.18 lacks F4; Parts III lacks F6/F7; Part VIII lacks F3 (`B:510–570`). | **Critical** | Complete one gold-standard specimen for every template and then instantiate it. |
| **J — Narrative** | **0%** | The topic offers plausible enterprise incidents, not yet written. | Zero 'Meridian Financial' occurrences in either draft; transcript discusses a different platform, CoLab (`T:29`). | **Critical** | Create fictional scenario charter, chronology, five composites, incident/decision chain, and disclaimer. |
| **O — Anti-Slop** | **55%** | Buzzword avoidance is relatively strong in the drafts. | Generic abstract conclusions (`R:91,112,228`); source catalogues with no consequence or judgment; transcript contains verbal padding and must not be pasted into book. | **High** | Four O1 tests per paragraph, C10 sweep, and human read-aloud line edit after adding mechanisms. |

The percentages in this table are **section-level editorial judgments**. They should not be conflated with the five 20-point compliance indices above. Across the governing Style Bible's other sections, substantial missing work also exists in diagram accessibility (H), cross-reference map/index (I), production/accessibility (K/L), and author QA (M).

## Style Bible control errors to resolve through a new style decision

1. C2 defines **eight control planes** (`S:154–172`): Identity, Gateway, Observability, Verification, Governance, FinOps, Data Protection, and Interoperability. The blueprint instead lists **six second-tier plus three third-tier planes** (`B:159–172`) and introduces **Semantic Context** as an additional named plane. This is **nine** named non-structural planes, not eight. The reference separately lists Security and Evaluation planes (`R:1197–1267`). These are not equivalent models. The Style Bible wins; remove or formally amend the inconsistency.
2. Chapter cross-references inside the Bible point to an older numbering scheme (`S:A2`; `S:F9`, `S:F10`, `S:F11`). Correct the Bible's cross-reference register using an explicit ratified style decision, rather than letting the manuscript silently contradict an 'authoritative' document.
3. The Style Bible's **O6** says 'no more than two em dashes per page'; **C10.3** uses 'three or more per page' as a tell. The hard rule is **O6/C3, maximum two**; treat C10.3 as a detection heuristic, not a permission to use three.
4. The Style Bible fixes **Meridian Financial** as fictional (`S:J1`). Add a front-matter disclaimer and a preflight name/brand screening before commercial publication; fictional status must be unambiguous.

---

# Stage 4 — Anti-Slop audit

## Evidence-bearing language tell table

No specified buzzwords such as **pivotal**, **crucial**, **leverage**, **facilitate**, **landscape**, **testament**, **showcase**, or **numerous** appeared in the two *book drafts* in their exact tested forms. **'Enhance'** was identified once as **'Enhanced' in a section title**, not as an empty claim (`R:256`); its severity is low. These words appear in the separate conversational transcript and are not counted as current book violations. This difference matters: labelling absent violations would be dishonest.

| Phrase from supplied material | Location | Severity | Concrete rewrite / correction |
|---|---|---|---|
| 'The result is not only a model of how agents work.' | `R:91` | Moderate, C10.2 | 'The model connects runtime boundaries to deployment decisions and governance controls.' Then show the connection. |
| 'The result is not only an architecture diagram.' | `R:112` | Moderate, C10.2 | 'Readers use the same component map to choose governance controls and compare deployment patterns.' |
| 'This is a strong foundation' | `R:228` | Moderate, O1 | 'The original seven-position stack omits identity enforcement, data ingestion, and release controls.' |
| 'Retrieval-Augmented Generation is not just “connect a vector database.”' | `R:1494` | High, C10.2/C3 | 'Enterprise retrieval requires permission filtering, data refresh, citation checks, and deletion propagation.' |
| 'The final architecture is not just a feature comparison.' | `R:2231` | Moderate, C10.2 | 'The decision record must explain why a capability passes security, cost, and operational gates.' |
| 'This prevents message-level interoperability without meaning-level interoperability.' | `B:253` | Moderate, O2: abstraction not mechanism | 'A context contract rejects a handoff when its customer ID maps to a different tenant or schema version.' |
| 'A shared enterprise agent fabric is a platform for governed agent execution across many use cases.' | `B:25` | High, E3 dictionary-style opening | Replace with an incident requiring a cross-business decision, then define the Fabric in analysis. |
| 'Use model routing as a first-class control' | `B:131` | Moderate, O2 | 'Route each request under a recorded policy that constrains model, tenant, region, risk, and budget.' |
| 'Recommended default: hybrid' | `B:101` | High, C7 evidence absent | 'Default to hybrid ownership when central controls are shared and domain workflows change independently; specify cost and deviation conditions.' |
| 'Use Ebbinghaus-style decay for non-pinned memory classes' | `B:appendix A`, `R:~923` | High, unsupported mechanism choice | 'Expire each memory class using policy-defined retention. Add a decay function only after measuring retrieval harm, legal retention, and task outcomes.' |
| 'The more context, tool access, memory, autonomy, and governance it has, the more agentic it becomes.' | `R:29` | High, conceptual confusion | 'Autonomy is the degree to which an agent selects and executes actions without approval; governance constrains autonomy, rather than increasing it.' |
| 'No one protocol covers all of this.' | `R:1309` | Low | Keep if followed immediately by boundary map and versioned contracts; do not multiply general introductions. |

**Transcript-only warning:** `T:1–47` contains 'brilliant amnesiacs', 'profound paradigm shift', dialogue fillers, and unsupported sweeping claims. It fails B1, B4, C10, J5, and O1 if imported as narrative. Do not turn it into the mandated Meridian vignette by renaming the speakers. The subject, CoLab, is not the book's fictional running organisation.

## Machine inspection: lexical and punctuation counts

| Measurement | Blueprint | Reference draft | Transcript (excluded) |
|---|---:|---:|---:|
| Curly-quote characters | 5 | 34 | 0 |
| Em dash characters | 22 | 93 | 24 |
| Unspaced em dashes | 0 | 0 | 24 |
| Exclamation marks | 0 | 0 | 18 |
| Ellipses | 0 | 2 | 12 |
| Exact 'not only/not just' starts | 0 | 6 | 3 |
| 'Just' | 0 | 2 | 69 |
| 'Simply' | 0 | 0 | 8 |
| Meridian Financial named | 0 | 0 | 0 |
| Direct HTTP(S) citations | 0 | 0 | 0 |

Counts are file-level, including Markdown headings, tables, and code, and therefore **flags for editorial triage**, not automatically verdicts. The source line-number CSV records matching phrases and all exceptions for manual review. Exclamation marks in the transcript reflect its non-manuscript status. Page-level dash compliance cannot be definitively measured until pagination; 93 dashes in the reference source require proof review, but do not establish a page breach by themselves.

## Content, rhythm, density, and human-voice diagnosis

- **Generic assertion rather than argument:** `R:95–112` announces difference twice, but cannot establish originality by inventorying adjacent domains. Replace with a side-by-side design choice the competing approach gets wrong, including consequence.
- **Catalogue rhythm:** `R:318–653` repeats 'This layer...' followed by a component table. This is useful research capture, not a mechanism-led chapter. Ch.10–15 require distinct hooks, interfaces, scaling signals, and decisions.
- **Synonym and structure cycling:** 'layer', 'plane', 'control', 'runtime', and 'tier' represent partially overlapping taxonomies (`R:246–317`; `B:148–172`). This is architectural ambiguity first, prose slop second. Do not simply replace words: fix the model.
- **Rule-of-three:** The blueprint's intentional 3-tier architecture should **not** be marked as artificial rule-of-three. The three tiers are an architectural proposition. The failure is their mismatch with C2, not the number three.
- **Overuse of dash:** not established page by page. The strongest violations are the transcript's **24 unspaced** dashes; book drafts use spaced dashes. A proof-stage dash cap still applies.
- **Density failures:** The entire source-draft intro `R:7–112` can be reduced significantly by collapsing repeated categories into a single two-page audience/decision argument. `R:214–317` repeats architectural setup three times; remove the original seven-position historical inventory from the main book, keep only the explanatory crosswalk. `R:1566–1785` restates lifecycle and ownership in successive lists. These portions can plausibly lose **30–50%** of their present words *without losing decisions*; the removed material must be replaced by substantive worked examples, not treated as publication-ready shortening.
- **No evidence of one distinct human voice:** the book drafts sound principally like a **consultant architecture inventory** with **AI-synthesis-like list patterns**; that is a *textual style classification*, not a claim about how the text was authored. Memory and DR passages sound more like technical practitioner notes. No causal enterprise narrative demonstrates a practitioner who has made a hard trade-off.

**Anti-Slop conclusion:** Lexical restraint is a relative positive. False depth, missing decisions, and catalogue structure are the more serious violations. A buzzword blacklist will not fix the manuscript.

---

# Stage 5 — Architecture quality review

| Dimension | Strengths in supplied text | Weaknesses / material missing | Publication gate |
|---|---|---|---|
| **Conceptual soundness** | Shared controls and separate domain use cases (`B:59–84`). | 'Fabric needed after >10 use cases' is unsupported heuristic (`B:39–47`); the paper lacks a cost break-even condition. | Replace numeric trigger with measurable architecture/cost criteria and a worked counterexample. |
| **Internal consistency** | A four-structural-layer foundation is stated (`B:152–158`). | Three contradictory canonical models; security/evaluation/semantic contexts overlap (`R:283–317`; `R:1145–1395`). | Ratify one C2-compliant model, give crosswalk for secondary 15-position engineering inventory, remove duplicate normative claims. |
| **Layer model** | Useful end-to-end inventory (`R:318–1144`). | Layer boundaries incorrectly mix runtime path with asynchronous operations, delivery, and governance. No input/output contracts. | For each structural layer: responsibility, synchrony, call chain, data and evidence contracts, failure modes, scaling. |
| **Control planes** | Identity/delegation, gateway, provenance, and verification are recognised (`R:1145–1196`). | Extra 'Semantic Context' plane conflicts with S:C2; gate placement and bypass paths not demonstrated. | Map required enforcement points, deny/fail-open policy by risk, pre/post-action checkpoints, and bypass tests. |
| **Governance** | Earned-autonomy idea (`B:139–144`), risk tiers, release gates (`R:1635–1660`). | No risk-to-approval matrix, accountability/RACI, delegation proof, exception authority, recertification schedule, or audit evidence example. | Demonstrate a tenant escalating a risk class and the veto/appeal logic. |
| **Security** | Action gateway, sandbox tiers, ACL-aware RAG, source poisoning (`R:654–980`; `R:1437–1475`). | Missing threat-to-control test, non-bypassability proof, idempotency, confused deputy, token theft containment, supply chain, policy cache invalidation, and emergency revoke. | Trace prompt injection → tool call → PDP → gate → external write; test deny/revoke under partial outage; map OWASP ASI01–10. |
| **Operational model** | Per-layer HA/DR and FinOps tables useful (`R:1876–1981`). | No SLO budgets, incident severity triggers, ownership escalation, degraded-mode authorization, test evidence, RPO/RTO figures per business tier, or sample postmortem. | Provide an incident with traces, runbooks, time-to-detection, evidence, and tested rollback/deactivation. |
| **Scalability** | Names queue depth, worker pools, warm pools, independent scaling (`R:1876–1926`). | No load test, concurrency envelope, queue growth model, batch economics, overload control, fan-out formula, or sample figures. | Worked 1→10→100-use-case capacity model with thresholds and failure experiments. |
| **Enterprise realism** | Tenant cost and identity, regulated data, operational ownership acknowledged. | Treats enterprise governance as list items; lacks procurement friction, legacy entitlements, multi-region constraints, disconnected SaaS, human appeals, and coexistence. | End-to-end Meridian application workflow across two systems with real authority boundaries and fictional evidence. |
| **Adoption likelihood** | Hybrid ownership and build/buy awareness (`B:88–107`). | No TCO model, uptake profile, funding model, platform SLA obligations, migration path, or minimum viable fabric. | A decision page showing when embedded SaaS agents beat shared fabric; 12-month staged adoption and cost model. |

## Three technical defects deserving immediate correction

**1. Autonomy is not a universal ladder.** `R:145–156` defines Level 6 as 'Multi-agent system' and Level 7 as 'Governed digital worker'. These describe topology and governance, not a higher amount of autonomy than Level 5. It would mislead an architect into granting controls according to an invalid ordinal classification. Replace with **orthogonal dimensions**: action authority, planning discretion, tool reach, operational persistence, multi-agent topology, risk/effect class, and governance assurance. A highly constrained multi-agent workflow can have less autonomy than a single-agent privileged executor.

**2. 'Non-bypassable' is an unproven design claim.** `B:238–240` says all mutable external actions must cross gateway enforcement. `R:769–817` also places a reflective pre-commit gate inside the agent path. Neither defines what prevents direct SDK calls, sidecar egress, service-to-service credentials, cached authorisations, or offline execution from bypassing policy. The reference must distinguish recommendation from independently enforced policy; review authorisation at execution time, not merely when the plan is formed. Write a control contract and an adversarial test matrix.

**3. Retry/rollback semantics are not generic.** `R:711–768`, `R:1661–1683`, and `B:496–506` imply generic retries, simulation, transaction wrappers, or rollback. Sending an email, charging a card, deleting an external record, or publishing externally cannot always be undone. Add per-tool **idempotency keys**, duplicate-detection, at-most-once/at-least-once semantics, compensation processes, action receipts, and human escalation after uncertain outcome. No source chapter currently shows these mechanisms together.

## Protocol and source-verification finding

`R:1305–1377` includes MCP, A2A, ACP variants, AP2, and other standards, with several version-sensitive capabilities described at a high level. The text says MCP moved to a stateless core in 2026. The **2026-07-28** specification supports this shift for its newer transport semantics, whereas the **2025-11-25** specification supports sessions. The book must explicitly distinguish protocol release, older deployed versions, optional extension, and architecture consequences. The official specification is available at [MCP 2026-07-28 transports](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/transports/index.mdx); compare the [2025-11-25 transport version](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-11-25/basic/transports.mdx). A2A Agent Card signing is an **optional** signed-card mechanism under the published specification, not proof that every card is authenticated: [A2A specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md). The Style Bible's version/date rule (`S:C5`, `S:F10`) must be enforced for every protocol entry.

The officially published [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) is an appropriate framework for threat coverage, but a list of ASI identifiers is not a security review. Every ASI class needs a control location, adversarial test, telemetry signal, owner, and evidence artefact. Check external claims with source/date/version before publication.

---

# Stage 6 — Audience assessment

| Audience | Score /10 | What they gain | Where they struggle | Missing content |
|---|---:|---|---|---|
| CIO | **4.0** | Organising concept for shared oversight. | No investment decision or value proof. | Cost range, option appraisal, strategic no-build criteria, risk exposure. |
| CTO | **5.0** | Architecture scope and ownership concept. | No scale/reliability numbers or validated strategy. | Platform strategy, vendor boundary, RTO/RPO, capacity, cost/control gates. |
| Enterprise architect | **6.5** | Rich candidate taxonomy and control inventory. | Contradictory canonical models, no traceable ADRs. | Interface diagrams, control matrices, decisions with deviations, source evidence. |
| Platform lead | **5.0** | Runtime/HA/DR component ideas. | No implementable contracts or completed playbooks. | Bootstrap sequence, admission and onboarding contracts, runbooks, test fixtures. |
| Security architect | **5.5** | Delegation, sandbox and tool-boundary awareness. | Enforcement not proven, threat model untested. | Trust boundary paths, red-team tests, key lifecycle, policy/PDP controls. |
| Product leader | **3.5** | Use-case/fabric ownership distinction. | No user journey, success hypothesis, adoption metrics. | Prioritisation, measurable outcomes, UX/HITL gates, domain ownership. |
| Engineering manager | **4.0** | Useful list of functions/risks. | Can't estimate delivery or staff. | Critical path, RACI, sequencing, acceptance tests, failure budget. |
| FinOps lead | **3.0** | Named cost drivers and accounting intentions. | No assumptions or model with actual inputs. | Per-task unit economics, chargeback policy, sensitivity cases, cost-versus-value. |

**Primary audience decision:** Enterprise architects and platform leads. CIO and FinOps readers are **secondary decision sponsors**, not equal-depth readers. This matches `S:A2` and avoids promising eight different books in one.

---


# Stage 7 — Ranking **every canonical blueprint chapter**

**Scope of ranking:** All 53 officially numbered chapter entries in the blueprint are ranked below. The score is **current publisher-sample fitness**, not subject importance, technical potential, or commercial potential. A score under 4/10 means the present prose cannot stand as a complete chapter. The source draft uses a different 59-section numbering scheme; it is assessed as research inputs, not misrepresented as 59 additional finished book chapters. **No entry qualifies as a publisher sample today.**

| Rank | Official chapter (blueprint line) | Fitness /10 | Best element | Weakest element | Must keep | Must improve | Sample now? |
|---:|---|---:|---|---|---|---|---|
| 1 | **Ch.1 The Case for a Shared Agent Fabric** (`B:23`) | 3.5 | Shared Fabric boundary | Starts as a dictionary definition | Multi-use-case decision problem | Replace opening with Meridian failure; prove the >10 trigger or remove it | No |
| 2 | **Ch.10 Canonical Tiered Architecture** (`B:150`) | 3.3 | Four-part structural inventory | Incompatible 6+3 plane taxonomy | Structural layer distinction | Restore eight-plane C2 model; show contracts | No |
| 3 | **Ch.11 Structural Core (ETCLOVG-Aligned)** (`B:176`) | 3.2 | Execution, tooling, context, lifecycle summary | No interfaces or scaling measures | Four structural concerns | Rebuild each under F6; show failure boundary | No |
| 4 | **Ch.18 Anti-Patterns Catalogue (Selected)** (`B:315`) | 3.1 | Ten useful failure candidates | No F4 format or detection signals | Memory ACL and prompt controls | Write an AP record for every item | No |
| 5 | **Ch.16 One-Page Fabric Decision Map (Condensed)** (`B:273`) | 3.0 | 15 named strategic decisions | None is an actual F1 decision page | Decision catalogue | Produce one page per decision plus reference map | No |
| 6 | **Ch.12 Identity and Delegation Control Plane** (`B:212`) | 2.9 | Short-lived delegated identity ideas | No delegation protocol or confused deputy test | Scope attenuation | Signed chain, PDP, execution-time policy check | No |
| 7 | **Ch.4 Multi-Use-Case Adoption Decision** (`B:71`) | 2.8 | Explicit conditions not to centralise | No quantified break-even | No-fabric option | Add cost and isolation decision table | No |
| 8 | **Ch.13 Agent Gateway Control Plane** (`B:229`) | 2.8 | Gateway responsibility list | Non-bypassability asserted without proof | Gateway enforcement ambition | Enforcement topology, bypass tests and fail-closed rules | No |
| 9 | **Ch.5 Build vs Buy vs Embed vs Partner** (`B:88`) | 2.6 | Buy/embed/build options | No option appraisal or supplier lock-in test | Reversibility concept | F1 decision with cost/risk evidence | No |
| 10 | **Ch.14 Semantic Context Control Plane** (`B:244`) | 2.6 | Entity identity and semantic conflict | Extra control plane conflicts with C2 | Context reconciliation requirement | Assign to agreed plane and define conflict schema | No |
| 11 | **Ch.7 Tenant Model** (`B:108`) | 2.5 | Isolation axes | No isolation assurance model | Tenant dimensions | Compare pooled, partitioned and dedicated models | No |
| 12 | **Ch.17 Decision Record Template** (`B:300`) | 2.4 | ADR fields and reversibility | No completed example | Evidence threshold and review date | Use exact F8 sample with rejected options | No |
| 13 | **Ch.3 Fabric vs Product vs Use Case** (`B:59`) | 2.3 | Separation of shared and domain responsibilities | Platform used as synonym for Fabric | Ownership boundaries | Add contract, RACI, and exceptions | No |
| 14 | **Ch.35 Change Management Model** (`B:496`) | 2.2 | Prompts/models/tools as versioned assets | No release decision or proof | Versioned change baseline | Canary thresholds, rollback, change evidence | No |
| 15 | **Ch.15 Protocol and Standards Layer** (`B:257`) | 2.1 | Protocols mapped to boundaries | No versioned entries | Boundary-first protocol policy | Add F10 entries and deployment caveats | No |
| 16 | **Ch.9 Autonomy Governance** (`B:139`) | 2.0 | Earned autonomy premise | No entry/exit thresholds | Evidence-gated autonomy | Risk-tier matrix with rollback and veto | No |
| 17 | **Ch.32 SLA/SLO Contract Model** (`B:459`) | 2.0 | Cost per successful task as SLO | No SLI thresholds or time windows | Unit-economics SLO concept | Specify targets, error budget and measurement | No |
| 18 | **Ch.8 Model Strategy** (`B:129`) | 1.8 | Model routing constraints | No policy engine or failure logic | Route by risk, region and budget | Trace a route and record fallback decision | No |
| 19 | **Ch.30 Platform Team Blueprint** (`B:431`) | 1.7 | Comprehensive role inventory | No budget or team capacity | Specialist operating roles | Team-sizing and platform/domain separation | No |
| 20 | **Ch.2 Agentic Capability as a Spectrum** (`B:51`) | 1.5 | Controls by autonomy and risk | No usable autonomy model | Risk-based policy premise | Define orthogonal autonomy dimensions and control mapping | No |
| 21 | **Ch.6 Operating Model: Central, Federated, Hybrid** (`B:99`) | 1.5 | Hybrid ownership default | One unsupported sentence | Central/domain split | Add accountable owners, trade-offs and exception trigger | No |
| 22 | **Ch.34 FinOps Operating Model** (`B:487`) | 1.5 | Tenant chargeback concept | No formula or worked arithmetic | Economic policy by risk | Build model and sensitivity analysis | No |
| 23 | **Ch.29 Stage 10: Decommission** (`B:418`) | 1.4 | Decommission is included | No secure deletion demonstration | Retirement evidence | Exit checklist, revocation and delete certificate | No |
| 24 | **Ch.31 Ownership Matrix (RACI)** (`B:447`) | 1.3 | Named control ownership candidates | No actual RACI matrix | Accountability requirement | Populate a real RACI and escalation chain | No |
| 25 | **Ch.25 Stage 6: First Use-Case Pilot** (`B:386`) | 1.2 | One use-case proof objective | No concrete pilot | End-to-end acceptance | Meridian pilot with metrics and red-team test | No |
| 26 | **Ch.22 Stage 3: Trust Chain and Security** (`B:358`) | 1.1 | Trust-chain alignment | No tested threat scenarios | Security-before-pilot sequencing | Map OWASP threat to execution tests | No |
| 27 | **Ch.26 Stage 7: Scale to N Use Cases** (`B:394`) | 1.1 | Scaling by onboarding class | No capacity or cost model | Persona/archetype separation | 10-use-case scaling threshold and owner | No |
| 28 | **Ch.27 Stage 8: Operate as Product** (`B:402`) | 1.1 | Operate as a product | SLOs unquantified | Incident ownership | SLO, error budget and support model | No |
| 29 | **Ch.28 Stage 9: Continuous Verification and Improvement** (`B:410`) | 1.1 | Continuous evaluation loop | No evaluation sample or policy | Failure-trace mining idea | Give versioned regression pack and rollback trigger | No |
| 30 | **Ch.33 Incident Model** (`B:476`) | 1.1 | Prompt injection and memory poisoning incidents | No incident response procedure | Distinct agentic incident categories | War story, detection, containment, recovery | No |
| 31 | **Ch.20 Stage 1: Platform Vision** (`B:340`) | 1.0 | Use-case scope and metrics | No user or success baseline | Time-to-first-use-case metric | Define sponsor mandate and exit gate | No |
| 32 | **Ch.23 Stage 4: Tenant Substrate** (`B:367`) | 1.0 | Isolated tenant substrate idea | No policy or data isolation proof | Separate tenant identity/memory/state | Specify data paths, tenancy tests and evidence | No |
| 33 | **Ch.24 Stage 5: Shared Services Bootstrap** (`B:376`) | 1.0 | Required shared services | Only a component list | Bootstrap order | Minimum build sequence and acceptance criteria | No |
| 34 | **Ch.19 Stage 0: Strategic Intent** (`B:332`) | 0.9 | Business case deliverable | No economics or entry criteria | Go/no-go viability question | Model 12-month scenario and decision record | No |
| 35 | **Ch.21 Stage 2: Reference Architecture** (`B:348`) | 0.9 | Topology and ADR deliverables | Nothing built or explained | Design-stage accountability | Reference diagram, contracts and ADR examples | No |
| 36 | **Ch.52 Example Artifacts** (`B:560`) | 0.8 | Five exemplar artefact types | No sample artefacts | Release and incident proof examples | Supply populated artefacts with fictional IDs | No |
| 37 | **Ch.49 Technology Decision Matrix** (`B:548`) | 0.7 | Technology matrix intention | No entries or choice conditions | Default and deviation format | Fill cost/risk/operation example rows | No |
| 38 | **Ch.50 Standards and Regulatory Map** (`B:552`) | 0.7 | Standards mapping intention | No mappings or editions | Cross-regulatory traceability | Use dated source-backed F11 entries | No |
| 39 | **Ch.46 Layer and Control-Plane Checklists** (`B:536`) | 0.6 | Evidence-based checklist requirement | No checklist exists | Evidence requirement | Populate F3 questions by layer | No |
| 40 | **Ch.47 Decision Record Templates** (`B:540`) | 0.6 | Decision-reference objective | No filled templates | One-page discipline | Include completed decision records | No |
| 41 | **Ch.48 Protocol and Boundary Map** (`B:544`) | 0.6 | Boundary-map intention | No actual map | Protocol-to-plane mapping | Add versioned map and labelled arrows | No |
| 42 | **Ch.51 Glossary** (`B:556`) | 0.6 | Glossary intention | No definitions or C2 coverage | Controlled vocabulary anchor | Write F9 entries; reconcile taxonomy | No |
| 43 | **Ch.53 Industry Addenda** (`B:570`) | 0.6 | Six sector overlay categories | No actual sector overlays | Sector boundaries | At least two evidence-backed sector decisions | No |
| 44 | **Ch.45 P10 — Retire Fabric** (`B:521`) | 0.3 | Fabric-retirement title | Generic template appears after heading | Fabric transition end state | Write distinct P10 rather than common instructions | No |
| 45 | **Ch.36 P1 — Build Business Case** (`B:512`) | 0.2 | Business-case playbook title | No playbook content | Business-case objective | Write complete F2 and fictional example | No |
| 46 | **Ch.37 P2 — Design Reference Architecture** (`B:513`) | 0.2 | Architecture playbook title | No playbook content | Design objective | Write complete F2 with artefacts and owners | No |
| 47 | **Ch.38 P3 — Stand Up Tenant Substrate** (`B:514`) | 0.2 | Tenant-bootstrap playbook title | No playbook content | Isolation objective | Write F2 plus testable tenant setup | No |
| 48 | **Ch.39 P4 — Onboard First Use Case** (`B:515`) | 0.2 | First-use-case onboarding title | No playbook content | Onboarding objective | Write F2 with executable admission gates | No |
| 49 | **Ch.40 P5 — Scale from 1 to 10 Use Cases** (`B:516`) | 0.2 | 1-to-10 scale trigger | No playbook content | Scale-stage boundary | Write F2 and capacity checkpoint | No |
| 50 | **Ch.41 P6 — Scale from 10 to 100+ Use Cases** (`B:517`) | 0.2 | 10-to-100+ scale trigger | No playbook content | Scale-stage boundary | Write F2 with failure isolation and finance | No |
| 51 | **Ch.42 P7 — Execute Model Upgrade Safely** (`B:518`) | 0.2 | Model-upgrade safety title | No playbook content | Change-risk focus | Write F2 using regression and canary data | No |
| 52 | **Ch.43 P8 — Handle Security Incident** (`B:519`) | 0.2 | Security incident title | No playbook content | Containment use case | Write F2 and crisis evidence ledger | No |
| 53 | **Ch.44 P9 — Retire Use Case** (`B:520`) | 0.2 | Retire-use-case title | No playbook content | Retirement use case | Write F2 and memory/credential revocation | No |

**Ranking caveat:** Ch.36–44 are just headings. Ch.45 is followed by instructions applying to every playbook, not by a P10 implementation. Ranking them at the bottom is a **completion assessment**, not a judgment that incident response or model upgrade is unimportant. This ranking should be revisited only after real chapters exist.

## Technical-source section ranking (not additional book chapters)

For acquisition samples, the best existing *source* fragments are: **R§21 memory and state**, **R§52 production readiness / per-layer scaling and DR**, **R§19 sandbox and isolation**, **R§32 interoperability standards**, and **R§54 evidence register**. Each requires conversion to the canonical book model. The source-fragment ordering is independent of the formal Ch.1–53 readiness table. The separate chapter-inventory CSV contains all **62 numbered technical source sections** (`§1–§59` plus `§25A–§25C`), start/end lines, and content flags. This avoids giving the illusion that 114 finished chapters have been read.

## Six-axis assessment of all 53 canonical chapters

This matrix makes the six submission criteria explicit **for every blueprint chapter**, rather than assessing only the top five. It assesses **demonstrated content in the uploaded drafts**, not the potential importance of a topic. The scale is **0 = absent, 1 = asserted or outlined, 2 = partly explained, 3 = convincingly demonstrated, 4 = independently supported and publication-grade**. Columns: **O** original thinking; **E** enterprise credibility; **A** architectural depth; **W** writing quality; **D** book differentiation; **M** requires minimal editing (high score means little editing required). No chapter earns M > 0 because none is complete to E1/F1/F2 requirements. These axis scores explain selection decisions but do not replace the chapter-by-chapter editorial comments above.

| Official chapter | O /4 | E /4 | A /4 | W /4 | D /4 | M /4 |
|---|---:|---:|---:|---:|---:|---:|
| Ch.1 The Case for a Shared Agent Fabric | 1 | 2 | 1 | 1 | 1 | 0 |
| Ch.2 Agentic Capability as a Spectrum | 0 | 1 | 0 | 1 | 0 | 0 |
| Ch.3 Fabric vs Product vs Use Case | 0 | 1 | 1 | 0 | 0 | 0 |
| Ch.4 Multi-Use-Case Adoption Decision | 1 | 2 | 1 | 0 | 1 | 0 |
| Ch.5 Build vs Buy vs Embed vs Partner | 0 | 2 | 1 | 0 | 0 | 0 |
| Ch.6 Operating Model: Central, Federated, Hybrid | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.7 Tenant Model | 1 | 2 | 1 | 0 | 1 | 0 |
| Ch.8 Model Strategy | 0 | 1 | 1 | 0 | 0 | 0 |
| Ch.9 Autonomy Governance | 1 | 0 | 1 | 0 | 1 | 0 |
| Ch.10 Canonical Tiered Architecture | 1 | 2 | 2 | 0 | 1 | 0 |
| Ch.11 Structural Core (ETCLOVG-Aligned) | 0 | 2 | 2 | 0 | 0 | 0 |
| Ch.12 Identity and Delegation Control Plane | 1 | 2 | 2 | 0 | 1 | 0 |
| Ch.13 Agent Gateway Control Plane | 1 | 2 | 2 | 0 | 1 | 0 |
| Ch.14 Semantic Context Control Plane | 1 | 2 | 2 | 0 | 1 | 0 |
| Ch.15 Protocol and Standards Layer | 0 | 1 | 1 | 0 | 0 | 0 |
| Ch.16 One-Page Fabric Decision Map (Condensed) | 1 | 2 | 1 | 0 | 1 | 0 |
| Ch.17 Decision Record Template | 0 | 1 | 1 | 0 | 0 | 0 |
| Ch.18 Anti-Patterns Catalogue (Selected) | 1 | 2 | 2 | 0 | 1 | 0 |
| Ch.19 Stage 0: Strategic Intent | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.20 Stage 1: Platform Vision | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.21 Stage 2: Reference Architecture | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.22 Stage 3: Trust Chain and Security | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.23 Stage 4: Tenant Substrate | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.24 Stage 5: Shared Services Bootstrap | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.25 Stage 6: First Use-Case Pilot | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.26 Stage 7: Scale to N Use Cases | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.27 Stage 8: Operate as Product | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.28 Stage 9: Continuous Verification and Improvement | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.29 Stage 10: Decommission | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.30 Platform Team Blueprint | 0 | 1 | 1 | 0 | 0 | 0 |
| Ch.31 Ownership Matrix (RACI) | 0 | 1 | 0 | 0 | 0 | 0 |
| Ch.32 SLA/SLO Contract Model | 1 | 2 | 1 | 0 | 0 | 0 |
| Ch.33 Incident Model | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.34 FinOps Operating Model | 0 | 0 | 1 | 0 | 0 | 0 |
| Ch.35 Change Management Model | 1 | 2 | 1 | 0 | 1 | 0 |
| Ch.36 P1 — Build Business Case | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.37 P2 — Design Reference Architecture | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.38 P3 — Stand Up Tenant Substrate | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.39 P4 — Onboard First Use Case | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.40 P5 — Scale from 1 to 10 Use Cases | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.41 P6 — Scale from 10 to 100+ Use Cases | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.42 P7 — Execute Model Upgrade Safely | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.43 P8 — Handle Security Incident | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.44 P9 — Retire Use Case | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.45 P10 — Retire Fabric | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.46 Layer and Control-Plane Checklists | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.47 Decision Record Templates | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.48 Protocol and Boundary Map | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.49 Technology Decision Matrix | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.50 Standards and Regulatory Map | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.51 Glossary | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.52 Example Artifacts | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.53 Industry Addenda | 0 | 0 | 0 | 0 | 0 | 0 |

The repeated zeros are substantive findings: a TOC entry is not evidence of original execution or literary craft. Strong technical *source fragments* in the second file are evaluated separately in Stage 8.


# Stage 8 — Best chapter for publisher submission

## Strict answer: none is ready

The canonical blueprint's highest-ranked entry is **Ch.1 — The Case for a Shared Agent Fabric** (`B:23–50`), but the entry has only a short description, two lists, and an unsubstantiated threshold. It fails E1, E3, E4, and E5. Sending it as a sample would undermine the book proposal. The technically richer source fragments are **not** full chapters and use a conflicting numbering system.

## Best **reconstruction candidate**: source §21, *Layer 9: Memory and State Management*

`R:818–980` provides the most credible starting material, particularly §21.1: tiers, write-path checks, cross-agent handoff patterns, provenance, contradiction handling, and DR. It is the closest supplied section to a differentiated enterprise judgment: **memory writes are governance decisions, not caching operations**. It supplies specific failure classes and operational consequences. The passage needs re-scoping to the canonical **Context structural layer** and the relevant C2 plane controls, a concrete example, contracts, failure thresholds, references, and F6/F7 closure.

### Candidate comparison

| Candidate source fragment | Original thinking | Enterprise credibility | Depth | Writing | Differentiation | Editing required | Verdict |
|---|---|---|---|---|---|---|---|
| `R§21` Memory and State | Moderate | High in concept | Strongest | Catalogue-heavy | Strongest | Major | **Best reconstruction candidate** |
| `R§52` Production readiness and HA/DR | Low–moderate | Strong operational instincts | Strong tables | Reference-only | Good | Major | Strong technical companion |
| `R§19` Isolation sandbox | Moderate | High | Good controls | List-heavy | Moderate | Major | Better technical than commercial sample |
| `R§32` Interoperability standards | Moderate | Moderate | Useful coverage | Uneven and volatile | Moderate | Major + version audit | High date/accuracy risk |
| `R§54` Evidence register | Moderate | High as governance principle | Some process detail | Template-driven | Good | Major + real evidence | Strong for reference reader |

### Top five to develop for publisher submission

1. **Memory and State Management** (`R§21`): most distinctive argument if converted into a governed-memory decision with traceable read/write contracts.
2. **Trust Chain: Identity, Delegation, and Action Enforcement** (rebuild from blueprint **Ch.12–13** and `R§25A–B`): central enterprise value proposition, ideally a second sample.
3. **Execution Isolation and Tool Boundaries** (`R§18–19`): concrete security and engineering mechanisms; make them demonstrably non-bypassable.
4. **Production Readiness, Scalability, and Recovery** (`R§52`): shows enterprise operational depth if complemented with numeric failure tests and SLOs.
5. **Architecture Decision Framework** (expand blueprint **Ch.16–17**): commercially strongest point of differentiation *if* it becomes a filled, evidence-based, genuinely one-page decision system.

**If compelled to send exactly one chapter tomorrow:** send **none**. If a commissioning editor accepts explicitly unfinished samples, send `R§21` labelled a *technical excerpt*, not 'publisher-ready Chapter 21'. The stronger commercial move is to transform it into a finished **Context and Memory** chapter and submit that later. Its advantage is causal potential, not its current prose quality.

---

# Stage 9 — Developmental edit roadmap

## Critical, major, and minor defects

**Critical — block acquisition:** (1) no complete manuscript sample; (2) conflicting normative architecture; (3) missing decision pages; (4) missing Meridian spine; (5) playbooks and reference chapters not written; (6) lack of source-to-claim verification for technical defaults and standards.

**Major — undermine credibility and adoption:** missing executable control contracts; invalid ordinal autonomy ladder; weak build/buy and economic arguments; no testable non-bypassability; unspecified RACI/SLO gates; repetitive inventories; absent case-study evidence; incomplete source/version register; inconsistent chapter cross-references; unproven rollout/decommission procedures.

**Minor — editorial polish after development:** curly quotes, repetitive 'not only' formulations, punctuation/sentence rhythm, title/section case, figure numbering, glossary alphabetisation, index terms, em-dash proof pass, and British spelling normalization.

## Ranked top 20 improvements

| Priority | Concrete improvement | Impact | Effort |
|---:|---|---|---|
| 1 | Ratify one architecture: 4 structural layers + 8 C2 control planes; publish crosswalk, owners, non-bypass points | **Critical** | High |
| 2 | Write one complete F6/F7 flagship chapter with mechanism, failure tests, evidence and artefacts | **Critical** | High |
| 3 | Instantiate every Ch.16 F1 decision page, not merely name the decisions | **Critical** | High |
| 4 | Establish Meridian Financial's fictional case ledger and causal running narrative | **Critical** | High |
| 5 | Define the enforceable identity-to-action trust chain, including PDP, tool gateway, authorisation timing and bypass tests | **Critical** | High |
| 6 | Replace the scalar autonomy ladder with a control-relevant multidimensional model | **Critical** | Medium |
| 7 | Write an actual first-use-case pilot, with initial conditions, failure, controls, evidence and result | **Critical** | High |
| 8 | Finish all ten F2 playbooks with owner/input/output/time/failure/exit, not just headings | **Critical** | Very high |
| 9 | Build a reproducible build/buy/embed/partner and no-fabric option appraisal | **High** | Medium |
| 10 | Publish a funded three-scenario cost/capacity model and tenant unit economics | **High** | High |
| 11 | Specify sandbox/tool side effects, idempotency, duplicate recovery, and compensation | **High** | Medium |
| 12 | Version-pin protocol/standard claims; create source/date/evidence register | **High** | Medium |
| 13 | Introduce tested security threat-to-control-to-evidence matrix, including OWASP ASI classes | **High** | High |
| 14 | Give SLOs, alert thresholds, severity, RACI, HA/DR drills and degraded-authority rules | **High** | High |
| 15 | Convert per-layer tables into causal explanation, cross-layer interfaces and scaling signals | **High** | High |
| 16 | Complete working memory/RAG examples with retention, conflict, deletion and cross-tenant denial | **High** | Medium |
| 17 | Build completed ADR, risk-gate, release, incident and decommission artefacts | **High** | Medium |
| 18 | Repair Style Bible cross-references through signed style decision; add canonical glossary lint | **High** | Medium |
| 19 | Audit each prose paragraph under B/C/O; delete redundant inventories and replace generic conclusions | Moderate | Medium |
| 20 | Commission figures, accessibility/EPUB review, proofing, index and production QA only after narrative/architecture freeze | Moderate | High |

### Dependency-based implementation order

**Phase A — freeze the book contract:** priorities 1, 4, 6, 18. Owners: developmental editor and lead architect. Exit gate: approved vocabulary register, chapter map, agreed C2 canonical topology, fictional narrative charter.

**Phase B — prove the book's differentiated product:** priorities 2, 3, 5, 7, 9, 11. Owners: technical architect, platform engineering reviewer, security reviewer. Exit gate: two complete model chapters, two fully populated decision records, one end-to-end policy/evidence path.

**Phase C — author the reference work:** priorities 8, 10, 12–17. Owners: module authors and domain peer reviewers. Exit gate: all F6/F7/F2/F3 templates conform and samples withstand tabletop review.

**Phase D — acquisition and production:** priorities 19–20. Exit gate: external technical reviews, genuinely representative opening/architecture/decision samples, title/market proposal, and accessibility plan.

### The first 50 **planned pages** to author or rewrite

The uploaded files are Markdown with no reliable print page numbers, so it would be false to cite 'pages 1–50' as physical existing pages. Allocate the first **50 target manuscript pages** as follows:

| Pages to develop | Canonical chapter or content | Why first |
|---:|---|---|
| **8** | **Ch.1:** why the shared Fabric exists and when it does not | Establish book promise and reader need with Meridian incident. |
| **10** | **Ch.5:** build/buy/embed/partner + no-fabric option | Prove judgment rather than advocacy and give procurement/funding basis. |
| **10** | **Ch.10:** canonical architecture and model reconciliation | Prevent every subsequent chapter from contradicting the book's vocabulary. |
| **10** | **Ch.12:** Identity and Delegation control plane | Strongest enterprise security trust boundary, testable end-to-end. |
| **12** | **Twelve individual F1 decision pages** from Ch.16's catalogue | Prove the distinctive, reproducible reader deliverable. |
| **Total: 50** | | |

The 12 decision pages are **12 separate one-page records**, not a 12-page violation of the F1 limit. Remaining Ch.16 decisions follow afterward.

### If limited to 30 working days

| Days | Deliverable and acceptance criterion |
|---|---|
| 1–4 | Architecture/vocabulary freeze; identify overlaps; draft corrected style decisions and table of contents; charter Meridian with fiction disclaimer. |
| 5–10 | Complete a flagship **Identity/Delegation and Agent Gateway** chapter with a sample transaction, enforcement test, failure table and E4 close. |
| 11–15 | Complete the **Memory/Context** chapter from `R§21`, including documented write policy, cross-tenant denial, contradiction case and TCO impact. |
| 16–20 | Complete **six priority F1 decision pages** plus first-use-case evidence: build/buy, tenant model, identity, gateway, memory, autonomy. |
| 21–25 | Independent security/architecture peer review; fix findings; verify dated standards and strengthen no-build cases; run lexical/style gates. |
| 26–30 | Build acquisition proposal: audience and competitive analysis, 2 polished sample chapters, sample decision pages, detailed chapter map and credible completion plan. |

**Thirty-day success is a defensible proposal package, not a finished 490-page book.**

---

# Stage 10 — Rewrite demonstrations

Each **AFTER** passage is a proposed replacement, not a claim that it already appears in the manuscript. The Style Bible governs the rewrite: short mechanism-led prose, British spelling, controlled terms, restrained fictional incident, decision/artefact connection. Full chapters still need the mandatory E4 closing blocks.

## Demonstration A — Weakest consequential chapter opening

**BEFORE, canonical Ch.1, `B:25–37`:**

> A shared enterprise agent fabric is a platform for governed agent execution across many use cases.
>
> It is not: a single chatbot, a single business workflow, a single model endpoint, a single team's AI project.

**AFTER — proposed replacement, fiction:**

> Meridian Financial's fourth AI pilot passed its functional tests. It failed the security review. The team could show what the agent had done, but not which employee had authorised its tool calls.
>
> Two other pilots had the same problem. Each business unit had built its own credentials, action logs, and approval process. One used a service account whose privileges exceeded the user's. Another stored approval decisions in a ticket comment.
>
> The executive sponsor proposed a central Fabric. The security architect disagreed with the timing. She wanted proof that shared controls would reduce the duplicated risk without crossing the business units' data boundaries.
>
> That became the first decision: should Meridian build a shared Fabric, extend its existing platforms, or keep isolated agent services? The team would record the answer in **Decision D-01: Fabric adoption**, with cost assumptions, isolation requirements, and a review date.

**WHY:** A real governance failure motivates the decision instead of opening with a dictionary definition. Each claim about Meridian is explicitly fictional. The result is an identifiable artefact, not a motivational slogan. The scene uses few actors, avoids rhetorical questions and dramatic dialogue, and stays in the B1 Part I register. It also leaves the no-build option live.

## Demonstration B — Weakest explanatory/control-plane section

**BEFORE, canonical Ch.13, `B:231–240`:**

> Gateway responsibilities: A2A routing and policy, MCP termination and tool enablement, model routing/failover policy, network egress governance.
>
> Non-bypassability requirement: all mutable external actions must cross gateway policy enforcement.

**AFTER — proposed mechanism excerpt:**

> The Gateway Control Plane enforces policy at the point where an agent requests an external action. The Harness may recommend a tool call. It cannot approve its own authority.
>
> The gateway receives the actor identity, tenant, delegated authority, target tool, operation, resource, and purpose. It verifies token audience and expiry. It then requests a policy decision against the current rules and resource attributes. A permit decision is bound to the exact operation and short validity window.
>
> The tool adapter verifies the permit again before committing a write. For an ambiguous result, it checks the action receipt or idempotency key before retrying. A timeout is not evidence that an action did not happen.
>
> The network blocks direct agent egress to protected write endpoints. If the policy service is unavailable, write requests fail closed. Read-only service may continue under a separately authorised degraded mode.
>
> The minimum evidence artefact records the actor, tenant, delegation chain, policy version, request hash, decision, target, effect, and outcome. Test this contract by attempting a direct write, reusing a permit, revoking authority mid-run, and interrupting the policy service.

**WHY:** The mechanism distinguishes Harness from independently enforced authority; specifies timing, policy inputs, failure mode, audit evidence, and bypass test. It exposes the operational cost and deliberately handles uncertain side effects. It fits Part III mechanism-first voice. A complete F7 chapter must also supply threat coverage, enforcement point, decision/default/artefact closing, and citations.

## Demonstration C — Narrative vignette: absent in the source

**BEFORE:** There is **no existing vignette to quote or identify as 'weakest'**. No Meridian Financial story appears in either draft, and `transcript.md` discusses **CoLab** in podcast dialogue (`T:1–47`, `T:399–405`). Substituting that dialogue would contravene J1, B4, and J5. The missing vignette is the defect.

**AFTER — new restrained Meridian vignette, proposed for Ch.25 / first pilot:**

> Meridian Financial had approved an insurance service pilot with access to customer-support records. A second pilot, operated by retail banking, used the same ticket integration. The two domains shared a tool description, but they did not share an authorisation contract.
>
> During testing, the insurance agent selected a retail banking ticket with a similar customer reference. The integration accepted the update. The pilot owner reversed the change, then asked for the original authorising identity. The logs contained a service account and a session number. Neither named the employee or the delegation scope.
>
> Maya, the platform lead, brought the evidence to the next design review. The security architect asked, "Which user authorised the update?" Maya could identify the initiating team, but not the delegating user. The two pilots lost write access until they could prove the chain.
>
> The team retained read-only operation while it introduced tenant-scoped identity, an action gate, and a decision receipt. It then repeated the cross-domain test. This time the gateway rejected the update before it reached the ticket system.
>
> The resulting artefact was **Decision D-07: Delegated action authorisation**, with a negative test proving cross-tenant denial.

**WHY:** A recognisable production failure has a bounded consequence, an accountable response, a tested corrective control, and a named artefact. It avoids a villain, speculation about feelings, rhetorical questions, long dialogue, and an inspirational closing. The scenario is **fictional**, not an assertion that an enterprise incident occurred. Publication requires the J1 disclaimer and a consistent case ledger.

---

# Stage 11 — Publisher readiness scorecard

| Area | Status | Why |
|---|---|---|
| Structure | **Fail** | An eight-part outline exists; chapter content and F6/F7 architecture do not. |
| Technical depth | **Partial** | Good source inventory, limited causal contracts, no verified worked implementation. |
| Consistency | **Fail** | Style Bible C2 and two competing architecture taxonomies conflict. |
| Narrative | **Fail** | No Meridian case exists in the manuscripts. |
| Editing | **Fail** | Not enough authored prose to line edit; structural work must precede copyedit. |
| Differentiation | **Unproven** | The decision-surface promise is distinguishable but unfulfilled. |
| Market position | **Unproven** | Audience plausible; no rigorous competing-title map, buyers, sample feedback, or positioning proof. |
| Production readiness | **Fail** | No completed diagrams, figure metadata, indexing, template QA, verified sources, EPUB proof, or final manuscript. |

**Final verdict: NOT READY.** More precisely: **Early Draft** is the production stage, and **Not Ready** is the acquisition-submission decision.

### Acquisition gates to change the decision

1. A ratified C2-compliant architecture with a published interface and owner crosswalk.
2. Two independently reviewed, complete, compliant sample chapters covering technical depth and enterprise judgment.
3. At least six filled F1 decisions with real default/trade-off/deviation/reversibility/evidence fields.
4. One complete fictional Meridian use-case trajectory spanning adoption, incident, revision, and retirement.
5. A full manuscript map that reconciles Ch.1–53 with the long-source numbering, removing duplicates.
6. A dated source register, original diagrams, and a credible authoring schedule.

---

# Stage 12 — Direct answers: the hard judgments

**1. What would cause a publisher to reject it?** The book does not exist in publishable chapter form. A commissioning editor expecting a differentiated sample gets a 53-entry outline, a second conflicting source taxonomy, and a transcript about a different platform. Additional causes: unsupported claims of originality, missing narrative despite the stated book promise, missing decision pages, and absent market comparisons.

**2. Single biggest weakness?** The absence of a **coherent, instantiated, decision-centred architecture chapter**. The normative contradiction is the strongest immediate technical symptom; the incomplete book promise is the deeper defect.

**3. Single biggest strength?** The source material identifies a worthwhile enterprise design problem: **how identity, tool authority, memory provenance, evaluation, economics, and operational recovery must work together across multiple agent use cases**. That can sustain a durable architecture reference if turned into contracts and decisions.

**4. What makes it category-defining?** Not a new taxonomy. It becomes distinctive when every important enterprise AI action can be followed **from initiating human authority through agent execution and gateway policy to evidence, cost, rollback/compensation, and governance review**, with an exact design decision at each boundary. That chain must be demonstrated for 'build Fabric', 'embed SaaS', and 'do not centralise'.

**5. Which 50 pages first?** See the **8+10+10+10+12** page development allocation in Stage 9. This is a proposed page budget because the current Markdown has no designed pagination.

**6. Which chapter would be sent tomorrow?** **None as publisher-ready.** The technically strongest reconstruction candidate is long-source **§21 Memory and State Management** (`R:818–980`). Label it as draft technical material if a publisher explicitly asks for an outline plus work-in-progress extract.

**7. Where should 30 days go?** Architecture/vocabulary freeze, one complete identity/gateway chapter, one memory/context chapter, six decision pages, a complete fictional decision trajectory, and independent technical review. Do not spend the month making the outline sound more elegant.

---

# Evidence appendix — audit scope, limitations, and repeatability

The companion machine-generated files contain:

- `editorial_chapter_inventory.csv`: all **53 blueprint chapters** and **62 numbered source sections**, location, word and prose counts, and flags for whether draft content discusses failure, decision, default, evidence, and prescribed closing sections. These flags are intentionally **broad proxies**, not judgments that a section passes E1/F6.
- `editorial_language_occurrences.csv`: exact file, physical line, matching term, and source line for the configured C10 language audit, including permitted uses of 'substrate' and 'harness' that **must not** be counted as violations under C2/O7.
- `editorial_metrics.json`: file counts and additional punctuation/vocabulary flags.

**Limitations:** This report assesses only supplied materials. It does not certify standard compliance, authorship, intellectual property provenance, production suitability, proprietary industrial experience, or market demand. Protocol/OWASP checks were limited to targeted high-impact external verifications, not an independent literature review of every standard. Scores depend on a declared editorial rubric and require human reviewer calibration before being treated as publication gates.

**Bottom line:** Keep the ambition but stop treating a component inventory as a reference book. Freeze one architecture, turn it into hard decisions and interfaces, and demonstrate its consequences through a fictional enterprise operating under credible constraints. The book can then be judged by what a reader can decide and build, rather than by how many subjects it names.
