# Chapter 16 Authoring Blueprint v1.0

**Book:** *The Enterprise AI Agent Fabric: Designing, Governing and Operating AI Agents at Scale*  
**Chapter:** 16 — Gateway Control Plane (Part III)  
**Document type:** Binding developmental-editor authoring contract; **not chapter prose**  
**Status:** Ready for professional drafting, contingent on this contract's source checks  
**As-of:** 9 November 2026  
**Governing sources:** Style Bible v1.2, especially B1–B4, C1–C3, D2–D3, E1–E5, F4/F7, H1–H8, M1–M3; *Enterprise AI Agent Fabric Development Blueprint* (frozen chapter 16); *Enterprise AI Agent Fabric Decision Catalogue* (frozen D-10, D-18, D-20); *Meridian Evidence Fixture v1.0.0* (frozen records and chronology).  
**Change control:** Do not edit source files, event IDs, dates, policies, decisions, registry entries, or outcomes. Editorial changes to this contract require a new blueprint version, not edits to the fixture.

## Executive drafting instruction

Show **how a proposed external mutation becomes a denied, attributable action**, why delegation is not execution permission, how a policy decision reaches an actual policy enforcement point (PEP), and how a controlled bypass attempt tests the boundary. End with the evidence and ownership consequences. The central proof is **not** that a diagram contains a Gateway. It is that the synthetic Week 9 request was denied before any external refund call, and that the synthetic direct-egress bypass test was also blocked. State expressly that these are fixture-level simulations, not production security results.

**Chapter proposition:** The Gateway Control Plane defines and coordinates policy enforcement for external actions. Protection depends on verified enforcement at deployed PEPs plus credential and network controls; an agent's proposed tool call is never itself authority.

**Reader:** enterprise architect and AI platform lead first; security architect, platform engineer and SRE second. **Register:** Style Bible B1 Part III — third-person, present-tense, mechanism-first, no rhetorical opening. **Chapter structure:** F7 verbatim. **Related decisions:** D-10 and D-18 primary; D-20 supporting, without rewriting its definition. **Related chapters:** 12 (Tooling), 15 (Identity), 18 (Verification), 19 (Governance), 21 (Data Protection), 27 (Trust Chain), 37 (Incident), 40 (Evidence), 48 (Security Response), 57 (Worked Artefacts). Prioritise four or five in the closing See also.

## Part 1 — Required outcomes and proof obligations

| Dimension | Reader/enterprise problem | The chapter must prove | Observable reader outcome |
|---|---|---|---|
| Reader | A diagram says “all calls pass the Gateway” without explaining how | Policy intent differs from runtime enforcement | Reader can identify PEP, policy input, control decision and target side effect |
| Enterprise | Teams integrate external tools through inconsistent credential and network paths | Shared action admission needs accountable routing and operating ownership | Reader can specify enforcement contract and failure-owner assignments |
| Security | Delegation can be mistaken for permission to mutate money; a service can bypass the proxy | A request for `refund:execute` exceeds the effective `refund:request` scope, and a separate direct-egress test is blocked | Reader can walk through both failures and identify how they differ |
| Governance | Policies and approvals exist but cannot be linked to individual decisions | Evidence references named policy, actor chain and recorded outcome | Reader can recognise a decision receipt rather than a permission token |
| Architectural | Central Gateway policy alone cannot prevent bypass by unmediated calls | Policy authority, PDP evaluation, deployed PEP, network/credential restrictions and target execution have distinct responsibilities | Reader can allocate ownership without inventing a ninth control plane |

**Acceptance demonstration:** A reviewer given only the chapter and named fixture excerpts can answer: (1) Who originated the read/prepare request? (2) Which rights survived delegation? (3) Which missing right caused primary denial? (4) At which enforcement point was mutation stopped? (5) How was direct routing tested? (6) What exact records allow reconstruction? (7) Why did a later candidate release fail despite the Gateway denial? Answers must map to frozen IDs.

**Explicit boundaries:** This chapter does not teach programming a real Gateway, claim cryptographically signed fixture tokens, verify production firewalls, certify an OWASP mapping, or adjudicate source-record truth. Ch15 owns identity/delegation mechanics; Ch13 owns semantic conflict; Ch18 owns behavioural release gates. Ch16 explains how their outputs influence action admission.

