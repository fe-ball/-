# MACHINE INTEGRITY AUDIT — V8 EXHAUST1

Semantic state represented by this package:

- current chronological checkpoint: **1939-05-10 24:00**;
- combat replay: **ACTIVE_COMBAT_REPLAY**;
- next chronological gate: **1939-05-11 Nomonhan opening clash / border incident sequence**;
- EXHAUST1 is an **ON_DEMAND_ONLY technical closure** and does not advance the clock;
- piston-aircraft exhaust accounting now uses **EX0/EX1/EX2/EX3 state-differential semantics**;
- B5N2 old `historical individual exhaust -> E1=0` ruling is superseded;
- historical EX2 late-war anchors cannot receive the full collector-to-stack speed card again;
- exact named-unit retrofit counts, including 1939-05-10 24th Sentai Ki-27 exhaust fit, remain allocation/history gates.

Semantic guards checked:

1. Asai contribution is not set to zero merely because a historical aircraft has individual exhaust; residual EX2->EX3 improvement remains possible.
2. The same historical EX2 performance anchor cannot receive a second EX0->EX2 full speed gain.
3. Ki-84 production 631 km/h-class anchor is treated as already individual-exhaust-side for exhaust accounting.
4. J2M2/3 and N1K historical EX2 performance bands retain only residual exhaust attribution; engine/cooling/QC remains the larger worldline lever.
5. D4Y/Ki-61 exhaust optimization is separated from radiator/Meredith-type heat-recovery accounting.
6. B5N2 is current-working EX0 collector-ring; old E1=0 closure is no longer authoritative.
7. Technical adoption state does not auto-create procurement, retrofit orders, sentai fit, sortie strength or combat results.

Integrity build convention:

- `PACKAGE-INVENTORY-V8.tsv` excludes itself, `FULL-PACKAGE-MANIFEST-SHA256-V8.tsv`, and `SHA256SUMS-V8.txt`.
- manifest/SHA hash every package file except the manifest and SHA files themselves; inventory is checksum-covered.
- final ZIP is unpacked independently and every manifest target is rehashed.

Counts are regenerated in the build step and recorded in the companion JSON.
