# MACHINE INTEGRITY AUDIT — V8 IDENTITY1

Semantic state represented by this package:

- current chronological checkpoint: **1939-05-10 24:00**;
- combat replay: **ACTIVE_COMBAT_REPLAY**;
- next chronological gate: **1939-05-11 Nomonhan opening clash / border incident sequence**;
- EXHAUST1 remains current; IDENTITY1 adds a cross-service historical-designation/hardware interpretation guard and does not advance the clock;
- same designation is no longer sufficient to copy a historical datasheet, configuration mix or ready rate;
- Navy critical mapping is explicit: worldline A7M=Gaifu; historical A7M Reppu maps to worldline A9M as an H-anchor;
- historical OOB count is separated from worldline lot/config, serviceability, forward deployment and combat use.

Semantic guards checked:

1. `47/47A` explicitly cross-reference `50/50A` and `49/49A`.
2. Historical Reppu references in current V8 files are labeled as historical A7M / worldline A9M anchors, avoiding collision with worldline A7M Gaifu.
3. EXHAUST1 no-double-count rules remain intact.
4. B5N2 old E1=0 ruling remains superseded.
5. Chi-Ha 200/220, Ha-Go no-blanket-turbo, dense-core AP and spall-liner allocation gates remain intact.
6. IDENTITY1 creates no procurement, retrofit counts, OOB changes or combat result.

Integrity build convention:

- `PACKAGE-INVENTORY-V8.tsv` excludes itself, `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv`, and `SHA256SUMS-V8.txt`.
- manifest/SHA hash every package file except the manifest and SHA files themselves; inventory is checksum-covered.
- final ZIP is unpacked independently and every manifest target is rehashed.

Counts are regenerated in the build step and recorded in the companion JSON.
