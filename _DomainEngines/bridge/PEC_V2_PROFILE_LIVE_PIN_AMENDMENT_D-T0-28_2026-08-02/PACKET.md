# D-T0-28 candidate — D-T0-27 live-baseline pin amendment

**State:** `AWAITING_RULING / NOT EXECUTED`

**Prepared:** 2026-08-02

**Decision ID:** D-T0-28

**Exact write path if later ruled O-A:**
`tools/practitioner_harness/test_live_baseline.py`

**Exact preimage SHA-256:**
`80823ee8dea253f91145302f37e618bdf8feb753f032a741d0aa0e4f0df1e70c`

**Exact proposed postimage SHA-256:**
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`

**Exact patch:** `TEST_PIN_PATCH.diff`

## 1. Decision requested

Should the owner authorize the one omitted D-T0-27 application write: a
conscious live-baseline pin update limited to the exact test path and exact
patch above?

D-T0-27 O-A is ruled and its exact profile postimage is materialized, but the
application remains `NOT EFFECTIVE`. The required targeted suite returns 16
passes and two failures because this test still pins the superseded D-T0-26
observations. The D-T0-27 application plan did not enumerate this test path,
so DOMAIN_ENGINE correctly stopped rather than widening by inference.

## 2. Exact acts under O-A

Apply `TEST_PIN_PATCH.diff` only when the live test file still equals the exact
preimage SHA above. The patch makes only these two conscious pin corrections:

1. `ABS_PATH_IN_EVIDENCE` expected count changes from two to one and removes
   only the PEC validation-report tuple. D-T0-27 regenerated PEC validation
   with repo-relative `profile_path`; the remaining OpenPipeStress validation
   evidence still carries the one permitted machine-absolute evidence path.
2. The PEC bridge-status expectation changes from
   `STALE / Gate 2 unknown / MANUAL_BRIDGE` to
   `ADOPTED / Gate 2 adopted / READ_ONLY`, matching the exact ruled and
   materialized D-T0-27 profile bytes. The test name and explanatory comment
   change only to state that conscious pin accurately; they do not declare the
   D-T0-27 application effective.

No other line or path may change under this decision.

## 3. Postconditions and verification

O-A execution succeeds only if all of the following hold:

- the test postimage equals SHA-256
  `7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`;
- changed-path containment shows only the exact test path for the amendment
  execution, plus separately authorized ruling/application records;
- the targeted suite passes all 18 tests:
  `tools/practitioner_harness/test_live_baseline.py`,
  `tools/practitioner_harness/test_adapter_domain_engines.py`, and
  `tools/practitioner_harness/test_bridge_status.py`;
- `tools/validation/test_validate_domain_engine_profile.py` passes all profile
  validator tests;
- `harness.py bridge-status` completes without findings and reports PEC
  `ADOPTED / Gate 2 adopted / READ_ONLY`;
- `harness.py self-check` completes and any findings are compared with the
  recorded pre-amendment baseline;
- the D-T0-27 five-file candidate manifest and 16-entry application manifest
  reproduce after any required register-hash refresh;
- D-PEC-74 accepted API schema/test/fixture hashes,
  `projects/pec/software-workflow.json`, and
  `projects/pec/chirality.project.json` remain unchanged;
- `git diff --check` passes; and
- after a commit exists, committed-range `coord-check` passes with no new
  absolute-path or authority-boundary defect.

Passing these checks permits the D-T0-27 application to return to CHANGE for
publication. It does not itself make D-T0-27 effective; durable exact merge
identity and the owning closeout record remain required.

## 4. Options

- **O-A — authorize the exact pin amendment (recommended).** Apply only
  `TEST_PIN_PATCH.diff` against the exact preimage, run every postcondition,
  and return the validated application to CHANGE.
- **O-B — defer.** Leave the test untouched and keep D-T0-27 materialized but
  not effective; D-T0-26 remains the effective durable profile posture.
- **O-C — amend or decline.** Name a different exact path, act, expectation,
  or verification set. Any changed postimage requires a revised packet and
  fresh exact hash before execution.

## 5. Nonbinding recommendation

Recommend O-A. Both failures are mechanical live pins whose governing source
observations changed exactly as D-T0-27 intended. The patch changes no harness
production behavior and preserves the rule that check expectations move only
through conscious, reviewable authority.

The owner may rule:

```text
D-T0-28: O-A.
D-T0-28: O-B.
D-T0-28: O-C — <exact amendment or decline>.
```

## 6. Rollback and authority fence

Before publication, any failed precondition or verification restores only the
test file to exact preimage SHA-256
`80823ee8dea253f91145302f37e618bdf8feb753f032a741d0aa0e4f0df1e70c`.
After publication, correction is forward-only through a successor decision.

This packet and any later O-A execution change no production harness logic,
profile bytes, profile semantics, project file, PEC source, software-workflow
registry, ScopeOfWork, decomposition, lifecycle, Task Management, accepted
artifact, adapter invocation, runtime behavior, release, professional
reliance, D-PEC-75 state, or cross-loop mandate. It performs no ruling and
does not claim D-T0-27 effective.
