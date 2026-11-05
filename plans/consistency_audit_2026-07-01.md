---
title: "Seed-to-Leaf Consistency Audit — 2026-07-01"
date: "2026-07-01"
status: "audit report / durable findings catalogue"
authority: "generated view, not authority; on any disagreement the cited sources govern"
produced_by: "2026-07-01 seed-to-leaf consistency audit (seven layer inspections + adversarial verification), run at owner direction"
audit_basis: "repo HEAD ~`0d2956ccb` (post-First-PR merge `71a67d0b1`)"
owner: "repo owner"
target_workspace: "repo-wide (root docs, projects/*, tools/, skills/, docs/thesis/)"
claim_discipline: "K-CLAIM-1 applies: nothing below binds; findings are reported observations, dispositions are PROPOSALS (HumanRuling: TBD) unless a ruled record is cited"
---

# Seed-to-Leaf Consistency Audit — 2026-07-01

> **Generated view, not authority.** Sources govern on disagreement. Produced by
> the 2026-07-01 seed-to-leaf consistency audit (seven layer inspections +
> adversarial verification) at owner direction. K-CLAIM-1 applies: this report
> binds nothing; every disposition below is a PROPOSAL (HumanRuling: TBD)
> unless it cites a ruled record.

This report exists so the audit's findings and parked-item catalogue live in
the repo rather than only in a session transcript. Per `plans/README.md` this
surface is advisory and non-governing; it does not supersede `docs/PLAN.md`,
decision records, accepted snapshots, or handoff states.

## 1. Verdict

Consistency holds from the thesis seeds to the most distant artifacts. The
findings cluster into one systemic vocabulary gap (§3), a short list of
confirmed drift (§4), and quantified lint (§4, item 6). Nothing found
contradicts a ruled decision or a frozen acceptance basis.

## 2. Verified exemplars (what held, and how it was checked)

- **Capability invariance** — clean at every layer: zero authority conditioned
  on model identity. Sole boundary case: the LEGACY skill
  `dbm-concordance-seed` gates register-freeze *eligibility* on model tier —
  process trust, not authority.
- **Approval binding** — all 53 app-dev CHECKING deliverables carry one
  git-resolvable human approval SHA (verified live with `git cat-file`),
  enforced identically by `transition.ts`.
- **Issuance records** — piping's single ISSUED deliverable (DEL-01-01) and
  the R4 exit chain are exemplary human-ruling records.
- **Claim language** — zero unattributed tool/agent claims in ~8,850 triaged
  hits; now mechanically linted by the harness (`FORBIDDEN_CLAIM_WORDS`,
  16/16 tests).
- **Snapshot immutability** — empirically perfect: all 183 gate-snapshot
  files are single-commit; 21/21 chirality GATE6 hashes recompute
  byte-for-byte.
- **Fractal kit** — complete in all 38 skills.
- **Overlay discipline** — both project overlays tighten, never weaken, the
  K-* floor.
- **Harness conformance** — the landed harness matches every ruled
  requirement: adapter-aware guard preconditions, `source_path` required by
  construction, byte-identical export copy.

## 3. Systemic finding — the S2 split

The epistemic labels ASSUMPTION / PROPOSAL / TBD are genuinely
operationalized. The warrant ladder UNWARRANTED → CITED → REVIEWED →
AUTHENTICATED is operationalized in **zero tools and one audit agent**; the
FACT label is used nowhere; `docs/TYPES.md` §10.5 maps no invariant to the
labeling act; and thesis ch. 5 §5.4 misattributes labeling enforcement to
R5/R6/R7.

**Disposition:** D-GOV-08 RULED: Option B (audit-time diagnostic), owner
ruling 2026-07-01.

## 4. Confirmed findings (adversarially verified)

1. **"CRITICAL findings" severity undefined** — `docs/TYPES.md` §10.4 and
   thesis ch. 6 use a severity term absent from the `SE_Design_Analysis` §7.3
   review enum. D-GOV-08 bundles the fix. *Thesis side executed 2026-07-02:
   ch. 6 and ch. 7 now cite the enum registered as TYPES §10.6 per D-GOV-08
   (owner-directed thesis reconciliation PR).*
2. **DEC-041 event count stale** — 42-vs-43. DEC-041 is snapshot-immutable, so
   the remedy is a forward reconciliation record (D-28 in the piping
   `_DECISIONS` surface; ruled O-A by the owner 2026-07-01), not an edit.
3. **AGENTS.md registry drift** — `AGENTS.md` indexes DELIVERABLE_TASK as live
   while the file exists only in gitignored `.archive/` (K-AGENTS-1
   registry-vs-narrative drift). *Resolved 2026-07-01: owner directed removal
   of the DELIVERABLE_TASK references (index row, narrative list, dispatch
   row); applied in the Phase 2 self-check-hardening PR alongside the GEN-9
   registry-currency check, whose live baseline now pins zero drift.*
4. **Thesis appendix A drift** — stale narrow K-PROV-1 wording, plus a false
   "reproduced faithfully from CONTRACT section 2" claim: the appendix omits
   exactly K-WRITE-2, K-AGENTS-1, K-DOMAIN-1..4 and three enforcement rows.
   *Resolved 2026-07-02: Appendix A regenerated from the live CONTRACT —
   all 27 invariants, the full §2 enforcement map, the general-form K-PROV-1,
   and as-of-date framing with the D-GOV-05 partial-ratification note
   (owner-directed thesis reconciliation PR).*
