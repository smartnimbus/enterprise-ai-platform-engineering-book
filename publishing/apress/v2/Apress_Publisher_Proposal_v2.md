# The Enterprise AI Agent Fabric

## Designing, Governing and Operating AI Agents at Scale

**Apress book proposal — Version 2**  
**Format:** Authored professional technical book, vendor-neutral, with a decision-led enterprise reference and worked artefacts  
**Intended imprint:** Apress, Springer Nature  
**Primary readership:** Enterprise architects and AI platform engineering leads  
**Secondary readership:** Security and identity architects; platform engineering leaders; SRE and operations leads  
**Estimated extent:** 448 planned chapter pages; approximately 478 pages including introductory matter and index (subject to commissioning and production)  
**Proposed structure:** 58 fixed chapters in eight parts; a 30-decision Atlas; eleven lifecycle stages; ten practitioner playbooks  
**Manuscript status:** Chapter 16 is an existing substantive draft; Chapter 13 is a developed authoring blueprint. All other chapters have defined briefs, with the majority of final narrative still to be written.

---

## The book in one sentence

**Building an AI agent is an application problem; operating many agents safely is a platform engineering problem.**

## The acquisition proposition

Enterprises are moving beyond agent demonstrations into portfolios of assistants, workflows and autonomous actors that read protected information and may act on business systems. The technical question is no longer merely how to build one capable agent. It is how to choose which capabilities should be shared, who is allowed to delegate consequential actions, how to recognise unresolved business context, and what evidence justifies releasing, scaling, changing or retiring a service.

*The Enterprise AI Agent Fabric* gives technology leaders a repeatable way to make and defend those decisions. It combines a vendor-neutral architectural reference with a **30-decision Atlas**, explicitly assigned responsibilities, measurable enforcement and verification conditions, and practical records that can be used in architecture reviews, product onboarding, security approval, operations and eventual exit. It treats 'do not build a shared Fabric' as a valid result when the economics or service boundaries do not support centralisation.

The book's distinctive teaching pattern is **decision-to-evidence engineering**: for each material enterprise choice, record the default and available alternatives, name the accountable owner, identify the actual enforcement or operating point, define the test or review needed, and specify what artefact would support acceptance. The method connects subjects frequently taught separately—platform ownership, agent identity, context provenance, security, evaluation, FinOps and retirement—without claiming to invent any of them.

Its intended readers are practitioners responsible for more than a single agent demo. They need an architecture they can explain to stakeholders and an operating method they can use to say *yes*, *not yet* or *no* to a proposed workload. The book is designed to be reopened at each such decision, rather than read once and discarded.

## Executive summary

AI agents introduce new choices into established enterprise engineering. They can carry delegated identity, assemble a response from inconsistent sources, select tools, revisit work after interruptions and produce externally consequential outcomes. As several teams adopt agents, isolated implementation choices become shared questions about trust boundaries, service ownership, cost, test evidence and eventual withdrawal. A successful pilot may show that a task is useful; it does not by itself establish that the organisation should fund or operate a central agent platform.

*The Enterprise AI Agent Fabric: Designing, Governing and Operating AI Agents at Scale* addresses that transition. It is a professional reference for enterprise architects and platform leads deciding whether, where and how to provide reusable capabilities across agentic workloads. The book begins with strategy and the choice not to build, progresses through architectural responsibilities and practical decision records, then follows adoption into operational ownership, incidents, economics, scale and retirement.

The reference distinguishes four Structural Layers—Execution Environment, Tooling, Context and Lifecycle—from eight cross-cutting Control Planes—Identity, Gateway, Observability, Verification, Governance, FinOps, Data Protection and Interoperability. Each is assigned a bounded responsibility. The point is not to demand twelve separate products or teams; it is to make authority and accountability visible regardless of the vendor or deployment architecture.

