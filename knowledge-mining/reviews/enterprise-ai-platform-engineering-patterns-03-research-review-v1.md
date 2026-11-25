# Enterprise AI Platform Engineering Patterns — Quality and Reuse Review v1.0

**Source:** user-supplied `03-research.zip`, reviewed 24 November 2026. **Status:** RESEARCH / PROPOSED; non-authoritative for the frozen book architecture, 58 chapters, 30 decision defaults or Meridian fixture. **Rights:** source archive not imported; public summary contains only editorially curated findings and source document IDs. A fuller 3,680-word review is maintained in the submitted research pack.

## Executive finding

The archive is principally an **EA Pulse / Alfabet replacement research library**, not an independently implemented Enterprise AI Agent Fabric reference system. 81 archive entries include 79 Markdown documents (~131,473 whitespace words), two directory entries, and approximately 507 URL occurrences. Source coverage is broad; 62 Markdown documents contain an explicit `Missing evidence` heading. There are no executable reference implementations or validation tests within the supplied ZIP. These are research/specification assets rather than deployed outcomes.

**Verdict:** selectively mine deterministic software engineering patterns; do not import the EA Pulse architecture, Kotlin/http4k/GKE project choices, Alfabet-specific scope or historical protocol assumptions into frozen Fabric authority.

## Quality rubric (1–5; editorial judgment)

| Area | Rating | Reason |
|---|---:|---|
| Requirements coverage | 4 | BR/FR/NFR/DR/IR/security/operational/transition coverage |
| Repeatable research structure | 4 | Charter, research template, assumptions, options, missing-evidence fields |
| Source-to-claim provenance | 3 | Many URLs, but claims not all verified against versioned primary statements |
| Originality | 2 | Mostly mature and reused engineering ideas |
| Implementation evidence | 1 | No independently runnable implementation supplied |
| Security assurance | 2 | Useful threat topics but overly absolute claims |
| Cost and performance evidence | 1 | No comparable measured baselines |
| 2026 currency | 2 | MCP legacy SSE recommendation already dated |
| Relevance to book | 3 | Useful supporting patterns; unrelated EA Pulse specifics |

## Pattern candidates and traceability

| Pattern | Archive source ID | Existing book chapters and decisions | Disposition |
|---|---|---|---|
| Contract-first APIs and schema compatibility | RSR-EXT-132, 133 | Ch12/22/39; D-09/D-21 | KEEP, independent evidence |
| Idempotent side effects and retries | RSR-EXT-036, 054 | Ch12/16/36; D-10/D-15 | KEEP after exactly-once correction |
| Deterministic trigger state machines | RSR-EXT-120–123 | Ch14/19/39; D-15/D-29 | KEEP with durable outbox |
| Evidence custody and audit chain | RSR-EXT-026, 048 | Ch17/40/57; D-24 | CORRECT privileged-tamper claims |
| Tenant/source access control | RSR-EXT-046, 047 | Ch7/13/15; D-04/D-11/D-19 | KEEP |
| Provenance and stable identifiers | RSR-EXT-033, 037–039 | Ch13/40/57; D-11/D-14 | KEEP |
| Conflict status and explicit uncertainty | RSR-EXT-027, 039 | Ch13/18/57; D-14/D-22 | KEEP |
| Read-only MCP interfaces | RSR-EXT-043, 044 | Ch12/16/22; D-09/D-21 | UPDATE transport and scope |
| UI/API parity and declarative changes | RSR-EXT-132, 133 | Ch22/39/42; D-21/D-29 | KEEP |
| Reversible export / migration integrity | RSR-EXT-040, 057–060 | Ch34/49/50; D-29/D-30 | KEEP |
| Risk-triggered human review | RSR-PROG-028–031 | Ch19/35/40; D-06/D-22 | KEEP |
| Static-first reader outputs | RSR-EXT-031, 035 | Ch17/40/51; D-24 | KEEP |
| Controlled claim status | RSR-EXT-027, 034 | Ch13/18/40; D-14/D-24 | KEEP |
| Dependency impact graph | RSR-EXT-013, 025 | Ch14/35/36; D-15/D-27 | SUPPORTING |
| Operational trigger/runbook discipline | RSR-EXT-053–055, 123 | Ch17/18/36; D-22–24 | KEEP |
| Retention, licensing and custody | RSR-EXT-049–052 | Ch21/34/50; D-25/D-30 | KEEP |
| Isolated bounded workers | RSR-EXT-042, 054, 056 | Ch11/14/35; D-07/D-15 | ANALOGY ONLY |
| Deterministic-first cost review | RSR-EXT-001, 005, SRC-011 | Ch8/20/38; D-17/D-26 | DERIVED RECOMMENDATION, NOT IMPLEMENTED |

