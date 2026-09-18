# GT E5-J / E5-JF INSTALLED PRODUCT CANON — V8 AIRPOWER6

> **AIRPOWER6 local-product authority.** Read `00A-MANDATORY-CHEAT-CAPABILITY-PREFLIGHT-CANON-V8.md` first. This file does not re-judge whether E5 is "too early" and does not apply a second reincarnator bonus. It closes the E5 pure-jet / aft-fan local installed ledger using the already accepted v40/v41/v43 E5 gas path and the v46 jet/JF accounting pattern.

## 0. Upstream held fixed

- E5 technology coordinate: PR6 / ~800 C class / component efficiency ~0.83.
- E5-S standard shaft gas path: 7.6 kg/s.
- E5 jet high-flow gas path: **8.4 kg/s** working center; this is a deliberate jet trim, not the standard 7.6 kg/s shaft point operated at choke.
- compressor: **5-stage axial booster + one centrifugal HP stage**, ~17.5 krpm, fixed IGV + interstage bleed; variable inlet swirl is allowed on high-flow trims.
- v40 cooling/pressure/mechanical ledger is retained: non-Ni quantity 765 C uses ~4% staged cooling flow; non-Ni 800 C full uses ~6%; Ni 800 C uses ~4%; combustor total-pressure loss ~3.5%.
- v39 `L_core` remains authoritative and is not replaced by historical early-jet TBO analogies.

Reproducible local calculation:
`99-SUPPORT-CURRENT/GT-REBASE-COMPUTATION/e5_j_jf_installed_v8.py`.

## 1. E5-J pure turbojet closure

The v46 nozzle/work balance, applied to the accepted E5 high-flow gas path, reproduces the old v48 pre-audit shadow almost exactly.

| product/rating coordinate | TIT | static thrust calc | static TSFC | fuel at full static point | verdict |
|---|---:|---:|---:|---:|---|
| **E5-J-Q** non-Ni quantity | 765 C | **426 kgf** | **0.838 kg/(kgf h)** | ~357 kg/h | product headline **425-430 kgf** |
| **E5-J-N** non-Ni full | 800 C | **451 kgf** | **0.827** | ~373 kg/h | product headline **450-455 kgf** |
| E5-J-Ni @800 C | 800 C | ~451 kgf | ~0.845 | ~381 kg/h | Ni buys life/hot-high margin at the same TIT, not free thrust/SFC |
| **E5-J-M selected short shadow** | 830 C Ni selected build | **471 kgf** | ~0.852 | ~402 kg/h | short/high-performance coordinate only; not common E5 headline |

Therefore:

- old **~300 kgf E5 jet** is superseded as a current product anchor;
- current normal E5-J discussion should use **~430 kgf quantity / ~450-455 kgf normal high-performance**;
- the already used aircraft planning band **445-460 kgf** is well centered inside the closed product envelope;
- **~470 kgf** is allowed as a selected short/high-output E5 point when the Ni/hot-section and emergency-minute ledger is paid; it is not a blanket fleet rating.

The E5 800 C generation coordinate remains meaningful: a short selected rating may exceed it without redefining the whole E5 generation, just as generation, material line and rating are separate axes.

## 2. E5-J mass and envelope

The v41 E5 shaft engine assembly is 390-460 kg including free power turbine, reduction and shaft-specific accessories. The pure jet removes the power-turbine/reducer output train, adds the 8.4 kg/s high-flow inlet/compressor trim and a real tailpipe/nozzle package, and retains the centrifugal compressor/diffuser diameter.

AIRPOWER6 product closure:

- **E5-J complete dry engine: 380-415 kg; center ~395 kg**.
- working maximum engine OD: **~0.69-0.76 m**, dominated by the centrifugal compressor/diffuser/combustor casing rather than the nozzle.
- working complete length: **~1.80-2.05 m** depending accessory/nozzle arrangement.

These are finished-engine coordinates, not nacelle/pylon/intake installation mass. Aircraft-local intake, mount, firewall, duct and fairing remain airframe accounts.

## 3. E5-JF aft-fan architecture

Architecture remains:

**E5 single-spool gas generator -> one-stage independent free LP turbine -> direct-drive one-stage aft fan + stator -> separate core/bypass exhausts.**

This is not a passive fan and not a two-spool compressor. The additional rotating spool is real, but the gas-generator compressor remains the E5 single spool.

Existing mature flight anchor is retained:

- bench static **535-565 kgf**;
- installed usable **515-545 kgf**;
- complete dry **455-505 kg**;
- BPR **~0.8-1.0**;
- FPR **~1.25-1.30**;
- matched-condition static TSFC **~15-18% below E5 pure-J**.

The AIRPOWER6 calculation explains this anchor rather than replacing it.

### 3.1 765 C practical/quantity gas-generator point

At FPR 1.30:

| BPR | static thrust | TSFC | fan shaft | free-turbine extraction |
|---:|---:|---:|---:|---:|
| 0.8 | ~506 kgf | ~0.705 | ~189 kW | ~195 kW |
| **0.9** | **~516 kgf** | **~0.692** | **~213 kW** | **~220 kW** |
| 1.0 | ~525 kgf | ~0.680 | ~237 kW | ~244 kW |

Against the same 765 C pure-J point (~426 kgf / 0.838 TSFC), BPR~0.9 gives roughly **+21% static thrust and -17% TSFC**.

### 3.2 800 C high-performance gas-generator point

At FPR 1.30, BPR 0.8-1.0 gives roughly **533-552 kgf** calculated. The existing installed usable upper anchor remains **~545 kgf**, because duct/free-turbine/fan mechanical release, installation scatter and life are product gates. Do not turn the ~552 calculation corner into an automatic service rating.

Thus the practical product ladder is:

