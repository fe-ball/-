# FIRE CONTROL / SIGHTING / BOMBING INTEGRATION — CANON — V8 FIREOPTICS1

> Session closure: 2026-09-05. Current combat checkpoint after this overlay: **1939-06-27 24:00**. This file promotes and revalidates the useful core of the older `asai-works-cross-domain-computation-fire-optics.md`, `asai-works-aviation-controls-gate.md`, and the aviation-torpedo sighting parent into the current V8 authority stack.
>
> This file does **not** mean that Asai manufactures every sight/director. Asai supplies upstream computation, metrology, electrical/QC methods, test services and selected components; Army/Navy arsenals, optical makers and aircraft/ship manufacturers perform weapon integration, procurement and service adoption.

## 0. Core rule — same weapon does not imply same fire effect

A weapon identity or aircraft designation is not enough to copy a historical hit probability, dispersion, bombing CEP, first-round hit rate or sortie damage result.

Resolve the complete chain:

`observation / target estimate -> sensor / sight -> input -> calculation / correction -> indication -> stabilization / boresight -> weapon mount / release mechanism -> ammunition / ballistic lot -> crew execution -> environment -> observed effect`

A worldline change at one stage changes only the error/time component that stage controls. It does not automatically erase the others.

Therefore:

- better optics do not create a generic combat hit-rate multiplier;
- better calculation does not overcome bad range/target-motion estimates;
- better boresight does not change projectile penetration or explosive effect;
- better bomb tables do not remove wind, formation, visibility, flak or pilot error;
- better director computation does not overcome mount slew, fuze-setting, ammunition-feed or sensor limits;
- a later historical gyro/reflector/director state may not be backdated solely because upstream computation capability exists.

## 1. Fire-control state tags

These tags supplement ID0-ID5/IDH and EX0-EX3. They describe the **fire-control chain**, not the vehicle identity.

- **FCS0 — historical/basic chain:** no current worldline change established beyond ordinary service variation.
- **FCS1 — calibration/QC chain:** historical sight/director architecture retained; optical quality, boresight, instrument calibration, ammunition lot control, mounting, maintenance and repeat setting are improved.
- **FCS2 — dedicated sight/calculator/workflow improvement:** a modified sight, mechanical calculator, release/lead aid, improved transmission or formalized test/table system is adopted. Adoption and weight/power/training remain gates.
- **FCS3 — integrated gyro/electrical/analog assistance:** synchro/resolver/gyro/servo or dedicated continuous analog elements reduce crew workload and follow-up delay. Date/type-specific; not a generic 1939 aircraft state.
- **FCS4 — mature integrated director/automatic-follow-up system:** requires a local weapon/director/servo/sensor audit. Never inferred from Asai computation capability alone.

## 2. 1939 fixed-gun fighter closure

### Ki-27 Type 97 fighter

For the current Nomonhan replay through 1939-06-27:

- standard service sight remains the **Type 89 telescopic gun sight**;
- **no blanket Army reflector-sight retrofit is current**;
- Navy reflector-sight capability is not permission to transfer a later/new sight into every Army Ki-27;
- current Ki-27 fire-control state is **FCS1**.

Worldline deltas allowed under FCS1:

- optical element centering/focus and acceptance consistency;
- sight-to-airframe datum calibration;
- gun boresight and convergence/re-zero repeatability;
- gun-mount fastener/alignment and vibration control where already paid by airframe/QC work;
- synchronization timing and functional acceptance;
- ammunition-lot consistency and tracer/ballistic table control;
- faster, more repeatable re-boresight after maintenance or gun replacement.

What is **not** granted:

- no gyro prediction sight;
- no automatic lead computation;
- no removal of the telescopic sight's field-of-view/head-position/G-load limitations;
- no fixed `+X% kills` or `+X% hit rate` card;
- no change in 7.7 mm projectile terminal effect unless ammunition is separately changed.

Combat replay should express the benefit primarily as fewer badly aligned aircraft, less ammunition wasted through systematic misalignment, and more repeatable first-burst placement when engagement geometry is already favorable. Pilot skill, range estimation, deflection judgment and tactical position remain dominant.

### Other 1939 Army/Navy fighters

Use the same method. Historical reflector sights that are genuinely fitted remain historical hardware anchors; the V8 delta is then residual FCS1/FCS2 calibration/integration unless a local adoption gate closes a different sight. Do not add a full sight benefit twice to a historical anchor that already includes it.

## 3. 1939 level bombing closure — Ki-21 / Ki-30 class

For current 1939 Army level/light bombing, keep the historical bombsight architecture/airframe station as the hardware anchor unless a local type file says otherwise. Do **not** put a future stabilized analog bombing computer into line units.

Current worldline state is **FCS1 with limited FCS2 workflow/test support**:

- bombsight optical calibration and mounting datum control;
- airspeed and altitude instrument calibration used by the bombing solution;
- bomb-type ballistic/drop tables built from better instrumented trials;
- release-delay measurement and release mechanism acceptance;
- wind-correction tables and setting cards;
- pre-sortie target folder / aimpoint preparation where reconnaissance allows;
- formation lead-bomber setting discipline;
- post-sortie statistical analysis of systematic miss direction and setting error.

The gain is mainly reduced **systematic aim/release error and repeat-setting scatter**. Random formation spread, turbulence, cloud, flak, crew estimation and target movement remain.

### Replay-use band

For a **well-briefed daylight area target** with usable weather, trained crews and pre-existing reconnaissance, current 1939 V8 may use a working **+5-10% effective target-area bomb concentration** versus a matched-history package with the same aircraft, bomb load, height and sortie count.

This is **not**:

- a universal CEP reduction;
- a point-target hit-rate multiplier;
- permission to multiply aircraft destroyed by 1.10;
- valid in poor visibility/night/strong evasive or badly formed attacks without a local reduction.

