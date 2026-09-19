# MACHINE INTEGRITY AUDIT — V8 1939REPLAY1 NANCHANG-A1

Expected final package structure after metadata regeneration:

- total files: **537**;
- `PACKAGE-INVENTORY-V8.tsv` data rows: **534**;
- `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv` data rows: **535**;
- `SHA256SUMS-V8.txt` targets: **535**.

Required final validation:

1. regenerate inventory excluding the three current metadata files;
2. regenerate manifest/SHA excluding manifest and SHA themselves but including the new inventory;
3. create a fresh ZIP;
4. run ZIP integrity test;
5. unpack to a fresh directory and require **535/535 SHA256 OK**.

Workflow state represented by this package is **ACTIVE_COMBAT_REPLAY** at **1939-04-26 24:00**. The next chronological gate is **1939-04-27 Nanchang Japanese counteroffensive**.