## Part 2 — Publisher-ready F7 outline and word/page budget

**Non-negotiable exact F7 headings, in order:** “What this layer decides” (F7 inherits the F6 literal heading; **do not silently rename it**), “The mechanism”, “Threat coverage”, “Failure modes”, “Enforcement point”, “Anti-patterns”, “Evidence artefact”, “Decisions to make”, “Defaults”, “Artefacts to produce”, “See also”. The **Evidence artefact** addition belongs after Anti-patterns and before the closing blocks in this authoring contract; F7 names the section but does not mandate placement. No invented alternative F7 sections. Subheadings inside *The mechanism* are allowed for navigation. The chapter heading itself is `Chapter 16: Gateway Control Plane`.

**Layout budget:** frozen **6.5 planned pages**, a publisher layout target rather than a precise word-to-page conversion. Plan **~2,250–2,550 prose/table-equivalent words** plus three compact diagrams, captions and one excerpted receipt table. This may require production adjustment if figures do not fit; do not drop technical evidence or exceed E5 to force the fit. Layout estimate: ~0.8 page diagrams 16-1/16-2, ~0.4 page 16-3, ~0.6 page tables, remainder text. An actual compositor must verify the final page count. Narrative is **no more than 150 words and about 5% of the chapter**, only the opening.

| F7 position | Drafting contract and purpose | Target words | Page allowance* | Figure | Required frozen evidence | Meridian placement |
|---|---|---:|---:|---|---|---|
| Opening hook | Show the Week 9 direct-route risk and stop condition; concrete failed operation, not literary scene. Finish by naming Gateway enforcement | 95 | 0.25 | — | `MF-EVD-DN-001` | `MF-EVT-012`, `MF-EVT-013`; factual foreshadowing only, Week 9 |
| What this layer decides | One-sentence boundary: admission of external actions and routing enforcement, not task selection or business approval | 35 | 0.10 | — | D-10, D-18 | `MF-REQ-REF-001` |
| The mechanism | Specify component responsibilities and trace request from intent through scoped evaluation to denied side effect; explain control vs deployed enforcement | 940 | 2.4 | 16-1, 16-2 | `MF-EVD-DG-001`, `MF-EVD-AU-001`, `MF-EVD-RC-001` (referenced, not duplicated) | `MF-EVT-009`–`012`; event IDs and timestamps in worked table |
| Threat coverage | Map trust-chain links and relevant OWASP Agentic categories with edition/version and source verification; avoid claiming that policy alone neutralises threat | 190 | 0.5 | — | source crosswalk, denial record | Week 7/8 references as conditions, Week 9 as enforcement |
| Failure modes | Table of bypass, missing scope, stale policy, PEP outage, replay, retry/duplicate, source conflict; symptom and control for each | 220 | 0.5 | — | `MF-EVD-AU-001`, `MF-EVD-DN-001` | `MF-EVT-011`–`013` |
| Enforcement point | Locate interception at `MF-SVC-PEP-001` and controlled egress boundary; explain fail-closed and negative-test requirements | 245 | 0.7 | 16-3 | `MF-EVD-DN-001.negative_bypass_test` | `MF-EVT-012`, `MF-EVT-013` |
| Anti-patterns | 3 F4 cards: gateway-only diagram, shared broad credential, decision receipt treated as signed permission; detection signal and correction | 180 | 0.45 | — | policy and receipt fields | Week 9 |
| Evidence artefact | Show one concise field-mapped authorisation-to-denial excerpt; prove no token, no outbound call and linked negative-test outcome | 265 | 0.7 | — | `MF-EVD-AU-001`, `MF-EVD-DN-001` | Week 9 and trace references |
| Decisions to make | 2–3 concise items matching frozen D-10/D-18, with D-20 as linked dependency | 55 | 0.1 | — | D-10/D-18/D-20 | — |
| Defaults | One-to-one matches to preceding bullets; no new deviation rules | 65 | 0.1 | — | D-10/D-18 | — |
| Artefacts to produce | Name `action-authorisation-contract.json`, `gateway-bypass-proof.md` and receipt reference | 55 | 0.1 | — | all three frozen records | — |
| See also | 4–5 cross-references, each with its reason | 35 | 0.1 | — | Ch12/15/18/19/57 | — |
| **Approximate total** | Section word targets are an editorial guide, not mandated pagination | **2,380** | **~6.0–6.5** | **3 diagrams** |  |  |

