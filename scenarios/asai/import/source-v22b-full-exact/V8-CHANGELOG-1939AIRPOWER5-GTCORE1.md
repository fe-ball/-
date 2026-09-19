# V8 CHANGELOG — 1939AIRPOWER5 / GTCORE1

Date: 2026-09-04

## Purpose

Repair the GT/jet audit after confirming that the v38-v46 propulsion rebaseline was already built on reincarnator foreknowledge, pre-paid industrial clocks, computation, QC/test infrastructure and organization-level convergence. Prevent future reviewers from applying a second historical-calendar downrating to those already-rebaselined values.

No combat-history clock is advanced. Current checkpoint remains **1939-04-20 24:00**.

## Highest-level changes

1. Added mandatory capability preflight `00A-MANDATORY-CHEAT-CAPABILITY-PREFLIGHT-CANON-V8.md`.
2. Rebased E6-S/JF/E7-E9 semantics in file 20 without undoing v46 E6-M installed values.
3. Separated GT life/rating semantics in file 21; rejected blanket substitution of historical early-jet TBO bands for accepted Asai-worldline life coordinates.
4. Added explicit 1939 readiness states for VSV, true two-spool, reheat/variable nozzle, aft/front fan, cooling and higher-PR work in file 22/22A.
5. Copied the selected v38-v48 upstream parents and calculation shadows into `99-SUPPORT-CURRENT/GT-REBASE-SOURCE-SELECTED/` so the mandatory capability rule is auditable from the current package without hunting through deep provenance trees.
6. Updated root START-HERE, PACKAGE-STATE, precedence and state-machine workfront.

## Retained accepted installed values

- E6-M pure-J non-Ni 870 C: product about **850 kgf**.
- E6-M pure-J Ni 920 C: product about **900 kgf**.
- E6-M-JF at accepted 835 C long-life production center: central calculation about **984 kgf**, product **950-1,000 kgf**.

These values are already cheat/computation-aware v46 outputs. AIRPOWER5 does not add a generic bonus and does not apply a generic historical penalty.

## E6-S repair

The E6-S standard compressor coordinate is 7.8 kg/s, with 7.6-8.2 kg/s as the working trim band. Same-cycle/nozzle shadows scaled from the accepted PR7 method give:

- 7.8 kg/s non-Ni 870 C: ~475.6 kgf;
- 7.8 kg/s Ni 920 C: ~505.2 kgf;
- 8.2 kg/s high-flow short trim non-Ni: ~500.0 kgf;
- 8.2 kg/s high-flow short trim Ni: ~531.1 kgf.

These are not yet a fully closed S-core finished-engine package because dry mass, diameter, local nozzle and qualification remain to be audited. They supersede the conversational shortcut that treated ~500/~530 kgf as the standard 7.8 kg/s coordinate.

## JF rating repair

The v46 835 C JF point is a deliberately selected long-life production center, not the maximum thermal capability of the architecture. The unchanged v46 model yields higher same-architecture capability shadows above 1,000 kgf as TIT rises. They do not become product ratings until gas-generator life, free-LP turbine, fan/shaft/bearing, duct/nozzle and inspection debt are closed.

## E7-E9 / advanced branch interpretation

- E-generation is a continuous technology-front coordinate, not an invention/model-year rail.
- VIGV/bleed and hollow cooled blades are already product/inherited technology before 1939.
- multi-row VSV = 1939 R2 subsystem work;
- true two-spool gas generator = 1939 R1-R2 coupling/rig work, no integrated fired flight core yet;
- reheat/variable nozzle = 1939 R2 short-duration static backend work, flight package open;
- front fan/true low-BPR = R1-R2 integrated-drive branch, flight engine open;
- advanced staged cooling = R1-R2, while base hollow cooling is already inherited/productized;
- E8/E9 mature-year labels remain technical-coordinate windows, not R&D start dates.

## Life semantics

Current documents must distinguish at least:

`L_mat / L_core / H_qual / TBO_prod or OH_prod / cycle-emergency ledger`.

Accepted v39 E4/E5 upstream `L_core` coordinates remain. Historical W1/Jumo/Welland hours may calibrate mechanisms and semantics but do not impose a calendar ceiling on Asai after the v38-v46 rebaseline.

## Remaining local GT work

The broad upstream GT capability basis is substantially closed. Remaining work is product-local:

- E5 pure-J / aft-fan installed audit;
- E6-S-J dry mass/diameter/nozzle/product qualification;
- E6-M-JF higher-rating endurance and backend qualification;
- reheat/nozzle installed augmentation and flight release;
- any selected true-two-spool/front-fan integrated engine;
- E7-E9 product maps only when an actual product/requirement is selected.

## Integrity

AIRPOWER4 source checksum set was reverified **402/402 OK** before AIRPOWER5 metadata rebuild. New root inventory/manifest/SHA256 are rebuilt for the final AIRPOWER5 tree.