For small point targets or rapidly changing tactical targets, use 0-5% unless a dedicated sight/workflow audit supports more.

## 4. Dive bombing and aviation torpedo boundary

The older aviation-torpedo parent remains valid in principle:

- Type 91 aerial-torpedo benefit comes strongly from instrumented air-to-water envelope testing, entry stabilization, depth-settling and production QC;
- 1941-class torpedo attack may use a dedicated sight + mechanical lead calculator when separately adopted;
- later electrical/gyro input aids are FCS2/FCS3 and remain date/type gated;
- no automatic target tracking or automatic release is implied.

Dive bombing likewise benefits from sight calibration, dive-angle/airspeed/release tables and release-delay repeatability. It does not receive an automatic combat hit percentage. Pull-out geometry, pilot training, target maneuver and AA remain separate.

## 5. Reconnaissance / photogrammetry connection

Asai computation and optical metrology have a large indirect effect on **target information**, not just the weapon sight:

- camera/lens individual calibration;
- distortion correction;
- stereo photogrammetry and map registration;
- standardized time/altitude/heading/photo numbering;
- shorter photo-to-target-folder cycle.

This may improve bombing or artillery preparation by improving the input target position. Do not count that improvement again as a second generic bombsight bonus if the replay already credits better target folders / acted-on intelligence.

## 6. Ground direct fire — 37 mm / tank guns / artillery

For current 1939 ground weapons, same gun designation does not imply identical service firing quality.

FCS1 can improve:

- sight zero and bore-sight relation;
- sight mount alignment;
- recoil-return consistency and inspection;
- ammunition lot velocity/weight consistency;
- range-table preparation;
- crew zero confirmation and workshop re-zero after repair.

It does **not** improve armor penetration by itself. Penetration belongs to gun/ammunition/impact velocity/obliquity. The dense-core AP program is a separate ammunition card.

Specific current guards:

- infantry Type 94 37 mm rapid-fire gun and Type 94 37 mm tank gun use different complete rounds; their special AP qualification/issue is separate;
- Ha-Go tank-gun sight/QC improvement does not make the historical short-case tank round equal to the infantry AT gun round;
- Chi-Ha 57 mm sight/QC improvement does not change the low-velocity 57 mm into a modern high-velocity AT gun.

Field artillery gains from tables, survey/QC and fire-plan processing only when meteorology, observers, communications and ammunition supply support them. Do not grant a generic artillery accuracy scalar.

## 7. Navy ship fire control / AA

The older cross-domain ordering remains current:

1. medium-caliber AA has potentially large benefit from continuous tracking, angle transmission, follow-up, fuze setting and reduced reset delay;
2. bombing/torpedo calculation is also high-value;
3. torpedo fire-control benefits from target-motion and gyro-angle workflow;
4. capital-ship main battery has smaller relative gain because historical mechanical fire-control was already strong;
5. 25 mm-class AA cannot have its mount traverse/elevation/feed limitations erased by a better calculator.

For any ship:

`range/target observation -> director -> calculator -> angle transmission -> mount follow-up -> fuze/ammunition -> crew drill`

must be audited separately. Aircraft electronics progress does not auto-install a ship director/radar. Better computation does not automatically raise gun ROF, traverse speed or shell lethality.

## 8. 1939-06-27 Tamsag / Soviet-airfield attack retrospective closure

The previously closed sortie scale and aircraft-loss accounting remain unchanged. FIREOPTICS1 changes the **bombing-effect attribution**, not the attack size.

For the pre-reconnoitered daylight airfield-area attack:

- use **+5-8% effective target-area bomb concentration** versus a matched-history attack of identical aircraft/bombs/height;
- apply the benefit primarily to dispersal/maintenance/fuel/airfield repair burden and the probability of damaging exposed aircraft/equipment;
- do **not** add a proportional permanent-aircraft-destruction bonus;
- current Soviet permanent-loss center remains the already closed ~22-aircraft class unless later source/event reconstruction separates air-to-air and ground loss more rigorously;
- Japanese loss closure is unchanged by this card.

This prevents two opposite errors: treating the bombing workflow as completely historical despite Asai-era calibration/computation, or turning better calibration into implausible precision bombing.

## 9. Mandatory no-backflow / no-double-count rules

1. `same aircraft / same gun / same bomb = same historical hit rate` is forbidden when FCS state differs.
2. `better sight = fixed kill multiplier` is forbidden.
3. `better computation = future gyro/automatic sight fitted` is forbidden unless adoption is closed.
4. Historical anchors that already include a reflector/gyro/director state receive only residual integration/QC; do not add the full conversion again.
5. Better reconnaissance target folders and better bombsight workflow are separate stages; credit each only once.
6. Better ammunition QC reduces lot scatter/variance; it does not create penetration/explosive energy.
7. Crew training/doctrine is not automatically improved by hardware/QC; training changes need a chronological mechanism.
8. Combat claims remain claims. Better fire-control engineering does not convert overclaim into confirmed kills.

## 10. Precedence

- identity / same-name guard: `50/50A`;
- historical vehicle delta: `47/47A`;
- piston exhaust: `49/49A`;
- current fire-control application ledger: `51A`;
- current chronological combat result: `60-CURRENT-1939-COMBAT-REPLAY`.

This current V8 file outranks the archived v24 cross-domain fire/optics and aviation-control parent files on any conflicting current interpretation.


## NOMONHAN-A2 photo/deep-fire routing
Aerial-photo target acquisition, metadata/change detection and long-range artillery mission allocation are further closed in `53-AERIAL-PHOTO-RECON-DEEP-FIRE-INTEGRATION-CANON-V8.md`. FCS improvement does not add gun range or ammunition.