*Page allowances are a planning allocation with shared figure/table space; do not sum them as typeset guarantees. No long full-JSON listings in Ch16; full specimen belongs in Ch57.

### Mandatory subsection logic inside “The mechanism”

1. **Proposed action is not authority.** Start with `MF-REQ-REF-001`, a **read/prepare** request for GBP 125.00. Compare with attempted `POST /refunds` (`MF-ACT-REF-001`), which would be a mutation.
2. **Delegation yields an effective scope.** Human `MF-HUM-RET-017` delegates to agent `MF-AGT-RET-004`, then service `MF-SVC-REF-002`, then mediated tool `MF-TOOL-REF-001`; the resulting scope is only `refund:request`. Mention audience and expiry as fixture fields but do not invent real signatures.
3. **Control Plane versus runtime PEP.** Explain policy ownership and distribution separately from enforcement at `MF-SVC-PEP-001`. The Gateway does not replace the Identity, Governance, Context, or Verification Control Planes.
4. **Policy evaluation inputs.** Use tenant, actor chain, requested scope, target resource and operation, context conflict, and human approval state; distinguish required preconditions from the primary denial reason.
5. **Denied effect.** Show `required_scope=FAIL`, `context_conflict_precondition=FAIL`, `human_execution_approval=ABSENT`; decision `DENY`; no authorisation execution token; no external tool invocation.
6. **Runtime negative route.** Show separately the simulated direct service-to-ledger egress attempt and `DENIED_BY_NETWORK_EGRESS`. A PEP denial and a route block are **two different control outcomes**.
7. **Later verification consequence (one sentence in mechanism or evidence).** Week 11 candidate `MF-REL-RET-0.2.0-rc1` failed its behavioural assertion after selecting the forbidden tool; do not suggest Week 9 action was executed or rerun in production.

## Part 3 — Reader journey, exactly sequenced

| Step | Present to reader | Why now | Understanding check |
|---:|---|---|---|
| 1 Problem | A £125 review request is transformed into a proposal to issue money | Stakes arise before technology terminology | Request does not grant execution |
| 2 Delegation | Scope narrows at each hop | Makes denial intelligible before policy processing | `refund:request` is not `refund:execute` |
| 3 Gateway | Policy coordination and action-admission boundary | Establishes what Gateway owns, and what it does not | Control Plane is not identical to proxy |
| 4 Enforcement | PEP at `MF-SVC-PEP-001` evaluates mandatory conditions | Connects abstract rule to an observable stopping point | No mutable tool call before positive admission |
| 5 Denial | Receipt shows `SCOPE_EXCEEDS_DELEGATION` and other failed conditions | Converts mechanism into an inspectable result | Primary and secondary reasons differ |
| 6 Bypass attempt | Direct service-to-ledger path is blocked by egress policy | Tests whether the normal gateway is actually unavoidable | Network denial does not equal PEP evaluation |
| 7 Evidence | Linked delegation, decision and denied-action receipts | Establishes reconstructability and accuracy | Receipt is not signed permission |
| 8 Decision | D-10 authorisation and D-18 bypass proof; D-20 as dependency | Lets reader transfer case to own architecture | Default and deviation remain frozen |
| 9 Operational consequence | Record denial, alert/escalate, preserve evidence; separate Week 11 failed promotion | Closes the operational loop, not just the request lifecycle | Blocked release and blocked mutation are distinct |

**Why this order is optimal:** The reader sees the dangerous proposed side effect first, then the authority that must be checked. The Gateway is introduced only after delegation explains its input. Normal-route denial precedes the bypass test because they prove different obligations. Evidence follows observable outcomes; the named decisions come after the reader understands the trade-off. The operational close makes consequences explicit without drifting into a second chapter on Verification.

## Part 4 — Frozen Meridian mapping and fact lock

