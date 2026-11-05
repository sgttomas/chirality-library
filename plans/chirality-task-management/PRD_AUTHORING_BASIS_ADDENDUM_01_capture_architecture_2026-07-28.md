# Chirality Task Management — Authoring Basis Addendum 01: Capture Architecture

| Field | Value |
|---|---|
| Date | 2026-07-28 |
| Status | `NON_AUTHORITATIVE_AUTHORING_INPUT` |
| Amends | Nothing. Supplements `PRD_AUTHORING_BASIS_2026-07-28.md` without modifying it |
| Parent basis | `plans/chirality-task-management/PRD_AUTHORING_BASIS_2026-07-28.md` |
| Session context | Owner-witnessed working session, 2026-07-28 (runtime code review + Task Management design discussion) |
| Prepared by | Agent synthesis under owner direction; provenance labels distinguish the two |
| Intended next use | Input to the fresh Agent 0 PRD inquiry named in the parent basis, section 12 |

## 1. Purpose and fence

This addendum preserves a design position reached after the parent basis was
recorded, concerning the parent basis's capture-and-promotion contract
(parent §5.3) and its interaction with open questions Q2, Q3, Q5, and Q16.

It is an authoring input, not a PRD, decision, adoption, or scope grant. The
design position below is **AGENT SYNTHESIS presented to and discussed with the
owner; it has not been owner-ruled**. The PRD inquiry should test it
adversarially, not inherit it as settled.

## 2. Owner direction of record for this addendum

Stated by the owner in the 2026-07-28 session, following the reviewer's
identification of a "capture surface collision" (existing governed surfaces —
TBD registers, Conflict Tables, open-issue sections, coordination notices,
out-of-brief observation returns — competing with any new Task Management
capture path):

