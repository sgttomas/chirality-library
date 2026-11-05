# D-T0-25 Application Archive — Bounded Whitespace Correction

**Status:** EXACT CORRECTION CANDIDATE — NOT APPROVED OR APPLIED
**Date:** 2026-07-28
**Cause:** Pre-commit `git diff --cached --check`
**Affected semantic surfaces:** none

## Exact correction

In
`accepted_candidate/DOMAIN_ENGINE_INDEX.diff`, remove only the single ASCII
space immediately before the newline on lines 4 and 6. Both lines are
space-only unified-diff context lines. No other byte changes.

- Before SHA-256:
  `a6cd22b453c77b5176261fba589e034f0dc448e0d68f7de7ae0ef6b551557168`
- After SHA-256:
  `ef1614fd5f3412606a8b9be4c23a5d989361859d7f61874cc6907127f74864eb`
- Before length: 999 bytes
- After length: 997 bytes
- Removed bytes: two ASCII spaces (`0x20`), one at each named line

The corrected file is byte-identical to the accepted file after applying only
that two-byte deletion. Its non-whitespace text, line count, and line sequence
are unchanged.

## Identity handling

The owner ruling and approved application packet remain unchanged and retain
the original approved candidate and artifact identities as historical
authority evidence. This packaging correction does not rewrite that ruling.

Only the directly dependent archive identities are regenerated:

- corrected accepted candidate manifest:
  `2bdf9a0e6dbf3ec585c0b8d3867112d45192ce40f8a2995ef91dcd4ed1bbd047`;
- corrected accepted artifact manifest:
  `2307b38adc6f1190ae86d72a027ddd035ee2ed7566fd6bc4935215a8b481f69b`;
- the application validator/result and outer archive manifest required to
  validate and identify the corrected archive.

The live register, D-T0-25 decision, Domain Engine Index, Receipt 29, owner
ruling, application record, applied-path register, handoff, and accepted
semantic/candidate postimages remain byte-identical.

## Authority boundary

This candidate creates no authority and changes no semantic, product, profile,
runtime, implementation, lifecycle, release, compatibility, reliance, P-A,
D-T0-26, or Git state. Application requires exact owner approval.