| Immutable ref | Exact content and outcome | First / subsequent chapter use | Forbidden interpretation |
|---|---|---|---|
| `MF-REQ-REF-001` | `2027-02-16T10:00:00Z`; synthetic Retail Service Desk Portal request; GBP 125.00; read/reconcile/prepare human decision; no money movement | Mechanism opening table and Figure 16-1 | Customer authorised payment execution |
| `MF-EVT-009` | `2027-03-01T11:00:00Z`, `DELEGATION_ATTENUATION`, `ALLOWED` | Delegation explanation, Figure 16-1 | A signed production token was validated |
| `MF-EVT-010` | `11:00:01Z`, `ACTION_REQUESTED`, `REQUESTED` | Requested `refund.issue` action in mechanism | Request was approved |
| `MF-EVT-011` | `11:00:02Z`, `POLICY_EVALUATED`, `DENIED` | Policy-check and evidence table | Policy granted a narrower execution permission |
| `MF-EVT-012` | `11:00:03Z`, `MUTATION_DENIED`, `DENIED` | Hook, PEP, Figure 16-2, evidence excerpt | A ledger call occurred and rolled back |
| `MF-EVT-013` | `11:00:04Z`, `DIRECT_BYPASS_TEST`, `PASS` | Enforcement point and Figure 16-3 | Production firewall or real refund processor was tested |
| `MF-EVT-014` | `2027-03-15T14:00:00Z`, `CANDIDATE_EVALUATED`, `FAIL` | Operational consequence, reference only | Same week-9 action was replayed in production |
| `MF-EVT-015` | `2027-03-15T14:00:03Z`, `RELEASE_BLOCKED`, `BLOCKED` | Final consequence/cross-reference to Ch18 | Week 11 release deployed or paid customer |
| `MF-EVD-DG-001` | Three hops; scopes narrow from case/product/refund request to `refund:request`; illustrative *unsigned* claims | Delegation figure and mechanism table | Cryptographic proof of signed authority |
| `MF-EVD-AU-001` | Authorisation **decision receipt**: `DENY`, `authorised_execution_token=null`, `signed_authorisation_status=NOT_ISSUED_DENIED` | Denial and evidence table | An authorisation **grant** or signed execution token |
| `MF-EVD-DN-001` | Denied action, `external_tool_called=false`, `financial_mutation_count=0`; negative route denied by network | Hook, negative-test Figure 16-3, evidence box | Proof of a deployed system's real network controls |
| `MF-EVD-CM-001` | Context manifest for earlier case | Referenced as a linked precondition | All source values reconciled |
| `MF-EVD-RC-001` | Conflict remains unresolved | Policy-evaluation input and Ch13 cross-reference | Latest CRM value wins |
| `MF-EVD-RG-001` | Later candidate release blocked after critical failed assertion | One short operational consequence, Ch18 link | Re-tested candidate passed or was promoted |

**Case invariants (check every draft and caption):** `MF-FIX-001`; `MF-CASE-REFUND-001`; tenant `MF-TEN-RET-001`; trajectory `MF-TRJ-001`; correlation `MF-TRACE-000001`; actor `MF-AGT-RET-004`; service `MF-SVC-REF-002`; tool `MF-TOOL-REF-001`; target `MF-SYS-LEDGER-001`; PEP `MF-SVC-PEP-001`; action `MF-ACT-REF-001`; attempt `MF-PEP-ATT-001`; policy `MF-POL-ACTION-v1.0`. The action amount is `amount_minor=12500`, `currency=GBP`; display as £125.00, never £12,500. Relevant context events `MF-EVT-001`–`008` occur earlier; do not transpose them into the Week 9 enforcement sequence.

## Part 5 — Authoritative illustration specifications

All three figures obey Style Bible H1–H8: only approved diagram types; at most **12 nodes and 20 edges**, left-to-right flow for sequence or top-to-bottom for trust boundary; each node label **four words maximum**; labelled edges as verbs; title/figure ID, one-sentence caption with v1.0, source note “Meridian Evidence Fixture v1.0.0 (synthetic)”, 2–3-sentence alt text, sufficient contrast, greyscale review, editable source and SVG export. Exact long IDs go in figure **legends**, not shortened or crowded node labels. No unlabeled arrows, decorative icons or fictional success paths. The diagrams are specifications, not finished images.

