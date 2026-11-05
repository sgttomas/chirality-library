# Task Management — execution guidance

## Bounded intake

Read the caller's concrete concern and sources. Confirm its significance and
lack of a current or identified successor home using the contract's eligibility
conditions. Intake requires only the federation preflight. Inspect relevant
existing register rows and notices after federation to avoid duplication; a
`scan` projection is optional and serves only that deduplication. The nine
domains of task management (Action Item, Assignment, Prioritization,
Deliverables, Work, Planning, Approval, Checking, Decisions; see
`plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md` §4) can help
expose a missing responsibility or decision; they are optional scanning
lenses, not nine compulsory stages.

Prepare the smallest useful disposition question. Explain what is known, why it
cannot presently be carried through ordinary work, what may resolve that problem
and which owner should decide. Recommend return to ordinary work, an amendment,
allocation/elevation, deferral with a checkable trigger, no action, or another
supported disposition. A completed comparison may recommend no register entry.

Present related concerns together at a meaningful boundary. Await actual human
promotion/disposition before register edits or external assignment. If no answer
arrives, preserve the intake and return its pending decision explicitly. Do not
record the concern as disposed or require independent project work to wait.

## Owner-selected register review

Perform only the requested modes after federation. When neither a supplied
concern nor review mode is given, show the local open-row position and relevant
currency findings, then ask what the human wants reviewed. No broad sweep is
automatic. The older generational practice—child-loop reviews after their work
lands, followed by Root—is an available human scheduling choice.

- **Triage:** prepare dispositions for the selected open rows with their grounds.
- **Harvest:** inspect selected structured sources such as non-ruled decisions,
  notices, evaluation/review findings, hold concerns, packet questions/conflicts,
  TBD registers and explicitly identified escalation records. Cite real sources;
  a token in ordinary prose is not by itself an actionable concern.
- **Staleness / closure echo:** compare cited sources with current evidence and
  report changed closure evidence or a source still showing an apparently closed
  concern. Preserve historical facts and the surviving owner.
- **Deferral review:** test the selected deferred rows' stated triggers. Report
  TRIGGER_FIRED, ACTIVATABLE through a named bounded contribution, or STILL_BLOCKED
  by an external act. Prepare an undispatched handoff where useful. Classification
  is evidence for a decision, not permission to execute or close the row.
- **Row maintenance / resolution:** apply only the recorded human decisions and
  explicitly authorized routing. Return resulting work to its owning instrument.

## Legacy-source retirement

Use the human's explicit source-retirement brief and perform federation before
assessment. Bind the source census or list by revision and hash. Compare it with
the current source sections so that removed, changed and newly added entries are
visible. Account for every supplied row, including NONE/no-current-task markers.
For compound entries, preserve the original identity and identify each meaning
that receives a distinct treatment. Follow relevant decisions, claims,
dependencies and formal-change handoffs far enough to establish that meaning.

For each entry, retain the source identity and text, assessed meaning, supporting
evidence, proposed treatment, destination and actual human decision. Group like
treatments for human review while individually identifying exceptions. Suitable
treatments include evidenced fulfillment, duplication, supersession or absence
of warrant; adequate preservation in governing scope; existing allocation to an
identified undertaking; a warranted document amendment; an owning human decision;
a qualified promotion candidate; or a pointer to an actual past result in the deliverable
MEMORY run index. An entry may
need more than one treatment. Keep any surviving obligation discoverable at its
actual source, including when another part of the entry is fulfilled.

Check coverage and semantic preservation before proposing removal: no missing or
duplicate originals, no stale source comparison, and every surviving meaning in
a real destination. An ordinary future requirement already stated in scope needs
no invented execution node. A proposed destination or nominal owner is not an
applied transfer or accepted allocation. Obtain the owning authorization for
substantive scope or issued-baseline changes. Apply human dispositions, verify
approved destinations and then remove the corresponding source entries within
the authorized write boundary. Preserve historical source snapshots unchanged.

Review the resulting account and documents independently when required by the
brief or project. Return exact applied treatments, evidence, source sections
removed and unresolved exceptions. After interruption, compare current sources,
decisions and partially applied destinations before resuming. Close the finite
account with the migration; later work reads the actual destination, rather than
maintaining the account as a parallel backlog. Historical checks remain bound
to their original inputs.

## Deterministic helpers and limits

The available utility is `tools/taskmgmt/taskmgmt.py` from the instruction/tool
root. Resolve it against the actual checkout. Use the invoking register explicitly.

| Command | Purpose and effect |
|---|---|
| `validate --register <path>` | Read-only schema and reference validation. |
| `scan --register <path> --out <path>` | Write a derived candidate projection from implemented structured-source classes; never promote a row. |
| `federation --register <path> --out <path>` | Survey tracked canonical registers/archives and write a derived relationship/coverage projection. |
| `archive --register <path> [--dry-run]` | Move already-CLOSED rows to REGISTER_CLOSED.csv after validation; never decide closure. |

The projection destination must be authorized and verified as Git-ignored before
scan/federation; the helper does not enforce ignoring. Check actual supported
arguments before use. There are no helper commands for human promotion,
prioritization, semantic deferral judgment, or automatic resolution.

The current scan handles non-ruled decisions, notice ledgers/unledgered notices,
Evaluation FINDINGS, named packet question/conflict/amendment CSVs, TBD registers
and limited HANDOFF_STATE blocker text. Run-record markers, review-report
sections, MEMORY and per-document token scanning are not implemented. Inspect
explicitly supplied concerns directly; perform a bounded manual supplement only
when the requested harvest includes unsupported sources. Report the actual
coverage and exclusions rather than treating helper success as a complete sweep.

## Cross-register federation findings

Report federation findings in the return with their class, rows and registers.
A finding that persists across federations is routed by where its repair lies:

- In the invoking register (for example `MISSING_NOTICE` for a local row whose
  `NoticeRef` cites no notice, or `REMOTE_CLOSED_LOCAL_OPEN`): prepare a
  row-maintenance candidate for human decision; repair only under that decision.
- In another loop (for example `LOCAL_CLOSED_REMOTE_OPEN`, or a notice the other
  loop owes): send a non-binding coordination notice to that loop's
  `execution/_Coordination/` when the invocation authorizes it, or return the
  finding to the caller for routing. Never write the other loop's register.

A persistent finding is not itself a register concern unless it meets the
intake eligibility conditions.

## Retained evidence

Retain exact human decisions and the inputs/evidence needed to check register
changes. Preserve returns from bounded TASK contributions and the parent's
assessment without repeating them in every deliverable or in MEMORY. Return
actual outcomes, pending decisions and pointers for continuation at closeout.
