# MACHINE INTEGRITY AUDIT — V8 1939REPLAY2 NANCHANG-A2

Semantic state represented by this package:

- current chronological checkpoint: **1939-05-10 24:00**;
- combat replay: **ACTIVE_COMBAT_REPLAY**;
- last closed combat gate: 1939-04-27 to 1939-05-09 Nanchang closeout;
- current concurrent technical events: E6 Twin No.1 first airframe flight 29 Apr; HS-2 first flight 4 May;
- E6 Single remains unflown;
- next chronological gate: **1939-05-11 Nomonhan opening clash / border incident sequence**;
- no Nomonhan future combat result, dense-core FIELD VALIDATED label or mobile-GT LIMITED STANDARD result is imported.

Semantic guards checked:

1. E6 Twin No.1 first airframe flight is not confused with later E6-M-J package flight.
2. HS-2 initial flight uses the ~475 kgf standard E6-S-J point; ~500 kgf high-flow and M0.6+ research envelope remain future.
3. Nanchang strategic result remains Japanese retention; worldline differences are tactical/operational depth, cohesion and loss deltas rather than new fantasy forces.
4. Chi-Ha remains absent from the Nanchang center branch.
5. Technical capability does not auto-create military procurement or combat deployment.

Integrity build convention:

- `PACKAGE-INVENTORY-V8.tsv` excludes the three current self-referential metadata files: itself, `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv`, and `SHA256SUMS-V8.txt`.
- the current manifest and SHA file hash every package file except the manifest and SHA file themselves; therefore the inventory file is itself checksum-covered.
- final ZIP must be independently unpacked and every manifest target rehashed before distribution.