### Figure 16-1 — Scope attenuation before action admission

- **Type/tool:** sequence diagram, Mermaid → SVG.
- **Purpose:** teach D-20's relationship to D-10, without taking over Ch15.
- **Nodes/participants:** 1 Human; 2 Agent; 3 Refund service; 4 Gateway PEP; 5 Refund tool (optional target); **five lifelines**.
- **Required node legend:** Human=`MF-HUM-RET-017`; Agent=`MF-AGT-RET-004`; Refund service=`MF-SVC-REF-002`; Gateway PEP=`MF-SVC-PEP-001`; Refund tool=`MF-TOOL-REF-001`.
- **Ordered labelled flows:** “delegates read/request” Human→Agent; “delegates request” Agent→Service; “requests action” Service→PEP; “evaluates scope” PEP internal note; “denies execution” PEP→Service. A dashed tool lifeline may show **“not invoked”** as a note, never an outgoing success arrow.
- **Callout:** effective scope = `refund:request`; attempted scope = `refund:execute`. Use `MF-EVD-DG-001` / `MF-EVT-009`–`012` in the legend.
- **Reader takeaway:** a narrower valid chain cannot authorise a wider operation.
- **Caption:** “Figure 16-1. Delegated scope narrows before Gateway admission; the requested refund mutation exceeds the effective grant (v1.0; synthetic Meridian fixture).”
- **Alt text:** “A human delegates a read-and-request workflow through an agent and refund service to the Gateway enforcement point. The Gateway denies the requested refund execution because the effective permission is narrower than the required action scope.”
- **Prohibited:** signed-token icon or claims; a service→tool arrow indicating the refund was executed.

### Figure 16-2 — Gateway evaluation and denied decision

- **Type/tool:** sequence diagram, Mermaid → SVG.
- **Purpose:** separate policy evaluation, PEP interception and evidence emission.
- **Nodes:** Agent; Refund service; Gateway PEP; Policy evaluator; Evidence store; Refund ledger (**six lifelines**). Legend maps PEP and ledger to exact IDs; the policy evaluator is a **logical responsibility**, not a newly established Meridian system identity.
- **Edges:** “proposes refund” Agent→Service; “requests mutation” Service→PEP; “requests decision” PEP→Policy evaluator; “returns deny” Evaluator→PEP; “records decision” PEP→Evidence store; “returns denial” PEP→Service. Ledger receives **no call**; indicate this with a non-flow note.
- **Decision inset (not extra node):** `required_scope=FAIL`; `context_conflict_precondition=FAIL`; `human_execution_approval=ABSENT`; primary reason `SCOPE_EXCEEDS_DELEGATION`.
- **Reader takeaway:** `MF-EVD-AU-001` records the `DENY` decision; `MF-EVD-DN-001` proves the synthetic no-call outcome. `authorised_execution_token` is null.
- **Caption:** “Figure 16-2. A Gateway PEP records a denied policy decision before any call reaches the refund ledger (v1.0; synthetic Meridian fixture).”
- **Alt text:** “The refund service proposes a mutation, but the Gateway enforcement point obtains a denial from the policy evaluator and records the outcome. No execution token or external ledger request is issued.”
- **Prohibited:** draw a real policy-evaluator host, cryptographic signing or successful PEP→ledger path that the fixture does not establish.

### Figure 16-3 — Direct-route negative bypass test

- **Type/tool:** trust boundary diagram, draw.io → SVG.
- **Purpose:** demonstrate D-18 independently of normal PEP admission.
- **Nodes and boundaries:** “Refund service” inside agent-workload trust boundary; “Network egress” enforcement component at boundary; “Gateway PEP” approved route; “Refund ledger” in separate external-system boundary. Four main components, two boundary boxes; **six or fewer total elements**.
- **Required edges:** service→PEP “submits for admission” (allowed **path design**, not successful refund call); service→egress “tries direct route”; egress→ledger edge must **terminate before ledger**, explicitly labelled “blocks direct route”. Label the denial with `DENIED_BY_NETWORK_EGRESS` in legend.
- **Legend:** service=`MF-SVC-REF-002`, PEP=`MF-SVC-PEP-001`, ledger=`MF-SYS-LEDGER-001`; test=`MF-EVT-013`; receipt=`MF-EVD-DN-001`.
- **Reader takeaway:** PEP checks govern the approved route; independent egress restrictions prevent unmediated direct access.
- **Caption:** “Figure 16-3. The synthetic direct service-to-ledger bypass test is blocked at network egress (v1.0; not production control evidence).”
- **Alt text:** “A refund service has an approved route through a Gateway enforcement point and a separately attempted direct network route. The direct route ends at a blocking egress boundary and does not reach the external refund ledger.”
- **Prohibited:** label the synthetic test as a real production penetration test; show a completed call to the target.

