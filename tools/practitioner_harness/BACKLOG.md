# Practitioner Harness — Development Backlog

> **Epistemic status: queued work — not authority, not a status surface.**
> Items here are candidate harness development, recorded so intent survives
> across sessions. Execution follows the established harness pattern: branch +
> PR, owner merges (PR #12/#13 precedent); any change that moves a pinned live
> measurement carries its conscious pin update in the same PR
> (`test_live_baseline.py`'s own convention). Remove an item by PR when done
> or when the owner declines it. Provenance: bridge-loop reflection of
> 2026-07-02 (`_DomainEngines/bridge/LOOP_RECEIPTS.md`, Receipt 0) unless
> noted.

| ID | Item | Gate | Source | Status |
|---|---|---|---|---|
| HB-PEC-1 | Make domain-engine profile observation multi-profile-safe, add PEC aliases/register/profile/project awareness, extend reference resolution for `projects/pec`, move the staged PEC profile into `_DomainEngines/profiles/pec.yaml`, and carry conscious live-baseline pin updates. | D-T0-16 O-A ruled; execute only after PR #51 merges and D-T0-11/D-T0-12 ruling records are published | `projects/pec/execution/_Coordination/AgentRuns/PEC_2026-07-04_tier0-prep/TOOLMAKER_BRIEF-harness_pec_registration.md` | executing on `codex/pec-harness-tranche`; includes PEC DRAFT + Gate 2 open test rider |
