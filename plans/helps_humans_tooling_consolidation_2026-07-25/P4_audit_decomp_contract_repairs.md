# P4 — AUDIT_DECOMP contract inconsistencies (request item 5)

**Disposition:** ADOPTED-PROPOSED (AMENDED — the request's framing is
insufficient in one place and incomplete in another)
**Basis:** VERIFIED by byte-level read of `agents/AGENT_AUDIT_DECOMP.md` and of
all five emitted `coverage_summary.json` files in the repo.

## 1. Why the request's framing needs amending

The request says: "IssueLog schema declares `CheckNumber` 1–11 while SPEC runs
12 checks". Both halves are true, but the implied fix — widen the range to
1–12 — **would still be wrong.**

The 12 checks are numbered **1, 2, 3, 4, 5, 6, 7, 8, 9, 9b, 10, 11**
(headings at lines 195, 204, 213, 227, 239, 256, 273, 289, 303, 325, 341, 359).
Check `9b` is not an integer. The schema declares
`| `CheckNumber` | integer | 1–11 (maps to check name) |` — so the declared
**type** is as wrong as the declared range, and no range widening can fix it.

The document already asserts 12 in three places (line 389 "all 12 checks",
line 433 `"check_count": 12`, line 462 SPEC), so the count is settled; only the
schema row disagrees.

**The invalid `CheckNumber=96` row** shipped by SCA-002 (ASSERTED-UPSTREAM from
the request) is consistent with an authoring agent with no valid value to
write for a check outside the declared domain.

## 2. Proposed exact-text changes

### 2a. `CheckNumber` type and domain — line 498

REPLACE:

```
| `CheckNumber` | integer | 1–11 (maps to check name) |
```

WITH:

```
| `CheckNumber` | string | One of `1`–`9`, `9b`, `10`, `11` (maps to check name). Not an integer: check `9b` is a lettered sub-check. Any value outside this set is invalid |
```

**Alternative the owner may prefer:** renumber `9b` → `10` and shift
`10`, `11` → `11`, `12`, restoring a clean integer domain `1`–`12`. That is
cleaner long-term but is a much larger diff — `### Step 9b` at line 325 and
every downstream reference would move, and prior IssueLog rows and snapshots
citing `10`/`11` would silently change meaning. **Recommendation: adopt the
string form above.** It is truthful about the current contract and breaks
nothing. Renumbering, if wanted, belongs in its own tranche with a migration
note.

### 2b. `coverage_summary.json` schema template — the two additive fields

The two fields named in the request are emitted by all three `pec` runs at a
stable insertion point: immediately after `objective_coverage_pct` and before
`package_shape_conformance`.

INSERT after line 424 (`     "objective_coverage_pct": 0.0,`):

```
     "deliverables_without_objective_mapping": 0,
     "in_ledger_rows_without_objective_mapping": 0,
```

(five leading spaces, matching the surrounding keys)

### 2c. Fix the mis-indented sibling key — line 426

VERIFIED incidental defect in the same block. Line 426 carries four leading
spaces where every sibling has five.

REPLACE:

```
    "derivative_package_status": "PASS|WARN|FAIL|SKIPPED",
```

WITH:

```
     "derivative_package_status": "PASS|WARN|FAIL|SKIPPED",
```

## 3. Two further drifts NOT in the request (VERIFIED)

The request names two additive fields. Scanning all five emitted files found
**two more** schema violations, both in
`projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_004_POSTCHANGE_2026-07-23_2027/coverage_summary.json`:

1. **Lines 10–16 emit a `repository_topology` object absent from the template
   entirely:**
   ```
     "repository_topology": {
       "packages": 10, "deliverables": 51, "objectives": 10,
       "scope_items": 78, "ledger_rows": 78
     },
   ```
2. **Line 40 sets `"closure_readiness": "READY_FOR_IMPLEMENTATION_HANDOFF"`,
   outside the template's declared enum `"PASS|WARN|FAIL"` (line 436).**

Emitted-file inventory:

| Path | Two named fields | Other drift |
|---|---|---|
| `pec/.../COV_SCA002_PRECHANGE_2026-07-25_1040/` | yes (26, 31) | — |
| `pec/.../COV_SCA002_POSTCHANGE_2026-07-25_1252/` | yes (9, 11) | — |
| `pec/.../COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/` | yes (9, 11) | — |
| `chirality-app-dev/.../COV_SCA_APP_004_PRECHANGE_2026-07-23_1330/` | no | — |
| `chirality-app-dev/.../COV_SCA_APP_004_POSTCHANGE_2026-07-23_2027/` | no | `repository_topology`; out-of-enum `closure_readiness` |

**Proposed handling — owner's ruling needed on which way each goes.** Each of
these is either a template gap (adopt the field) or a bad emission (the run was
non-conforming). They are not equivalent:

- `repository_topology` looks like a genuinely useful addition; recommend
  **adopting** it into the template as an optional object.
- `READY_FOR_IMPLEMENTATION_HANDOFF` is a *lifecycle* value in a *readiness*
  field whose enum is a three-way verdict; recommend treating it as a **bad
  emission**, not widening the enum.

No exact-text diff is offered for these two pending that ruling.

## 4. The root cause, and why the schema is the only fix surface

**No tool generates `coverage_summary.json`.** `grep -rln "coverage_summary"
tools/` returns exactly one hit and it is a retirement note
(`tools/REGISTRY.md:328`, recording that `serialize_workspace_state.py` was
superseded by this JSON). The file is authored free-hand by the AUDIT_DECOMP
agent from the prose template.

(That citation is line 328, not 327: this packet's own added registry row for
`validate_decomposition_registers.py` shifted it by one. Noted because a
line-pinned citation that drifts is the same defect class as P5's.)

That explains all four drifts: there is no code path to constrain the output,
so the template is simultaneously the specification and the only enforcement.
Five emissions have produced four distinct divergences.

**Candidate for a later tranche, not proposed here:** a
`tools/validation/validate_coverage_summary.py` that checks an emitted
`coverage_summary.json` against the declared schema. That would convert this
from a prose contract into a checkable one — squarely the
"deterministic work becomes tools" principle. It is not proposed now because
the schema must be made correct *first* (this proposal), or the validator would
encode the current defects. Sequence: adopt P4 → then build the validator.

## 5. Compatibility

- All three proposed edits are contract text in a single agent file; no tool,
  caller, or registry changes.
- Existing snapshots are unaffected — they are immutable historical artifacts,
  and the two `pec` runs' extra fields become conforming rather than
  undeclared once 2b lands.
- Rerun `python3 tools/validation/validate_agent_instructions.py agents/AGENT_AUDIT_DECOMP.md`
  after the change (it validates structure, required sections, and reference
  ranges; none of these edits touch those, but the check is cheap).
- Note P5 in this packet also edits `AGENT_AUDIT_DECOMP.md` (the Variant
  Section Binding table at lines 110–115). The two proposals touch disjoint
  line ranges and can land together or separately.
