# D3A1 TYPE 99 CARRIER BOMBER — PISTON / TP / DIVE-BOMBING COMPARATIVE CLOSEOUT — 1939-1941 — V1 D3AAUDIT1

**Status:** CURRENT TECHNICAL CLOSEOUT / no combat-clock advance.  
**Purpose:** close the Type 99 carrier bomber as a baseline for later D4Y/B7A work, test whether an E5-S-T turboprop conversion has serial value, and provide a reusable 1941 dive-bombing realization model.

## 1. Historical airframe anchor

Use the late D3A1 Model 11 historical-like airframe as the basic physical anchor:

- crew: **2**;
- length: **~10.20 m**;
- span: **~14.37 m**;
- wing area: **~34.9 m2**;
- empty mass: **~2.40 t**;
- maximum takeoff mass: **~3.65 t**;
- engine: **Kinsei 44, ~1,070-1,075 hp class**;
- maximum speed: **~387 km/h at ~3 km** historical comparison anchor;
- 3 km climb: **~6.4-6.5 min**;
- range: **~1,470 km class** historical comparison anchor;
- standard anti-ship bomb: **250 kg Type 99 No.25 ordinary/SAP class** on fuselage trapeze;
- optional additional light bombs: **2 x ~60 kg class** underwing;
- fixed landing gear and dive brakes are retained.

The D3A is not treated as a bad aircraft merely because the undercarriage is fixed. Its airframe has low wing loading, excellent dive-control geometry and good carrier handling. The fixed gear is, however, a large parasite-drag floor that limits the return on later propulsion cleanup.

## 2. Current worldline piston D3A1

Current worldline differences remain evolutionary:

- early lots may retain historical-like EX0 collector exhaust;
- later/new-build lots progressively adopt **EX2** where lot/date supports it;
- EX0 -> EX2 gives a physical **~+4-6 km/h** clean maximum-speed increment;
- engine/propeller matching, cooling, vibration, production acceptance and serviceability are more repeatable;
- dive-brake vibration and directional-stability debugging close faster because instrumented flight testing is normal rather than exceptional;
- sight calibration, airspeed/altitude calibration, dive-angle tables and release-delay acceptance are FCS1/FCS2 beneficiaries.

Use **~391-393 km/h class at ~3 km** for a later EX2/QC D3A1 working maximum-speed band. Do not add a second generic exhaust or QC speed bonus on top of this.

Normal mission range remains approximately **~1,430-1,500 km class** depending bomb/fuel/deck condition. There is no free large range multiplier.

## 3. Dive-bombing operating envelope

### 3.1 Ordinary 1940-41 naval dive profile

For replay/planning, a trained D3A unit normally works inside:

- attack setup altitude: **~2.5-5.0 km**, weather/target/cover dependent;
- dive angle: **~45-60 degrees** ordinary service band;
- dive-brake controlled speed: **~400-440 km/h class**;
- ordinary ship-target release altitude: **~450-650 m**;
- lower release is possible but pays sharply in pull-out margin and AA exposure;
- higher release is possible when smoke, maneuver or flak prevents a clean late aim, with corresponding accuracy loss.

This is not an automatic-release system. Pilot training, target motion, wind, smoke, AA, dive alignment and pull-out geometry remain decisive.

### 3.2 Why Asai/FCS work matters

The worldline gain is primarily reduced systematic error and scatter:

- bomb-sight boresight repeatability;
- calibrated airspeed and altitude;
- measured release delay;
- dive-angle/airspeed/release tables;
- bomb-lot / suspension / trapeze acceptance;
- post-exercise analysis of consistent miss direction;
- better target folders where photo reconnaissance exists.

Do **not** apply a universal hit-rate multiplier. Instead, a well-calibrated worldline unit may use the upper half of the appropriate planning band when training, visibility and attack geometry justify it.

## 4. 1941 direct-hit realization model

The D3A bombing model is deliberately layered:

`attack aircraft reaches dive setup -> usable dive established -> valid release -> bomb functions -> geometry produces direct hit / near miss`