## Part 6 — Technical explanation contracts

| Concept | Explain precisely | Misunderstanding to correct | Required worked anchor | Forbidden simplification |
|---|---|---|---|---|
| Delegation | Human→Agent→Service→Tool is the **logical actor/action path**, with effective authority determined by scopes, audiences and expiry | “A tool invoked by an agent inherits all human privileges” | `MF-EVD-DG-001` hop list, effective `refund:request` | Treat delegation as consent for financial mutation, or as verifiably signed production credentials |
| Scope attenuation | Effective rights are an intersection/restriction across authorised hops, never a union of claims | “Service account rights can expand an earlier principal's authority” | show scopes at each of the three hops; compare `refund:execute` | Use algebra that implies granting rights at a later hop |
| Policy evaluation | PEP passes a named set of inputs for decision; default deny on missing scope/proof; distinction between primary and secondary conditions | “Model intent or risk score is a policy decision” | `MF-EVD-AU-001.policy_evaluation` | Describe a prompt instruction as enforceable policy or infer exact live PDP location |
| Authorisation receipts | Record decision context, policy/version, actor, target, requested/effective scope, correlation, denial reason, and token status | “An AuthorisationReceipt always authorises execution” | `MF-EVD-AU-001` and `MF-EVD-DN-001` field-by-field excerpt | Claim signed token, real cryptographic proof or an issued authorisation token in this fixture |
| Non-bypassability | Requires PEP on approved mutation path **and** credential/egress/target-side limits on alternate paths; test both | “Central routing diagram proves calls cannot bypass Gateway” | `MF-EVT-013`, `negative_bypass_test`, target received=false | Claim one simulation proves universal or production-level non-bypassability |

**Technical accuracy requirements:** Name policy decision point (PDP) as the evaluation responsibility and policy enforcement point (PEP) as the runtime intercept. Explain the contract without inventing a dedicated physical PDP host. For D-10, the **normative** default demands a signed scoped receipt before an **allowed** mutation; this denied fixture appropriately issues **no** signed permission. For D-18, network and credential restrictions are required control categories; the fixture demonstrates only a synthetic negative egress outcome, not all possible credentials and routes. For D-20, cryptographic signing is the frozen default but the synthetic delegation record explicitly is not signed. Maintain all three distinctions.

### Threat coverage research rule

F7 requires a mapping to **specific OWASP Agentic AI (ASI) threat categories** and trust-chain links, with authoritative publication version/date and a reference note. Before the final technical draft is approved, verify the exact contemporary category IDs and labels against the primary OWASP text. No speculative ASI code or invented standard version enters the authoring contract. Author should map only supported threats (e.g., privilege misuse/delegation abuse, tool misuse, compromised integration or unsafe external action) to concrete Gateway controls, and document residual threats not resolved here (prompt injection, poisoned Context, model mis-selection). Trust links to describe: originator→agent, agent→service, service→PEP, PEP→external target, and PEP→evidence store. Ownership boundaries must not shift from Ch15/Ch13 to Ch16.

## Part 7 — Editorial failure catalogue and fixes

