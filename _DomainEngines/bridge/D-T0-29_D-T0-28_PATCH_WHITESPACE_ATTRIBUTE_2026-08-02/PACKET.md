# D-T0-29 candidate — exact whitespace attribute for D-T0-28 patch evidence

**State:** `AWAITING_RULING / NOT EXECUTED`

**Prepared:** 2026-08-02

**Decision ID:** D-T0-29

**Exact prospective production write:** `.gitattributes` only

**Exact preimage SHA-256:**
`7dece5526cb8dd98264bab5c96be95235cd482b1b1da4e623b63489dae1e1fe2`

**Exact proposed postimage SHA-256:**
`c0d9e5b7e3bbca1f41087959d6095e75d578fef172123050da7145f52fb9d89f`

**Exact patch:** `GITATTRIBUTES_PATCH.diff`, SHA-256
`5f8b79da4942e7daafb96107c3ef3d97b7b202ecc762319bba93d7ed55dd2a6a`

## 1. Decision requested

Should the owner authorize one exact Git whitespace attribute so the
candidate-whitespace gate treats D-T0-28's four format-mandated unified-diff
blank context markers as patch grammar rather than trailing prose whitespace?

The exact line, placed immediately after the existing unified-diff convention,
is:

```gitattributes
_DomainEngines/bridge/PEC_V2_PROFILE_LIVE_PIN_AMENDMENT_D-T0-28_2026-08-02/TEST_PIN_PATCH.diff -whitespace
```

The D-T0-28 patch remains exact SHA-256
`db807bef647db3ef6cd7f4208e5bb5ac5e8ee2775b6a8a19eaeb70434476a499`.
The applied test postimage remains exact SHA-256
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`.

## 2. Named convention and reason

Root `.gitattributes` already records the repository convention:

```gitattributes
# Unified-diff artifacts carry format-mandated blank context lines
# (a single space); disable whitespace checks for them entirely.
execution/_ScopeChange/**/*.diff -whitespace
```

D-T0-28's `TEST_PIN_PATCH.diff` is outside that path pattern but contains the
same required single-space context markers. The candidate-whitespace validator
runs Git's `diff --check` for committed candidates and honors Git attributes.
The exact-path attribute extends no pattern and exempts no other file.

Changing the ruled patch to a zero-context representation would replace its
exact owner-ruled identity. Marking it binary would reduce reviewability.
This exact attribute is therefore the smallest repair that preserves the
ruled evidence and the existing Git convention.

## 3. Exact act under O-A

Only if `.gitattributes` still equals the exact preimage above, apply
`GITATTRIBUTES_PATCH.diff` and require the exact postimage above. No other line
or path may change as the prospective production act under this decision.

## 4. Options

- **O-A — authorize the exact attribute (recommended).** Apply the exact patch
  against the exact preimage, run every verification below, and return the
  D-T0-27/D-T0-28 application to CHANGE.
- **O-B — defer.** Leave `.gitattributes` unchanged; preserve the ruled patch
  bytes but keep PR publication blocked on candidate whitespace.
- **O-C — amend or decline.** Name a different exact attribute, path,
  representation, or disposition. Any changed postimage requires a revised
  exact packet and fresh hashes before execution.

## 5. Verification and postconditions

O-A execution succeeds only if all of the following hold:

- `.gitattributes` preimage and postimage reproduce the exact hashes above;
- `GITATTRIBUTES_PATCH.diff` reproduces its exact hash and passes
  `git apply --check`;
- `git check-attr whitespace --
  _DomainEngines/bridge/PEC_V2_PROFILE_LIVE_PIN_AMENDMENT_D-T0-28_2026-08-02/TEST_PIN_PATCH.diff`
  reports `whitespace: unset`;
- D-T0-28 `TEST_PIN_PATCH.diff` remains SHA-256
  `db807bef647db3ef6cd7f4208e5bb5ac5e8ee2775b6a8a19eaeb70434476a499`
  and remains applicable to its exact preimage or reversible from its exact
  postimage;
- `tools/practitioner_harness/test_live_baseline.py` remains SHA-256
  `7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`;
- the candidate-whitespace validator passes its staged/unstaged checks and,
  after a commit exists, the CI-equivalent `--base-ref` committed-range check;
- D-T0-27/D-T0-28/D-T0-29 manifests reproduce after any exact mechanical
  resealing required by ruling/application records;
- committed-range `coord-check` passes with no new blocker;
- relevant D-T0-28 targeted and profile-validator checks remain passing; and
- `git diff --check` passes under the exact attribute.

Passing these checks removes only the whitespace-publication blocker. It does
not itself make D-T0-27 or D-T0-28 effective; exact CHANGE publication and
merge identity remain required.

## 6. Rollback and authority fence

Before publication, any failed precondition or verification restores only
`.gitattributes` to exact preimage SHA-256
`7dece5526cb8dd98264bab5c96be95235cd482b1b1da4e623b63489dae1e1fe2`.
After publication, correction is forward-only through a successor decision.

This packet changes no validator code or behavior, D-T0-28 patch/test bytes,
profile, project, PEC path, source, software-workflow registry, ScopeOfWork,
decomposition, lifecycle, Task Management, accepted artifact, runtime,
adapter invocation, release, professional reliance, D-PEC-75 state, or
cross-loop mandate. It performs no ruling and does not claim D-T0-27 or
D-T0-28 effective.
