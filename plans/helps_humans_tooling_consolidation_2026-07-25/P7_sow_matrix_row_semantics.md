# P7 — Matrix row semantics and the AC→VER union (request item 8), plus the B8 boundary-owner disposition

**Disposition:** ADOPTED-PROPOSED
**Basis:** VERIFIED by byte-level read of `matrix_links` in this run. The
21-row/10-contract back-scan and the DEL-02-03 self-catch are
ASSERTED-UPSTREAM from `BATCH_B3_FANIN.md`.

## 1. The behaviour, stated exactly

`tools/scope_of_work/derive_review_checklist.py`, `matrix_links` (lines 60–84),
called once from `derive()` at line 90.

Per matrix row the function harvests **all** `AC-NNN` from cell 3 and **all**
`VER-NNN` from cell 4, then (lines 75–81) walks every AC and appends every VER
to that AC's list. It is a **full cross-product within the row**, not a
positional pairing. Given:

```
| OUT-001 | ... | ... | AC-001, AC-002 | VER-001, VER-002 | ... |
```

both AC-001 and AC-002 receive both VER-001 and VER-002. There is no notion of
AC-001↔VER-001 correspondence.

The request characterises this correctly: it is a **superset**, so no AC ever
loses its own method and coverage stays conservative — but REVIEW checklists
carry deterministic over-linkage noise, and byte-identical re-derivation (QA
item 18) can never reveal it, because the noise is deterministic.

Two additional VERIFIED observations not in the request:

