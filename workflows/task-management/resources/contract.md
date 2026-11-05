# Task Management — contract

## Ownership and authority

Task Management owns the invoking loop's Action Item register and the bounded
intake, finite retirement accounts or decision-support records needed for that invocation. It cites other
state at its owning source: scope, decisions, lifecycle, dependencies, work
graphs, memory and evidence. Register rows record concerns and dispositions;
they neither direct production nor grant scope, priority or acceptance.

Promotion and disposition are human acts. WORKING_ITEMS applies the exact
recorded decision; TASK never writes register rows. Dispatched to TASK, this
workflow runs inspection-only and returns candidate rows; a register-write
grant to TASK is ineffective. A manager may inspect and
prepare an intake within the authority supplied by its caller, but cannot turn
its recommendation into an owner decision. Accountable ownership remains human.
Do not write another loop's register or assume a notice assigns work there.

Preserve canonical register schema and IDs, source/evidence identities and
closure grounds. Existing OPEN, DEFERRED, ELEVATED and CLOSED states describe
concern disposition, not implementation progress. There is no IN_PROGRESS task
state. A changed closure source is reported stale rather than silently reclosed.

## Eligibility for development-loop intake

Apply the same eligibility conditions to a substantive PR and the final closeout.
A PR boundary does not itself require an intake, and a qualified concern need not
wait for final closeout when its actual allocation problem needs disposition now.

A bounded intake must identify all of the following:

- A concrete concern and evidence establishing its material significance.
- Why it cannot reasonably be handled through the current authorized work,
  investigation, decision, deliverable reconciliation or scope-change route.
- Why there is no identified successor undertaking or receiving owner already
  carrying it, including an explicitly preserved next-loop steer.
- The missing allocation, decision or precursor that could make progress possible.

Use the undertaking as the boundary, not the chat session. Ordinary unfinished
work stays in its graph when sessions change. Waiting for an input, review,
execution slot or a later planned node is not by itself an intake trigger.
The absence of a deliverable can call for a mapping investigation or scope
change within the undertaking; it is not automatically a register concern.
A closeout or census may identify an owning route without assigning the work.
Check the receiving undertaking and authority before treating that route as
allocation. Do not promote all residual claims or future requirements merely
because the current graph does not include them.

If these conditions do not hold, return the concern to its ordinary owning work
or explain why no action is warranted. A genuine intake records a missing home;
it never converts unfinished necessary production into completed work.

## Entry and federation

Select the workflow directly; the brief supplies the loop and bounded intake, review modes or explicitly
named legacy-source retirement. The local register normally lives at
`execution/_Coordination/_TaskManagement/REGISTER.csv` under the project/root
concerned. Use its actual adopted location, including retained domain shapes.
Do not create a new register or schema unless authorized.

Before each requested mode, perform the D-GOV-33 federation survey of canonical
Git-tracked registers and their closed-row archives. Use `taskmgmt federation`
when available. Bounded intake needs only this federation; `taskmgmt scan` is
optional there, for deduplication. Persistent cross-register findings are
routed as the method describes. Discover sanctioned shapes, validate inputs, derive relationships
from governed fields rather than Notes, and state COMPLETE/PARTIAL coverage and
operational failures. Emphasize relevant relationships while disclosing exclusions
and integrity errors. Federation writes only a derived projection; registers
remain unchanged. A non-Root intake does not become authority over other loops.

An unavailable helper needs equivalent read-only inspection with truthful limits;
missing evidence must not be hidden by a claimed complete manual fallback.
PARTIAL supports only conclusions independent of the missing inputs. Neither
preflight nor missing tooling creates a standing gate on ordinary development.

## Capture and review boundaries

A supplied concern is inspected directly with its source; no harvest is required
to rediscover it. An explicit finding from graph execution can support intake,
but planned nodes and graph state are not scanned into register candidates.
MEMORY may locate a previous run and its sources; do not mine it for future assignments
or store a pending intake there.

When a source already preserves the concern and its grounds, cite it. Otherwise
retain one concise note under the invoking Task Management home, for example
`intake/<concern>.md`, labelled candidate for human disposition. It needs the
concern, evidence, significance, missing home and proposed treatment—not a new
execution-state schema. Its existence creates no Action Item or approval.
After disposition, the register is the maintained disposition record; retain the
intake as its source rather than synchronizing another status list.

A broad harvest occurs only within a requested register-review scope. The
supported structured sources and helper limits are in the method. Do not scan
all prose for TBDs, import graph backlogs, or silently widen the supplied scope.
An unreviewed candidate remains visibly awaiting human disposition in the intake
return; no automatic register row, priority or foreign assignment follows.

## Explicit legacy-source retirement

A human may authorize one-time examination and retirement of a named source
population, including a legacy work list. This authorization supplies an input
inventory to assess; it does not declare every entry a concern eligible for
promotion or authorize recurring harvesting of ordinary work. Record the named
source revision and reconcile it with current source sections before proposing
removal. Include no-current-task markers, later additions and compound entries.
A marker describes the source's recorded state, not project completion.

Preserve each original entry's identity, meaning and evidence. A compound entry
may have several treatments; keep those parts traceable to the original without
claiming multiple originals. Prepare grouped treatments with individually named
exceptions and exact destinations. The human decides the dispositions; promotion
into a register still requires its own actual decision and eligibility. A scope,
ownership or issued-baseline amendment follows its actual owning authority.

The finite disposition account is migration evidence. An obligation adequately
preserved in its governing Scope of Work need not gain a graph node or register
row when the human has not selected an undertaking for it. Ordinary future
requirements never move into MEMORY. A terse MEMORY run entry may point to the actual
retirement result without discharging the associated commitment.

Apply an approved amendment or transfer and verify the destination before
removing its source entry. Preserve lifecycle/history, frozen inputs and the
source evidence. Do not rewrite historical checks to certify a different basis.
If a decision, destination or authorization is missing, retain the affected live
entry and return that exception; independent approved treatments may continue.
At completion, preserve the closed account as historical evidence, with surviving
obligations pointing to their actual homes. It is not another maintained backlog.

## Resolution and completion

Resolution occurs through ordinary owning work: authorized implementation or
investigation, deliverable amendment, scope-change intake, or an identified
external undertaking. Prepare and route the relevant intake under the actual
human decision. WORKING_ITEMS can coordinate selected resolution within its
assignment; this does not change its role or transfer another owner's authority.
A concern may gain a home before its underlying obligation is fulfilled. Keep
that distinction explicit in the disposition and linked receiving work.

Close only with the appropriate decision and evidence, including duplicate,
rejected or superseded outcomes. Do not infer closure from a passed scan or an
unchanged register. A register-changing invocation returns the exact changes,
human basis, evidence and unresolved concerns; validate live/archive structure.
Archive already-closed rows only when requested or included in the assignment.

Keep the result in its owning Task Management records and provide a pointer to
the caller. A Task Management invocation creates no separate loop receipt;
a loop whose instructions require one central receipt links its actual Task
Management outcome from that receipt when applicable. Other loops retain their own
recording contracts. Preserve historical receipts and their validation. Source
integration follows
standing Git authority and applicable checks; no separate old launcher gate is
introduced. Ending the invocation leaves unruled concerns and genuine blockers
explicit, with a return to the human for their disposition.
