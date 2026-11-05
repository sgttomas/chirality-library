# P-A Effective-State Rebuild Record

**Date:** 2026-07-28
**Application basis:** `2c8e4168220b49f1e83a45aa916a6eb29856f0b4`
**Accepted profile candidate:** `db36664d9fbd3dc3c348e51dc5367d52753faf0eff10c13d36340f6cc019b8ae`
**Accepted index candidate:** `777cc1400c5aef17a3e4c3aa40f8de4d533b1228fbeb88d76ab3a4ca1bdcb690`
**Rebuilt profile postimage:** `0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6`
**Rebuilt index postimage:** `d0822ebe28fcd037664790baf3518ad363796a4d5ea3abf61ea426ef4d1b5cdf`

## Reason

The accepted planning bytes correctly described themselves as an unapplied
candidate. Publishing those annotations unchanged after application would
make the live profile and current-summary index falsely say that P-A remained
unapplied. The current-basis rebuild therefore changes only preview-state
annotations. The accepted candidate is preserved byte-for-byte under
`accepted_candidate/`, and every semantic P-A field remains unchanged.

## Exact annotation substitutions

Profile:

1. `STALE legacy binding (OD7-G3 P-A exact candidate; not applied)` →
   `STALE legacy binding (D-T0-26; applied 2026-07-28)`
2. `Current candidate` → `Current`
3. `This candidate preserves` → `D-T0-26 preserves`
4. `OD7-G3 P-A exact candidate: semantic demotion only` →
   `D-T0-26 P-A application: semantic demotion only`
5. `this STALE candidate grants` → `this STALE profile grants`

Domain Engine Index:

1. The banner's candidate-preview sentence becomes the D-T0-26
   effective-state sentence.
2. The PEC row's provenance suffix
   `OD7-G3 P-A candidate` becomes `D-T0-26`.

The application validator performs these substitutions deterministically and
requires the resulting bytes to equal the live postimages.
