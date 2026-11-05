# D-T0-20 - PROPOSAL: pec instance-content visibility for LLM-hosted agents (residual of D-T0-14)

**Status:** RULED — O-B affirmed by owner 2026-07-06 (verbatim below).
**Date prepared:** 2026-07-05
**Decision ID:** D-T0-20 (residual of `D-T0-14`, 2026-07-03 residual-row convention)
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the residual-row packets `D-T0-17`/`D-T0-18` and the
frame-only shape of `D-T0-14_pec_data_residency.md`.

## Why this row exists now

D-T0-14 was **deferred with the O-A CLOSED default kept in force**, and the
owner's deferral reasoning asked for exactly this moment (verbatim, from the
D-T0-14 packet):

> Let D-PEC-01 preparation force the O-B ruling with a concrete data case in
> front of you, rather than pre-authorizing egress in the abstract.

The concrete case has now arrived, three times over, and it is broader than
the per-run capture bases D-PEC-01 has been granting:

1. **The weekly workflow (D-PEC-10 O-A).** The owner's ruled intent makes the
   agent "the primary means of making updates" across five source documents.
   Triage of real intake items requires the agent to *read those items* —
   instance content — and the 272-item real-data triage run is already parked
   on an owner visibility-basis confirmation (D-PEC-10 packet, Scope note 4).
2. **The harness bridge (`D-T0-19`).** An app-dev-hosted agent is a Claude
   Agent SDK session: every tool result it reads — dry-run reports, row-level
   errors, intake items — is routed to the model provider (Anthropic API).
   Under CLOSED, that routing is not authorized for real instance content.
3. **The built-in agent UI (`D-PEC-16`).** The adopted upload-agent brief
   carries the RV-12 rider: "the LLM-backed-mapper step remains gated on a
   future D-T0-14 residency ruling; … routing instance content to an external
   model is not authorized under the current CLOSED residency." This row is
   that future ruling's home.

Without this row, every real-data agent act needs a fresh per-run enumeration
(the D-PEC-01 pattern), which cannot carry a weekly standing workflow.

## Decision to rule

What pec instance content an LLM-hosted agent (loop agent, harness-hosted
agent, or built-in-UI agent — all are external-model sessions) may read in the
course of the ruled workflows, and therefore what may be routed to the
owner-configured model provider.

## What this row changes (and what it does not)

Changes (under O-B or O-C): the standing visibility basis for agent sessions
on real data — replacing per-run enumerations for the covered surfaces.

Does NOT change: pec RBAC and person-bound attribution (the agent person's
visibility is still bounded by its role grant); K-AUTH-1/K-DOMAIN-3 human-only
acts; K-DOMAIN-4 professional-boundary claims; the D-PEC-01/RV-11 conventions
for what may be **committed** to the repo (capture limits are a separate
question from model visibility — a materially new data source still needs
fresh owner confirmation of capture limits before its exports are committed);
**the mutation basis** — this row rules visibility/egress only; the D-PEC-10
scratch/demo-basis rider and the deferred pilot-DB basis (owner 2026-07-05:
"Another time") stand, so agent operation against a real/non-scratch DB needs
its own future row regardless of what this one rules;
`_DomainEngines/profiles/pec.yaml` `data_residency` until the ruled option's
mechanism updates it; piping's engine-specific D-T0-04 OPEN ruling (unrelated
regime).

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Keep CLOSED. Agent sessions on real data see only owner-dropped file content, count-level report summaries, and row-level errors for the dropped rows themselves (the D-PEC-12 §4 baseline). | No standing workflow on real data: triage of real intake items, LLM mapping over instance content, and the harness bridge's real-data use all stay blocked or per-run-enumerated; the built-in UI ships deterministic-only. |
| O-B | **Enumerated OPEN surface.** Agent sessions may read, and route to the owner-configured model provider, exactly: (i) intake items and their dispositions; (ii) `import_proposal` records, dry-run/apply reports, and import-related history entries; (iii) the profile's `chirality_readable_artifacts` set as enumerated in `_DomainEngines/profiles/pec.yaml` (register export CSVs, sponsor-brief/package-pack renders, Explain payloads, ImportReport JSON, the committed README/docs/fixtures files, and scratch/owner-approved drill/backup/restore evidence); (iv) owner-dropped weekly files. All under the agent person's RBAC visibility, `is_admin=0`. Anything outside the enumeration stays CLOSED. | The ruled weekly workflow, the bridge, and the built-in UI's LLM features all become **visibility-lawful** on real data under one standing basis (the mutation basis for a real/non-scratch DB remains its own future row); the enumeration is auditable against the profile and RBAC; egress remains bounded to the owner-configured provider. |
| O-C | Full OPEN (piping D-T0-04 parity): the agent may see any instance content its RBAC visibility reaches. | Simplest to operate; gives up the enumerated audit surface for a pilot dataset that includes real project execution content. |

## Recommendation (non-binding)

O-B. It is the smallest surface that makes the owner's ruled workflows real,
it is checkable (the enumeration maps one-to-one onto profile-named artifact
classes and RBAC-visible record types), and it preserves CLOSED as the default
for everything unenumerated. O-C is defensible for a single-operator local
pilot, but O-B loses nothing the ruled workflows need.

## On ruling (mechanism)

Record the ruling verbatim here and in the register row. O-B/O-C: one
execution PR updates `_DomainEngines/profiles/pec.yaml` (`data_residency`
value and open-issue annotation; validator re-run VALID), annotates the RV-12
rider in the adopted upload-agent brief with a dated pointer to this ruling
(no rewrite of the adopted text), and records the basis in the pec register;
the D-PEC-10 Scope-note-4 visibility confirmation for the 272-item run is
thereby either discharged (if the owner says so in the ruling) or remains a
separate owner act. O-A: the row closes; per-run D-PEC-01-style bases remain
the only path to real content.

## Human ruling

**Ruling:** O-B. Owner ruling of record (2026-07-06, in-session steer, Ryan
Tufts, verbatim):

> D-T0-20: I rule O-B, the enumerated OPEN surface exactly as listed
> (i)–(iv), under the agent person's RBAC, is_admin=0. This ruling also
> discharges the D-PEC-10 Scope-note-4 visibility confirmation for the
> 272-item run. The mutation basis is unchanged: scratch/demo only — agent
> operation against my real/non-scratch DB still requires its own future
> row. For clarity: the pilot-scratch instance is within the scratch/demo
> mutation basis, so the 272-item triage run may proceed on it.

**Ruling SHA:** received with `main` at `4c636e53e` (tag
`pre-bridge-session-2026-07-06`); published by this packet's PR.

**Mechanism executed (same PR):** `_DomainEngines/profiles/pec.yaml`
`data_residency` updated to the O-B enumerated-OPEN value with a dated
open-issue annotation (validator re-run VALID); the RV-12 rider in the
adopted upload-agent brief annotated with a dated pointer to this ruling (no
rewrite of the adopted text); basis recorded in the pec register (pointer row
`D-PEC-18`). The D-PEC-10 Scope-note-4 visibility confirmation for the
272-item run is discharged by the ruling text above; the mutation basis is
untouched — scratch/demo only, with the pilot-scratch instance inside that
basis per the ruling's clarity sentence.