- **Silent row drop.** Line 70 skips any row without exactly 6 cells or whose
  cell 0 is not a bare `OUT-NNN`. No diagnostic is emitted. Downstream,
  `derive()` raises at lines 100–101 ("AC has no links entry") or 119–120 ("AC
  has neither VER nor HUMAN_REVIEW") — errors that point at the AC while the
  actual fault is a malformed row. A misleading error is worse than a silent
  superset.
- **`HUMAN_REVIEW` is discarded when a cell also carries VER refs.** Line 74
  uses `re.fullmatch` against the *whole* cell 4, so `VER-001, HUMAN_REVIEW: x`
  fails the fullmatch and the human-review method is dropped while the VER refs
  survive via line 73. This mirrors `common.py:272` and may be intended, but it
  is unstated.

## 2. Why NOT to change the linkage

The obvious fix — intra-row positional pairing — is the wrong move:

1. It would **change the output** of `derive_review_checklist.py` for the 21
   affected rows across 10 accepted contracts, which the B3 fan-in already
   dispositioned as *accepted-as-conservative, no revision ordered*. Changing
   the deriver would silently invalidate that disposition.
2. Positional pairing is ambiguous by construction. `AC-001, AC-002` against
   `VER-001` has no positional answer, and `AC-001, AC-002` against
   `VER-001, VER-002, VER-003` has three.
3. QA item 18 requires byte-identical repeated derivation. That is preserved
   either way, but a linkage change makes old and new checklists differ, which
   is exactly the drift class this contract exists to prevent.

**The defect is not in the deriver's arithmetic. It is that the row semantics
were never stated.** Fix the contract, and warn where the contract is not met.

## 3. Proposed changes

### 3a. State the row semantics — `skills/scope-of-work/SKILL.md`

ADD to the Non-negotiable constraints block:

```
- In the Output and Evaluation Matrix, a row's verification references apply to
  every acceptance criterion in that row. Group acceptance criteria in one row
  only when the row's verification set is exactly the union of those criteria's
  own methods; otherwise give each acceptance criterion its own row. Checklist
  derivation is row-scoped and cannot recover a finer pairing.
```

### 3b. Make it checkable — `skills/scope-of-work/QA_CHECKS.md`

ADD as item 20 (after P6's item 19, if P6 is also adopted; otherwise item 19).
Item 20 is mode-agnostic; P1 §2e(ii) carries the canonical QA mode-scoping
header and already names it. **If P7 is adopted without P1**, add alongside it:
"Item 20 applies to every mode."

```
20. No Output and Evaluation Matrix row carries multiple `AC-*` with a
    verification set larger than the union of those criteria's own methods; the
    derived checklist entry for each `AC-*` names no method that does not
    verify it.
```

### 3c. Add a deriver warning — `tools/scope_of_work/derive_review_checklist.py`

The minimal, non-breaking change: detect the over-linkage shape and warn on
stderr without altering the derived JSON.

INSERT after line 73 (`verification_refs = ver_re.findall(cells[4])`):

```
        if len(acceptance_refs) > 1 and len(verification_refs) > 1:
            print(
                f"WARNING: matrix row {cells[0]} groups {len(acceptance_refs)} "
                f"acceptance criteria with {len(verification_refs)} verification "
                f"methods; every criterion in this row will receive all "
                f"{len(verification_refs)} methods. Split the row for exact "
                f"1:1 linkage.",
                file=sys.stderr,
            )
```

(`sys` is already imported.)

**Why stderr and not a failure:** the derived JSON is unchanged, so QA item 18
byte-identity holds and the 10 accepted contracts stay valid. The warning makes
the previously-invisible condition visible at authoring time — which is exactly
where DEL-02-03's authoring run caught it unaided.

### 3d. Optionally, surface the silent row drop

Also worth adding at line 70, but **not** bundled with the above — it is a
different defect and may change behaviour for contracts with unusual matrix
formatting:

```
        if len(cells) != 6 or not out_re.fullmatch(cells[0]):
            if len(cells) > 1 and any(ac_re.search(cell) for cell in cells):
                print(
                    f"WARNING: matrix row skipped ({len(cells)} cells, "
                    f"cell 0 = {cells[0]!r}) but it contains AC references; "
                    f"downstream 'unlinked AC' errors may originate here.",
                    file=sys.stderr,
                )
            continue
```

**Owner's call.** Recommended, because it converts a misleading downstream
error into an accurate upstream one, but it warrants its own test.

## 4. The B8 boundary-owner validator candidate — declined for the register validator

`BATCH_B8_FANIN.md` §3.1 nominated, for the OI-013/item-2 consolidation:

> a checkable rule: every act enumerated in a boundary-exclusion requirement
> resolves to a named owner in the cited claim

**Disposition: DECLINED as a check in `validate_decomposition_registers.py`;
ADOPTED-PROPOSED as a separate `tools/scope_of_work/` capability plus a skill
QA method.**

Reasons:

1. **Wrong input grammar.** The register validator's domain is CSV registers.
   This rule reads `ScopeOfWork.md` prose — requirement bodies and claim
   bodies. Giving one tool two input grammars and an undeclared semantic
   dependency is precisely the territory violation the component standard
   guards against.
2. **Only half of it is deterministic.** "Every act *enumerated in* a
   boundary-exclusion requirement" requires segmenting a natural-language
   sentence into acts. That is semantic judgment, and tools do not do semantic
   judgment. What *is* deterministic is the second half: given a set of
   act→owner citations, check that each cited owner ID resolves to a defined ID
   in the named claim.
3. **The recurrence record is skill evidence, not tool evidence.** Three
   appearances (B6-F2, B8-F1, caught at authoring in B7) of a check that a
   dispatched agent was briefed to perform and did not. That is a method that
   should be a named, repeatable QA step — a skill concern.

**Proposed split, for a later design pass:**

- **Skill (`scope-of-work` QA):** a stated method — "for each
  boundary-exclusion requirement, enumerate its acts and name an owner for
  each, citing the claim that carries the owner" — plus a QA item asserting
  one-for-one coverage. This is where the semantic work lives.
- **Tool (`tools/scope_of_work/`):** a checker for the deterministic half —
  every owner ID cited in a boundary-exclusion requirement resolves to a
  defined ID in the cited claim. `common.py` already supplies the section and
  ID machinery.

Not built in this tranche: it needs its own design pass and the owner's ruling
on the semantic/deterministic split. Recorded so the B8 nomination is not lost.

## 5. Compatibility

- 3a and 3b are contract text; 3c adds stderr output only. Derived checklist
  JSON is byte-identical in all cases, so QA item 18 and the 10 accepted
  contracts are unaffected.
- 3c should ship with a test in a `tools/scope_of_work/` test file asserting
  (i) the warning fires for a multi-AC/multi-VER row and (ii) the derived JSON
  is unchanged by its presence.
- The B3 fan-in's "accepted-as-conservative, no revision ordered" disposition
  stands. Nothing here reopens it.
