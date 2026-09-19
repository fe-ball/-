# ASAI FULL V5 MECHFIX1 — Machine Integrity Audit

**Overall: PASS**

Scope: structural/payload audit. The final inventory/manifest/SHA256SUMS are regenerated after this report and are verified during final package build.

- TSV schema: PASS — 144 TSV files, 4195 data rows, 0 width/parse problems.
- JSON parse: PASS — 6 JSON files.
- XLSX container/XML: PASS — 4 workbooks; 0 container/XML problems; 0 stored formula-error tokens.
- Embedded V4 byte identity: PASS — 111 original V4 files checked.
- Gate-number presence 36–76: PASS — missing none.
- Case-fold collisions: PASS — 0.
- Symlinks: PASS — 0.
- Control pointer existence: PASS.

## Mechanical repair included

- `ASAI-1937-MANCHURIA-BRANCH-PNL-V1.tsv` now obeys its four-column schema; `Branch ROCE` remains 8.8 percent and is represented as a four-field row.
- `01-BASE-V4` is byte-identical to the uploaded V4 archive.
- V5 precedence, file-level master index, and supersession guard are present at package root.
