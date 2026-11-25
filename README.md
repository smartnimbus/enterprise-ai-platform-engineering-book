# The Enterprise AI Agent Fabric

**Book:** *The Enterprise AI Agent Fabric: Designing, Governing and Operating AI Agents at Scale*

This is the controlled manuscript and editorial workspace for a proposed professional reference book. The repository operating model is [REPOSITORY-GOVERNANCE.md](REPOSITORY-GOVERNANCE.md). The architecture, 58-chapter structure, D-01–D-30 decision IDs/defaults, and Meridian Evidence Fixture v1.0 are frozen by prior programme decisions. The consolidated book, evidence and publishing materials are available on the default `main` branch.

## Start here
- [Style Bible v1.2](editorial/style/style-v1.2.md)
- [58-chapter development blueprint](editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md)
- [58-chapter Table of Contents](editorial/outlines/Enterprise_AI_Agent_Fabric_Revised_TOC.csv)
- [30-decision catalogue](decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv)
- [Meridian evidence dossier](meridian/fixture/Meridian_Evidence_Fixture_v1.0.md)
- [Chapter 16 draft](manuscript/part-03/chapter-16-gateway-control-plane-v1.0.md)
- [Chapter 13 acquisition sample and review status](publishing/apress/acquisition-samples/README.md)
- [Chapter 13 authoring blueprint](editorial/authoring-blueprints/Chapter_13_Authoring_Blueprint_v1.0.md)
- [Chapter 16 authoring blueprint](editorial/authoring-blueprints/Chapter_16_Authoring_Blueprint_v1.0.md)
- [Apress proposal v2 — current](publishing/apress/v2/Apress_Publisher_Proposal_v2.md)
- [Apress competitive dossier v2](publishing/apress/v2/Apress_Acquisition_Competitive_Dossier_v2.md)
- [Apress submission contents](publishing/apress/v2/APRESS-SUBMISSION-PACKAGE-v1.md)
- [Prior Apress draft (historical)](publishing/apress/Apress_Publisher_Proposal_Draft.md)
- [Industry comparison v2](knowledge-mining/cross-project-analysis/fabric-industry-comparison-v2.md)
- [Historical review and source limitations](knowledge-mining/forensic-review/MASTER_FORENSIC_REPORT.md)
- [Public import status and exclusions](knowledge-mining/RESEARCH-IMPORT-STATUS.md)

## Authority and protection

The material in `archive/historical/` is historical source content, **not** a replacement for the frozen book. Working chapter drafts are editorial work, not publisher-approved print copy. The Meridian case is fictional; its evidence demonstrates consistency but not a real deployment or cryptographic attestation.

**Do not upload** original historical ZIP/7z archives, proprietary enterprise inventory, third-party reference libraries, large raw source extracts or credentials to this public repository without rights, confidentiality and security clearance. Evidence-only source artefacts should be stored in an appropriately restricted repository.

All changes require a branch and reviewable pull request after the one-time governance bootstrap.

## One-main-branch navigation and convergence

**Operating model:** `main` is the sole permanent, approved documentation branch. Use short-lived `docs/*`, `fix/*`, or `research/*` branches for reviewable changes; after an approved PR is merged and verified, its working branch may be deleted. Release history is preserved by immutable release tags and Git history. This navigation policy does **not** replace the review, source-rights, frozen-change or approval rules in `REPOSITORY-GOVERNANCE.md`.

### Integrated source history

The original [book baseline PR #1](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/1), [programme PR #2](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/2), [pattern PR #3](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/3) and [manuscript recovery PR #4](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/4) were merged into `main` on 25 November 2026. Their historical reviews remain accessible. **A merge is not independent editorial acceptance or rights clearance.**

### One-click document sections on `main`

- **Manuscript:** [Drafts](manuscript/), [TOC](editorial/outlines/Enterprise_AI_Agent_Fabric_Revised_TOC.csv) and [development blueprint](editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md).
- **Atlas:** [D-01–D-30 catalogue](decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv), [F1 production pages](decisions/pages/).
- **Meridian:** [Dossier and machine-readable evidence](meridian/fixture/).
- **Editorial:** [Style Bible](editorial/style/style-v1.2.md), [authoring blueprints](editorial/authoring-blueprints/) and [reviews](editorial/reviews/).
- **Research:** [Forensic and provenance review](knowledge-mining/forensic-review/), [cross-project research](knowledge-mining/cross-project-analysis/).
- **Authoring QA:** [Phase 1–3 audit history](governance/proposals/knowledge-system/audit-history/), [Phase 4–7 authoring validation](governance/proposals/knowledge-system/authoring-validation/), [Phase 8 trial](governance/proposals/knowledge-system/phase8-real-author-trial/).
- **Production:** [Book completion plan](governance/proposals/knowledge-system/book-completion/), [publishing proposal](publishing/apress/).
- **Decision-support tooling:** [Digital Twin design](governance/proposals/knowledge-system/digital-twin/), [programme operating model](governance/proposals/knowledge-system/programme-os/).

**Current state:** The controlled source and proposal documents are now accessible from `main`. Their editorial, publication and permissions status is recorded in the documents themselves; presence in GitHub does not imply external approval.
