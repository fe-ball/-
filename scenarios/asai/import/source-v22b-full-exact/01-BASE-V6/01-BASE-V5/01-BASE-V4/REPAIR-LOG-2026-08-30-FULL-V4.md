# FULL V4 repair / integration log — 2026-08-30

## Integration intent

The user requested a clean FULL handoff without old/new terminology contamination. The V4 architecture therefore uses a hard namespace boundary: current reconstruction files are under `01-CURRENT-BRANCH/`; all earlier payloads are under `90-SOURCE-QUARANTINE/`.

## Changes made

1. Integrated the complete 2026-08-29 FULL V3 source payload rather than only its 856-file index.
2. Preserved all 8/29 source files byte-for-byte, including the nested v48r3/Marine V10 archive.
3. Promoted the 8/30 reconstruction layer as the sole current-branch namespace.
4. Rewrote only packaging/entry-point text in `00-START-HERE.md` and `02-TOPIC-SOURCE-MAP.md`; claim semantics in `03-CURRENT-BRANCH-INDEX.tsv` were not silently rewritten.
5. Added `TERMINOLOGY-AND-SUPERSESSION-GUARD.tsv` from the current claim index to make old/new wording collisions explicit.
6. Added `SOURCE-RESOLUTION-MAP-2026-08-30-FULL-V4.tsv` for all 856 raw-source records.
7. Replaced the misleading RECONSTRUCTION V1 integrity statement about a rebuilt FULL archive with a new audit based on the actual V4 package.
8. Rebuilt current-layer and full-package SHA256 manifests and tested final ZIP CRC.

## Semantic preservation rule

No legacy claim is promoted merely because its source is bundled. Quarantine preserves evidence; current claim status controls branch truth.