CAP and heavy AA mainly reduce the number of aircraft reaching a stable release. Do not also multiply the post-release hit probability by the same disruption penalty unless the attack geometry itself is degraded.

### 4.1 Valid-release completion after reaching the attack area

| condition | valid-release completion |
|---|---:|
| trained unit, moderate fighter/AA pressure | **~0.78-0.90** |
| favorable surprise / weak defense | **~0.90-0.96** |
| heavy fighter interception / dense AA / smoke | **~0.55-0.75** |
| badly broken formation / poor visibility | **~0.40-0.65** |

### 4.2 Direct-hit probability per valid 250 kg release

| target/geometry | direct-hit planning band |
|---|---:|
| anchored/restricted large ship, clearly visible | **~30-45%** |
| maneuvering carrier / battleship / large cruiser, ordinary coordinated attack | **~18-28%** |
| elite/favorable long-axis or momentarily constrained target | **~25-35%** |
| alert evasive ship under smoke / heavy disturbance | **~8-15%** |
| destroyer / small fast ship | **~6-12%** |

These are planning bands, not guaranteed combat percentages. They are calibrated to the broad historical fact that prewar moving-target dive-bombing exercises clustered around ~20%, Midway produced an exceptional ~27.5% U.S. carrier-dive-bomber result, while real Japanese attacks could range from poor results under smoke/AA to very high local success by elite sections.

### 4.3 Whole-sortie direct-hit implication

For a trained D3A force that actually reaches the target area, the ordinary moving-capital-ship band is therefore roughly:

**0.78-0.90 valid release x 0.18-0.28 hit/release = ~14-25% direct hits per attacking aircraft**

before aircraft lost or turned back prior to target-area arrival are counted.

Under severe disruption, ~5-12% per attacking aircraft is entirely plausible. Under favorable surprise and elite geometry, ~23-34% is plausible.

This decomposition is the required future replay method.

## 5. Bomb effect

### 5.1 Type 99 No.25 ordinary / SAP class

Use approximately:

- bomb mass: **~250 kg**;
- explosive charge: **~60-62 kg class**;
- delayed-impact SAP role against ships.

Operational effect:

- destroyer / light ship: one direct hit can be catastrophic or mission-killing;
- cruiser: serious local damage/fire is common, one hit is not an automatic loss;
- carrier: one hit can cause flight-deck/hangar/fire damage and can mission-kill if it intersects fueled/armed aircraft, fuel lines, magazines or elevators; secondary fires often matter more than nominal explosive mass;
- battleship: normally topside/light-deck damage rather than guaranteed vital penetration; do not treat 250 kg SAP as an 800 kg armor-piercing substitute.

### 5.2 60 kg class wing bombs

The two light wing bombs are useful against:

- airfields;
- AA positions;
- soft deck targets;
- vehicles / exposed installations;
- shore targets.

Do not count them as equivalent additional capital-ship killing power to the central 250 kg SAP bomb.

## 6. E5-S-T turboprop D3A conversion study

### 6.1 Why it is physically credible

Current E5-S-T is a mature ~1,000 hp shaft/turboprop package:

- quantity/continuous ~952 hp;
- normal ~1,000 hp;
- selected ~1,050-1,060 hp;
- complete installed powerplant center ~575 kg;
- a ~3.2-3.3 m three-blade constant-speed propeller is adequate.

Kinsei 44 dry-engine mass is in the same broad half-tonne class, so this is not a huge weight-saving conversion. The gain is a narrower nose, lower vibration and kerosene commonality, not a fantasy removal of hundreds of kilograms.

### 6.2 Working conversion mass / drag

Use:

- empty weight: **~2.33-2.39 t, center ~2.36 t**;
- maximum takeoff: **~3.55-3.65 t** depending fuel/bomb/test gear;
- parasite-drag reduction: only **~2-4%, center ~3%**.

The smaller turbine nose cannot erase fixed-undercarriage drag, dive-brake installations and the existing carrier-airframe drag floor.