| Failure to reject | Observable symptom in draft | Required edit |
|---|---|---|
| Architecture jargon instead of mechanism | “The Gateway orchestrates trust” without inputs, checks and effects | Replace with precise path, policy inputs, PEP verdict, target/no-target outcome |
| Unsupported non-bypass claim | “No agent can bypass this Gateway” based on one sketch | Qualify as design requirement; show normal-route denial and separate synthetic egress test; state limits |
| Tutorial drift | Multi-page MCP configuration, Kubernetes manifests or vendor CLI | Reduce to boundary contract and test method; refer to companion material, not implementation tutorial |
| Cryptographic handwaving | “Signed delegation verified” based on illustrative JSON | Say structure simulated; no real signature; distinguish future production obligation |
| Receipt ambiguity | Authorisation receipt described as approval | Show `policy_evaluation.decision=DENY` and `authorised_execution_token=null` |
| Chronology collapse | Week 11 candidate behaves as if it executed Week 9 attempt | Split into March 1 denial and March 15 candidate evaluation; retain zero side effects |
| Wrong security cause | Unresolved record described as the sole primary reason | Primary `SCOPE_EXCEEDS_DELEGATION`, two secondary conditions, all from frozen receipt |
| Scope inflation | Agent gains `refund:execute` after service delegation | Show the intersection and explicit missing right |
| Unverified OWASP category | ASI number cited without source or edition | Verify primary standard/version before publication or leave citation pending editorial review |
| Excessive narrative | Long imagined meetings, dialogue or internal monologues in Part III | Keep only opening ≤150 words / ~5%, then mechanism-first technical prose |
| Overloaded figures | Full enterprise diagram with every plane and flow | Use only Figures 16-1/2/3, one purpose each, ≤12 nodes/20 edges |
| Missing operation evidence | Says denied but omits who/what/when/policy | Include minimum field-level excerpt, trace ID and zero-call postcondition |
| Generic ending | “Security is crucial for success” | Close with exact F7 Decisions, Defaults, Artefacts, See also |
| Wrong ownership | Gateway portrayed as creator of human consent or data truth | Attribute provenance to Context, delegation semantics to Identity, exceptions to Governance and release assertions to Verification |
| Uncontrolled prose | C10 forbidden words, uniform rhythm, synonym cycling | Apply Style Bible C1/C2/C10 and O; active mechanism-first sentences ≤30 words |

## Part 8 — Final author brief: execution contract

### Assigned author mission

Produce **Chapter 16 — Gateway Control Plane**, approximately 6.5 designed pages, using exact F7 structure and this authoring blueprint. Show why enterprise agents cannot execute mutable external actions merely because they generate plausible tool calls. Prove the architecture's intended enforcement contract through the frozen fictional Meridian Week 9 denial and its independent direct-route negative test. Use the Week 11 release failure only to show why operational Verification remains separate.

### Required source pack and read order

1. Style Bible v1.2: A1–A3, B1–B3, C1–C3/C10, D2–D3, E1–E5, F4/F7, H1–H8, M1–M3.
2. Frozen development blueprint: Chapter 16 purpose, page count, structure, ownership mapping, and relevant chapter connections.
3. Frozen Decision Catalogue: D-10, D-18, D-20 **exact defaults** and deviation conditions.
4. Meridian fixture: `README.md`, `original-request.json`, `event-ledger.json`, `03-delegation-record.json`, `04-authorisation-receipt.json`, `05-denied-action-receipt.json`, `02-reconciliation-record.json`, `06-release-gate-report.json`, and `authoring-registry.json`.
5. Verified primary OWASP Agentic AI publication for the precise F7 Threat coverage crosswalk. This is a **fact-checking dependency**, not permission to alter frozen fixtures or the architecture.

### Writing sequence (do not reorder final chapter headings)

1. Prepare a **fact sheet** of exact IDs, timestamps, scope sets, denial reasons and non-effects from the source pack.
2. Draft “The mechanism” first, anchored to the Week 9 event ledger, with the F7 component table and the precise PDP/PEP distinction.
3. Draft the evidence field excerpt directly from both receipts, preserving actual JSON field/value pairs.
4. Write three diagram briefs and approve node/edge lists before illustration; apply the figure specifications above.
5. Draft “Threat coverage”, “Failure modes”, “Enforcement point” and three F4 anti-pattern cards.
6. Write D-10 and D-18 decision/default closing bullets, one-to-one; mention D-20 as a linked identity dependency rather than changing it.
7. Write the opening hook last, ≤150 words and no narrative in body; use failure/mechanism opening, no rhetorical question.
8. Verify exact F7 order and complete the See also links; make every cross-reference target actual frozen chapters.
9. Run factual cross-reference, security-review, language/anti-slop, diagram, accessibility and compositional-layout gates.

