# The Enterprise AI Agent Fabric — Style Bible

**Version 1.2 | Status: Ratified | Applies to: All authors, editors, illustrators, diagrammers, and reviewers**

This document is the single source of truth for how the book *The Enterprise AI Agent Fabric* is written, drawn, formatted, and produced. It is binding. Where it is silent, the author must escalate to the editor before inventing a convention. Where it conflicts with personal preference, this document wins.

**Changes in v1.2:** Adds Part O (Anti-Slop Discipline) integrating the unslop skill into the book's editorial system. Extends C1 (rhythm, rule of three, synonym cycling), C3 (colon usage, adverb discipline, em dash frequency, curly quotes), C10 (six-subsection expanded forbidden words table), B3 (two new narrative vs reference examples), M1–M2 (anti-slop pass in author workflow), and Part N (SD-015 to SD-017). Resolves two conflicts between unslop and the book's conventions in favour of the book.

**Changes in v1.1:** Added narrative quality bar (J5), narrative dosing (E5), two-book accommodation (A4), restrained narrative register (B4), narrative good/bad examples (B3.2), sharpened "what the book is not" statement (A3), and SD-011 to SD-014.

All v1.0 content is retained unless explicitly revised.

---

## Part A — Editorial Identity

### A1. The Book Promise

The book promises the reader three things, in order of priority:

1. **A decision surface.** Every major fabric decision is reduced to a one-page template with a default, a trade-off, a deviation condition, and an artefact.
2. **A reference architecture.** Every structural layer and control plane is explained with its purpose, failure modes, scaling signals, and anti-patterns.
3. **A practitioner's journey.** A narrative spine that shows a fictional organisation making and recovering from real fabric decisions, so the reader can recognise themselves and their organisation in the story.

The book does **not** promise: a tutorial on a specific framework, a vendor recommendation, a certification prep, or a code repository. Those are companion artefacts, not the book.

### A2. Reader Personas and Reading Modes

| Persona | Primary need | Reading mode | Which parts |
|---|---|---|---|
| **Executive sponsor** | Justify investment, understand risk, set direction | Skim | Parts I–II, Chapter 16 (one-page decision map), Appendix B (business case example) |
| **Enterprise architect** | Design the fabric, defend the architecture | Reference | Parts III–IV, VI, VIII |
| **Platform lead** | Build and operate the fabric | Implement | Parts III, V, VII, VIII |
| **Security architect** | Threat-model, control, audit | Reference | Chapters 11, 15, 18, 29 |
| **Domain team lead** | Onboard a use case | Implement | Parts V, VII (especially P4–P5) |
| **CFO / FinOps lead** | Cost model, chargeback | Skim + Reference | Chapter 23, Part IV (FinOps decision), Appendix B |

### A3. What the Book Is Not

The book is a **reference architecture with a narrative spine**. It is not a novel with reference appendices. When the narrative standard and the reference standard conflict, the reference standard wins.

| The book is not… | Because… | What it is instead |
|---|---|---|
| A novel | The narrative exists to teach judgment, not to entertain. When the story and the mechanism conflict, the mechanism wins. | A reference architecture whose strategic and lifecycle sections are carried by vignettes. |
| A specification | The templates are binding within the book, but the book does not govern any external system. | A blueprint with reproducible templates. |
| A manifesto | The book argues for the fabric, but it names the conditions under which the fabric is the wrong choice. | A decision surface with an argument. |
| A blog collection | The book has a spine. The essays do not. | A book with a companion blog, not a blog bound as a book. |
| A tutorial | The book does not teach a framework. It teaches the decisions that any framework must serve. | A reference architecture and practitioner's blueprint. |

### A4. The Book and Its Possible Companion

This Style Bible governs **the reference book** — *The Enterprise AI Agent Fabric: Reference Architecture and Playbook*. It does not govern a companion narrative book, if one is written.

The relationship is as follows:

| Artefact | Governed by | Style |
|---|---|---|
| **The reference book** (this book) | This Style Bible | Hybrid: narrative opens and closes each part, reference carries the body |
| **A companion narrative book** (if written) | A separate style decision | Pure narrative, Phoenix Project model, ~250 pages, C-suite audience |
| **Companion essays** (blog) | The book's style for reference sections; free for narrative | Self-contained, 2,000–5,000 words each |

**Rules for the companion narrative book, if it is written:**

1. It inherits the narrative quality bar (J5) and the character ethics (J2–J3) from this Style Bible.
2. It does **not** inherit the reference chapter templates (F6, F7), the decision templates (F1), or the checklist templates (F3).
3. It does **not** repeat the reference book's content. It *refers* to it.
4. It uses the same Meridian Financial scenario but may extend it with new characters and incidents.
5. It is written **after** the reference book, not before.

**Rules for the reference book if the companion is planned:**

1. The reference book's narrative spine remains intact. It is not thinned to make room for the companion.
2. The reference book's narrative sections point to the companion where deeper narrative is available ("The full story of the gateway build is told in *[companion title]*, Chapter 4").
3. The reference book remains **complete without the companion**. The companion augments, it does not substitute. This mirrors SD-010 for the companion site.

---

## Part B — Voice and Tone

### B1. The Five Voice Registers

The book uses **five distinct voices**, one per part. The register changes because the reader's cognitive mode changes. A single voice across 490 pages is a failure of craft.

| Part | Register | Model | Sentence style | Person | Tense |
|---|---|---|---|---|---|
| **I–II (Orientation, Strategy)** | Conversational authority | Brooks, Hohpe | Short to medium, declarative | Second person ("you") and first plural ("we") | Present |
| **III (Architecture)** | No-nonsense precision | Newman, Fowler | Medium, mechanism-first | Third person ("the gateway enforces…") | Present |
| **IV (Decision Cheat Sheet)** | Prescriptive | Fowler | Short, imperative | Second person ("Choose X when…") | Present |
| **V (Lifecycle)** | Narrative-anchored, restrained | Newman, not Kim | Short to medium, declarative, scene-led | Third person narrative, then second person analysis | Past (scene) → Present (analysis) |
| **VI–VIII (Operating Model, Playbooks, Reference)** | Operational | GoF, Pragmatic Programmer | Short, procedural | Imperative ("Do X. Record Y.") | Imperative |

### B2. Tone Calibration

| Dimension | Position |
|---|---|
| **Formality** | Professional but not stiff. Contract with the reader, not distance from them. |
| **Confidence** | Assertive on defaults, honest on trade-offs. Never hedge a decision; always name the conditions under which it flips. |
| **Warmth** | Present in Parts I–II and V. Absent in Parts IV and VIII. |
| **Humeur** | Dry wit permitted sparingly in Parts I–II only. Never in templates, checklists, or reference material. |
| **Urgency** | High in war stories and playbooks. Neutral in architecture. |
| **Judgement** | The book has opinions. It states them, defends them, and shows when they fail. It does not pretend to be neutral. |

### B3. Good vs Bad — Reference Prose Examples

| Bad | Why | Good | Why |
|---|---|---|---|
| "It is important to consider the various factors when selecting a tenant model." | Passive, hedged, tells nothing | "Default to pooled compute with isolated data and identity. Choose hard isolation only when the contract, the regulator, or the data class demands it." | Active, decisive, names the default and the deviation |
| "The MCP gateway plays a crucial role in the architecture." | Adjective as evidence | "The MCP gateway enforces four things: protocol termination, per-tool rate limits, credential scoping, and egress policy. Without it, those controls are scattered across Layer 0, Layer 6, and the security plane." | Mechanism as evidence |
| "Teams often struggle with memory poisoning." | Vague, no mechanism | "Memory poisoning happens when an agent writes a fact it cannot later provenance. The control is a write-path gate: no durable memory without a source, a confidence score, and a policy class." | Names the failure and the control |
| "This is best practice in the industry." | Appeal to authority | "OWASP ASI06 treats memory poisoning as a first-class threat. The 2026 production pattern is a write-path gate with provenance and TTL." | Cites the standard and the pattern |
| "The gateway plays a pivotal role in ensuring that agent calls are secure, highlighting its importance in the evolving landscape of AI governance." | Puffery, superficial -ing, AI vocabulary | "The gateway terminates the protocol, scopes the credential, and logs the call. Without it, those three controls are implemented four different ways by four different teams." | Mechanism, specificity, consequence |
| "Experts believe that memory poisoning will become a significant concern. As the industry continues to evolve, organisations must remain vigilant." | Vague attribution, formulaic challenge, generic conclusion | "OWASP ASI06 treats memory poisoning as a first-class threat. The 2026 production pattern is a write-path gate with provenance and TTL." | Named source, named standard, named pattern |