5. **NEW pointer break** —
   `projects/chirality-piping/execution/_Reconciliation/_LATEST.md` targets a
   file retired to `.archive/` on 2026-06-03 (commit `349a2ab33`). Newest
   surviving sibling is the 2026-05-03 SCA002 summary. Disposition: repointed
   to it with a dated note, 2026-07-01, per owner ruling.
6. **Quantified lint** — ~82 instruction/plan files carry machine-absolute
   paths (worst: the app-dev pi-assessment cluster, including 15 references
   into the external `/projects/pi` repo). Of ~95k total `/Users/` hits, ~91k
   are permitted run-record evidence.

## 5. Refuted by verification (recorded so they are not re-raised)

- **DEL-01-01 ISSUED no-SHA "finding"** — refuted; covered by the parked
  piping schema-alignment item. Narrow residue: a possible forward re-binding
  record attaching allowlist identity + commit SHA `8b8d1781d`.
- **Domain source-manifest "disclosure gap"** — refuted; a category error on
  reference time. Acceptance bases are frozen and intact. Benign residue: a
  disclosure *asymmetry* — two domains disclose post-acceptance source drift
  in open-issue registers, the chirality-piping domain does not.

## 6. Parked / low catalogue (durable home is this report)

Items below are low-severity, deferred, or fold into already-parked work. All
are PROPOSALS until the owner rules or a maintenance touch resolves them.

1. `AGENTS.md` DELIVERABLE_TASK index row correction (§4 item 3). *Resolved
   2026-07-01 per the owner-directed removal recorded there.*
2. OPS-K-AUTH-2 "if used" qualifier removal, at OPS-catalog reconciliation.
3. DAG APPROVAL_RECORDs lack git-SHA binding — fold into the parked piping
   schema alignment.
4. DEL-01-01 forward re-binding record (optional; §5).
5. Absolute-path relativization when files are next touched. Worst-5 list:
   `pi-agent-harness-assessment.md` (26), `pi-assessment/01` (22), `/03` (19),
   `/02` (19), `insp03_assessment_index` (18).
6. `create_snapshot_folder.sh` lacks a refuse-if-exists guard (legacy,
   pre-harness).
7. Piping-domain disclosure-symmetry note (§5, second residue).
8. Legacy `dbm-concordance-seed` model-tier wording — reword in evidence terms
   if the skill is revived.
9. Harness self-check, future check: `_LATEST` pointer target exists and is
   the newest sibling (would have caught §4 item 5). *Resolved 2026-07-01:
   landed as the GEN-7 pointer-currency check (PR #3, merge `12894ad3f`).*
10. App-dev `_Coordination/_LATEST` one-row decision-frontier lag
    (self-described discovery-only).

## 7. Thesis owner-revision pack (accumulated across 2026-07-01 sessions)

For the owner's next thesis revision pass; none of these are agent-editable
under the terminal-artifact rule without direction. *Direction given
2026-07-02: the owner authorized a full thesis reconciliation pass ("rectify
all defects as much as practicable, include previous audit findings"); the
items below were executed in that PR except where noted.*

- Appendix A regeneration from the current CONTRACT — or soften the
  faithful-reproduction claim to subset-as-of-SHA. *Executed 2026-07-02
  (regenerated; as-of-date framing).*
- Appendix A K-PROV-1 row update to the general-claim form. *Executed
  2026-07-02.*
- Ch. 4 §4.7.2 vs appendix A design-time list reconciliation (add K-CLAIM-1
  to ch. 4's list). *Executed 2026-07-02 (ch. 4 and ch. 8 lists updated to
  the live CONTRACT §2 map).*
- Glossary WRITE_SCOPE: 6-to-8 values. *Executed 2026-07-02.*
- Invariant-count 20/21-vs-27 sweep (ch. 6/7/8/10, appendices A/C).
  *Executed 2026-07-02: mutable counts removed from prose per the
  registries-over-count-prose rule.*
- CITE-key mismatches (Ji2023 family). *Executed 2026-07-02: chapter CITE
  keys normalized to references.md keys; missing entries (Ouyang2022,
  Lewis2020, Min2023, Bunge_ontology, SE_textbook cross-ref) added.*
- Ch. 5 §5.4/§5.3.4 labeling-enforcement attribution — executed 2026-07-01 as
  dated additions per the D-GOV-08 ruling; retained here for the pack's
  completeness. *The §5.4 table cell itself corrected 2026-07-02.*
- SPEC section-3.3-vs-3.2 citation nicety in §9.3.5. *Verified 2026-07-02:
  thesis §9.3.5 cites SPEC §3.3, which is the transition-rules section with
  the authorized-actor table — correct as written; no edit made.*
- The at-first-PR annotations for ch. 8/9 present-tense enforcement claims —
  guard and harness now exist; annotate at next owner revision. *Executed
  2026-07-02: dated notes added to ch. 8 §8.6.2 and ch. 9 §9.4.2.*

## 8. Method note

Seven opus layer inspections, census-then-sample coverage, adversarial
refutation of every significant finding; three inspector failures were re-run
to completion (~1.5M tokens total).

Standing observation: the system was healthiest at its extremities and
fuzziest in its self-descriptions — the harness's backlog is this report's
finding list.
