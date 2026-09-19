# MACHINE INTEGRITY AUDIT — V15

Status: **PASS**.

- Expected/final total files: **962**
- Expected/final SHA-256 manifest entries: **960**
- Expected/final package-inventory entries: **959**
- Manifest exclusions: exactly `FULL-PACKAGE-MANIFEST-SHA256-V15.tsv` and `SHA256SUMS-V15.txt`
- Inventory exclusions: itself plus the V15 manifest/checksum pair
- New V15 visual-current files under `83-CURRENT...`: **16**
- V15 master visual rows: **18**
- Fuselage/boom station rows: **171**
- Combat clock advanced: **NO**

## Visual/geometry structural checks

- All 18 master IDs are unique.
- P1, P2, Material No.1/2, E5 future-form, Ki-42, HS-2, E5 Twin, E6 Single, E6 Twin, E6-B, X-TP, A7M Gaifu, A8N Sakufu, Ki-40, AT-3, H1 and H2 are present.
- Trapezoid/piecewise wing-area reconstruction matches the locked reference areas within **1%**, with zero audit errors.
- Reference aspect-ratio recomputation matches the master table.
- All fuselage/boom station sets terminate at the locked length and stay within locked maximum width/height envelopes.
- Landing-gear track remains inside the relevant wing/rotor envelope.
- A7M tip fold is locked at y=5.45 m and gives ~10.90 m horizontal folded width.
- A8N piecewise wing integrates to ~30.952 m² before rounded-tip/fillet correction to the 31.0 m² reference and uses the y=3.50 m major fold.
- A8N cold-flow cascade is explicitly bypass-only; no core-nozzle vector, hover or vertical landing is introduced.
- E6 Single old 14.2 m² visual proxy is superseded by the 17.5 m² visual/service geometry.
- E6 Twin old 14 m² shortcut is rejected; V15 uses 19.0 m² / 10.90 m reference geometry.
- Ki-42 V15 geometry is explicitly a CG-OML reference, **not** a fabricated claim of a recovered manufacturer production drawing.
- Material No.1 and P2 are separate physical aircraft but deliberately share exact external OML for structural A/B comparison.
- H1/H2 retain 1930s/1940 mechanical rotor-head/control visual language; no modern electronic-stabilization hardware is backfilled.
- AT-3 receives a 1941 design-freeze OML only; 1941 flight/OOB remains zero.
- J2N, H3, HS-3 and clean-sheet E7 final OML remain intentional non-closes.

## Authority checks

- V12 fixed-wing performance/procurement authority is retained.
- V13 helicopter performance/development authority is retained.
- V14 ground/naval authority is retained.
- V15 is highest authority only for fictional-aircraft visual/outer-mold-line questions.
- No naming, procurement, OOB, measured performance, combat result or post-1941 operational history was created by the visual closeout.

TSV schema, duplicate-ID, geometry-equation and pointer checks: **PASS**.
Final independent ZIP extraction/hash verification: **PASS** — 962 total files, 960 manifest entries, 0 missing, 0 size mismatches, 0 SHA-256 mismatches.