### B3.2 Good vs Bad — Narrative Examples

The narrative sections have their own quality standard, defined in J5. These examples illustrate it.

| Bad | Why | Good | Why |
|---|---|---|---|
| "The team was very frustrated with the lack of a shared gateway. They had many meetings about it and eventually decided to build one." | Vague, no stakes, no specificity | "By the fourth meeting about the gateway, the security architect had stopped attending. Her absence was the decision. If security had given up, the gateway would be built without security's input — and it would fail its first audit." | Specific detail, specific consequence, specific decision |
| "Maya was a strong leader who inspired her team to build the fabric." | Adjective as evidence, no mechanism | "Maya did not ask her team to work weekends. She asked them one question: 'which of these four pilots would you bet your name on?' They chose one. The other three were cancelled that afternoon." | Mechanism as evidence, specific action |
| "The breach was a wake-up call for the organisation." | Cliché, no mechanism | "The breach report was eleven pages. The board read the first page and asked one question: 'how many other agents could do this?' Nobody knew. That was the finding." | Specific artefact, specific question, specific gap |

### B4. The Restrained Narrative Register

The narrative register in Part V is **restrained**, not literary. It follows five rules.

| Rule | Specification | Why |
|---|---|---|
| **Sentence length** | 15–25 words. Shorter than the reference register. | Narrative requires momentum. Long sentences slow the scene. |
| **Dialogue** | Maximum four exchanges per vignette. Reported speech after the opening exchange. | Dialogue in a reference book reads as screenplay. Reported speech preserves the information without the performance. |
| **Interiority** | Maximum one sentence per character per vignette. | The reader needs to know what the character is *deciding*, not what they are *feeling*. |
| **Metaphor** | Maximum one metaphor per vignette, and only if it is a construction, biology, or logistics metaphor (C9). | The vignette is not the place for allegory. |
| **Ending** | Every vignette ends with a sentence that names the decision or artefact it motivates. | The story is the vehicle; the artefact is the destination (SD-009). |

**The restraint test:** Read the vignette aloud. If it sounds like a novel, it is too literary. If it sounds like a case study, it is too dry. The target is a **well-written incident report** — vivid enough to create recognition, restrained enough to stay in service of the reference that follows.

---

## Part C — Language Rules

### C1. Sentence and Paragraph Discipline (Extended)

- **Maximum sentence length:** 30 words. Anything longer is two sentences.
- **Maximum paragraph length:** 6 sentences. Anything longer is two paragraphs or a list.
- **One idea per paragraph.** If a paragraph contains "and also," it is two paragraphs.
- **Lists over prose** where the content is enumerable. If you can count the items, list them.
- **Tables over prose** where the content is comparative. If there are two or more attributes across two or more subjects, tabulate.
- **No nested parentheses.** If a parenthetical needs a parenthetical, the sentence is wrong.
- **Vary rhythm deliberately.** Mix short sentences (5–10 words) with medium ones (15–25 words). A paragraph of uniform-length sentences is machine-shaped (see O4). No paragraph should have more than two sentences of the same length in a row.
- **Rule of three is not a rule.** If the content has two items, list two. If it has four, list four. Forcing three items into every list is an AI tell (see C10.2).
- **Do not cycle synonyms.** The controlled vocabulary (C2) exists precisely so that the same concept uses the same word. If you find yourself reaching for a synonym, you are violating C2, not improving the prose.

### C2. Terminology

The book uses a **controlled vocabulary**. Terms in the table below are used exactly as defined, everywhere, every time. Synonyms are forbidden in normative text.

| Term | Definition | Forbidden synonyms |
|---|---|---|
| **Fabric** | The shared platform substrate serving multiple use cases | platform (when meaning fabric), infrastructure |
| **Use case** | A single agentic application built on the fabric | agent (when meaning use case), solution |
| **Agent** | A runtime instance executing a persona | bot, assistant (unless citing an external product) |
| **Persona** | The dynamic configuration (prompt, model, tools) of an agent | role, character |
| **Archetype** | The static security boundary a persona executes within | class, template, type |
| **Structural layer** | One of the four runtime layers (E, T, C, L) | runtime layer, core layer |
| **Control plane** | One of the eight cross-cutting planes (Identity, Gateway, Observability, Verification, Governance, FinOps, Data Protection, Interoperability) | cross-cutting concern, management plane |
| **Tenant** | The isolation unit (workspace, org, use case, business unit) | customer (unless meaning external customer), account |
| **Harness** | The host runtime that owns the event loop, step limits, checkpoints, and policy hooks | loop, orchestrator |
| **Trajectory** | The full sequence of reasoning, tool calls, observations, and outputs for one run | trace (unless meaning OTel trace), execution |
| **Behavioural assertion** | A discrete, observable expected action | test (when meaning assertion), check |

**Controlled vocabulary overrides unslop.** Terms in this table are used exactly as defined. Unslop's jargon list (C10.6) does not apply to these terms when they are used in their defined sense. "Harness" is the book's name for the host runtime; it is not jargon. "Substrate" is the book's name for the tenant isolation layer; it is not jargon. Authors who are tempted to replace these with "base" or "runtime" are violating the controlled vocabulary, not removing slop.

### C3. Grammar and Mechanics (Extended)

| Rule | Standard |
|---|---|
| **Voice** | Active by default. Passive only when the actor is unknown or irrelevant. |
| **Person** | Second person for directives ("you choose"), first plural for shared reasoning ("we can see"), third person for mechanisms. |
| **Tense** | Present for facts, defaults, and mechanisms. Past for narrative scenes. Future only for consequences. |
| **Contractions** | Permitted in Parts I–II and V. Forbidden in Parts IV, VI, VII, VIII. |
| **Serial comma** | Always (Oxford comma). |
| **Em dash** | Spaced ( — ), not unspaced (—). |
| **Em dash frequency** | No more than two per page (see O5). Three or more in a paragraph is a tell. |
| **Colon usage** | Colons are for lists and examples only. A colon as a mid-sentence connector ("If you're coming from traditional automation: instead of...") is forbidden. |
| **Ellipsis** | Forbidden in prose. |
| **Exclamation marks** | Forbidden everywhere. |
| **Semicolons** | Permitted; preferred over comma splices. |
| **Curly quotes** | Straight quotes only (""). Curly quotes ("" "") are an AI tell. |
| **Adverbs** | Cut every adverb that props up a weak verb. "Runs quickly" becomes "is fast" or the number. "Significantly improves" becomes the measured delta. |

### C4. Numbers, Units, Dates, Currency

| Category | Convention | Example |
|---|---|---|
| Numbers 0–9 | Spelled out | "three layers" |
| Numbers 10+ | Numerals | "12 control planes" |
| Units | SI, with a space between value and unit | "200 ms", "4 GiB" |
| Percentages | Numeral + % | "26% of calls" |
| Dates | ISO 8601 in tables and code; "14 March 2026" in prose | `2026-03-14` / "14 March 2026" |
| Currency | ISO 4217 code + numeral, no decimals in prose | "USD 1.2M", "GBP 450K" |
| Ranges | En dash, no spaces | "10–15 minutes" |
| Ordinals | Numerals with suffix above tenth | "1st", "12th", "21st" |

### C5. Product, Protocol, and Standard Names

- **First mention:** full name with acronym in parentheses. "Model Context Protocol (MCP)."
- **Subsequent mentions:** acronym only. "MCP."
- **Version pinning:** mandatory for protocols. "MCP 2026-07-28", "A2A v1.0". Never "the latest MCP".
- **Product names:** exact vendor casing. "Kubernetes", "PostgreSQL", "Google Cloud", "Amazon Web Services".
- **Standard names:** exact standard naming. "OWASP Top 10 for Agentic Applications (ASI01–ASI10)", "NIST AI 100-2 E2025".
- **No product placement:** no product is named as "recommended". Products appear in examples and in the technology decision matrix, never as endorsements.