The **Decision Atlas** is the central reader artefact. Thirty one-page decisions each set out the context, default, alternatives, trade-offs, deviation conditions, reversibility and expected output. Instead of presenting controls as an isolated checklist, the book connects each choice to a named owner, enforcement or operating point, test and evidence record. Eleven lifecycle stages tell the reader when these decisions are made or revisited. Ten practitioner playbooks explain how to complete the work in common enterprise situations, from a business case to an incident or a Fabric retirement.

A fictional organisation, **Meridian Financial**, provides a recurring example. Its deliberately synthetic records include conflicting customer-product information, bounded delegation, a denied refund-changing action, an attempted bypass and a failed release assertion. The case illustrates how decisions, evidence and accountability relate; it is not presented as proof that a real enterprise deployed the described controls. Worked examples throughout the book are labelled by evidence class and indicate what a reader would need to verify in an actual environment.

Two proposed sample chapters show the technical contrast at the heart of the book. **Chapter 13, Context**, teaches how information is retrieved, classified, reconciled and retained without silently turning a source conflict into business truth. **Chapter 16, Gateway Control Plane**, teaches how an agent's proposed external action is admitted or denied against authority, policy and non-bypassability requirements. Their corresponding Atlas pages demonstrate how the same technical boundary becomes a reviewable enterprise decision. Together they illustrate a practical reference that can be used to resolve disputes between architecture, security, platform delivery and operations.

The final book is planned as 58 concise chapters in eight parts, with an estimated total extent of approximately 478 pages including front matter and index. It is intended for readers familiar with enterprise software systems who need a disciplined way to evaluate, build, buy, govern and operate agent capabilities at organisational scale. It is not a single-framework programming tutorial, a law or regulation commentary, or an argument that every enterprise should build its own Fabric.

## Reader audience and purchase triggers

### Enterprise architects — primary

The enterprise architect is asked to evaluate a portfolio of proposed agents, not a single technical proof of concept. The purchase trigger is an investment, architecture or risk decision that requires defensible alternatives and named ownership. The reader uses the book to distinguish platform-level requirements from domain-specific ones, document a shared-versus-local decision, and require evidence before permitting higher autonomy. The resulting artefacts include decision records, tenant-boundary specifications, threat considerations and an exit plan.

### AI platform leaders — primary

The AI platform lead is accountable for making funded capabilities reusable without becoming owner of every business outcome. The trigger may be a second or third use case demanding the same identity, tool, model, evaluation or observability functions; it may instead be a production incident revealing inconsistent controls. The book equips this reader to specify the platform as a product, agree onboarding contracts, assign service responsibility, measure a task's cost and require verifiable release conditions. The reader is not directed to purchase or implement a particular vendor stack.

### Security, identity and data architects — secondary

These readers need to explain what an agent is authorised to do, on whose behalf, for how long, with which data, and how a failed or bypassed control would be detected. The book treats the action boundary as a technical enforcement obligation. It keeps identity claims distinct from business truth, and governance policy distinct from the mechanisms that block an unauthorised action.

### SRE, operations and platform product teams — secondary

These readers inherit the system after deployment. They need to reconstruct an agent action, understand recovery obligations, distinguish failed evaluations from production incidents, identify who may change a model or tool contract, reconcile charges and know how to retire a use case without losing necessary evidence. Operational playbooks connect the architecture and decisions to those responsibilities.

**Assumed experience:** Enterprise applications, distributed systems, service ownership and standard security principles. Specialist familiarity with LangChain, LangGraph or any other agent SDK is not required.

## Why this book is needed

The market includes strong books about agent application development, AI governance, identity and platform engineering. Each addresses material parts of the problem. Their presence makes the market more credible while increasing the need for a sharply defined reader promise. This book focuses on the *cross-domain decision and its operational evidence*: should a shared service exist; what should it own; what is delegated; what must be tested; when should a release fail; how does the use case justify its cost; and how are access, data and service obligations unwound at retirement?

