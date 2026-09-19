# MACHINE INTEGRITY AUDIT — V8 AIRPOWER4 AIRFRAME1

## Source verification
Source tree: `ASAI-WORLDLINE-HANDOFF-2026-09-03-FULL-V8-1939AIRPOWER3-HOMARE1`.

Before AIRPOWER4 edits, the source package's `SHA256SUMS-V8.txt` was independently checked:
- listed entries: **394**;
- SHA256 matches: **394**;
- mismatches: **0**;
- missing: **0**.

No source paths were intentionally deleted.

## AIRPOWER4 intentional content delta before metadata rebuild
New numbered audit files:
- file 15 high-power propeller/cooling canon;
- file 16 Homare/Ha-43 airframe integration canon;
- file 17 machine-readable airframe integration ledger;
- file 18 1943Q1 technical snapshot;
- file 19 1942 requirement/procurement replay gate.

Existing content files intentionally updated:
- root dated START-HERE;
- root CURRENT START-HERE;
- file 04 Shiden integration window/cross-reference;
- file 08 propeller chronology supersession/cross-reference;
- file 09 AIRPOWER4 supersession notice on the preserved older session rollover;
- file 10 current technical workfront / next boundary;
- file 14 piston-engine-to-airframe handoff;
- `PACKAGE-STATE-V8.tsv`;
- `PRECEDENCE-2026-09-03-FULL-V8.tsv`.

Additional AIRPOWER4 metadata files:
- `V8-CHANGELOG-1939AIRPOWER4-AIRFRAME1.md`;
- this audit MD;
- matching audit JSON.

## State-machine invariants
- combat clock advanced: **NO**;
- current revalidated combat checkpoint: **1939-04-20 24:00**;
- furthest prior explored old branch: **1939-09-01 00:00 / post-Nomonhan**;
- combat replay: **HOLD_FOR_AVIATION_AUDIT**;
- active technical domain: **PISTON_AVIATION**;
- post-1943 combat/procurement outcomes remain branch-dependent.

## Metadata policy
Final V8 metadata is rebuilt in this order:
1. `PACKAGE-INVENTORY-V8.tsv` over all ordinary files, excluding the three self-referential current metadata files;
2. `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv`, including the rebuilt inventory but excluding itself and `SHA256SUMS-V8.txt`;
3. `SHA256SUMS-V8.txt` over the same files represented by the full manifest.

Expected final counts after AIRPOWER4 metadata files are present:
- total files: **404**;
- inventory entries: **401**;
- full-manifest/SHA entries: **402**.

## Final validation — PASS
Release build validation completed:
- total files: **404**;
- inventory entries: **401**;
- manifest/SHA entries: **402**;
- tree SHA256 verification: **402/402 OK**;
- missing listed files: **0**;
- ZIP compressed-data test: **PASS**;
- ZIP round-trip extraction: **404 files restored**;
- round-trip SHA256 verification: **402/402 OK**.