> "I'm very interested in your ideas for #3 the 'capture surface collision'
> (and it will affect #1 and #2). #4 I agree with you and #5 can be cleaned
> up as you indicated."

> "So regarding #3 should existing write surfaces, the result of agent
> instructions, persist with a small change to add some kind of metadata tag
> that can be found easily via scanning tools the Task Management uses to
> find 'action items'? Or do we reformat agents instructions and tooling to
> force such writes to a central database?"

The owner posed the two options as a genuine question and directed that the
resulting understanding be preserved for a future session. The owner did not
rule between them in this session.

Owner agreement recorded in the same exchange:

- **Agreed (#4):** the source framework's escalation model
  (discipline → package → project logs, upward elevation of the unresolvable)
  should be explicitly mapped onto the Agent 2 → Agent 1 → Agent 0/human
  hierarchy in the PRD.
- **Agreed (#5):** vocabulary cleanups — "praxeology" → "praxiology" for
  corpus consistency; and elevate parent Q18 (semantic separation of "task" /
  `TASK` Agent 2 shell / Task Management product), which is load-bearing, not
  cosmetic.

## 3. The recommended capture architecture (AGENT SYNTHESIS)

**Compressed statement:** capture is deterministic and in-place; promotion is
judgment and in-register; the service owns the scan and the views, never the
truth.

Neither of the two posed options is recommended in pure form. The
recommendation is a two-stage, three-layer design:

### Layer 1 — Existing surfaces persist untouched; the scanner meets them where they are

Existing governed conventions are already machine-recognizable: `TBD`
markers, Conflict Tables with `HumanRuling = TBD`, open-issue sections,
`FAILED_INPUTS` statuses, coordination notices with unacknowledged
acknowledgment fields. A deterministic scanner harvesting candidates from
these existing structures delivers day-one value with **zero agent
instruction changes**. (Evidence this signal already exists un-aggregated:
the 2026-07-28 tandem comparison's "29 of 30 routed notices
delivered-but-unacknowledged" finding was produced by exactly this kind of
scan.)

### Layer 2 — One small additive marker, adopted gradually

A single standardized inline grammar (working shape:
`AI-CANDIDATE: <concern> | <evidence-ref>`) for concerns that fit no existing
structure. Introduced through HELPS_HUMANS as instruction files are touched in
ordinary maintenance (registry-lifecycle style, per R15), never as a big-bang
rewrite of the agent suite. The marker designates a **candidate**; it is not
the Action Item and carries no lifecycle state.

### Layer 3 — The Action Item register is the only new authoritative object, and it is file-native

Promotion is a judgment act (Agent 1 / Agent 0 / human, per parent §5.3 and
the source corpus's triage model) that **writes a git-tracked record** in
per-level registers (working shape: `_TaskManagement/` at project, package,
and discipline levels, mirroring the source's three-log structure and the
agreed #4 hierarchy mapping). The record carries K-PROV-1-style provenance to
the source location. Lifecycle state lives in the register, never in the tag.
The service proper is: scanner + candidate inventory (a derived, rebuildable
snapshot under the rebuildable-cache rule) + register views + staleness
checks (tag whose Action Item vanished; Action Item whose cited source moved
— K-STALE semantics reapplied).

## 4. Why the central-database option was recommended against (AGENT SYNTHESIS)

Four independent arguments, each held sufficient alone:

1. **Foundational conflict.** DIRECTIVE §2.1 places all cross-session project
   truth in git-tracked files. A mandatory central write-target makes the
   service authoritative for cross-session truth on day one — the crack in
   the load-bearing decision that parent Q2/Q3 must not slide into.
2. **Enforcement routed through the weakest layer.** Instruction-text
   conformance is soft (thesis §8.6.2). A dual-write obligation enforced only
   by instruction text creates a *silent* failure mode: work done, DB write
   skipped, item lost — the exact failure the product exists to fix, now with
   false confidence. A capture system whose recall depends on perfect
   instruction-following by the agents whose imperfect following motivated it
   is circular.
3. **Fails parent Q16.** A required write path makes service unavailability
   block agents or force noncompliance. The PEC precedent (D-PEC-67/68:
   file-native fallback always sufficient; the coordination plane only ever
   improves throughput) is the posture Task Management should be born with.
4. **Migration cost and the §7 anti-goal.** Rewriting the agent suite plus
   revalidation to produce the "mandatory workflow imposed on every act of
   work" that parent §7 explicitly forbids.

**Why the pure tag option was also rejected:** if the tag is the record, the
scan becomes the authority — rewrites and renames silently lose items, tags
cannot carry a disposition lifecycle without bloating into an inline
database, and recall still depends on tagging discipline.

## 5. The recall problem, stated honestly (AGENT SYNTHESIS)

Discovery-plus-promotion does not by itself capture concerns an agent neither
records in an existing convention nor tags. Two mitigations, both
praxiological (read-side), neither a write obligation:

- **Scan at existing gates.** The source cadence (daily deliverable
  statusing, weekly package planning) maps to existing gates: a nine-domain
  scan becomes a read/disposition step at fan-in validation and session
  handoff. One added checklist line at gates that already exist.
- **Measure capture coverage.** An AUDIT_EPISTEMIC-style audit compares scan
  candidates against promoted/dispositioned items and reports the gap — this
  supplies parent Q19's measurement and a computable Q20 falsification
  candidate: *candidates accumulate without disposition faster than they
  close*.

## 6. Hierarchy mapping guidance: the source's escalation model and Agent 0/1/2 (AGENT SYNTHESIS; owner agreed the mapping should be made explicit)

The source corpus's operating structure transfers onto the runtime hierarchy
with almost no deformation, and the PRD should state the mapping rather than
leave it implicit. The reason the transfer works is worth recording: both
frameworks index authority to **accountability-status, not capability**
(thesis §9.3.5). The 9-rules document assigns obligations by role — never by
how skilled the role-holder is — exactly as the K-* catalog does. A mapping
between two capability-invariant structures survives model changes and staff
changes alike.

### 6.1 The tier mapping

| Source framework | Chirality analogue | Register / disposition surface |
|---|---|---|
| Discipline worker; identifies risks and HOLDs during work | Agent 2 / bounded TASK agent; acts only inside its brief, returns out-of-brief observations upward (parent §5.3) | Discipline/deliverable-level candidates; no disposition authority |
| Discipline lead; triages discipline log | Agent 1 within its accepted activation, or the human discipline lead | Discipline-level register: triage, dedupe, resolve-in-scope |
| Package level (project engineer + task coordinator); triages, plans, mitigates, works; elevates the unresolvable | Agent 1 manager (e.g. WORKING_ITEMS, one activated package) within its latitude | Package-level register: disposition within accepted scope; elevation upward |
| Project leadership; receives elevated items, makes cross-package calls | Agent 0, alone or in consultation with the human | Project/program-level register |
| Client / external authority; gives direction logged at project level and disseminated down | Owner and external parties; reserved human acts where latitude ends | Project-level register entries with dissemination downward |

Three consequences the PRD should draw:

1. **Register levels mirror authority tiers** so every register has exactly
   one unambiguous triage owner (this narrows parent Q7). An Action Item's
   register level *is* its current escalation position; elevation is a
   recorded move between registers, preserving provenance — not a copy.
2. **Escalation is the existing notice flow, reused.** "Transferred up,
   triaged, elevated when unresolvable" is byte-for-byte the parent-mediated
   coordination rule already in AGENTS.md (children report to parents; Agent 1
   reports to Agent 0; consequential matters return to the human). Task
   Management adds durable registers under that flow; it must not add a
   second escalation channel beside it.
3. **RASCI maps with one hard constraint.** Agents may hold R, S, C, and I.
   **A is human-only, invariantly** (K-AUTH-1) — no register field, view, or
   report may show an agent as accountable for an Action Item's completion.
   This is the concrete schema-level form of the parent §6.3 requirement that
   agent execution never be confused with professional accountability, and of
   parent Q9.

### 6.2 Where the human framework and agent doctrine diverge — do not map these

Two rules in the source corpus are written for human teams and must **not**
be transferred literally:

- **Lateral communication.** The source directs that "communication occurs
  across all channels, not just through leadership," and that disciplines
  proactively resolve inter-discipline needs together. For humans this
  stands. For agents it is *prohibited*: siblings do not message directly and
  children do not bypass parents (AGENTS.md, supervised many-to-many rules).
  The reconciliation is the register itself: **shared reads are allowed, so
  a register a sibling can read is the sanctioned lateral-visibility
  surface** — durable filesystem coordination in place of live sibling
  messaging, consistent with "durable surfaces complement live agency and
  never become hidden authority." The PRD should present registers as
  exactly this: the lateral channel agents are otherwise denied.
- **The inter-discipline NOT.** The source excludes routine inter-discipline
  needs from Action Item tracking (track at discipline level; escalate only
  on HOLD risk). In agent terms the analogue exclusion is: ordinary
  work-graph dependencies between deliverables belong to the dependency
  registers (K-DEP-1), not to Task Management — reinforcing parent §7's
  "must not become the authoritative dependency graph." Only a dependency
  *at risk of causing a HOLD* crosses into an Action Item, citing the
  dependency row as evidence.

## 7. Effect on the parent basis's open questions

| Parent OQ | Effect of this position (if adopted by the PRD) |
|---|---|
| Q2 / Q3 (persistence, authority) | Narrowed: authoritative store is git-tracked per-level registers; any database is a derived, rebuildable index the service never owns |
| Q5 (promotion warrant) | Narrowed: promotion rubric is the source corpus's HOLD-centered trigger list (with its explicit NOTs), applied at triage — adapt it, do not re-derive it |
| Q8 (deterministic vs judgment operations) | Sharpened: scan/inventory/views/staleness = deterministic service ops; promotion/disposition/closure = Agent 1 / Agent 0 / human judgment acts |
| Q16 (service unavailable) | Answered by construction: registers and tags remain readable and writable as plain files; only the derived views degrade |
| Q7 (association levels) | Narrowed: register levels mirror authority tiers (§6.1); an Action Item's level is its escalation position, and elevation is a recorded move between registers |
| Q9 (assignments vs accountability) | Sharpened: RASCI adapted with A human-only invariantly (§6.1, consequence 3); agents may hold R/S/C/I |
| Q19 / Q20 (measurement, falsification) | Candidate metrics named in §5 above |
| Q18 (vocabulary) | Unchanged in substance; elevated in priority per owner agreement (#5) |

New authority-surface note for the PRD: the Action Item register makes Task
Management the first new owner of authoritative cross-cutting truth since the
domain engines. The PRD should give it the same explicit treatment
K-DOMAIN-1..4 gave engines: named ownership, protected paths, declared
agent-write rules.

## 8. Recommended handling by the PRD inquiry

1. Treat this addendum as a labeled input alongside the parent basis and the
   source corpus — orient from governed records first, use this as a
   challenge set, per the established review method.
2. Adversarially test §3–§6 (in particular: is Layer-1 recall against
   existing conventions actually high enough to defer Layer 2? and does the
   §6.2 register-as-lateral-channel reading hold up against the hidden-
   authority prohibition?).
3. Reconcile the promotion pipeline with every existing capture surface by
   name (TBD registers, Conflict Tables, open-issue sections, coordination
   notices, observation returns) — superseding, federating, or leaving each
   in place explicitly, so the anti-goal fails neither as a dump nor as
   fragmentation.
4. Adopt no bytes without a separate owner act.

No project execution tree, package, deliverable, agent-instruction change,
tool, schema, or implementation is created by this record.