The book seeks to help practitioners avoid three predictable sources of waste. **First**, prematurely centralising agent capabilities because an experimental workload appeared successful. **Second**, specifying governance requirements without allocating an actual enforcement point or confirming that bypass is prevented. **Third**, accepting positive demonstrations without reliable negative tests, evidence custody, cost attribution or exit planning. These are engineering decisions that can be taught through comparative alternatives and inspectable artefacts, not through an assertion that a new diagram alone solves them.

Evidence of agent adoption and platform demand is evolving. Industry surveys support the relevance of the topic but do not establish a sales forecast for this book. The acquisition proposition therefore rests on identifiable reader jobs and manuscript deliverables, not a numerical estimate of a purported 'agent fabric market'.

## Contribution and differentiation

**Decision-to-evidence engineering** is the book's principal organising method. A reader can start with an enterprise choice and follow it through six questions:

1. **Decision:** What choice is being made, and which default or alternative is justified?
2. **Accountability:** Who owns the decision, who operates the service and who may approve a deviation?
3. **Enforcement:** Which component or human process actually makes the chosen constraint effective?
4. **Verification:** Which positive and negative tests, measurements or observations would challenge the claim?
5. **Evidence:** What retained record allows a later reviewer to reconstruct the decision and outcome?
6. **Lifecycle:** When must the choice be revisited, reversed, funded differently or retired?

For example, a design may require delegated identity and policy checks before any externally mutable tool call. The choice is not complete merely because a policy exists in a document. A reader must identify the authorising actor, the precise action scope, the point that can prevent the call, tests for alternative egress paths, and the records demonstrating a denied or permitted result. An Atlas entry captures the contractual decision; a Control Plane chapter explains its mechanism; a playbook and worked evidence specimen make it usable.

The contribution is an integrated reference and teaching format, not exclusive ownership of agent gateways, decision records, control planes, platform products, autonomy governance or systems assurance. The manuscript will acknowledge adjacent specialist work and explain the scope in which its own tools are useful.

### What the reader takes away

- A defensible recommendation to establish—or not establish—a shared enterprise Fabric.
- A consistent vocabulary for four Structural Layers and eight Control Planes, with explicit ownership boundaries.
- Thirty reusable decision-page structures that support reviews and deviation management.
- A method for checking authorisation, context provenance and data isolation without silently expanding permission.
- Release and incident evidence patterns, including negative outcomes and their interpretation.
- A way to relate model and tool behaviour to cost per successful task rather than token cost alone.
- Ten step-by-step practitioner playbooks, from initial funding through model change, incident response and retirement.

## The book's construction and reader experience

The text is organised into eight coherent parts. A reader may follow it from first principles to operations, or use the decisions and reference material independently during a particular review. Cross-references direct readers to the one chapter responsible for explaining a mechanism; later chapters apply that mechanism instead of restating it in conflicting terms.

| Part | Chapters | Reader purpose | Planned chapter pages |
| --- | --- | --- | ---: |
| I. Foundations | 1–4 | Establish when shared infrastructure is justified and the risks of autonomy | 36 |
| II. Enterprise Strategy | 5–9 | Choose sourcing, ownership, tenancy, model strategy and sponsorship | 55 |
| III. Canonical Architecture | 10–22 | Distinguish layer responsibilities and cross-cutting enforcement/operating controls | 92 |
| IV. Decision Atlas | 23 | Consult thirty repeatable decisions and the artefacts they require | 30 |
| V. Delivery Lifecycle | 24–34 | Apply decisions from strategic intent to retirement | 55 |
| VI. Operations | 35–40 | Own reliability, incidents, cost, releases and evidence | 54 |
| VII. Practitioner Playbooks | 41–50 | Execute ten repeatable enterprise tasks | 70 |
| VIII. Reference | 51–58 | Use templates, standards references, controlled terms and evidence specimens | 56 |
| **Total** | **58 chapters** | | **448** |

