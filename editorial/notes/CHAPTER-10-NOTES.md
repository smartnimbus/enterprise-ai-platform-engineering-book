# CH-010 — The Canonical Fabric Architecture

Status: working authoring guidance; chapter contract remains proposed unless separately ratified. Source: Chapter 10 vs Chapter 41 conversation, authoring package §§4–20. Existing Blueprint and Style Bible are authoritative for their respective domains.

## Mission and rationale

Bridge Chapter 1's shared-investment argument and Chapters 13/16's mechanism-level examples. Explain the whole reference architecture through responsibilities and interactions, not a product list. Chapter 10 selected as next sample recommendation for whole-book coherence; Chapter 41 deferred as stronger evidence of procedural breadth. Neither proves sustained authoring throughput.

## Source requirements

Eight planned pages; 5% narrative allocation; maximum narrative 150 words. Two primary figures 10-1 and 10-2; execution/ownership crosswalk; read and mutable-action trajectories, three logical paths, evidence joins and enforcement boundaries. Primary Atlas links D-07 and D-18. Consult Development Blueprint, Style Bible v1.2, frozen TOC and chapter contract before drafting. Proposed working word allocation 1,800–2,550; page fit not demonstrated.

## Teaching sequence

Opening failure: a mutable action cannot be attributed to one policy decision across two pilots. Fictional, not a recorded refund. Explain four Structural Layers (Execution Environment, Tooling, Context, Lifecycle) and eight Control Planes (Identity, Gateway, Observability, Verification, Governance, FinOps, Data Protection, Interoperability). Explain request/action, authority/control and evidence relationships. Trace permitted reads with unresolved business status; trace denied proposed refund and separate simulated bypass test; distinguish later release-test failure. End with decisions, defaults, artefacts and references as required by actual style specification.

## Guardrails and rejected alternatives

- Do not turn logical responsibilities into twelve mandatory deployed products or sequential execution tiers.
- Do not introduce a ninth plane or fifth layer.
- Do not give Context authority to override source ACL or resolve unresolved truth by newest-wins.
- Do not equate authenticated identity with business approval or Gateway denial with correct behaviour.
- Do not imply every read crosses a central Gateway proxy.
- Do not create a successful Meridian refund. A permitted-write path may be conditional only, separate from recorded synthetic outcomes.
- Prefer two complementary figures, not one giant diagram. See [diagram rationale](../figures/DIAGRAM-RATIONALE.md).
- Keep mechanism detail in Chapters 11–22; do not duplicate Chapters 13 or 16. Keep appraisal procedure in Chapter 41.

## Related sources

[Blueprint](../outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md), [Style Bible](../style/style-v1.2.md), [decision catalogue](../../decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv), [Meridian notes](../../knowledge/MERIDIAN-EVIDENCE-NOTES.md). Read exact D-07 and D-18 defaults from catalogue; resulting artefacts execution-isolation-profile.yaml and gateway-bypass-proof.md. No actual production proof is claimed.

## Intended next use

Write manuscript and native figure sources from these constraints; check page fit and exact evidence links. This file is not that manuscript.
