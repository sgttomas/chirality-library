# P1 — scope-of-work: explicit INIT-mode branches (request item 1)

**Disposition:** ADOPTED-PROPOSED (AMENDED — widened from 3 files to 4)
**Basis:** VERIFIED by byte-level read of all four companion files and of
`tools/scope_of_work/map_scope_of_work_claims.py` and
`report_scope_of_work_parity.py` in this run. Canary evidence
(three `MODE=INIT` runs) is ASSERTED-UPSTREAM from the routed request.
**Priority:** this is the D-PEC-63 canary-halt dependency (request §preamble).

## 1. The defect, stated precisely

`SKILL.md` declares three modes in Method steps 1–3 and then silently collapses
to a CONVERT-only pipeline in steps 4–7. The same collapse occurs in
`TOOL_POLICY.md` steps 3–5, in `BRIEF_SCHEMA.md`'s write boundary, and in 11 of
`QA_CHECKS.md`'s 18 items.

**One place gets it right** — `BRIEF_SCHEMA.md` line 18, `ExpectedOutputs`:
`for conversion, distinct evidence candidate, clean production contract, and
finalization report; applicable claim map/parity/checklist`. That conditional
phrasing is the pattern the other statements need. This proposal propagates it.

**The gap is currently safe but unstated.** `--source-dir` is `required=True`
in both `map_scope_of_work_claims.py` (line 29) and
`report_scope_of_work_parity.py` (line 133), so TOOL_POLICY step 4 is literally
unexecutable under `MODE=INIT`; the tools are structurally CONVERT-only. Three
INIT runs completed only because the dispatching brief pre-ruled the conflict.

