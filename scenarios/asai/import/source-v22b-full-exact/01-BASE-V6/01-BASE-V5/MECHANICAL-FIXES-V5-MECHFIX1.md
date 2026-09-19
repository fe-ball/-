# V5 mechanical fix 1 — 2026-08-30

This package keeps the V5 semantic/worldline content intact and repairs package-engineering issues only.

Changes:
- repaired the single malformed TSV row in `ASAI-1937-MANCHURIA-BRANCH-PNL-V1.tsv` by restoring the declared four-column schema; the ROCE value remains 8.8 percent and no modeled value is changed;
- added `PRECEDENCE-2026-08-30-FULL-V5.tsv`;
- added `CURRENT-MASTER-FILE-INDEX-V5.tsv` as a mechanical file-level authority/navigation index (not a new semantic claim ledger);
- added `TERMINOLOGY-AND-SUPERSESSION-GUARD-V5.tsv` from already-explicit V5 rulings;
- added V5 machine-integrity audit JSON/Markdown;
- regenerated package state, payload inventory, SHA-256 manifest and final checksum set with explicit non-circular coverage rules.

Integrity coverage:
- `PACKAGE-INVENTORY-V5.tsv`: payload/control files, excluding inventory itself, manifest and SHA256SUMS;
- `FULL-PACKAGE-MANIFEST-SHA256.tsv`: every file except the manifest itself and SHA256SUMS;
- `SHA256SUMS-V5.txt`: every file except SHA256SUMS itself.

The embedded `01-BASE-V4` is not modified.
