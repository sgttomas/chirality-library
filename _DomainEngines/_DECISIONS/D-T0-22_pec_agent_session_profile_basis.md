# D-T0-22 — pec agent session-profile basis (harness capability egress)

**Status:** RULED 2026-07-07 (owner launcher steer, verbatim below).
**Date prepared:** 2026-07-07
**Decision ID:** D-T0-22 (residual of `D-PEC-21`'s retained-restriction
rationale, per the 2026-07-03 residual-row convention)
**Prepared by:** PEC work loop agent. The direction act is the owner's
(K-AUTH-1; D-GOV-04) and was received in the launcher steer before this
packet existed; the packet records it verbatim and gives it a register home,
following the D-T0-19/D-T0-20 in-session-steer precedent. Companion source
tranche: pec-local `D-PEC-22`.

## Why this row exists

The D-PEC-21 packet's retained-restriction rationale (2026-07-07) kept the
SDK session hermetic — `tools: []` (no built-in filesystem/shell/web tools)
and `settingSources: []` (no user/project settings, hooks, skills, or
`~/.claude` MCP servers) — because the sidecar subprocess runs as the owner's
OS user: built-in tools would let the model read machine content outside the
agent person's RBAC and the D-T0-20/21 residency basis, with everything read
egressing to the model provider. That packet earmarked widening as "a
residency/mutation-basis decision — its own future tier-0-companion row if
the owner wants it, not a default."

The owner now wants it, as an opt-in profile.

## Owner direction of record (2026-07-07, launcher steer, Ryan Tufts, verbatim)

> Now add in functionality for `tools: []` and `settingSources: []` and my
> rationale is adding yet a higher level of agent capability, so I can test
> the limits before this app is actually used.  You are already an agent
> with such abilities and I manage just fine.  Don't remove any of the
> previous restrictions from the code, just allow a profile for the agent
> that permits these to be used.

## Recorded interpretation (agent)

A second, config-selected **session profile** for the SDK engine, exactly
parallel to the D-T0-21 access-basis mechanism:

- `PEC_AGENT_SESSION=hermetic|open`, **default `hermetic`** — the ruled
  D-PEC-21 hermetic session byte-for-byte as shipped; nothing existing is
  removed or weakened.
- `open` (owner-selected per launch, an env act at his screen, never a
  stored default): the SDK session runs with its built-in tool set enabled
  (the `tools: []` restrictor is not applied) and
  `settingSources: ['user','project','local']` (the harness's normal
  settings surface), for designer/sole-user limit-testing before real use.
- **Excluded regardless of profile** (unchanged, structural): the pec
  human-act boundary — no accept/apply/reject-of-others/`force`/conversion-
  disposition tool exists on the bounded acts surface in either profile; the
  D-T0-21 access basis and clamp are untouched (an `open` session still
  reads pec records only through the basis-clamped pec tools); loopback-only
  transport; credential hygiene.
- **Disclosure:** the active profile is stated on `/agent/health` alongside
  the access basis — never widened silently.

## Residency note (what `open` egresses)

Under `open` the model may read owner-machine content via the harness's own
tools as the owner's OS user, and everything read egresses to the model
provider. This is precisely the consequence the D-PEC-21 rationale named;
the owner's direction accepts it knowingly for limit-testing ("You are
already an agent with such abilities and I manage just fine"). pec
instance-content visibility remains governed by D-T0-20/21; the real/
non-scratch mutation basis remains its own future row, unmoved.

## Human ruling

**RULED — 2026-07-07** by the owner direction quoted verbatim above
(launcher steer; K-AUTH-1). Mechanism per the recorded interpretation;
source tranche executes under pec-local `D-PEC-22` inside its fence.