**Amendment to the request's framing.** The request named three files. Two
corrections:
1. `QA_CHECKS.md` must be included — item 3 is not merely conversion-shaped,
   it is *actively wrong*: it requires `_STATUS.md` to remain `IN_PROGRESS`,
   which fails a correct INIT run sitting at `OPEN`. Under the closing clause
   ("Any failure produces a failed return … it does not silently weaken the
   acceptance gate"), a literal reading makes INIT unsatisfiable against its
   own QA contract on 9 further counts (see §2e for the reconciled partition).
2. `TOOL_POLICY.md`'s "Required order" has **8** steps, not 7. The request says
   "steps 4–7"; the affected unconditional steps are 3, 4, and 5.

## 2. Proposed exact-text changes

### 2a. `skills/scope-of-work/SKILL.md` — Method steps 4–7

REPLACE lines 41–52:

```
4. Refine the evidence candidate without dropping conversion source markers.
   Define stable IDs, complete the output/evaluation matrix, preserve epistemic
   labels, and mark substantive ambiguity `CONFLICT`.
5. Run source mapping and parity on the evidence candidate, then use the
   deterministic finalizer to create a separate clean production contract and
   external finalization report. Require the map and parity report to bind the
   clean production hash.
6. Validate, derive the REVIEW checklist, and optionally render HTML from the
   clean production contract only.
7. Return both candidate paths, source/evidence/production hashes, finalization
   report, claim map, parity report, checklist, validation result, conflicts,
   and `_STATUS.md` before/after hash.
```

WITH:

```
4. Refine the working contract. Define stable IDs, complete the
   output/evaluation matrix, preserve epistemic labels, and mark substantive
   ambiguity `CONFLICT`. For `CONVERT`, the working contract is the evidence
   candidate and its conversion source markers are never dropped. For `INIT`,
   the working contract is the production `ScopeOfWork.md` itself; there is no
   evidence candidate and no source marker.
5. For `CONVERT` only: run source mapping and parity on the evidence candidate,
   then use the deterministic finalizer to create a separate clean production
   contract and external finalization report. Require the map and parity report
   to bind the clean production hash. `INIT` produces no evidence candidate,
   runs no mapping, parity, or finalization, and authors the production
   contract directly.
6. Validate and derive the REVIEW checklist from the production contract, and
   optionally render HTML from it. Under `CONVERT` the production contract is
   the clean finalized artifact and no other.
7. Return the production contract path and hash, validation result, checklist,
   conflicts, and the `_STATUS.md` hash — unchanged under `NO_STATUS_TOUCH`, or
   before/after when the brief authorizes a status act. For `CONVERT`,
   additionally return the evidence-candidate path, source and evidence hashes,
   finalization report, claim map, and parity report.
```

Rationale for step 7's status clause: the canary found that step 7's
"`_STATUS.md` before/after hash" is a read-only invariant under
`NO_STATUS_TOUCH`, not a pair. The replacement states both cases.

### 2b. `skills/scope-of-work/TOOL_POLICY.md` — Required order steps 3–5

REPLACE lines 9–15:

```
3. Refine the evidence candidate through bounded reasoning without removing
   source markers.
4. Run `map_scope_of_work_claims.py` and
   `report_scope_of_work_parity.py` independently of the authoring judgment.
5. Run `finalize_scope_of_work.py` into a distinct production-candidate path;
   rerun mapping and parity with `--production-scope-of-work` so both bind and
   verify that exact clean artifact.
```

WITH:

```
3. In `CONVERT`, refine the evidence candidate through bounded reasoning
   without removing source markers. In `INIT`, author the production
   `ScopeOfWork.md` directly from accepted decomposition and source evidence;
   there is no evidence candidate to refine.
4. In `CONVERT`, run `map_scope_of_work_claims.py` and
   `report_scope_of_work_parity.py` independently of the authoring judgment.
   Both tools require `--source-dir` and are structurally conversion-only; they
   are not run under `INIT` or `VERIFY`.
5. In `CONVERT`, run `finalize_scope_of_work.py` into a distinct
   production-candidate path; rerun mapping and parity with
   `--production-scope-of-work` so both bind and verify that exact clean
   artifact. `INIT` has no finalization step: the authored contract is the
   production contract.
```

Steps 6, 7, and 8 need no change — they are genuinely mode-agnostic
(`validate_scope_of_work.py`, `derive_review_checklist.py`, and
`render_scope_of_work.py` all operate on any valid `SOW_V1` production file),
except that "the clean production candidate" / "the clean production SOW"
should read "the production contract" for INIT to be covered by the same words.
**Optional smaller variant** if the owner prefers a minimal diff: change only
steps 3–5 as above and leave 6–8 alone, accepting that "clean production
candidate" reads as CONVERT vocabulary for an INIT run.

### 2c. `skills/scope-of-work/BRIEF_SCHEMA.md` — write boundary

REPLACE lines 34–40:

```
Permitted targets are limited to:

- an evidence-candidate `ScopeOfWork.md` in the isolated conversion workspace;
- a separate clean production-candidate `ScopeOfWork.md` and external finalization report;
- a requested untracked/on-demand `ScopeOfWork.html`; and
- run-local claim-map, parity, deterministic checklist, receipt, and return
  artifacts.
```

WITH:

```
Permitted targets are limited to:

- for `INIT`, the production `ScopeOfWork.md` at `{ScopePath}/ScopeOfWork.md`;
- for `CONVERT`, an evidence-candidate `ScopeOfWork.md` in the isolated
  conversion workspace, plus a separate clean production-candidate
  `ScopeOfWork.md` and external finalization report;
- a requested untracked/on-demand `ScopeOfWork.html`; and
- run-local claim-map, parity, deterministic checklist, receipt, and return
  artifacts.
```

This is the substantive authorization gap: as written, an INIT-authored
production `ScopeOfWork.md` has **no** permitted write target in the
enumeration, and the three canary runs were authorized only by the dispatching
brief's own fence.

### 2d. `skills/scope-of-work/BRIEF_SCHEMA.md` — the three undeclared metadata keys

The PEC wave used `STATUS_POLICY`, `DECOMP_VARIANT`, and `PHASE` as brief
metadata. None are declared in **this** skill's schema — but two of the three
are established repo-wide vocabulary, and an earlier draft of this proposal
got their basis badly wrong. Corrected:

**`STATUS_POLICY` — a live three-value vocabulary already exists.** (An earlier
draft claimed "zero hits anywhere". That was false.) It is defined in
`skills/semantic-matrix-build/` — `BRIEF_SCHEMA.md:23`, `SKILL.md:78-86`,
`QA_CHECKS.md:131-133` — and reused by `skills/lens-register/`:

| Value | Meaning (`semantic-matrix-build/SKILL.md:82-84`) |
|---|---|
| `PRESERVE_CURRENT` | Do not change lifecycle state; record the ruling |
| `ADVANCE_ON_PASS` | On PASS, set/verify the next state, only if `_STATUS.md` edits are authorized |
| `NO_STATUS_TOUCH` | Do not edit `_STATUS.md` at all |

**The two-value vocabulary proposed in the earlier draft is withdrawn.** A
second, incompatible spelling of the same concept in a sibling skill is exactly
the drift this packet exists to remove. Adopt the existing vocabulary verbatim.

**`DECOMP_VARIANT` — a live protocol variable, not merely an enum.** (An earlier
draft claimed it "exists only as an enum in `validate_enum.py`". Also false.) It
is used across five agent instruction files — `AGENT_SCOPE_CHANGE.md`,
`AGENT_AUDIT_DECOMP.md` (which branches on it), `AGENT_AUDIT_SCOPE_CLOSURE.md`,
`AGENT_REVIEW.md`, `AGENT_PROJECT_SETUP.md` — and is declared in the
`BRIEF_SCHEMA.md` of `four-documents`, `semantic-matrix-build`, `lens-register`,
`domain-documents`, and `scope-change-packet`. `validate_enum.py:36` is the
canonical enum backing an established variable, not its only home.

Because four sibling skills already declare it, this skill should declare it
the same way rather than inventing phrasing.

ADD to the Optional fields table (after line 30, `CustomInstructions`):

```
| `RuntimeOverrides.STATUS_POLICY` | `PRESERVE_CURRENT`, `ADVANCE_ON_PASS`, or `NO_STATUS_TOUCH`, with the meanings defined in `skills/semantic-matrix-build/SKILL.md`. `ADVANCE_ON_PASS` additionally requires the brief to authorize `_STATUS.md` writes; absent that authorization the run does not edit status and reports the ruling | `NO_STATUS_TOUCH` |
| `RuntimeOverrides.DECOMP_VARIANT` | `PROJECT` or `SOFTWARE`, matching the accepted decomposition basis; canonical enum `DECOMP_VARIANT` in `tools/validation/validate_enum.py`. `DOMAIN` is out of this skill's scope | inferred from `DECOMPOSITION_BASIS` |
| `RuntimeOverrides.PHASE` | Project-loop phase label carried for run-record attribution only; it grants no authority and changes no tool behavior | empty |
```

**Default choice, re-derived.** `semantic-matrix-build` defaults to
`PRESERVE_CURRENT` because its Phase 2.3 runs write `_SEMANTIC.md` beside a
deliverable already in flight. This skill's INIT runs are the first act on an
`OPEN` deliverable, and the PEC wave briefs used `NO_STATUS_TOUCH` with the
status act carried as a separate, separately-recorded step. `NO_STATUS_TOUCH` is
therefore the correct default here — a *different* default from the sibling
skill, drawn from the *same* vocabulary. That is the intended relationship;
flagging it so the divergence is a decision rather than an accident.

**Variant spelling to flag for the owner:** `PRESERVE_CURRENT_STATE` appears in
at least one earlier template, against the live `PRESERVE_CURRENT`. It is not
proposed for adoption; if it is still live anywhere it should be normalized to
`PRESERVE_CURRENT` in a separate hygiene pass. Not fixed here — out of scope.

**Remaining owner decision:** `RuntimeOverrides.SOURCE_STATE` (line 17) already
exists and partly overlaps — `SOURCE_STATE` says what state the deliverable is
in, `STATUS_POLICY` says whether this run may change it. Confirm both are
wanted before adopting.

### 2e. `skills/scope-of-work/QA_CHECKS.md` — mode scoping

Two changes.

**(i) Item 3 — the actively-wrong one.** REPLACE line 5:

```
3. `_STATUS.md` is byte-identical and remains `IN_PROGRESS`.
```

WITH (the canary's own suggested restatement, adopted verbatim in substance):

```
3. `_STATUS.md` is byte-identical and its lifecycle state is unchanged.
```

The hardcoded `IN_PROGRESS` has no backing: `BRIEF_SCHEMA.md` line 17 declares
the state as brief-supplied via `SOURCE_STATE`, and `common.py`
`read_lifecycle_state` never compares against `IN_PROGRESS`. No tool enforces
the current wording; it is prose that fails correct runs.

**(ii) Mode scoping for the list.**

An earlier draft's header placed item 4 in the CONVERT-only set while the
commentary called it mode-agnostic. **Resolved: item 4 is mode-agnostic.** The
underlying validation (`validate_scope_of_work.py`) runs on any valid `SOW_V1`
production file regardless of mode, and the canary's INIT-applicable subset
`{4, 8, 9, 13, 16, 18}` includes it. Only its *wording* is CONVERT-flavoured,
which 2e(iii) below fixes.

**Count, reconciled.** An earlier draft said 11 conversion-only in prose and
enumerated 10 in its header — both wrong, and inconsistent with each other.
The correct partition is three-way, not two-way:

| Class | Items | Count |
|---|---|---|
| CONVERT-only | 2, 5, 6, 7, 10, 11, 12, 14, 17 | **9** |
| Mode-agnostic | 1, 3, 4, 8, 9, 13, 16, 18 | 8 |
| Conditional on `RENDER_HTML`, mode-independent | 15 | 1 |
| | | **18** |

The request's canary summary said 11 conversion-only; the refuter's independent
classification said 10. The whole difference is two judgment calls, both of
which I resolve toward mode-agnostic and state openly:

- **Item 1** ("the exact pilot variance covers the deliverable path") is an
  authority check that applies to any run under the pilot, not a conversion
  step.
- **Item 15** (repeated HTML rendering is byte-identical) is gated by
  `RENDER_HTML`, not by mode — `TOOL_POLICY.md` step 8 renders "only when a
  derivative was requested", which INIT may also request. Counting it as
  CONVERT-only is what yields the refuter's 10.

If the owner reads item 15 as CONVERT-only, the count is 10 and the header's
third sentence should be dropped. Flagging it as a one-item judgment call
rather than silently picking.

INSERT after line 1 (`# QA CHECKS — scope-of-work`) and before item 1:

```

Items 2, 5–7, 10–12, 14, and 17 apply to `CONVERT` only; under `INIT` they are
`NOT_APPLICABLE` and are recorded as such rather than passed or failed. Items
1, 3, 4, 8, 9, 13, 16, and 18 apply to every mode. Item 15 applies whenever an
HTML derivative was requested, in any mode. Items 19 and 20 apply to every
mode. `VERIFY` runs the mode-applicable subset read-only.
```

This is the minimal-diff form: it scopes the list without rewriting nine items.
The alternative — annotating each item inline with `(CONVERT)` — is a larger
diff and is **not** recommended, because the item numbers are cited by
`SKILL.md` and by run records and should stay stable.

**Items 19 and 20 are added by P6 and P7 in this packet** (upstream-ID citation
and matrix row semantics). Both are mode-agnostic. This header block is the
**canonical** statement of QA mode scoping for the packet; P6 and P7 reference
it rather than restating it. If P6 or P7 is adopted without P1, the adopting
proposal must carry the corresponding clause instead.

**(iii) Item 4's wording.** REPLACE line 6:

```
4. Evidence-candidate frontmatter, headings, IDs, references, and matrix validate.
```

WITH:

```
4. Working-contract frontmatter, headings, IDs, references, and matrix validate.
```

One word, and it removes the last reason to misread item 4 as CONVERT-only.

## 3. Compatibility

- No tool changes. All four proposed edits are contract text.
- `validate_skill_metadata.py` enforces frontmatter, companion-file presence,
  single-line description, and `allowed-tools` syntax — none of which these
  edits touch. Rerun it after the change: `python3
  tools/validation/validate_skill_metadata.py`.
- Existing CONVERT briefs and accepted CONVERT run records remain conforming;
  every CONVERT sentence retains its current force, now explicitly scoped.
- Accepted INIT contracts from the D-PEC-63 wave become *retroactively
  conforming* rather than brief-excepted. That is the point of the change, and
  it is a strengthening, not a weakening — but it is a semantic acceptance the
  owner should make knowingly.
