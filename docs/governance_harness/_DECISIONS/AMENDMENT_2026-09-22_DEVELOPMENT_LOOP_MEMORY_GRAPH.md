# Development-loop memory and graph-recording amendment

Status: owner acceptance reported by HELP_HUMAN (Agent 0); implementation in
the instruction tranche, effective for the shared instructions on publication.
This is an amendment record, not a newly numbered D-GOV decision.

Recorded: 2026-09-22 (America/Edmonton). The date records this transcription;
it does not assert a separate timestamp for the owner's acceptance.

Source: Agent 0 reports that the human's message immediately after presentation
of the third-draft ZIP and link was, verbatim:

> this is approved. You can continue with your plan.

Agent 0 identifies the referent as the exact third-draft review package at
`plans/proposals/development-loop-memory/`, including the proposed amendment
and coordinated Root SPEC §9.8, Root PRD E-1 and Piping pointer revisions.
`AUTHORITY_AMENDMENT.md`, `README.md`, and `BASIS.json` identify the proposed
changes and their source basis. The locally presented archive was
`development-loop-memory-third-draft-2026-09-22.zip`; Agent 0 verified its
SHA-256 as `dcdbe0e7a5aa53a4f35510ca9a6d016655cb1380e88bcce59753848a5ff31ad6`.
That digest identifies implementation evidence; the owner did not type or
approve a digest token or assign a decision ID. The archived predecessor
`.archive/pre-third-draft-reviewed-candidate.zip` is not the accepted ZIP.

## Accepted amendment and scope

1. For future entries under the adopted development-loop revision, replace
   D-GOV-17 M4-A's `## Decisions And Evidence` minimum with the `## Runs` table
   in `docs/templates/MEMORY_TEMPLATE.md`. Each row gives a stable run ID and
   date, terse work done in that deliverable, and pointers to its PR and central
   evidence, decisions, scope changes, Task Management transfers or substantive
   completion as applicable. Central records retain decision authority and
   detail. Keep the canonical `MEMORY.md` filename and
   `# MEMORY - {{DEL-ID}}` title convention. Existing entries and headings remain historical;
   no mass rewrite or `_MEMORY.md` migration follows from this amendment.
2. For App and Piping development loops that adopt the revised instructions,
   the sole current local graph is Git-tracked at the project-relative path
   `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`.
   `loop/LOOP_INIT.md` names the actual selected path. Commit the graph early
   in the undertaking's PR sequence and update it as work proceeds. The
   AgentRuns tree retains required run evidence and a link to the graph and its
   examined revision; it does not host a second current copy. This changes
   Root `docs/SPEC.md` §9.8 and `docs/PRD_ROOT.md` E-1 for those adopting loops.
   The Piping 2026-09-19 standing-procedure pointer is aligned to the same
   location. Other loops retain their own accepted graph and evidence basis.

The accepted instruction package also aligns graph construction, bounded
reconciliation, conditional Task Management, deliverable commitments,
preparation, and App/Piping `LOOP_INIT` entry. Its named legacy censuses are
inputs to a separately authorized, one-time retirement; this amendment does
not decide an individual App or Piping `Remaining` disposition.

## Supersession and preservation

With respect to D-GOV-17, this record supersedes only M4-A's minimum section
for future memory entries. The original ruling remains at
`docs/governance_harness/_DECISIONS/D-GOV-17_model_capability_doctrine.md`;
its other dispositions still apply. The earlier Root SPEC §9.8 and PRD E-1
wording remains in Git history, and Piping's 2026-09-19 adopted procedure and
archive retain their historical meaning. This prospective graph location does
not relocate old graphs or rewrite run evidence. Existing lifecycle, formal
change, issued-baseline, review and acceptance boundaries remain with their
owning records.

The instruction tranche manifest and its PR provide the changed-path and
validation record. Publication of shared source is distinct from adoption or
corpus repinning by App, Piping, Runtime or PEC; their routed M6 notices identify
their own follow-up. Management manual v6 and guide v2 publication, including
HTML/DOCX/PDF derivatives, is a human-owned follow-up excluded from this
instruction PR. Acceptance of the instruction package does not claim those
derivatives were published.