### Running case: Meridian Financial

Meridian is a fictional enterprise deliberately used for a consistent, inspectable scenario rather than a claim of production deployment. Its frozen refund-and-context evidence demonstrates a conflict between product data sources, limited delegation, denial of an unauthorised financial mutation, the separation of runtime enforcement from evaluation, and what an unsuccessful release assertion looks like. The book will clearly separate synthetic fixture facts from suggested reader exercises, future design examples and any externally supported facts. Neither Meridian's events nor Atlas defaults will be rewritten to make a more convenient story.

### Decision Atlas

A compact set of thirty entries anchors the book's practical use. Each entry identifies the question, frozen default, alternatives, trade-offs, deviation conditions, reversibility and expected artefact. The Atlas covers not only runtime constraints but whether the organisation should create a shared Fabric, how to source components, whose authority applies, how to justify cost, and how to retire use cases and shared infrastructure. The standalone Atlas pages are presented in a consistent F1 layout so they can be used as review and workshop references.

### Practitioner playbooks

Ten playbooks take the reader through business-case development, reference architecture, tenant substrate, first onboarding, scaling, model upgrades, security incidents and retirement. Each is intended to provide a clear entry condition, actors and owners, actions, evidence requirements, abort conditions and completion records. The playbooks are application guides, not alternative definitions of architecture.

## Illustrative reader exercise: the interrupted financial action

A customer-service agent receives inconsistent product information from two sources and proposes a refund-related action. A weak architecture might let the agent choose the newest record and proceed. The approach taught in this book instead preserves source provenance, records unresolved conflict, checks the actor's delegated authority at the mutable-action boundary and declines the action when the required authorisation is missing. An evaluation later asks whether the candidate agent behaved within its declared constraints. The fictional Meridian evidence records a denial and failed release assertion, not a successful refund or a proven deployed system.

From this case the reader can produce a Context Manifest, a constrained delegation record, an action-decision receipt, a negative enforcement check and a release-gate record. The point is to move from a principle such as 'agents should be governed' to a reconstructable chain of engineering and human decisions.

## Commercial fit and competitive context

Apress serves working technologists and enterprise practitioners. The proposed book is designed as a durable professional reference rather than a fast-moving catalogue of model APIs. Its immediate peers include Apress books on governance, enterprise agent adoption and AI identities, plus O’Reilly books addressing AI agent platforms and agent governance, and broader AI systems engineering literature.

The book does **not** claim that competitors omit evaluation, security, identity or operational controls. *Building AI Agent Platforms*, for example, addresses substantial platform implementation and product concerns; *AI Agent Governance* addresses agent governance in depth. The proposed difference is the decision-centric structure connecting business justification to named enforcement, verifiable evidence, cost and eventual withdrawal. The accompanying **Apress Acquisition Competitive Dossier v2** supplies a qualitative buyer comparison and publisher-catalogue links.

## Author and contributor information