### C6. Capitalisation

| Category | Convention |
|---|---|
| Chapter titles | Title case |
| Section headings | Sentence case |
| Table headers | Sentence case, bold |
| Diagram labels | Sentence case, except proper nouns and protocol names |
| Terms in the controlled vocabulary | Capitalised only when referring to the named concept (e.g., "the Identity Control Plane", but "identity enforcement") |

**Exception:** Chapter titles use title case. This is not a title-case tell because it is a deliberate structural convention for the chapter, not a stylistic tic applied across the book. Section headings remain sentence case (see SD-017).

### C7. Hedging, Confidence, and Evidence

The book distinguishes **three levels of claim**, each with a required form.

| Level | Form | Required evidence | Example |
|---|---|---|---|
| **Default** | "Default to X." | A cited standard, a measured pattern, or a named production example | "Default to pooled compute with isolated data. This is the pattern documented in the 2026 multi-tenant agent literature." |
| **Recommendation** | "Recommend X when Y." | A trade-off analysis | "Recommend hard isolation when the data class is regulated. It costs approximately 3× the pooled model in compute but removes the shared-tenancy threat class." |
| **Observation** | "X is observed in Y." | A named source or pattern | "Uber runs 800+ MCP servers behind a single gateway. The pattern is a dual-plane design: registry as control plane, proxy as data plane." |

Forbidden constructions: "best practice", "industry standard", "well known", "obviously", "clearly", "simply", "just", "it goes without saying". If a claim needs one of these, it needs evidence instead.

### C8. Person and Tense

- **Parts I–II:** second person and first plural. "You are designing a fabric. We will walk through four decisions."
- **Part III:** third person. "The gateway control plane enforces five things."
- **Part IV:** second person imperative. "Choose pooled when… Choose isolated when…"
- **Part V:** third person narrative past ("The team met on a Tuesday…"), then second person analytical present ("You now have a revised Stage 2 record.")
- **Parts VI–VIII:** imperative. "Record the decision. Attach the artefact. Schedule the review."

### C9. Inclusive and Global English

- **No idioms** that depend on a specific culture. "Move the needle" → "improve the metric". "Ballpark" → "approximate".
- **No sports, military, or religious metaphors.** Architecture metaphors should be drawn from construction, biology, or logistics.
- **Gender-neutral by default.** "The architect", "they", "the team".
- **No ableist language.** "Blind spot" → "unexamined area". "Sanity check" → "consistency check".
- **No violent language.** "Kill switch" is retained as a named industry term; "kill the process" becomes "terminate the process".

### C10. Forbidden Words and Phrases (Replaced — Six Subsections)

The forbidden words table is the book's most-used editorial tool. It is organised into six subsections, each targeting a distinct class of AI tell. Authors check every paragraph against all six.

#### C10.1 Content tells

| Forbidden | Replacement |
|---|---|
| pivotal moment / testament to / evolving landscape / setting the stage for / indelible mark / deeply rooted | (state what happened) |
| highlighting / ensuring / reflecting / showcasing / fostering (as sentence-opening -ing phrases) | (delete; or expand with the actual evidence) |
| nestled / vibrant / breathtaking / groundbreaking / renowned / stunning / must-visit | (use neutral description) |
| Experts believe / Industry reports suggest / Some critics argue | (name the source or delete) |
| Despite challenges, [X] continues to thrive | (name the specific challenge and the specific response) |

#### C10.2 Language tells

| Forbidden | Replacement |
|---|---|
| additionally / crucial / delve / enduring / enhance / garner / interplay / intricate / landscape (abstract) / pivotal / showcase / tapestry (abstract) / testament / underscore / vibrant | (use the plain word) |
| serves as / stands as / boasts / features (as fancy ways to say "is" or "has") | is / has |
| "Not just X, but Y" | (state the point directly) |
| Rule of three (forcing three items into every list) | (use the natural number) |
| Synonym cycling (protagonist / main character / central figure in one paragraph) | (pick one, repeat it) |
| False ranges ("from X to Y" where X and Y are not on a scale) | (list the topics directly) |
| facilitate | help |
| numerous | many |
| in the event that | if |
| utilize | use |
| leverage (as a verb) | use |

#### C10.3 Style tells

| Forbidden | Replacement |
|---|---|
| Reflexive em dash (three or more per page) | (rewrite one as a period) |
| Colon as mid-sentence connector | (end the sentence; the colon is for lists and examples only) |
| Boldface on every proper noun or acronym | (bold only defined terms on first use) |
| Inline-header list where the bold label restates the line ("**Performance:** Performance improved...") | (convert to prose, or use a bold lead-in that names the item and is followed by *new* detail) |
| Decorative emojis | (delete) |
| Curly quotes (" ") | Straight quotes (" ") |

**Exception:** Chapter titles use title case (C6). This is not a title-case tell because it is a deliberate structural convention for the chapter, not a stylistic tic applied across the book.

#### C10.4 Communication artifacts

| Forbidden | Replacement |
|---|---|
| "I hope this helps!" / "Let me know if..." / "Of course!" / "Certainly!" / "Found the smoking gun!" | (delete) |
| "While specific details are limited..." | (find the source or delete the claim) |
| "Great question!" / "You're absolutely right!" | (respond directly) |

#### C10.5 Filler and hedging

| Forbidden | Replacement |
|---|---|
| In order to | To |
| Due to the fact that | Because |
| It is important to note that | (delete) |
| could potentially possibly be argued that it might | may |
| The future looks bright | (state the specific plan or fact) |
| Significantly improves | (state the measured delta) |
| Runs quickly | (state the number) |

#### C10.6 Abstract metaphor nouns

The following nouns are forbidden when used as abstract metaphors. They are permitted when they are defined terms in the book's controlled vocabulary (C2).

