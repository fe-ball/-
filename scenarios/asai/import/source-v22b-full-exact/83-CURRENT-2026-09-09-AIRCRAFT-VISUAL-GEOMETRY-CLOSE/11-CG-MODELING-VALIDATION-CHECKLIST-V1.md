# CG MODELING VALIDATION CHECKLIST V1

A model is V15-canonical only if all applicable checks pass:

1. overall length/span/rotor diameter and wing area agree with `01-CG-GEOMETRY-MASTER`;
2. wing root/tip chord, sweep, dihedral, washout and wing-root station agree;
3. fuselage loft passes through the station envelopes in `02` without adding a second major bulge;
4. canopy/cabin does not change the stated crew/cabin architecture;
5. landing-gear track/wheelbase and retraction/fixed arrangement agree;
6. propeller diameter or nacelle diameter/engine module is correct for the engine family;
7. E6-M-JF models show the longer aft-fan body; pure-J nacelles do not acquire a fake fan fairing;
8. A8N cold-flow cascade moves only the bypass stream; no hot-core VTOL nozzle;
9. A7M and A8N wing folds occur at their locked axes and produce the stated folded widths;
10. mission/bomb bay doors remain flush when closed and do not become permanent external bomb racks;
11. H1/H2 rotor blade count, rotor diameter, tail-rotor side and gear architecture are correct;
12. historical Ki-76 is modeled from historical geometry rather than re-skinned as P2;
13. J2N/H3/HS-3/E7 clean-sheet future types are not given a definitive OML from this file set;
14. livery/tactical codes are clearly separated from OML authority.

The modeling asset may add sub-centimeter fillets, panel gaps and serial-specific antennae, but must not change silhouette-defining dimensions without a new visual-geometry revision.