**Proposed author:** [Author's publishing name — to be confirmed]  
**Professional title and organisation:** [Confirm authorised wording]  
**Relevant experience:** [Provide factual years, named responsibilities and relevant enterprise architecture / platform / AI engineering experience]  
**Public contributions:** [Provide publication, conference, standards, open-source or training links that may be independently verified]  
**Intended distribution and audience access:** [Describe only demonstrable readership, professional networks or speaking channels]  
**Technical contributors and reviewers:** [Add confirmed names and permitted affiliations, if applicable]

The book is designed to be credible through worked decisions and clear technical evidence. The author's professional biography will establish the specific practitioner experience underpinning those examples. No client deployment, certification, sales audience or endorsement is represented here without permission and verification.

## Manuscript delivery and production

The fixed 58-chapter plan allows work to proceed in coordinated groups once the technical exemplars establish the voice and depth expected of the book. The present material includes a substantive Chapter 16 draft, extensive Chapter 13 and Chapter 16 authoring blueprints, the full Decision Atlas catalogue, the Meridian synthetic evidence fixture and detailed chapter briefs. These reduce planning and assembly effort but do not replace original narrative authorship or external technical review.

The current planning estimate for a complete manuscript is approximately **980 qualified human hours** including chapter writing, reuse, technical editing, citation work and integration. The estimated extent is 448 chapter pages plus front matter and index. A six-month delivery would require sustained capacity of approximately 38 qualified human hours a week across authorship, specialist review and editorial work. The actual contractual date should be agreed only after the author and any collaborators confirm their available capacity and the scope of the publisher's requested sample and figure work.

Apress can first receive two fully edited technical examples—Chapter 13 (*Context*) and Chapter 16 (*Gateway Control Plane*)—together with six representative F1 decision pages. The remaining manuscript proceeds through the fixed structure in a phased editorial sequence; chapter order and frozen technical meanings remain unchanged.

## Planned illustrations and learning resources

Figures will include conceptual and logical architecture views, request and delegation sequences, Context provenance and conflict flows, non-bypassability paths, lifecycle and evidence chains, and selected operational worksheets. The diagrams will be line-readable in print and accessible in digital formats, with clear legend, source ownership and descriptions. Example artefacts use invented organisations and identifiers or references with the required permissions.

A small companion download may provide editable decision templates, checklists and synthetic example records, but the book itself will contain the explanations necessary to understand and apply the method. No external repository or executable reference implementation is a prerequisite for the reader to follow the chapters.

## Proposal facts and submission details

| Field | Proposed value |
| --- | --- |
| Book title | *The Enterprise AI Agent Fabric* |
| Subtitle | *Designing, Governing and Operating AI Agents at Scale* |
| Publisher | Apress / Springer Nature |
| Category | Professional enterprise architecture, platform engineering and agentic AI |
| Format | Authored vendor-neutral professional reference |
| Primary buyers | Enterprise architects; AI platform leads |
| Secondary buyers | Security/identity architects; engineering and operations leaders |
| Technical assumptions | Familiarity with enterprise software architecture; no single agent SDK required |
| Planned chapters | 58 across eight parts |
| Planned body | 448 chapter pages |
| Planned total | Approximately 478 pages with front matter and index |
| Supplementary content | Optional reusable records/checklists and synthetic evidence examples |
| Current completed material | One substantive Chapter 16 draft; Chapter 13 blueprint and frozen source/decision assets |
| Submission samples | Two full technical chapters and six F1 pages planned; **not supplied as final samples with this v2 proposal** |
| Author, contact and distribution | To be completed from verified author information |
| Delivery date | To be agreed based on committed resources and publisher schedule |

## Full chapter synopsis (fixed structure)

The section list below preserves the existing chapter identities. Each entry states the reader's practical outcome; the detailed 58-chapter development blueprint supplies the technical specification for authorship.

**01. I. The Case for a Shared Fabric.** Establish the repeat-use-case problem → identify shared economics/control triggers. Related decisions: D-01.

**02. I. Agent Capability, Autonomy and Risk.** Tie capabilities to permitted actions → classify autonomy envelope. Related decisions: D-05, D-16.

**03. I. Fabric, Product, Use Case and Tenant.** Draw ownership boundaries → assign responsibility without ambiguity. Related decisions: D-06, D-04.

**04. I. When Not to Build a Fabric.** Identify disqualifying conditions → choose an alternative. Related decisions: D-01, D-02.

**05. II. Build, Buy, Embed or Partner.** Compare acquisition patterns → defend a reversible choice. Related decisions: D-02.

**06. II. Central, Federated or Hybrid Ownership.** Allocate authority → choose team structure and exception path. Related decisions: D-03, D-06.

**07. II. Tenant Isolation and Sovereignty.** Select isolation model → name mandatory data and identity boundaries. Related decisions: D-04, D-25.

**08. II. Model Strategy and Unit Economics.** Design route and fallback policy → justify spend/performance bounds. Related decisions: D-17, D-26.

**09. II. Earned Autonomy and Sponsorship.** Specify promotion criteria → fund only evidenced autonomy. Related decisions: D-05, D-16, D-23.

**10. III. The Canonical Fabric Architecture.** Lock E/T/C/L plus eight planes → trace a request and its evidence. Related decisions: D-07, D-18.

**11. III. Execution Environment.** Isolate work → specify sandbox and quota contracts. Related decisions: D-07, D-08.

**12. III. Tooling.** Make tool invocation typed and bounded → implement action contracts. Related decisions: D-09, D-10.

**13. III. Context.** Govern retrieval, memory and meaning → specify provenance and contradiction handling. Related decisions: D-11–14.

**14. III. Lifecycle.** Own the Harness and trajectory → design interruption/resume and multi-agent coordination. Related decisions: D-15, D-16.

**15. III. Identity Control Plane.** Constrain actors/delegation → verify non-expanding authority. Related decisions: D-19, D-20.

**16. III. Gateway Control Plane.** Enforce each mutable external action → prove non-bypassability. Related decisions: D-10, D-18.

**17. III. Observability Control Plane.** Correlate events and outcomes → reconstruct trajectories. Related decisions: D-24.

**18. III. Verification Control Plane.** Gate behaviours and releases → specify assertions/evidence. Related decisions: D-22, D-23.

**19. III. Governance Control Plane.** Establish risk decision rights → govern exceptions and autonomy. Related decisions: D-05, D-29.

**20. III. FinOps Control Plane.** Govern budgets/chargeback → attribute cost per successful task. Related decisions: D-26.

**21. III. Data Protection Control Plane.** Protect personal/regulated data → prove retention and deletion. Related decisions: D-25, D-30.

**22. III. Interoperability Control Plane.** Version boundary contracts → accept or reject protocol changes. Related decisions: D-21.

**23. IV. The Fabric Decision Atlas.** Make every major choice reproducible → complete 30 decision pages. Related decisions: D-01–30.

**24. V. Stage 0: Strategic Intent.** Establish demand and alternatives → authorise or stop discovery. Related decisions: D-01–03.

**25. V. Stage 1: Fabric Vision.** Define product and success criteria → approve measurable scope. Related decisions: D-05–06.

**26. V. Stage 2: Reference Architecture.** Specify topology/control contracts → approve baseline. Related decisions: D-07–15, D-18.

**27. V. Stage 3: Trust Chain and Security.** Threat-model runtime and delegation → accept bounded risk. Related decisions: D-10, D-19–21, D-25.

**28. V. Stage 4: Tenant Substrate.** Build isolation and context partitions → evidence no cross-tenant leak. Related decisions: D-04, D-11–14.

**29. V. Stage 5: Shared Services Bootstrap.** Stand up gateway, observability and verification → pass control smoke tests. Related decisions: D-17–18, D-22, D-24.

**30. V. Stage 6: First Use Case.** Onboard a bounded use case → make a go/no-go decision. Related decisions: D-05, D-16, D-23.

**31. V. Stage 7: Scale to Twelve Use Cases.** Enforce onboarding archetypes → expand without policy drift. Related decisions: D-04, D-29.

**32. V. Stage 8: Operate as a Product.** Institute SLOs/on-call/chargeback → evidence service ownership. Related decisions: D-26–28.

**33. V. Stage 9: Continuous Verification.** Detect regression and requalify → sustain earned autonomy. Related decisions: D-22–23.

**34. V. Stage 10: Retirement.** Retire a use case and plan Fabric exit → preserve/delete records correctly. Related decisions: D-30.

**35. VI. Team Design and Responsibility Matrix.** Name owners and deputies → resolve every handoff. Related decisions: D-03, D-06, D-29.

**36. VI. Reliability, Service Levels and Continuity.** Define error budgets and recovery → test a service tier. Related decisions: D-27.

**37. VI. Incident Command and Security Response.** Contain bad actions → assign incident command and evidence custody. Related decisions: D-28.

**38. VI. Unit Economics, Showback and Chargeback.** Attribute usage and value → reconcile unit economics. Related decisions: D-26.

**39. VI. Release, Change and Version Control.** Control prompts/tools/models/policies → prevent unreviewed production change. Related decisions: D-21–23, D-29.

**40. VI. Audit Evidence and Assurance Reviews.** Reconstruct permission, action and outcome → produce audit-ready evidence. Related decisions: D-20, D-24, D-30.

**41. VII. P1: Build the Business Case.** Execute sourcing and financial appraisal → obtain funding gate. Related decisions: D-01–03, D-26.

**42. VII. P2: Design the Reference Architecture.** Apply structural/control contracts → obtain design approval. Related decisions: D-07–22.

**43. VII. P3: Stand Up the Tenant Substrate.** Provision and test tenant partitions → sign isolation proof. Related decisions: D-04, D-11–14, D-25.

**44. VII. P4: Onboard the First Use Case.** Register/verify/release use case → approved production pilot. Related decisions: D-05, D-16, D-23.

**45. VII. P5: Scale from One to Ten Use Cases.** Template onboarding and cost policy → controlled portfolio. Related decisions: D-06, D-26, D-29.

**46. VII. P6: Plan for Ten to One Hundred-Plus.** Capacity and isolation stress-test → scale/no-scale plan. Related decisions: D-08, D-27, D-29.

**47. VII. P7: Execute a Model Upgrade.** Compare candidate with baseline → gated canary or rollback. Related decisions: D-17, D-22–23.

**48. VII. P8: Handle a Security Incident.** Contain, preserve and recover → verified safe resumption. Related decisions: D-10, D-20, D-28.

**49. VII. P9: Retire a Use Case.** Revoke access and dispose data → audited use-case retirement. Related decisions: D-30.

**50. VII. P10: Retire or Replace the Fabric.** Move/terminate tenants and preserve obligations → executable exit. Related decisions: D-02, D-27, D-30.

**51. VIII. Layer and Control-Plane Checklists.** Enable evidenced inspection → verify all 12 architecture units. Related decisions: D-07–25.

**52. VIII. Architecture Decision and Risk Records.** Supply accepted templates → produce a complete ADR and exception. Related decisions: D-01–30.

**53. VIII. Protocol and Boundary Reference.** Locate versioned protocols → choose and check contracts. Related decisions: D-09, D-21.

**54. VIII. Technology Decision Matrix.** Compare implementation categories without endorsement → evaluate alternatives. Related decisions: D-02, D-07, D-17.

**55. VIII. Standards and Regulatory Map.** Map named standards to controls → prepare compliance crosswalk. Related decisions: D-19, D-25, D-28.

**56. VIII. Glossary and Controlled Vocabulary.** Find exact meanings → eliminate synonym drift.

**57. VIII. Worked Evidence and Delivery Artefacts.** Inspect full specimens → reproduce usable records. Related decisions: D-20, D-23, D-30.

**58. VIII. Industry Adoption Overlays.** Translate constraints to sectors → adapt risk and data choices. Related decisions: D-01, D-04, D-25.


## Selected references

The companion competitive dossier identifies and links the seven main comparable titles. The broader manuscript will cite primary technical and scholarly sources where specific technical mechanisms, protocols, standards or empirical claims are discussed. This proposal does not use agent adoption survey results as a claim about a quantified addressable book market.

Springer Nature professional-book submission context: https://support.springernature.com/en/support/solutions/articles/6000083155-publish-a-new-book-with-springer  
Book proposal form: https://media.springer.com/full/springer-instructions-for-authors-assets/pdf/SN_BPF_EN.pdf
