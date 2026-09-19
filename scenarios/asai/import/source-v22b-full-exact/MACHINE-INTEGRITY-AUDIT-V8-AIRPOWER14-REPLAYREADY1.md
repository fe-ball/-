# MACHINE INTEGRITY AUDIT — V8 AIRPOWER14 REPLAYREADY1

Expected final package structure after metadata regeneration:

- total files: **532**;
- `PACKAGE-INVENTORY-V8.tsv` data rows: **529**;
- `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv` data rows: **530**;
- `SHA256SUMS-V8.txt` targets: **530**.

Required final validation:

1. regenerate inventory excluding the three current metadata files;
2. regenerate manifest/SHA excluding manifest and SHA themselves but including the new inventory;
3. create a fresh ZIP;
4. run ZIP integrity test;
5. unpack to a fresh directory and require **530/530 SHA256 OK**.

Workflow state represented by this package is **READY_TO_RESUME_COMBAT_REPLAY** at **1939-04-20 24:00**. Package generation itself does not advance the clock.
