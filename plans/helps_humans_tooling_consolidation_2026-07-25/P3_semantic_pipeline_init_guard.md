# P3 — `validate_semantic_pipeline_scope.py`: add `--step init` (request item 4)

**Disposition:** ADOPTED-PROPOSED
**Basis:** VERIFIED by read of the tool and its only importer.
**Priority:** repo-general hygiene. The request itself notes PEC ruled Q1=(b)
(semantic pipeline unused for PEC), so nothing is blocked on this.

## 1. The gap

`STEP_CHOICES` (line 32) is `(*STEP_ALLOWED, "p3", "sow-p3")`, which unpacks
the `STEP_ALLOWED` dict's keys — so the live choice set is
`("semantic", "lens", "p3", "sow-p3")`. There is no `init`, and argparse
(line 45) rejects `--step init` with exit 2 before any logic runs.

A `MODE=INIT` scope-of-work run therefore has no write-scope guard at all,
while every other pipeline step has one.

Step names are branched on in exactly five places: lines 45 (argparse), 92 and
94 (allow-list selection), 129 and 144 (format-resolution gate). The tool is
table-driven, so the change is small.

## 2. Proposed exact-text change

REPLACE lines 26–29:

```
STEP_ALLOWED = {
    "semantic": {"_SEMANTIC.md", "_STATUS.md"},
    "lens": {"_SEMANTIC_LENSING.md"},
}
```

WITH:

```
STEP_ALLOWED = {
    "init": {"ScopeOfWork.md", "_STATUS.md"},
    "semantic": {"_SEMANTIC.md", "_STATUS.md"},
    "lens": {"_SEMANTIC_LENSING.md"},
}
```

That single insertion flows automatically into `STEP_CHOICES` (line 32), into
the argparse choices (line 45), and into the allow-list dispatch at line 92
(`if step in STEP_ALLOWED`). `_run_records/` is already covered by
`ALWAYS_ALLOWED_PREFIXES` (line 33). No other line needs to change for the
basic guard.

### Derivation of the allowed write set

`{"ScopeOfWork.md", "_STATUS.md"}` is pinned by three independent sources:

1. `agents/AGENT_PROJECT_SETUP.md:304-306` — the Phase 2.2 dispatch specifies
   `MODE: INIT` with "`STATUS_POLICY` and exact `ScopeOfWork.md` write target".
2. The calibrated git-status formula in
   `projects/pec/execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md:406-410`:
   "exactly n new `ScopeOfWork.md`, n modified `_STATUS.md`, n+1 run-record
   additions … Zero other paths."
3. Observed post-INIT deliverable contents across the D-PEC-63 wave.

`_STATUS.md` is included because the wave's INIT runs perform an authorized
status act. Under a `NO_STATUS_TOUCH` brief the file is simply unmodified, and
an allow-list is permissive, not mandatory — so one entry serves both postures.

## 3. Optional stricter variant (owner's call)

`--step sow-p3` fails closed when the production format is *not* already
`SOW_V1` (lines 144–146). `init` is its mirror image: it should arguably fail
closed when a production contract *already exists*, per `SKILL.md:32` —
"`INIT` requires no production contract".

To add that, extend line 129 from `if args.step in {"p3", "sow-p3"}:` to
`if args.step in {"init", "p3", "sow-p3"}:` and add after line 146:

```
        if args.step == "init" and production_format in {"SOW_V1", "MIGRATION_DUAL"}:
            print("ERROR: init requires no existing production contract", file=sys.stderr)
            return 2
```

**Recommended: adopt the basic guard now, defer the stricter variant.** The
format-resolution path has its own fail-closed semantics and an inverted gate
deserves its own test before it can block a run. Do not adopt the strict
variant without adding a test for it.

## 4. Open question the owner should rule on

`skills/scope-of-work/TOOL_POLICY.md:11-18` names intermediate artifacts —
evidence candidate, finalization report, claim map, parity report, review
checklist. None appear in the observed post-INIT file set, which implies they
either land outside the deliverable folder or are not produced under INIT
(P1 proposes the latter explicitly). **If P1 is adopted, this is settled and
the two-entry allow-list is correct.** If P1 is not adopted, confirm where
those artifacts land before this guard goes live, or a conforming INIT run
could be failed by it.

## 5. Compatibility

- **One code caller**, and it is safe: `tools/validation/test_semantic_artifact_validators.py:15`
  imports the pure function `validate_changed_paths`, not `main`. Adding a
  dict key cannot affect it.
- **Protocol callers all use existing steps** and are unaffected:
  `agents/AGENT_PROJECT_SETUP.md:412` (`--step semantic`), `:433` (`--step lens`),
  `:458` (`--step p3`); `skills/lens-register/SKILL.md:80` and
  `TOOL_POLICY.md:25`; `skills/semantic-matrix-build/TOOL_POLICY.md:34`;
  `docs/governance_harness/FOUR_DOCUMENT_CONSUMER_INVENTORY.md:63`.
- **Test to add** alongside the change, in
  `tools/validation/test_semantic_artifact_validators.py`, following the
  existing per-step pattern: an `init` run allowing `ScopeOfWork.md`,
  `_STATUS.md`, and `_run_records/...`, and rejecting `_SEMANTIC.md`.
  This proposal does not write that test; it should land in the same tranche as
  the change.
- **Registry:** `tools/REGISTRY.md`'s row for this tool does not enumerate step
  names, so no registry edit is needed. Confirmed by read.
