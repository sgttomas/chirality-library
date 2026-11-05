# ADOPTED design brief — PEC embedded upload agent (D-PEC-07 O-C, design-only track)

> **Epistemic status: ADOPTED design brief — implementation still gated.**
> Prepared under the D-PEC-07 O-C ruling (2026-07-05) and adopted by owner
> ruling on 2026-07-05. Adoption authorizes no implementation; implementation
> still requires a future tranche authorization opening the exact pec source
> fence (F-PEC-1). The §16 contracts, profile
> `operation_proposal_contract`, and ADR-002 zero-dependency posture govern.

## Adoption ruling (2026-07-05)

Owner ruling of record (verbatim, 2026-07-05, in-session, Ryan Tufts):

> S-3 (brief): I adopt the brief. Change its status from CANDIDATE to ADOPTED and record
> this adoption ruling in it. Adoption authorizes NO implementation: I am deferring the
> source-tranche gate — do not author or request a tranche, and the F-PEC-1 fence stays
> closed. One adoption rider (RV-12): the LLM-backed-mapper step remains gated on a future
> D-T0-14 residency ruling; the adopted brief must state that routing instance content to
> an external model is not authorized under the current CLOSED residency. All other brief
> fixes (RV-13 K-AUTH-2/hash binding, RV-14 CSV-only v1, and RV-15 through RV-21) are
> deferred to the tranche packet as named obligations and need not be applied now.

Adoption closes only the brief-adoption gate. The source-tranche gate remains
deferred; no tranche is authored or requested by this adoption.

> **RV-12 rider annotation (2026-07-06, dated pointer — no rewrite of the
> adopted text):** the "future D-T0-14 residency ruling" the rider gates on
> has now been made: tier-0 `D-T0-20` (residual of D-T0-14) RULED O-B
> 2026-07-06 — LLM-hosted agent sessions may read, and route to the
> owner-configured model provider, exactly the enumerated surface (i)–(iv)
> under the agent person's RBAC, `is_admin=0`; everything unenumerated stays
> CLOSED; the mutation basis (scratch/demo only) is unchanged. Ruling
> verbatim: `_DomainEngines/_DECISIONS/D-T0-20_pec_harness_agent_residency.md`.

## Goal (owner's words, D-PEC-07)

"I want the embedded agent to accept a file upload from me and take action
accordingly to update things. That's one end goal."

## Design sketch

In-app flow mirroring the proven file-drop pathway, as first-class records:

1. **Upload** — new RBAC'd route (`config.manage`) accepting a spreadsheet/
   CSV upload; stored content-addressed (SHA-256) outside the DB; size-capped.
2. **Proposal record** — an `import_proposal` record per the profile's
   operation_proposal_contract lifecycle (`draft → ready_for_review →
   accepted → rejected → applied`): source file hash, detected/declared
   contract, agent-produced mapping (reusing `IMPORT_TEMPLATES/
   IMPORT_MAPPING.md` shapes), mapped-CSV preview, dry-run report
   (accepted/updated/conflict/reject counts + row detail) computed against a
   transaction that is rolled back.
3. **Agent seam** — the mapping/dry-run step is where the agent acts. v1 can
   be deterministic (known shapes from IMPORT_MAPPING.md); an LLM-backed
   mapper slots in behind the same proposal record later without changing the
   lifecycle. Under the current D-T0-14 CLOSED residency, routing instance
   content to an external model is not authorized; any LLM-backed mapper that
   sees instance content remains gated on a future D-T0-14 residency ruling.
   The agent NEVER applies.
4. **Human accept + apply** — accepting the proposal is an RBAC'd in-app act;
   apply executes the real `importContract` in a transaction, links the
   resulting import history to the proposal, and closes it `applied`.
   `force` remains a separate explicit control, default off.
5. **Audit** — proposal + apply land in history/audit like §16 imports today.

## Prerequisite repairs riding this tranche (from D-PEC-01 evidence)

- RAIL unanchored-row idempotency: match intake rows by imported `item_id`
  on re-import (evidence-03 seam finding) so re-drops update instead of
  duplicating.
- Multi-file schedule support: accept the schedule extractor shape (see
  evidence-04 mapping) natively or via stored mapping profiles.

## Out of scope

Auto-apply, agent-initiated imports, `force=true` defaults, non-import write
actions, SSO — all unchanged. No pilot-readiness or go-live implication.

## Adoption gate

This brief is adopted. Next lawful step, only on future owner direction:
TOOLMAKER-style tranche packet with exact file fence under
`projects/pec/{server,web,core}/**` + tests → owner authorizes →
implementation PR(s) with the standing belt-and-braces checks.

## Deferred tranche-packet obligations

The adoption ruling defers these review findings to the future tranche packet;
they are not applied by this brief-adoption edit:

- RV-13: K-AUTH-2/hash binding, proposal-version binding, and stale-proposal
  refusal semantics.
- RV-14: CSV-only v1 or a separate dependency/runtime ruling.
- RV-15: history-vs-audit choice for proposal/accept/apply records.
- RV-16: permission naming for upload, map, accept, apply, `force`, and read
  access to stored raw files/previews.
- RV-17: dry-run/apply deterministic contract, preview stability,
  stale-dry-run detection, and apply-failure lifecycle handling.
- RV-18: evidence-04 schedule wording and dry-run report field completeness.
- RV-19: upload-store lifecycle, backup/restore relationship, retention,
  deletion, MIME/extension policy, project scoping, and read-side RBAC.
- RV-20: coordination precedent note.
- RV-21: CSRF posture.
