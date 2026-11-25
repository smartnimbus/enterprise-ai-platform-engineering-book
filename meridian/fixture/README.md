# Meridian Evidence Fixture v1.0.0

**Classification:** FICTIONAL / SYNTHETIC / EDITORIAL. No real customers, production systems, cryptographic signatures, payment execution or regulator approvals are represented. The invented date anchor begins **2027-01-04** at fictional Week 1; it translates the manuscript's *relative* chronology into unambiguous UTC example timestamps.

**Authority:** The frozen Style Bible v1.2, 58-chapter construction blueprint and Decision Catalogue remain governing. This package fixes synthetic example values only; it does not change architecture or decisions. Do not describe fictional numbers as measured enterprise results.

**Fixture identity:** `MF-FIX-001` / `MF-CASE-REFUND-001` / trajectory `MF-TRJ-001` / correlation `MF-TRACE-000001`.

## Authority and contents

* `organization.json`: group, business units, tenant profiles, systems, services, tools, owners; three example tenants do **not** mean only three tenants exist enterprise-wide.
* `identities.json`: human principals (including the six fixed recurring characters), agent, workload/service identities, policy versions and scope boundaries.
* `original-request.json`: the exact synthetic GBP 125.00 refund-review request. The user requested **review and preparation**, never execution.
* `context-records.json`: exact, time-aligned Record A `MF-REC-A-001` (ACTIVE) and Record B `MF-REC-B-001` (CLOSED), same canonical product and effective date.
* `event-ledger.json` / `.csv`: 15 ordered observations across manuscript Weeks 7, 8, 9 and 11.
* Six numbered evidence JSON files: one Context Manifest, Reconciliation Record, Delegation Record, Authorisation Receipt, Denied-Action Receipt and Release-Gate Report.
* `authoring-registry.json`: immutable IDs, names, conventions, relationships and editorial rules.
* `validation-report.json`: machine-generated fixture validation results (script included).

## Immutable scenario spine

| Fictional date | Manuscript week | Scenario event | Outcome |
|---|---|---|---|
| 2027-02-16T10:00:00Z | Week 7 | A mislabelled insurance result escapes the *index lookup*; the source/tenant recheck blocks its use | Insurance record **not** admitted to context |
| 2027-02-22T09:12:02Z | Week 8 | Retail Product Registry and CRM disagree about product status | **UNRESOLVED**, data owner escalation |
| 2027-03-01T11:00:03Z | Week 9 | An agent requests a refund mutation outside effective delegated scope | Gateway **DENIED**, zero external tool calls |
| 2027-03-15T14:00:03Z | Week 11 | The candidate agent selects a forbidden tool despite unresolved source conflict | Critical assertion **FAIL**, promotion **BLOCKED** |

The source-index leakage is a **detected tenant-isolation failure at lookup**, not an authorised access and not a successful exposure to the agent context. The negative recheck protects consumption. This is the authoritative interpretation for future illustrations.

## Six-record chain

`MF-EVD-CM-001` → `MF-EVD-RC-001` → `MF-EVD-DG-001` → `MF-EVD-AU-001` → `MF-EVD-DN-001` → `MF-EVD-RG-001`.

Chronology: the Manifest and Reconciliation precede the week-9 action. The release report at Week 11 cites prior case evidence and also describes a **new** candidate test; it does not assert the same Week-9 tool call was replayed into production.

### Scope contract

* Human `MF-HUM-RET-017`: `case:read`, `product:read`, `refund:request`.
* Agent `MF-AGT-RET-004`: cannot have rights wider than the originator and its registered runtime grant.
* Service `MF-SVC-REF-002`: `case:read`, `refund:request`; delegates only `refund:request` to Tooling mediation.
* Tool `MF-TOOL-REF-001` requires `refund:execute`; neither delegated token nor explicit human execution approval provides this.
* Gateway `MF-POL-ACTION-v1.0` denies the side effect before tool execution. Direct egress is denied in a **synthetic negative test**.

`refund:request` is permission to propose/submit for an authorised review, **not** permission to issue a refund. No tool was run; no financial posting exists. The authorisation record may be called a *receipt of denial decision*, but never a *signed permission token*.

### Decision and manuscript crosswalk

| Frozen decision | Primary test | Fixture records | Chapters |
|---|---|---|---|
| D-10 Authorise mutable tool actions | Missing `refund:execute` must deny | 03, 04, 05 | 12, 15, 16, 27, 48 |
| D-11 Control retrieval access | Quarantine mislabelled insurance result and recheck sources | 01, event ledger | 7, 13, 21, 28, 43 |
| D-14 Reconcile semantic identities | Retain incompatible values as unresolved | 01, 02 | 13, 18, 22, 28 |
| D-18 Prove Gateway non-bypassability | Direct bypass route cannot reach target | 04, 05 | 10, 12, 16, 27, 42 |
| D-20 Control delegation chains | Effective scopes monotonically narrow | 03, 04 | 14, 15, 16, 40 |
| D-23 Set release and autonomy gates | Failed critical assertion blocks promotion | 06 | 9, 18, 30, 33, 39, 47 |

**Chapter 57** reproduces all six files as faithful specimens, with editorial formatting only, preserving IDs and outcomes.

## Diagram source invariants

Every future diagram must show these same labels: `MF-TEN-RET-001`, `MF-AGT-RET-004`, `MF-SVC-REF-002`, `MF-TOOL-REF-001`, `MF-POL-ACTION-v1.0`, `MF-EVD-DN-001` and `MF-EVD-RG-001` when relevant. The trust-boundary illustration must show the enforcement at `MF-SVC-PEP-001`, not inside a model prompt. Separate the context data flow from the action-permission flow and do not draw a successful edge to the refund ledger. Style Bible H1–H8 governs diagram types and accessibility.

## Editorial use and versioning

1. Reference IDs exactly. Do not abbreviate canonical IDs in caption text unless showing a legend mapping.
2. All manuscript quotations of events must be derived from this register; illustrative dialogue is not evidence.
3. Never silently fix Record A or B. This fixture's conflict deliberately remains unresolved.
4. Fixes to narrative typos without changed facts can use patch increments; changes to IDs, outcomes or claims require editorial change review and a new minor/major version.
5. Preserve v1.0.0 as published. Maintain a migration map when IDs are superseded.
6. Run `python validate_fixture.py` before reusing or exporting.
7. Time order is fictional and relative chronology is part of the frozen manuscript.