### Minimum copy-ready evidence field list

| Record | Required displayed fields (keep exact names/values in snippet/table) |
|---|---|
| `MF-EVD-DG-001` | `chain_id`, `effective_scopes`, `requested_action_scope`, `scope_does_not_expand`, `signature_status` |
| `MF-EVD-AU-001` | `policy_id`, `policy_evaluation.decision`, `policy_evaluation.primary_reason`, `policy_evaluation.required_scope`, `policy_evaluation.context_conflict_precondition`, `policy_evaluation.human_execution_approval`, `authorised_execution_token`, `signed_authorisation_status` |
| `MF-EVD-DN-001` | `reason_code`, `enforcement_point`, `external_tool_called`, `financial_mutation_count`, `negative_bypass_test.result`, `negative_bypass_test.target_received_request`, `negative_bypass_test.proof_type` |
| `MF-EVD-RG-001` | `candidate_release`, `assertion.assertion_result`, `gate_verdict`, `production_deployment` (one-sentence operational linkage only) |

### Exact output inventory

- **Chapter draft:** `chapter-16-gateway-control-plane-v1.0.md`, all F7 headings.
- **Diagram source briefs:** `figure-16-1-scope-attenuation.md`, `figure-16-2-gateway-denial.md`, `figure-16-3-direct-bypass.md`; illustration source exported as SVG under the book's figure conventions.
- **Evidence excerpts:** `chapter-16-evidence-excerpts.md` with machine-traceable source fields; do not reproduce modified synthetic JSON as genuine evidence.
- **Editorial crosswalk:** `chapter-16-source-crosswalk.csv` with statement→fixture ref or external technical citation, decision ID, section and reviewer.
- **Review record:** `chapter-16-quality-gates.md` with dated pass/fail and open issues.

### Release gates for drafting acceptance

| Gate | Verification method | Pass condition |
|---|---|---|
| Canonical alignment | Check every ID and field against fixture JSON/event ledger | **Zero** invented, contradictory or silently edited fixture values |
| F7 exactness | Heading and content audit | All required F7 headings, order, component/failure tables, three F4 anti-patterns, evidence artefact |
| Security precision | Independent security-architect review | Scope, PDP/PEP, side effects, bypass limitations and synthetic-signature caveats accurate |
| Decision integrity | Compare D-10/D-18/D-20 with catalogue | No rewritten default/deviation/reversibility; D-10/D-18 actionable, D-20 linked |
| Story chronology | Event- and timestamp-level audit | Week 9 and Week 11 distinct; external refund calls=0; mutation count=0 |
| Visual compliance | H1–H8 diagram checklist | All 3 specs/figures comply; legends retain exact IDs; greyscale, source, caption, alt text |
| Style compliance | M2 anti-slop + C1/C2 audit | Prose ≤30 words per sentence; Part III narrative limits, no forbidden generic claims |
| Reader comprehension | Two independent target-reader exercises | Readers locate requested scope, failed PEP check, bypass block and evidence record without author explanation |
| Production fit | Typesetter or equivalent layout proof | Fits planned 6.5 pages or records a documented exception without omitting mandatory evidence |

**Stop conditions:** Stop and return for editorial resolution if the draft requires changing an immutable fixture fact, assigning Gateway ownership of a different plane, claiming unverified production security, introducing a new normative decision, or using an OWASP category without verified primary support. No other ambiguity justifies an invented fact.

## Locked acceptance vignette (editorial summary, not chapter prose)

A synthetic human requested a £125 refund **review**. A later agent attempted a financial mutation, which exceeded effective delegated authority. The synthetic PEP denied the call before it reached the external ledger. A controlled synthetic direct-route attempt was blocked by egress policy. A separate later candidate release failed because the agent selected the forbidden action despite conflicting source records. Chapter 16 explains the Gateway enforcement boundary and its evidence; it does not make either denial a production result or turn the release test into a real payment.

---

**Document status:** Chapter 16 Authoring Blueprint v1.0. This is the binding author brief for a future chapter draft. No chapter text, normative architecture revision, Decision Atlas update, or Meridian fixture mutation is included.