| Forbidden as metaphor | Replacement | Permitted as controlled vocabulary |
|---|---|---|
| substrate | base | **Yes** — "tenant substrate" is the book's name for the isolation layer |
| wedge | add | No |
| vector | way, method | No |
| locus | point | No |
| vantage | point of view | No |
| nexus | centre | No |
| primitive (as noun) | building block | No |
| harness | (the mechanism's real name) | **Yes** — defined in C2 as the host runtime |
| surface (as in "API surface") | API | No |
| bedrock | base | No |
| scaffolding | setup | No |
| modality | type, form | No |
| paradigm | model, approach | No |
| gold-plating | more than the job needs | No |
| ratchet | (the mechanism's real name) or "a limit that only tightens" | No |
| evacuate (for moving code) | move out | No |
| endgame | the last phase | No |
| north star | goal | No |
| flywheel | (the mechanism's real name) | No |

---

## Part D — Depth Calibration

### D1. Depth by Part

Depth is not a single dial. It is calibrated per part to match the reader's cognitive mode.

| Part | Depth target | What "in depth" means here |
|---|---|---|
| **I — Orientation** | Conceptual | Enough depth to change the reader's mental model. No mechanisms. No configuration. |
| **II — Strategy** | Decision-level | Each decision explained through its trade-offs, not through its implementation. The reader should be able to defend the decision to a board. |
| **III — Architecture** | Mechanism-level | Every layer and control plane explained with its purpose, components, failure modes, scaling signals, and anti-patterns. Implementation-agnostic. |
| **IV — Decisions** | One page | No more depth than fits on one page per decision. If it does not fit, it is not one decision. |
| **V — Lifecycle** | Procedural | Each stage with entry criteria, activities, artefacts, exit criteria. |
| **VI — Operating Model** | Operational | Each function with its RACI, its SLO, and its incident class. |
| **VII — Playbooks** | Step-by-step | Each step executable without consulting another chapter. |
| **VIII — Reference** | Lookup | Each entry self-contained, cross-referenced, and short. |

### D2. Depth by Chapter Type

| Chapter type | Depth ceiling | Depth floor |
|---|---|---|
| Layer chapter (Part III) | 15 pages | 8 pages |
| Control plane chapter (Part III) | 12 pages | 6 pages |
| Decision page (Part IV) | 1 page | 1 page (non-negotiable) |
| Lifecycle stage (Part V) | 8 pages | 4 pages |
| Operating model chapter (Part VI) | 12 pages | 6 pages |
| Playbook (Part VII) | 10 pages | 5 pages |
| Reference entry (Part VIII) | 2 pages | 200 words |

### D3. The Rule of Necessary Depth

Depth is justified only when it changes the reader's action. If a paragraph does not:

- change a decision,
- enable an implementation,
- prevent a failure, or
- resolve a confusion,

it is cut. The editor enforces this rule without exception.

---

## Part E — Chapter Architecture

### E1. Standard Chapter Template

Every chapter in Parts III–VI follows this template.

| Section | Purpose | Length |
|---|---|---|
| **Opening hook** | One paragraph or one short scene that establishes why this chapter matters | 50–150 words |
| **What this chapter decides** | A one-sentence framing of the decision or mechanism the chapter addresses | 1 sentence |
| **The mechanism** | The architecture, the pattern, or the process explained | 60–70% of chapter |
| **Failure modes** | What breaks, and why | 10% |
| **Anti-patterns** | What not to do, with the reason | 10% |
| **Decisions to make** | A bulleted list of decisions the reader must record | 3–7 bullets |
| **Default positions** | The recommended default for each decision | 3–7 bullets |
| **Artefacts to produce** | The documents, configurations, or records the chapter produces | 1–5 items |
| **Cross-references** | "See also" links to related chapters and templates | 2–5 links |

### E2. Chapter Lengths

| Part | Target chapter length | Target part length |
|---|---|---|
| I | 8–12 pages | 40 pages |
| II | 10–15 pages | 60 pages |
| III | 8–15 pages | 100 pages |
| IV | 1 page per decision, ~25 decisions | 30 pages |
| V | 4–8 pages per stage | 60 pages |
| VI | 6–12 pages per chapter | 60 pages |
| VII | 5–10 pages per playbook | 80 pages |
| VIII | Variable | 60 pages |

Total target: **~490 pages** including front matter, index, and appendices.

### E3. Chapter Openings

Permitted opening patterns:

1. **Scene.** A short vignette from the Meridian Financial running scenario. Used in Parts I–II and V.
2. **Failure.** A concrete failure that the chapter will teach the reader to prevent. Used in Part III.
3. **Decision.** A direct statement of the decision the chapter addresses. Used in Part IV.
4. **Mechanism.** A one-sentence statement of how the mechanism works. Used in Part III control plane chapters.

Forbidden opening patterns: dictionary definitions, historical trivia, quotations from famous people, rhetorical questions.

### E4. Chapter Closings

Every chapter closes with three mandatory blocks, in this order:

1. **"Decisions to make"** — bulleted list.
2. **"Defaults"** — bulleted list, matched one-to-one to decisions.
3. **"Artefacts to produce"** — bulleted list with the file name or record name the reader must create.

Then, and only then, a **"See also"** block with cross-references.

### E5. Narrative Dosing

Narrative is dosed, not dominant. The ratio is fixed per part and is non-negotiable without an SD entry.

| Part | Narrative allocation | Where it appears | Maximum narrative length |
|---|---|---|---|
| **I — Orientation** | 40% narrative, 60% reference | Opening scene per chapter, then analytical prose | 400 words per chapter |
| **II — Strategy** | 30% narrative, 70% reference | Opening scene per chapter, then decision analysis | 300 words per chapter |
| **III — Architecture** | 5% narrative, 95% reference | Opening hook only (E3, pattern 2). No narrative in the body. | 150 words per chapter |
| **IV — Decisions** | 0% narrative | None. The decision template is the chapter. | 0 words |
| **V — Lifecycle** | 50% narrative, 50% reference | Opening scene per stage, then procedural reference, then closing scene | 600 words per stage |
| **VI — Operating Model** | 10% narrative, 90% reference | Occasional war story in the opening hook | 200 words per chapter |
| **VII — Playbooks** | 25% narrative, 75% procedural | War story per playbook (F5) | 300 words per playbook |
| **VIII — Reference** | 0% narrative | None. | 0 words |

**The narrative drift rule:** If a narrative section exceeds its maximum length, it is not a vignette — it is a scene, and scenes belong in the companion novel (A4). The editor enforces the ceiling without exception.

**The register transition mechanism:** Every transition from narrative to reference is signalled in three ways:

1. **Visual:** the narrative appears in the War Story callout box (G4). The reference appears in standard typography.
2. **Structural:** the narrative ends with a sentence that names the decision or mechanism the reference will explain.
3. **Typographic:** the first reference paragraph after a narrative section begins with a bold lead-in ("**The mechanism.**") that re-establishes the register.

---

## Part F — Content Templates

Templates are the book's operating system. Every template must be reproduced identically every time it appears. Consistency is a form of respect for the reference reader.

### F1. Decision Template (Part IV)

```
### D-XX: [Decision name]

**Context.** One paragraph. What problem does this decision solve?
**Default.** One sentence. The recommended position.
**Why.** Two to four sentences. The evidence, the principle, or the measured pattern.
**Trade-off.** One sentence in the form "This buys X at the cost of Y."
**When to deviate.** Two to four bullets. The conditions under which the default is wrong.
**Reversibility.** One-way door / Two-way door.
**Artefact.** The document, record, or configuration this decision produces.
**See also.** Cross-references.
```

One page maximum. No exceptions.

### F2. Playbook Template (Part VII)

```
## P-X: [Playbook name]

**When to use.** One paragraph. The situation that triggers this playbook.
**Preconditions.** Bulleted list. What must be true before starting.
**War story.** 150–300 words. A short scene of a team facing this situation.
**Steps.** Numbered, each with:
  - Action
  - Owner
  - Input
  - Output
  - Time
**Failure modes.** Bulleted list. What goes wrong at each step.
**The artefact you now have.** Bulleted list.
**The decision you must record.** One sentence.
```

### F3. Checklist Template (Part VIII)

```
### C-X: [Layer or control plane] checklist

| # | Question | Why it matters |
|---|---|---|
| 1 | [Yes/no question] | [One sentence] |
| 2 | … | … |
```

Every question is answerable with evidence. If a question cannot be evidenced, it is not a checklist item.

### F4. Anti-Pattern Template (Chapter 18)

```
### AP-XX: [Anti-pattern name]

**What it looks like.** One sentence.
**Why it happens.** One sentence.
**Why it fails.** One sentence.
**The correct pattern.** One sentence with a cross-reference.
**Detection signal.** One metric or observation that reveals it.
```

### F5. War Story Template (Part VII)

```
**War story.** [Name], the platform lead at [Meridian], received the call on a Friday afternoon. [One sentence establishing the stakes.] [Two to three sentences showing the action taken.] [One sentence showing the outcome.] [One sentence connecting the story to the playbook that follows.]
```

War stories are 150–300 words. They are written in past tense, third person, and they always end with a connection to the playbook.

### F6. Layer Chapter Template (Part III structural core)

```
## Chapter N: [Layer name]

[Opening hook — a failure scene.]

### What this layer decides
[One sentence.]

### The mechanism
[The layer's components, in a table, with one paragraph per component group.]

### The interface with adjacent layers
[One paragraph per adjacent layer, naming the boundary and the contract.]

### Failure modes
[Table: failure, cause, symptom, control.]

### Scaling signal
[The metric that drives autoscaling, with the threshold.]

### Anti-patterns
[Two to four anti-patterns using the F4 template.]

### Decisions to make
[Bulleted.]

### Defaults
[Bulleted, matched.]

### Artefacts to produce
[Bulleted.]

### See also
[Cross-references.]
```

### F7. Control Plane Chapter Template (Part III control planes)

Same as F6, with three substitutions:

- "Scaling signal" becomes **"Enforcement point"** — where the control plane intercepts the runtime path.
- "Interface with adjacent layers" becomes **"Threat coverage"** — which OWASP ASI categories and which trust-chain links this control plane secures.
- Add a new section, **"Evidence artefact"** — what the control plane emits that proves it is working.

### F8. ADR Template (used within the book as an example artefact)

```
# ADR-XXX: [Title]

**Status.** Proposed / Accepted / Superseded
**Date.** YYYY-MM-DD
**Decision makers.** [Roles]

## Context
[One paragraph.]

## Options
1. [Option A] — [one-sentence summary]
2. [Option B] — [one-sentence summary]
3. [Option C] — [one-sentence summary]

## Decision
[One paragraph.]

## Consequences
- Positive: [bulleted]
- Negative: [bulleted]
- Neutral: [bulleted]

## Reversibility
[One-way door / Two-way door, with rationale.]
```

### F9. Glossary Entry Template (Chapter 30)

```
**Term.** [Definition in one sentence.] [Context in one to two sentences.] See [chapter] for [the decision or mechanism it appears in].
```

Every glossary term must also appear in a chapter, a decision, or a checklist. No orphan terms.

### F10. Protocol Entry Template (Chapter 14)

```
### [Protocol name and version]

**What it is.** One sentence.
**What boundary it addresses.** One sentence naming the layer or plane.
**What it replaces or complements.** One sentence.
**The 2026 state.** Two to three sentences on the current specification, with the date.
**What it does not do.** One to three sentences on the boundary.
**Decision.** A cross-reference to the relevant decision in Part IV.
```

### F11. Standards Map Entry Template (Chapter 29)

```
| Standard | Version | What it covers | Where this book addresses it |
|---|---|---|---|
| OWASP ASI01–ASI10 | 2025-12 | Agentic threat taxonomy | Ch. 15, Ch. 18 |
```

---

## Part G — Visual Style

### G1. Page Layout and Grid

| Property | Specification |
|---|---|
| Trim size | 7.5 × 9.25 in (O'Reilly standard) |
| Margins | 0.75 in top, 0.75 in bottom, 0.9 in inside, 0.7 in outside |
| Text column | Single column |
| Body type size | 10.5 pt |
| Line height | 14 pt (1.33×) |
| Baseline grid | 14 pt |
| Running head | Chapter title (left), book title (right) |
| Folio | Outside bottom corner |
| Callout column | Full width, boxed, indented 0.25 in each side |

### G2. Typography

| Element | Typeface | Weight | Size | Colour |
|---|---|---|---|---|
| Body | Source Serif 4 | Regular | 10.5/14 | #1A1A1A |
| Chapter title | Source Sans 3 | Bold | 28/32 | #0B2545 |
| Section heading (H1) | Source Sans 3 | Semibold | 18/22 | #0B2545 |
| Subsection heading (H2) | Source Sans 3 | Semibold | 14/18 | #13315C |
| Table header | Source Sans 3 | Bold | 9/12 | #FFFFFF on #13315C |
| Table body | Source Sans 3 | Regular | 9/12 | #1A1A1A |
| Code (inline) | JetBrains Mono | Regular | 9/13 | #1A1A1A on #F4F4F0 |
| Code (block) | JetBrains Mono | Regular | 8.5/12 | #1A1A1A on #F4F4F0 |
| Caption | Source Sans 3 | Italic | 8.5/11 | #4A4A4A |
| Footnote | Source Serif 4 | Regular | 8/10 | #4A4A4A |

Both typefaces are open-licensed (SIL OFL). No proprietary typefaces anywhere in the book.

**Boldface discipline (see C10.3):** Bold is used only for (a) defined terms on first use, (b) table headers, and (c) the six callout-type labels. Bold is not used on every proper noun, acronym, or noun phrase. When in doubt, do not bold.

### G3. Colour Palette

The book uses a single, colour-blind-safe palette with five roles. Every colour has a greyscale equivalent and a pattern fallback for print.

| Role | Hex | Greyscale | Pattern fallback | Use |
|---|---|---|---|---|
| **Primary** | `#0B2545` | 15% grey | Solid | Structural core, headings, primary diagrams |
| **Secondary** | `#13315C` | 25% grey | Solid | Secondary structure, table headers |
| **Accent A (defaults)** | `#F2A541` | 60% grey | Diagonal hatch | Decision defaults, recommended paths |
| **Accent B (control planes)** | `#2A9D8F` | 45% grey | Cross-hatch | Control planes, enforcement points |
| **Accent C (anti-patterns)** | `#E76F51` | 55% grey | Dotted | Warnings, anti-patterns, failure modes |
| **Neutral light** | `#F4F4F0` | 96% grey | None | Code blocks, callout backgrounds |
| **Neutral mid** | `#4A4A4A` | 70% grey | None | Captions, secondary text |
| **Neutral dark** | `#1A1A1A` | 90% grey | None | Body text |

Forbidden: gradient fills, drop shadows, bevels, 3D effects, photographic textures.

### G4. Callout and Box Styles

Six callout types, each with a fixed visual treatment.

| Callout | Border | Background | Icon | Used for |
|---|---|---|---|---|
| **Decision** | Left bar 4 pt, `#F2A541` | `#FFF8EC` | ◆ | Defaults, recommendations |
| **Warning** | Left bar 4 pt, `#E76F51` | `#FDF0EC` | ▲ | Anti-patterns, failure modes |
| **Evidence** | Left bar 4 pt, `#2A9D8F` | `#EAF5F3` | ● | Cited standards, measured patterns |
| **Definition** | Top and bottom rule 1 pt, `#13315C` | None | None | Controlled vocabulary terms |
| **War story** | Full box 0.5 pt, `#4A4A4A` | `#F4F4F0` | None | Narrative vignettes |
| **Artefact** | Dashed box 0.75 pt, `#0B2545` | None | ⬚ | Documents and records to produce |

Icons are rendered in Source Sans 3 glyphs or as simple geometric shapes. No illustrated icons, no emoji.

### G5. Iconography

The book uses **six icons only**, all geometric:

| Icon | Meaning |
|---|---|
| ◆ | Decision / default |
| ▲ | Warning / anti-pattern |
| ● | Evidence / standard |
| ⬚ | Artefact |
| → | Cross-reference |
| ◇ | Open question |

Forbidden: any icon that requires interpretation. If an icon is not on this list, it does not appear.

### G6. Tables and Matrices

Tables are the book's primary analytical tool. They follow a fixed format.

| Rule | Specification |
|---|---|
| Header row | Bold, `#13315C` background, white text |
| Body rows | Alternating `#FFFFFF` and `#F4F4F0` |
| Borders | Horizontal 0.5 pt only. No vertical borders. |
| Column alignment | Text left, numbers right, symbols centre |
| Max columns | 8 |
| Max rows per table before splitting | 20 |
| Caption | Above the table, "Table N-X: [title]" in italic |
| Footnote | Below the table, "Source: [reference]" |
| Empty cell | En dash (–), never blank |

Matrices (heatmaps, RACI, decision maps) use the colour palette's greyscale equivalents, with symbols (`●`, `◐`, `○`, `–`) as the primary encoding. Colour is redundant, never primary.

**Inline-header list rule (see C10.3):** A bold lead-in that restates the line ("**Performance:** Performance improved...") is a tell. Convert to prose. A bold lead-in that names the item and is followed by *new* detail ("**Schema in TypeScript.** Tables live in one file.") is permitted.

### G7. Code and Configuration Formatting

| Rule | Specification |
|---|---|
| Language tag | Mandatory on every code block |
| Line length | 80 characters maximum |
| Line numbers | Included only when referenced in prose |
| Comments | Sparse, English, explaining *why* not *what* |
| Placeholder values | `<angle-brackets>`, never `YOUR_VALUE_HERE` |
| Secrets | Never. Use `<redacted>` in every example. |
| Long lines | Wrapped with `↩` marker, not truncated |

---

## Part H — Diagram Style

### H1. Diagram Taxonomy

The book uses **eight diagram types only**. Each has a fixed purpose and a fixed notation.

| Type | Purpose | Used in |
|---|---|---|
| **Context diagram** | Show the fabric in its environment | Chapters 3, 13 |
| **Container diagram** | Show the fabric's major containers (C4 level 2) | Chapters 10–12 |
| **Component diagram** | Show the components within one container (C4 level 3) | Layer chapters (Part III) |
| **Sequence diagram** | Show a runtime flow across components | Layers 6–8, Chapter 15 |
| **Trust boundary diagram** | Show where trust changes hands | Chapter 15, Chapter 11 |
| **State machine** | Show lifecycle states and transitions | Part V |
| **Layer stack** | Show the structural core and control planes | Chapter 10, Chapter 11 |
| **Decision tree** | Show branching logic for a decision | Part IV, selected decisions |

Diagrams not on this list require editor approval and a documented reason.

### H2. Universal Diagram Conventions

| Convention | Specification |
|---|---|
| **One idea per diagram** | If a diagram needs two sentences to explain, it is two diagrams. |
| **Maximum elements** | 12 nodes, 20 edges. Anything larger is split. |
| **Direction** | Top-to-bottom for layering, left-to-right for flow, radial only for context. |
| **Labels** | Every node and edge is labelled. No unlabelled arrows. |
| **Legend** | Every diagram with more than four element types carries a legend. |
| **Title and ID** | Every diagram has a title and a figure ID ("Figure N-X"). |
| **Caption** | Every diagram has a one-sentence caption below it. |
| **Source note** | If adapted from a source, the source is cited in the caption. |
| **Alt text** | Every diagram has a 2–3 sentence alt text for accessibility. |
| **Greyscale test** | Every diagram must be legible in greyscale. |
| **Version** | Every diagram is versioned; the version appears in the caption. |

### H3. Notation

The book uses a **restricted notation**, compatible with C4 and readable without C4 expertise.

| Element | Shape | Border | Fill |
|---|---|---|---|
| **Person / actor** | Rounded rectangle | 1 pt solid | White |
| **System (fabric)** | Rectangle with bold top bar | 1 pt solid, 3 pt top bar | White |
| **Container** | Rectangle | 1 pt solid | Light grey `#F4F4F0` |
| **Component** | Rectangle | 0.75 pt solid | White |
| **Structural layer** | Stacked rectangle | 1 pt solid | Primary or secondary |
| **Control plane** | Hexagon | 1 pt solid | Accent B |
| **External system** | Rectangle, dashed border | 1 pt dashed | White |
| **Data store** | Cylinder | 1 pt solid | Light grey |
| **Queue / event bus** | Rectangle with one rounded end | 1 pt solid | Light grey |
| **Trust boundary** | Dashed rounded rectangle | 1.5 pt dashed | None |
| **Flow (synchronous)** | Solid arrow, filled head | 1 pt | — |
| **Flow (asynchronous)** | Dashed arrow, open head | 1 pt | — |
| **Flow (data)** | Solid arrow, open head, labelled with data class | 1 pt | — |

Forbidden: cloud shapes, server clip-art, stick figures, 3D boxes, shadows.

### H4. Colour-Blind Safe Palette for Diagrams

Diagrams use a **restricted palette** that works in greyscale and for all common colour-blindness types.

| Element class | Colour | Greyscale | Pattern |
|---|---|---|---|
| Structural core | `#0B2545` | 15% grey | Solid |
| Control planes | `#2A9D8F` | 45% grey | Cross-hatch |
| Defaults / recommended | `#F2A541` | 60% grey | Diagonal hatch |
| Anti-patterns / warnings | `#E76F51` | 55% grey | Dotted |
| External | `#4A4A4A` | 70% grey | Solid, thin |
| Neutral fill | `#F4F4F0` | 96% grey | None |

Every diagram is **redrawn or verified** in greyscale before publication. Colour is always redundant with shape, label, or pattern.

### H5. Label Rules

| Rule | Specification |
|---|---|
| Label case | Sentence case, except protocol and product names |
| Label length | 4 words maximum per node label; details in caption or legend |
| Edge labels | Verb phrases ("reads", "invokes", "publishes to") |
| Acronyms | Expanded on first use in the diagram, or in the legend |
| Numbers | Only when they carry meaning (e.g., "3 replicas", "≤ 200 ms") |
| Units | Always with the value ("200 ms", not "200") |

### H6. Tooling

| Diagram type | Tool | Output format |
|---|---|---|
| Context, container, component | Excalidraw (hand-drawn) or draw.io (structured) | SVG, 2× PNG |
| Sequence, state machine | Mermaid | SVG |
| Layer stack, decision tree | Excalidraw | SVG |
| Trust boundary | draw.io | SVG |

All diagrams are stored as source files in the book's repository and exported as SVG. Raster exports are used only for the print edition, at 300 dpi.

### H7. Accessibility

- Every diagram has alt text of 2–3 sentences, describing what the diagram shows and what the reader should take from it.
- Every diagram's information is also expressed in prose or in a table. The diagram is never the only place a fact lives.
- Contrast ratio between text and fill is minimum 4.5:1.
- No information is encoded by colour alone.

### H8. Diagram Anti-Patterns

| Anti-pattern | Why it fails | Correct pattern |
|---|---|---|
| The "everything" diagram | 40 nodes, unreadable, useless | Split into context, container, and component views |
| The unlabelled arrow | The reader cannot tell what flows | Label every edge with a verb |
| The mystery box | A node labelled "AI" or "ML" | Name the specific component |
| The 3D cloud | Decoration, not information | A rectangle with a border |
| The colour-only legend | Fails for colour-blind readers and in greyscale | Colour plus shape plus label |
| The vendor logo | Implies endorsement, ages badly | Named text labels |
| The screenshot | Unmaintainable, breaks on update | Redrawn diagram with source file |
| The architecture astronaut | So abstract it says nothing | One idea per diagram, maximum 12 nodes |

---

## Part I — Cross-References and Navigation

### I1. Internal Referencing

| Rule | Specification |
|---|---|
| Chapter reference | "Chapter N" (never "see above" or "see below") |
| Section reference | "Chapter N, section N.N" |
| Figure reference | "Figure N-X" |
| Table reference | "Table N-X" |
| Decision reference | "Decision D-XX" |
| Playbook reference | "Playbook P-X" |
| Checklist reference | "Checklist C-X" |

### I2. "See Also" Convention

Every chapter ends with a "See also" block containing 2–5 cross-references, each in the form:

```
→ Chapter N, [title] — [one-sentence reason for the reference]
```

### I3. Chapter Dependency Map

A single dependency map appears in the front matter (Figure 0-1) showing which chapters can be read independently, which have prerequisites, and which are reference-only. The map is also reproduced in the companion site.

### I4. Indexing

The index is exhaustive for the controlled vocabulary, protocol names, standards, and pattern names. It is **not** exhaustive for common words. Index entries are generated by the editor, not the author.

---

## Part J — Examples and Case Studies

### J1. The Meridian Financial Running Scenario

The book uses a single fictional organisation, **Meridian Financial**, as the through-line narrative.

| Attribute | Specification |
|---|---|
| **Name** | Meridian Financial |
| **Size** | 12,000 employees, 3 business units (retail banking, insurance, wealth management) |
| **Regulatory posture** | UK-regulated, FCA and PRA, GDPR-scoped, moderate risk appetite |
| **Fabric maturity at the start** | Four fragmented single-agent pilots, no shared substrate |
| **Fabric maturity at the end** | A shared fabric serving 12 use cases, 3 tenant types, 1 external SaaS pilot |
| **Characters** | A platform lead, a security architect, a sponsor, a domain team lead, an SRE. All composites. |
| **Ethics** | No real organisation is depicted. All names, numbers, and incidents are fictional. Any resemblance is coincidental and disclaimed in the front matter. |

### J2. Composites and Ethics

- Every character is a composite of multiple practitioners. No character is a portrait of a real person.
- Every incident is a synthesis of multiple public or anonymised incidents. No incident is a single-source reproduction.
- No vendor is disparaged or endorsed in a scenario.
- No regulator is described as acting outside its published remit.

### J3. Anonymisation Rules

When a scenario draws on a real production pattern, the source is cited in a footnote in general terms ("a large European bank", "a hyperscale provider") unless the source has published the pattern publicly (in which case the source is named).

### J4. Worked Examples

Every worked example follows this format:

```
**Example N-X.** [Situation.] [Decision.] [Outcome.] [Lesson.]
```

Worked examples are 100–200 words. They are not case studies; they are illustrations of one mechanism or one decision.

### J5. The Narrative Quality Bar

Narrative sections in this book are **vignettes, not scenes**. They exist to create recognition — the reader should think "I have been in that meeting" — not to entertain. The quality bar is therefore different from the reference bar, and both must be met independently.

**What a good vignette does:**

| Requirement | Standard | Example |
|---|---|---|
| **Situational clarity** | The reader understands the stakes within two sentences | "The CISO called at 4:47 on a Friday. One agent had sent a customer statement to an external endpoint." |
| **Recognition** | The situation is one the reader has plausibly experienced or feared | A governance meeting where nobody can answer "who approved this tool?" |
| **Consequence** | The vignette shows what happens when a decision is *not* made | The breach that a gateway would have prevented |
| **Artefact connection** | The vignette ends by naming the decision or artefact it motivates | "That was the week they started building the gateway." |

**What a good vignette does not do:**

| Prohibition | Reason |
|---|---|
| More than three named characters | Vignettes trade character depth for situational clarity. Three is the maximum the reader can track without the vignette becoming a scene. |
| Dialogue longer than four exchanges | Dialogue in a reference book reads as screenplay. Use reported speech after the opening exchange. |
| Interiority beyond one sentence per character | The reader does not need to know what the character is feeling. They need to know what the character is *deciding*. |
| Metaphor that requires unpacking | The vignette is not the place for allegory. If a metaphor needs explanation, it belongs in the reference, not the scene. |
| A villain | The Phoenix Project's villain problem is documented. Characters in this book are competent people facing systemic trade-offs, not antagonists. |
| Rhetorical questions | Forbidden in all prose (E3). |

**The reference/narrative boundary test:** After writing a narrative section, ask: "If I removed every technical term, would the reader still understand the decision this section motivates?" If yes, the vignette is doing its job. If no, the vignette is a lecture in disguise.

**Worked example — good vs bad:**

| Bad vignette | Why it fails | Good vignette | Why it works |
|---|---|---|---|
| "Maya sat in the meeting and thought about all the architectural layers she needed to design. The gateway, the identity plane, the observability stack. It was overwhelming." | Interiority, no stakes, lists mechanisms | "Maya had four weeks to answer one question: for any agent call in the last month, who made it, what did it touch, and what was the result? She could not. The gateway was the only way to answer it." | One question, one decision, one artefact |
| "The team argued about whether to build or buy. Some wanted a vendor, others wanted to build. Eventually they decided to build." | No stakes, no consequence, no specificity | "The vendor demo had been impressive until the security architect asked where the audit logs were stored. The vendor's answer — 'in our cloud, under our control' — ended the meeting. The build decision was made in the car park." | Specific detail, specific consequence, specific decision |
| "The CISO was very angry about the security breach. He shouted at the team for an hour about all the things they had done wrong." | Villain, no mechanism, no lesson | "The CISO did not raise his voice. He asked one question: 'which gateway did this call go through?' There was no gateway. The silence lasted longer than the shouting would have." | Restraint, mechanism, recognition |

---

## Part K — Accessibility and Globalisation

### K1. Accessibility

The book must meet **WCAG 2.2 AA** for all digital formats and the **EPUB Accessibility 1.1** specification for the ebook.

| Requirement | Implementation |
|---|---|
| Text contrast | ≥ 4.5:1 |
| Non-text contrast | ≥ 3:1 |
| Alt text | Every figure, table, and diagram |
| Semantic structure | Heading hierarchy in EPUB, ARIA landmarks in HTML |
| Reading order | Verified for screen readers |
| Colour independence | No information by colour alone |
| Font size | User-adjustable in ebook |
| Reflow | Verified in EPUB and HTML |
| Captions | Every figure and table |

### K2. Global English
The book is written in **International English** with British spelling (the primary author's locale), with the following rules:

- Spelling: British (organisation, colour, prioritise).
- Units: SI, with imperial in parentheses only where the imperial figure is the source.
- Dates: ISO 8601 in tables, spelled out in prose.
- Currency: ISO 4217 code with numeral.
- Idioms: forbidden.
- Cultural references: restricted to internationally recognised examples.

The editor runs a **locale-agnostic pass** on every chapter before copyedit.

### K3. Culturally Neutral Examples

- No sports metaphors.
- No military metaphors (except "kill switch", which is retained as a named industry term).
- No religious references.
- No political references.
- No brand-name comparisons.

---

## Part L — Production and Formats

### L1. Print Edition

| Property | Specification |
|---|---|
| Format | Paperback and hardback |
| Paper | 80 gsm cream |
| Binding | Perfect bound |
| Colour | Full colour interiors (justified by the diagram palette) |
| Trim | 7.5 × 9.25 in |
| Extent | ~490 pages |

### L2. Digital Edition

| Property | Specification |
|---|---|
| Format | EPUB 3.3, PDF |
| Reflow | Verified |
| Interactive diagrams | None (static SVG) |
| Code samples | Syntax-highlighted, copyable |
| Cross-references | Hyperlinked |
| Index | Hyperlinked |

### L3. Audio Edition

| Property | Specification |
|---|---|
| Narration | Single narrator, neutral accent |
| Chapters | All chapters except reference material |
| Tables and diagrams | Narrated as a summary; full content available in the digital companion |
| Code | Not narrated; announced as "code sample available in the digital edition" |
| Duration | Estimated 14–18 hours |

### L4. Companion Site

The companion site contains:

- All diagrams as SVG source files.
- All templates as editable documents.
- The Meridian Financial scenario as a standalone narrative for training use.
- Errata and version history.
- A community-contributed anti-patterns list (curated by the editor).

The book is **complete without the companion site**. The site augments, it does not substitute.

---

## Part M — Author Workflow and QA

### M1. Pre-Writing Checklist

Before writing a chapter, the author confirms:

- [ ] The chapter type is identified (F6, F7, or other).
- [ ] The depth target is set (D1, D2).
- [ ] The chapter template is selected (E1).
- [ ] The opening pattern is chosen (E3).
- [ ] The narrative allocation is set (E5).
- [ ] The narrative quality bar is understood (J5).
- [ ] The closing blocks are drafted (E4).
- [ ] The diagrams are sketched and named (H1).
- [ ] The cross-references are identified (I1).
- [ ] The controlled vocabulary terms are listed (C2).
- [ ] The forbidden words table (C10) is reviewed.
- [ ] The four anti-slop tests (O1) are understood.

### M2. Pre-Submission Checklist

Before submitting a chapter, the author confirms:

**Structural**
- [ ] No sentence exceeds 30 words.
- [ ] No paragraph exceeds 6 sentences.
- [ ] Every claim is at Default, Recommendation, or Observation level with evidence (C7).
- [ ] Every protocol is version-pinned (C5).
- [ ] Every table has a caption and source note (G6).
- [ ] Every diagram has a title, caption, alt text, and greyscale test (H2).
- [ ] Every chapter ends with the three mandatory blocks (E4).
- [ ] Every template is reproduced identically (Part F).
- [ ] Narrative sections are within their allocation (E5) and meet the quality bar (J5).
- [ ] Narrative transitions signal the register change (E5).

**Anti-slop pass (new in v1.2)**
- [ ] No forbidden word from C10.1 (content tells) appears.
- [ ] No forbidden word from C10.2 (language tells) appears.
- [ ] No forbidden style pattern from C10.3 (style tells) appears.
- [ ] No forbidden communication artefact from C10.4 appears.
- [ ] No forbidden filler or hedge from C10.5 appears.
- [ ] No forbidden abstract metaphor noun from C10.6 appears, except in the controlled vocabulary (C2).
- [ ] The paragraph rhythm is varied (no more than two same-length sentences in a row).
- [ ] No rule of three is forced; lists use the natural number.
- [ ] No synonym cycling appears within a paragraph.
- [ ] Em dashes appear no more than twice per page and not three times in a paragraph.
- [ ] No colon is used as a mid-sentence connector.
- [ ] No curly quotes; only straight quotes.
- [ ] Every adverb is justified or replaced with a stronger verb.
- [ ] The chapter passes the four anti-slop tests (O1).
- [ ] The chapter passes the "Could this be another book?" test (O3).
- [ ] The chapter passes the "Read it aloud" test (O4).
- [ ] The chapter passes the "Have an opinion" test (O5).

**Locale and accessibility**
- [ ] The chapter passes the locale-agnostic pass (K2).
- [ ] The chapter passes the accessibility pass (K1).

### M3. Editorial Workflow

| Stage | Owner | Output |
|---|---|---|
| 1. Outline | Author | Chapter outline with template selected |
| 2. First draft | Author | Complete draft |
| 3. Self-review | Author | Pass through M2 |
| 4. Structural edit | Editor | Structural feedback |
| 5. Second draft | Author | Revised draft |
| 6. Line edit | Editor | Line-level edit |
| 7. Anti-slop edit | Editor | Part O pass; patterns from C10 removed |
| 8. Copyedit | Copyeditor | Grammar, style, consistency |
| 9. Fact-check | Technical reviewer | Every claim verified |
| 10. Diagram review | Diagrammer | Every diagram verified against H2 |
| 11. Accessibility review | Accessibility editor | K1 verified |
| 12. Production | Typesetter | Final files |

No chapter advances past Stage 6 until M2 is satisfied. No chapter advances past Stage 10 until every diagram passes the greyscale test. No chapter advances past Stage 7 until the anti-slop edit is complete.

---

## Part N — Style Decisions Log

| ID | Decision | Rationale | Date | Reversible? |
|---|---|---|---|---|
| SD-001 | Five voice registers, one per part | A single voice across 490 pages fails the reader at some point | 2026-11 | Two-way |
| SD-002 | British spelling, International English | Primary author locale; global readability | 2026-11 | Two-way |
| SD-003 | Source Serif + Source Sans + JetBrains Mono | Open-licensed, legible, professional | 2026-11 | One-way (locked at production) |
| SD-004 | Five-role colour palette with greyscale and pattern fallback | Accessibility and print integrity | 2026-11 | Two-way |
| SD-005 | Eight diagram types only | Consistency and editor verification | 2026-11 | Two-way |
| SD-006 | One-page decision template, no exceptions | The decision surface is the book's core product | 2026-11 | One-way |
| SD-007 | Meridian Financial as single running scenario | Narrative coherence without repetition | 2026-11 | Two-way |
| SD-008 | No product endorsement, no vendor recommendation | Longevity and credibility | 2026-11 | One-way |
| SD-009 | Every narrative section ends with an artefact | Discipline against narrative drift | 2026-11 | One-way |
| SD-010 | Companion site augments, never substitutes | The book must be complete standalone | 2026-11 | One-way |
| SD-011 | Narrative is dosed (E5), not dominant | The hybrid fails if the narrative outweighs the reference. The architect is the primary reader. | 2026-11 | Two-way |
| SD-012 | Narrative quality bar (J5) is distinct from reference quality bar | Vignettes trade character depth for situational clarity. They are not scenes. | 2026-11 | Two-way |
| SD-013 | The reference book may spawn a companion narrative book (A4) | The two-book strategy is the cleanest answer for serving both audiences. The reference is written first. | 2026-11 | Two-way |
| SD-014 | The restrained narrative register (B4) replaces "Kim (restrained)" | The register must be definable, testable, and teachable. "Restrained" is not. | 2026-11 | Two-way |
| SD-015 | Em dashes are permitted, frequency-limited to two per page | The em dash is a legitimate typographic device in reference prose; the tell is overuse, not the character | 2026-11 | Two-way |
| SD-016 | Controlled vocabulary (C2) overrides unslop's abstract-metaphor list | The book's named concepts ("harness", "substrate") are its product; substituting them with plainer words would break the controlled vocabulary | 2026-11 | Two-way |
| SD-017 | Title case for chapter titles is a structural convention, not a title-case tell | The book uses title case for chapter titles only; section headings remain sentence case | 2026-11 | One-way |

---

## Part O — Anti-Slop Discipline (New in v1.2)

The book must read as though a human wrote it. Not because AI cannot write well, but because the patterns that mark AI-assisted writing are recognisable, and they undermine the book's credibility with the experienced practitioners who are its primary readers. A reader who sees "it's not just a gateway, it's a pivotal moment" will close the book.

This Part defines the philosophy and tests. The mechanical forbidden words list lives in C10. The two are used together: Part O tells the author *what to aim for*, C10 tells the author *what to avoid*.

### O1. The Four Tests

Every paragraph must pass four tests before it advances to the editor.

| Test | Question | Failure mode |
|---|---|---|
| **Specificity** | Does the paragraph say what the mechanism is, what it does, or what breaks without it? | Generic praise, vague attribution, promotional language |
| **Plausibility** | Could a human practitioner have written this sentence, or does it read like an LLM's summary of a topic? | Puffery, superficial -ing phrases, formulaic challenges |
| **Density** | Does every sentence carry information, or does the paragraph pad its word count with hedging, filler, and restatement? | Hedge stacks, filler phrases, generic conclusions |
| **Soul** | Does the paragraph have a point of view? Does it commit to a judgement? | Neutral listing, false balance, "on the one hand / on the other hand" |

### O2. The "Say What It Does" Rule

Replace every sentence that names a *feeling* with a sentence that names a *mechanism*, a *number*, or an *instruction*. The test: can the sentence be restated as a concrete fact or a concrete action? If not, cut it.

| Feeling | Mechanism |
|---|---|
| "The database stays close at hand." | "The client reads from a replica in the same region." |
| "SQL you can read." | "`.toSQL()` returns the exact string the driver sends." |
| "Types that follow your schema." | "A column rename fails the build." |
| "The gateway enforces five things." | "The gateway terminates the protocol, scopes the credential, applies the rate limit, logs the call, and forwards the request." |

### O3. The "Could This Be Another Book?" Test

If a sentence could appear unchanged in another project's documentation, it says nothing about this project. Cut it, or replace it with a sentence that names a specific mechanism, standard, or measurement from *this* book.

### O4. The "Read It Aloud" Test

Read the paragraph aloud. If the rhythm is uniform, if every sentence is the same length, if there are no short sentences after long ones, the paragraph is machine-shaped. Vary the rhythm deliberately (see C1).

### O5. The "Have an Opinion" Test

The book has opinions. It says "default to X" and "X fails when Y". It does not say "there are pros and cons to consider". If a paragraph presents two sides without committing to one, it is not slop-free; it is judgement-free. Add the judgement.

### O6. The Em Dash Frequency Rule

The em dash is a legitimate typographic device in reference prose (see SD-015). The tell is overuse. No page may contain more than two em dashes. No paragraph may contain three. If a paragraph contains three or more, rewrite at least one as a period, comma, or restructured sentence. The em dash is a tool; the tool is not the tell. The tell is the reflexive substitution of the em dash for a period.

### O7. The Controlled Vocabulary Exception

Unslop's abstract-metaphor list (C10.6) does not apply to terms in the controlled vocabulary (C2). "Harness" is the book's name for the host runtime. "Substrate" is the book's name for the tenant isolation layer. Authors who are tempted to replace these with "base" or "runtime" are violating the controlled vocabulary, not removing slop (see SD-016).

### O8. What Unslop Does Not Justify

Not every part of unslop belongs in this book. The following unslop rules are **not** adopted:

| Unslop rule | Why not adopted |
|---|---|
| "Avoid em dashes entirely" | Conflicts with C3 and with the reference book's typographic voice (SD-015). |
| "no parentheses" | The Style Bible permits parentheses. It forbids *nested* parentheses. Unslop's blanket ban is too strict. |
| "no en dashes" | The Style Bible uses en dashes for numeric ranges (C4). Unslop's ban would break the numeric conventions. |
| "Use 'I' when it fits" | The Style Bible's person conventions (C8) already specify when first person is used. Unslop's general permission is not needed. |
| "Let some mess in" | The Style Bible's precision is a feature, not a bug. "Mess" in a reference book is a defect. |
| "Be specific. Not 'this is concerning' but 'there's something unsettling about agents churning away at 3am'." | The example is narrative voice, which the Style Bible already governs through J5 and B4. Unslop's version is loose; the Style Bible's version is precise. |

### O9. The Anti-Slop Pass in the Editorial Workflow

The anti-slop edit is Stage 7 of the editorial workflow (M3). It is distinct from the line edit (Stage 6) and the copyedit (Stage 8). Its purpose is narrow: remove AI tells, restore human rhythm, and confirm the paragraph passes O1. The editor performing the anti-slop pass uses C10 as the checklist and Part O as the quality bar.

---