# Validation Plan — D-T0-26 / P-A

1. Accepted package identities reproduce.
2. Provisional ID and the complete planned ranges are collision-free.
3. Every `PREIMAGE` row in `APPLICATION_MANIFEST.csv` reproduces.
4. Every `CANDIDATE` row reproduces.
5. The future owner ruling is transcribed verbatim before a live write.
6. Writes are limited to `APPLICATION_PACKET.md` §Exact write surfaces.
7. No implementation, SCA, Git, or unlisted lifecycle action occurs.
8. Run the Git-pinned profile validator on the staged live profile; require VALID with STALE / MANUAL_BRIDGE and semantic deny-all checks.
