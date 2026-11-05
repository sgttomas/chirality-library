# D-T0-26 Effective-State Closeout

**Status:** `EFFECTIVE_STATE_RECORDED_PENDING_CHANGE`
**Date:** 2026-07-28
**Closeout basis:** `dc89356eb4db715bfe8357b25d8831c752cb822e`
**PublicationSHA:** `7948eef43fe27eacd482688d9249a1ad2b92471c`
**EffectiveSHA:** `dc89356eb4db715bfe8357b25d8831c752cb822e`

## Proof

- Merge `dc89356eb4db715bfe8357b25d8831c752cb822e` has second parent
  `7948eef43fe27eacd482688d9249a1ad2b92471c`.
- The merge is the exact closeout basis.
- The live D-T0-26 decision SHA-256 is
  `d3c1968dbd27b39975af6367403c7f0ff3cc88222608c543a5bc7b5a007cc630`,
  byte-identical to the publication commit.
- The frozen application directory is byte-identical between the publication
  commit and the closeout basis.
- Its `ARTIFACT_HASHES.sha256` is
  `cca5fb058465c42d0570258aafe1ae304472722b59934268992b19298871ac1c`
  and reproduces 21/21 entries.

## Effect

This record supplies terminal Git identity only. The already-effective P-A
profile semantics, frozen ruling/application package, and every authority
boundary remain unchanged.
