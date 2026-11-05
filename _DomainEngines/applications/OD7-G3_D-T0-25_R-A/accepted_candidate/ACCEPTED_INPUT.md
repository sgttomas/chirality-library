# OD7-G3 R-A — D-T0-23 Residual Classification Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-R-A`
**Provisional carrier:** `D-T0-25`
**Source basis:** D-T0-23, D-PEC-58, accepted PEC PRD v2.1, Root PRD O-11
**Detailed clause register:** `../evidence/D_T0_23_RESIDUAL_CLASSIFICATION.csv`
**Exact index candidate:** `../candidate_tree/R-A/_DomainEngines/DOMAIN_ENGINE_INDEX.md`
**Exact index diff:** `../diffs/R-A_DOMAIN_ENGINE_INDEX.diff`

## Exact candidate decision

Preserve D-T0-23 byte-for-byte as historical authority. Adopt the accompanying
clause-level residual classification as the current interpretation of its
relationship to PEC v2:

1. Shared runtime ownership, project/domain authority separation,
   checkout-contained evidence, stable project identity, the no-production-
   dual-loop rule, and fail-closed runtime-client behavior remain current.
2. D-T0-23 clause 4's allocation of deterministic acts, RBAC, reporting,
   visibility, data boundaries, and project-specific tool semantics to a PEC
   adapter is historical for the frozen v0.4 application and is not PEC v2
   scope. D-PEC-58 is the later controlling PEC ruling.
3. D-T0-20 and D-T0-21 remain historical visibility/access authority for the
   frozen application only. D-T0-22 remains historical; its negative
   no-ambient-authority guard is carried independently by D-GOV-20.
4. The one-cycle proxy and scratch/demo pilot statements are historical
   migration evidence, not PEC v2 release requirements.
5. D-T0-23's statement that D-PEC-49 was awaiting ruling is corrected by the
   later D-PEC-58 closure of D-PEC-49 as moot.
6. D-PEC-58 closed the product-rebaseline residual. No production-data or
   production-mutation authority was thereby created.
7. Runtime execution may fail closed while governed work continues through
   accepted file-native truth; those are distinct failure boundaries.

This decision interprets lineage. It creates no product function, external
consumer duty, profile execution authority, or implementation authorization.

## Exact future register row candidate

```markdown
| D-T0-25 | Residual classification of D-T0-23 after D-PEC-58: preserve the ruled record unchanged; classify the retired PEC v0.4 adapter allocation, visibility/access bases, proxy and pilot as historical; retain shared-runtime ownership, authority separation, no-dual-loop, checkout-contained evidence, stable identity, and fail-closed client boundaries as current | Exact OD7-G3 R-A candidate; clause register in the accepted packet | **OPEN — exact candidate not yet ruled** | Lineage coherence only; no profile, product, or implementation authority |
```

## Conditional write surfaces

- `_DomainEngines/_DECISIONS/D-T0-25_*.md`
- `_DomainEngines/_DECISIONS/_REGISTER.md`
- `_DomainEngines/DOMAIN_ENGINE_INDEX.md` only through the exact R-A diff
- Tier-0 receipt/pointer surfaces required by the then-current closeout

## Acceptance boundary

An owner ruling must identify this exact candidate hash. Publication requires
an execution-time ID rescan. Acceptance does not accept `P-A` or any PEC-local
candidate.
