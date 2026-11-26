# Session continuity — operating instructions

Author direction: repository is permanent system of record; meaningful GPT work must be preserved. Effective working instruction for significant sessions, subject to existing repository authority and publication controls. No new architecture or approval framework.

## Start

Read CURRENT-STATE, NEXT-SESSION, ACTIVE-DECISIONS, OPEN-QUESTIONS and BACKLOG. Verify live revision, workstream and relevant source paths; do not assume prior status. Read the relevant knowledge, chapter, diagram and publishing notes. Choose the requested bounded task; no automatic execution of all backlog items.

## During

Save actual deliverables at canonical locations as soon as coherent, especially before long context windows or tool-heavy work. Keep a short capture inventory: item, destination, source, privacy class, status. Record accepted decisions distinctly from recommendations. Do not create duplicate manuscript masters or silently alter frozen sources.

## Close

Use [checklist](SESSION-COMPLETION-CHECKLIST.md). Update relevant notes, register, task status, open questions, current state, next-session instructions and append a session record. Review prompts and diagrams for new durable guidance; record N/A with reason if unaffected. Commit and verify actual remote content. The self-referential final commit SHA belongs in the user delivery receipt or next session snapshot, not inside its own commit.

## Status semantics

CHAT_ONLY: actual deliverable not preserved remotely. DRAFT_CAPTURED: actual draft saved but not accepted. COMMITTED: verified remote file; INTEGRATED: verified authoritative baseline contains it. ACCEPTED: relevant author/editor approval evidenced. BLOCKED: named dependency; DEFERRED: explicitly postponed. Distinguish evidence, approval and custody. An incomplete session may still preserve partial work; never mark it closed.

## Task tracking

[BACKLOG.md](BACKLOG.md) is a bounded continuity view for current session work and recovery, not a second master execution programme. Link existing issue/work item or earlier authoring queue IDs where known; update existing task tracking when applicable, otherwise create a local recovery ID. Retain historical programme records unchanged unless actual status evidence supports an update.

Use [capture rules](../knowledge/CHAT-CAPTURE.md) and [prompt library](../prompts/README.md). Existing proposed machine-readable handover template remains available at governance/proposals/knowledge-system/HANDOVER-TEMPLATE-v1.yaml; do not claim its unimplemented target paths exist.
