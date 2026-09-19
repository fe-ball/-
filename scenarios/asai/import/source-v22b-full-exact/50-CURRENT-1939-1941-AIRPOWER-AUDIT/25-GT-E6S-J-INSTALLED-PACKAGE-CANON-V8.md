# GT E6-S-J INSTALLED PACKAGE CANON — V8 AIRPOWER7

> **AIRPOWER7 local-product authority.** Read `00A-MANDATORY-CHEAT-CAPABILITY-PREFLIGHT-CANON-V8.md`, `20-GT-E6S-JF-E7-E9-REBASE-CANON-V8.md` and `21-GT-LIFE-RATING-SEMANTICS-CANON-V8.md` first. This file closes the E6-S pure-jet package around the already accepted PR7 small core. It does not re-rate E6-M and does not use historical early-jet values as a second ceiling.

## 0. Parent identities held fixed

- E6-S compressor: **7 axial + 1 centrifugal HP**, PR7, design corrected flow **7.8 kg/s**, working trim **7.6-8.2 kg/s**, ~18 krpm.
- mechanically scheduled **VIGV + stage-4 bleed** is standard E6-S architecture.
- centrifugal impeller tip coordinate is ~471 m/s, which at 18 krpm implies an impeller diameter of almost exactly **0.50 m**; this is close to E5 and remains the main small-core diameter driver.
- E6 thermal coordinates remain non-Ni **870 C / ~5% cooling-bleed** and selected Ni **920 C / ~4.5%** unless a local rating deliberately chooses a lower TIT.
- v46 pure-jet nozzle accounting is retained: inlet recovery, compressor work, combustor loss, cooling/bleed, accessory/mechanical work, turbine work and a real choked nozzle are all paid before thrust is quoted.

Reproducible local calculation:

`99-SUPPORT-CURRENT/GT-REBASE-COMPUTATION/e6_s_j_installed_v8.py`

## 1. Static installed engine-side closure

| rating coordinate | flow | TIT | static thrust | static TSFC | full-static fuel | status |
|---|---:|---:|---:|---:|---:|---|
| C long-duration shadow | 7.8 kg/s | 820 C | ~444 kgf | ~0.780 | ~346 kg/h | lower thermal duty option |
| C+ long-life shadow | 7.8 | 835 C | ~454 kgf | ~0.786 | ~357 kg/h | long-duration comparison |
| intermediate | 7.8 | 850 C | ~463 kgf | ~0.792 | ~367 kg/h | rating interpolation |
| **N non-Ni standard** | **7.8** | **870 C** | **~476 kgf** | **~0.799** | **~380 kg/h** | **standard E6-S-J development rating** |
| M Ni selected | 7.8 | 890 C | ~487 kgf | ~0.807 | ~394 kg/h | selected hot/high point |
| **M Ni upper** | **7.8** | **920 C** | **~505 kgf** | **~0.820** | **~414 kg/h** | selected Ni upper coordinate |
| **HF non-Ni short** | **8.2** | **870 C** | **~500 kgf** | ~0.799 | ~399 kg/h | **short/high-flow trim** |
| HF Ni upper short | 8.2 | 920 C | ~531 kgf | ~0.820 | ~435 kg/h | short selected ceiling; not standard |

Therefore the AIRPOWER5 pre-audit distinction is retained and promoted:

- **standard-flow E6-S-J = ~475 kgf non-Ni / ~505 kgf Ni**;
- **8.2 kg/s high-flow short trim = ~500 / ~530 kgf**;
- the latter is not silently converted into the standard catalog rating.

## 2. Nozzle closure

At sea-level static the accepted points are choked in the v46-compatible model.

- 870 C / 7.8 kg/s effective throat area: **~0.0286 m2**, equivalent circular diameter **~0.191 m**;
- 920 C / 7.8 kg/s: **~0.0278 m2**, equivalent **~0.188 m**;
- 8.2 kg/s high-flow points require roughly **0.0293-0.0300 m2**, equivalent **~0.193-0.196 m**.

This is the effective nozzle throat, not the outer tailpipe/nacelle diameter. A simple robust convergent rear nozzle is sufficient for the first HS-2 flight package; variable-area/reheat nozzle work remains the separate advanced branch in file 22.

## 3. Complete dry mass and envelope

E6-S does not pay an E6-M-sized frontal-area tax. Its centrifugal impeller diameter remains almost the same as E5; the main physical change is two additional axial stages, VIGV scheduling hardware and the PR7/higher-TIT hot-section update.

AIRPOWER7 closure:

