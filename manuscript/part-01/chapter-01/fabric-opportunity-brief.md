### Fabric Opportunity Brief

*Illustrative completed example · Initial architecture decision*

**Business problem**

Two hypothetical funded production use cases require equivalent capabilities for identity integration, approved tool connectivity, verification and operational evidence.

Independent implementation could create duplicated expenditure and inconsistent support arrangements.

**Decision under consideration**

Determine whether the identified capabilities should remain domain-local or be provided through a shared service.

**Alternatives**

| Option | Description | First-year cost |
|---|---|---:|
| A | Independent delivery | £120,000 |
| B | Shared delivery of equivalent capabilities | £100,000 |

*All costs and use-case conditions are hypothetical.*

**Indicative economic outcome**

**£20,000**

Potential first-year cost difference in favour of shared delivery, before verification of the complete cost assumptions.

**Required ownership**

| Responsibility | Accountable role |
|---|---|
| Funding decision | Investment sponsor |
| Architecture recommendation | Enterprise architecture lead |
| Shared service delivery and operation | Designated platform service owner |
| Individual business outcomes | Respective business domain owners |
| Control requirements | Relevant security and architecture authorities |

*Roles are proposed for this example. No actual appointments or approvals are claimed.*

**Material trade-offs**

Shared delivery may reduce duplicated engineering and establish more consistent control contracts.

It also introduces common operational dependencies, continuing platform expenditure and the need to manage requirements from multiple consumers.

**Evidence required before investment approval**

| Requirement | Expected evidence |
|---|---|
| Funded demand | Confirmed production use-case commitments |
| Equivalent requirements | Comparison of the required control contracts |
| Economic justification | Like-for-like cost assessment |
| Operational feasibility | Accepted service responsibilities and requirements |
| Security compatibility | Assessment of relevant isolation and segregation constraints |
| Existing service reuse | Assessment of capabilities already available within the enterprise |

**Provisional decision**

Evaluate shared delivery.

The illustrative economic comparison supports further investigation. It does not establish that the investment has been approved or that the expected savings have been achieved.

Until the conditions in D-01 are evidenced, domain-local delivery remains the default.

**Verification after an approved implementation**

Compare actual onboarding expenditure, continuing service costs, operational responsibilities and control effectiveness against the conditions supporting the investment.

**Reconsideration conditions**

Reopen the decision if funded demand changes, the use cases develop materially different requirements, segregation obligations change, operating costs exceed the supporting assumptions or the service owner cannot sustain the required capability.

**Alternative outcome**

If only one funded use case exists, independent delivery costs £60,000 compared with £85,000 for shared delivery.

Under these illustrative conditions, retain domain-local delivery and reconsider the shared option when additional justified demand emerges.

**Resulting artefact**

Fabric Opportunity Brief, providing input to the formal `fabric-adoption-adr.md` required by D-01.

*Evidence classification: hypothetical teaching example. No actual enterprise investment, production deployment, approval, control result or financial saving is claimed.*

