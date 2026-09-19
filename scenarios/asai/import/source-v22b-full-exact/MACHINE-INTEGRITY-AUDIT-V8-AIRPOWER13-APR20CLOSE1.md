# MACHINE INTEGRITY AUDIT — V8 AIRPOWER13 APR20CLOSE1

Expected final package structure after metadata regeneration:

- total files: **525**;
- `PACKAGE-INVENTORY-V8.tsv` data rows: **522**;
- `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv` data rows: **523**;
- `SHA256SUMS-V8.txt` targets: **523**.

Required final validation:

1. regenerate the inventory excluding the three current metadata files;
2. regenerate manifest/SHA excluding manifest and SHA themselves but including the new inventory;
3. create a fresh ZIP;
4. run ZIP integrity test;
5. unpack to a fresh directory and require **523/523 SHA256 OK**.

No combat-clock advance is represented by package generation.