- **complete dry E6-S-J: ~400-445 kg, center ~420 kg**;
- maximum engine OD: **~0.70-0.77 m**, center ~0.735 m;
- complete engine length: **~1.95-2.22 m**, center ~2.08 m.

Engineering delta from the closed E5-J center (~395 kg):

- two added axial rotor/stator rows + longer compressor case: roughly +10-16 kg;
- VIGV mechanism / schedule hardware: +3-5 kg;
- PR7 compressor/diffuser/shaft/bearing strengthening: +3-6 kg;
- higher-TIT cooling/manifold/liner/turbine-root update: +4-8 kg;
- newer detailed design and removal of E5-specific development allowances offset part of the gross addition.

The resulting center near 420 kg is also consistent with the separately accepted E6-M pure-jet mass implied by the E6-M-JF ledger; the S-core remains substantially lighter while its centrifugal casing keeps diameter relatively large for its flow.

## 4. 1939-04-20 qualification state

Do not confuse core maturity with this backend's product state.

### Already inherited / paid

- E6-S PR7 compressor/VIGV/bleed architecture is product-side mature enough for shaft derivatives.
- pure-jet fuel/nozzle/control/aircraft operation is inherited from E5-J.
- high-speed instrumentation and E5-J inlet/nozzle calibration are inherited through HS-1 and E5 single/twin flight work.

### E6-S-J local state at the checkpoint

- physical flight-development engines exist;
- full engine ground running and aircraft-installed ground/taxi integration exist for HS-2;
- standard first-flight coordinate is **7.8 kg/s / non-Ni 870 C / ~475 kgf**;
- the 8.2 kg/s ~500 kgf trim is a later/special envelope-expansion point, not required for first flight;
- engine-side state = **late R3 / R4 flight-release candidate**;
- aircraft first-flight release is still pending the final HS-2 aircraft/inlet/flutter/brake/emergency board and is not converted here into a flown result.

The exact accumulated rear-package qualification hours are not fabricated here. E6-S core endurance and E5-J backend experience are inherited, but the E6-S-J combination still owes its own flight-release sign-off and later product endurance.

### Not yet claimed

- R5 qualified general aviation product;
- R6 serial/service maturity;
- measured altitude thrust / speed map from HS-2 flight;
- a fleet TBO or field MTBO.

## 5. Life/rating semantics

No new blanket E6 life number is invented. Use file 21:

- `L_core` / hot-section life is an E6 material/rating coordinate and remains a separate audit from this rear package;
- E6-S-J nozzle/controls/accessories inherit substantial E5-J experience and therefore do not reset all development clocks to zero;
- 8.2 kg/s high-flow and 920 C Ni points accrue their own high-flow/high-TIT minute and inspection debt until product endurance is proven;
- a later service TBO must be derived from E6 teardown evidence, not imported from W1/Jumo/Welland history and not inferred directly from E5 `L_core`.

## 6. Consequence for HS-2

The current HS-2 architecture does not require a new engine core and does not need an 850-900 kgf E6-M.

At 1939-04-20:

- HS-2 has one dedicated airframe in completed / ground-test / high-speed-taxi release band;
- installed propulsion is one **~420 kg dry E6-S-J development package**;
- initial flight is planned on the **~475 kgf standard-flow non-Ni point**;
- ~500 kgf non-Ni high-flow is an envelope-expansion option after engine/inlet data are satisfactory;
- the dedicated research-aircraft mission therefore remains consistent with the previously closed ~1.7-1.9 t class HS-2 concept without consuming the much larger E6-M.

## 7. What this closes / what remains

### CLOSED

- E6-S-J standard/high-flow thrust distinction;
- static TSFC/fuel-flow coordinates;
- effective nozzle throat band;
- complete dry mass / OD / length engineering product band;
- 1939-04-20 qualification state as late-R3 / R4 flight-release candidate;
- HS-2 initial engine/rating identity.

### OPEN / later measured or local product audit

- HS-2 measured altitude/inlet/thrust/drag map after first flight;
- E6-S-J R5 service qualification / TBO / production yield;
- any E6-S-J operational military product or procurement;
- reheat/variable-nozzle derivative;
- any different inlet/aircraft installation beyond the HS-2 development package.

## 8. Supersession guard

Superseded where conflicting:

- `E6-S-J standard = 500/530 kgf` without distinguishing 7.8 vs 8.2 kg/s;
- `E6-S-J must wait for a new dedicated core`;
- `E6-S-J is already a qualified service product on 1939-04-20`;
- `HS-2 first flight requires E6-M`.