## Material source caveats

- **RSR-EXT-048** says PostgreSQL triggers guarantee perfect capture and prevent DBA tampering. Not established; privileged database access and tampering threat model demand independent evidence custody.
- **RSR-EXT-036** uses PostgreSQL keys for idempotency. Good local pattern, but does not guarantee exactly-once effects across downstream systems.
- **RSR-EXT-043** prefers SSE as remote MCP transport. The 2026 MCP specification uses Streamable HTTP and marks legacy HTTP+SSE deprecated.
- **RSR-EXT-120/121** treat Postgres LISTEN/NOTIFY as asynchronous engine. Notifications are wake-ups, not persistent jobs/acknowledgement.
- **RSR-EXT-132/133** prefer contract-first OpenAPI. Useful; code-first with generated audited contracts is also a valid controlled option.
- **RSR-EXT-026** uses hashes/append-only events. Compliance/tamper claims require independent key custody, off-host anchoring and threat assumptions.

## Deterministic-first pattern filter

Before calling an LLM, ask whether SQL, schema validation, OpenAPI diff, declarative rules, a durable queue, policy-as-code, provenance ledger or graph traversal can reliably produce the required result. The LLM is optional for ambiguous natural-language interpretation or explanation, never its own approval authority for high-impact actions. Measure incremental quality, p95 latency, total cost per **safe successful task**, and failure rates against the deterministic baseline.

## Technology analogy (external, not established by this archive)

Terraform: declarative desired state/plan/drift. GitLab Runner: pooled job executor and ephemeral workers. Kubernetes: jobs, quotas and controllers. Redis: cache/streams only when justified; at-least-once consumer semantics. OPA: deterministic PDP with separately enforced PEP. Entra ID: human/workload federation; delegation not inferred from authentication. Azure Policy: resource compliance, **not** business tool-call authorisation. Service mesh: workload traffic and authz on covered paths, **not** universal bypass protection. Platform Engineering: paved-road reuse, but platformisation only where justified.

Official primary references:
- https://developer.hashicorp.com/terraform/language/state/locking
- https://docs.gitlab.com/runner/executors/
- https://keda.sh/
- https://redis.io/docs/latest/develop/use-cases/streaming/
- https://www.openpolicyagent.org/docs/deploy
- https://www.openpolicyagent.org/docs/management-decision-logs
- https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation
- https://learn.microsoft.com/en-us/azure/governance/policy/overview
- https://istio.io/latest/docs/reference/config/security/authorization-policy/
- https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Metrics before claiming lower cost/higher scale

Compare equivalent tests across three routes: deterministic-only, bounded LLM-assisted, and agentic. Track quality, total infrastructure and support cost, model spend, calls/task, safe successes, p95/p99 latency, queue depth, duplicate side effects, cross-tenant denial tests, and bypass attempts. No source evidence here supports numeric claims of savings.

## Immediate research action

P0: correct evidence-tamper claims, MCP transport, and source-to-claim trace. P0: set up deterministic-vs-LLM comparison. P1: retry/outbox crash tests, PEP negative tests and cost breakeven evaluation. P2: rights assessment for historical external/client material. **Do not copy raw archive or unverified source claims into the public book repository.**

**Editorial verdict:** supporting research with high practical reuse potential; not proof of an implemented architecture. The frozen Atlas, Style Bible, Meridian fixture and Chapter 16 remain authoritative.
