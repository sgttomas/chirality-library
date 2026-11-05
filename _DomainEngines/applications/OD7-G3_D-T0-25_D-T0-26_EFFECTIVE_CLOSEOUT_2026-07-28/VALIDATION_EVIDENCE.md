# Effective-State Closeout Validation Evidence

**Date:** 2026-07-28
**Basis:** `dc89356eb4db715bfe8357b25d8831c752cb822e`

## PEC profile

Command:

```text
tools/validation/validate_domain_engine_profile.py _DomainEngines/profiles/pec.yaml
```

Result: `VALID`; profile status `STALE`; errors `0`; warnings `0`.

Derivative report:
`PEC_PROFILE_VALIDATION.json`, SHA-256
`bd5828d4b8843e0e2f99a64fbdc3d9b024f41b6963c968a937877d4f1f1a8a1a`.

## Practitioner harness

Command:

```text
pytest tools/practitioner_harness -q
```

Result: `349 passed in 50.22s` on the complete generated closeout package
before evidence sealing.

## Closeout checks

- Frozen D-T0-25 application manifest: 26/26
- Frozen D-T0-26 application manifest: 21/21
- Effective-state validator before generated-evidence sealing: 65/65 PASS
- `git diff --check`: pass