### 6.3 Speed

Because the E5-S-T altitude-power map remains bracketed, do not assume 1,000 hp at 3-4 km.

Working TP-D3A speed band:

| altitude | E5-S-T D3A working band |
|---:|---:|
| sea level | **~355-362 km/h** |
| 1 km | **~355-365 km/h** |
| 3 km | **~350-378 km/h; center ~365** |

The later EX2/QC piston D3A1 remains faster at the altitude setting the normal headline speed.

### 6.4 Range

Use E5-S-T part-load fuel-economy guards already established by B5NAUDIT1. Lower vibration and kerosene density do not cancel the cruise-SFC penalty.

Working TP mission range:

**~1,000-1,180 km class**, depending bomb/fuel condition.

Thus serial TP conversion trades away a major carrier-strike advantage without producing a useful speed jump.

### 6.5 Dive bombing

The TP conversion gives:

- lower engine/airframe vibration;
- smaller nose cross-section / somewhat improved forward view;
- turbine-at-sea experience;
- dive-specific turbine governor/reducer/prop data.

But during the controlled dive, dive brakes and airframe geometry determine speed. Engine type does not turn D3A into a more accurate dive bomber by itself. A TP D3A still uses the same 250 kg trapeze, same wing, same fixed gear and the same pilot-dependent dive geometry.

### 6.6 Procurement decision

**Do not serially re-engine D3A1 with E5-S-T.**

Allow **2 aircraft**, with a third only if useful for simultaneous carrier/dive instrumentation work, as a 1940 technical program for:

- carrier kerosene handling;
- dive-brake / prop-governor interaction;
- low-vibration sight and camera measurement;
- bomb-trapeze/store-separation measurement;
- salt/FOD/reducer/accessory experience;
- inheritance into later carrier TP proposals.

No frontline TP-D3A squadron is created.

## 7. Replacement tempo implication

The worldline advantage is stronger in **replacement readiness** than in D3A re-engineering.

D3A development benefits already paid for:

- faster closure of dive-brake vibration;
- better flight instrumentation;
- production/QC discipline;
- standardized dive/release test methods;
- mature high-speed store separation work from D3A plus E5/E6 torpedo/bomb programs.

Meanwhile current engine canon gives domestic DB601/Atsuta a plausible **~2-4 month schedule improvement** plus materially better 1940 pilot-lot / 1941 production health than history.

Therefore the future D4Y audit should test a **~3-6 month earlier effective replacement opportunity** than historical planning, not because D3A becomes bad sooner but because the successor can become trustworthy sooner. These months are a screening opportunity and are **not automatically additive** or a closed D4Y service date.

If D4Y passes structural/dive/carrier/engine gates, D3A new-production taper can rationally begin during **1941 H2** rather than waiting for a late emergency change in 1942. Until D4Y is audited, D3A1 remains the serial carrier-dive-bomber baseline.

## 8. Design consequence for later carrier air groups

D3A1 establishes four durable lessons:

1. **~20% class moving-ship direct-hit performance is already realistic for trained dive bombing**, so a successor must improve survival, payload, radius and sortie generation rather than merely claim accuracy.
2. 250 kg SAP can mission-kill a carrier through secondary effects but does not provide guaranteed capital-ship destruction; heavier/internal bomb carriage has real value.
3. Fixed gear makes propulsion cleanup increasingly low-return; the next generation should buy retractable gear and cleaner weapon carriage before paying for exotic propulsion.
4. Future B7A-like unification is attractive only if it preserves dive geometry while also inheriting high-speed torpedo handling.

## 9. Guards

This closeout does **not**:

- advance combat beyond 1939-12-31;
- inject 1941 combat results into replay;
- claim every D3A sortie hits at a fixed percentage;
- create a serial TP D3A;
- automatically move D4Y service into 1941 without its own audit;
- give 250 kg bombs battleship-killing power independent of hit location;
- double-count EX2, FCS or QC gains already present in current ledgers.