- **JF-Q / practical mission:** ~515-525 kgf at the 765 C quantity line;
- **JF-N / selected high-performance:** ~535-545 kgf installed after backend qualification;
- bench/selected development points may extend toward the existing ~565 kgf bench anchor without becoming a general aircraft rating.

## 4. Fan geometry and rotational speed

For 8.4 kg/s core flow, FPR 1.30, hub/tip ~0.72, face velocity ~110 m/s:

| BPR | bypass flow | fan tip D | fan hub D | speed |
|---:|---:|---:|---:|---:|
| 0.8 | 6.72 kg/s | ~0.363 m | ~0.261 m | ~13.0 krpm |
| **0.9** | 7.56 kg/s | **~0.385 m** | **~0.277 m** | **~12.3 krpm** |
| 1.0 | 8.40 kg/s | ~0.406 m | ~0.292 m | ~11.6 krpm |

Tip speed is ~247 m/s and the simple combined relative tip Mach is ~0.80. No transonic/highly-loaded fan is required.

Release band:

- fan tip **~0.36-0.41 m**;
- speed **~11.5-13.2 krpm**;
- free-turbine/fan power **~0.20-0.24 MW** at the principal FPR1.30 points.

## 5. Aft-module mass and package consequence

Scaling the already accepted E6 aft-module component ledger to the E5 fan diameter/power gives an E5 aft-module addition of roughly:

- fan/stator/local casing: ~20-30 kg;
- one-stage free LP turbine/nozzle row: ~15-22 kg;
- shaft/bearings/seals/support: ~12-18 kg;
- bypass duct/rear casing/reinforcement: ~15-20 kg;
- controls/oil/local accessories: ~5-8 kg;
- **total addition: ~70-95 kg; center ~85 kg**.

This is consistent with the retained total E5-JF dry mass **455-505 kg, center ~480 kg** when the E5-J center is ~395 kg.

Working JF complete length is **~2.25-2.55 m**.

### Important geometry correction

The E5 centrifugal compressor/diffuser already drives a ~0.69-0.76 m maximum engine OD. The aft-fan tip is only ~0.36-0.41 m and its local casing is roughly ~0.47-0.54 m. Therefore **E5-JF does not pay a large new maximum frontal-area tax merely because it has an aft fan**.

Its principal aircraft taxes are:

- ~70-95 kg/engine added dry mass;
- ~0.45-0.55 m additional rear package length;
- greater rear wetted area and local structure;
- CG / mount / tailpipe integration;
- added free-spool controls, bearings and inspection.

This narrows the expected clean high-speed penalty relative to old shorthand descriptions.

## 6. Life / inspection / rating semantics

Do not overwrite v39 `L_core`:

- E5 Ni @800 C: **400-700 h** rated core hot-section coordinate;
- E5 non-Ni @800 C full: **150-300 h**;
- E5 non-Ni @760-770 C quantity: **350-600 h**.

AIRPOWER6 adds product-planning intervals without claiming fleet historical MTBO:

### E5-J-Q / JF-Q, non-Ni 765 C

- mature hot-section inspection planning: **~50-75 h early, ~75-100 h after stable teardown evidence**;
- product scheduled-removal/OH target: **~250-400 h** depending starts/mission duty;
- `L_core` remains 350-600 h and is not replaced by the OH target.

### E5-J-N non-Ni 800 C full

- hot-section inspection: **~40-60 h**;
- scheduled-removal/OH target: **~100-200 h**;
- appropriate for high-value/high-performance duty, not the quantity workhorse line.

### E5 Ni 800 C used for life/hot-high margin

- inspection: **~75-100 h** working target;
- scheduled-removal/OH target: **~300-450 h** if the Ni margin is spent on life rather than higher thermal rating.

### selected 820-830 C short rating

Do not assign a generic TBO by extrapolation. Record cumulative high-TIT/emergency minutes and require hot-section inspection after a defined accumulated budget. Initial working budget is **30-60 cumulative minutes between special inspection/review**, to be widened only by E5-family test evidence.

JF does not automatically shorten the gas-generator `L_core`; the added cold/free-spool module gets its own bearing/fan-cycle ledger. Early JF inspection can remain more frequent while the additional spool is being matured even though the hot-section coordinate is inherited.

## 7. 1937-39 chronology

Current chronology is:

- 1933-34: E4-scale fan/free-turbine rig work;
- 1934-35: E4/E5 transition full-scale rigs;
- 1935-36: E5 JF is a planned military-twin comparison backend;
- 1936 Q2-Q3: E5 single pure-J flight generation established;
- 1937 Q1-Q2: E5 Twin No.1 pure-J flight;
- **1937 Q4: E5 Twin No.2 aft-fan first flight**;
- 1938: durability, controls, mission fuel, module exchange and maintenance maturation;
- 1939-04-20: E5-J is mature reference/evaluation propulsion; E5-JF is a mature practical-mission comparison propulsion, not a concept awaiting first proof.

Any surviving statement that treats Sep-Oct 1938 as the first E5 aft-fan flight is superseded on chronology while its later measured engine anchors may remain valid.

## 8. What this closes / what remains local

CLOSED:

- E5-J static thrust/TSFC rating coordinates;
- E5-J dry mass and engine envelope working product band;
- E5-JF fan diameter/rpm/power;
- E5-JF aft-module mass explanation;
- E5-JF rating/life semantics and 1937 Q4 first-flight chronology.

Still aircraft-local:

- exact inlet/duct/nacelle drag and altitude map on each airframe;
- mission-average fuel/range; static TSFC improvement must not be converted directly into a fixed range percentage;
- exact E5 Twin follow-on J/JF propulsion mix;
- any Ki-42 JF derivative;
- field historical TBO statistics versus engineering release targets.
