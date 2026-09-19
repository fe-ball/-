# ASAI NAVAL AERIAL TORPEDO EFFECTIVENESS / EMPLOYMENT CLOSURE — 1941 YEAR-END — V1 TORPEDO41CLOSE1

**Status:** CURRENT V10 technical/doctrinal closure for planning and later replay.  
**Combat clock:** NOT ADVANCED. China remains 1939-12-31 24:00; this file defines a projected/technical 1941-year-end weapon-system state and does not pre-record 1940-41 combat outcomes.  
**Scope:** Type 91 Mod 1/Mod 2 aerial torpedo power, qualified release/run reliability, hit-realization model, target-class planning bands, B5N2/G3M2/G4As/G4M/B6N employment inheritance, and implications for future carrier-attack-aircraft composition.

## 0. Executive closure

By 1941 year-end the Imperial Navy possesses a **mature but not magical aerial-torpedo system**. The main advance is not a blanket hit-rate multiplier. It is a better-separated weapon chain:

1. aircraft/formation must obtain a valid terminal attack opportunity;
2. the torpedo must be released inside a qualified speed/height/attitude envelope and enter the water normally;
3. the torpedo must run on the commanded line;
4. target motion and evasive maneuver determine whether the run intersects the hull;
5. a valid hit then applies the Type 91 warhead damage ladder.

This semantic split is mandatory in later replay. Fighter interception, AA disruption, cloud, navigation and formation break-up reduce **valid releases**. They do not directly reduce the intrinsic post-release hit band of a torpedo already running correctly.

## 1. 1941 weapon state

### 1.1 Type 91 Mod 1 — retained service weapon

Historical/service anchor retained:
- total mass: **~784 kg**;
- length: **~5.275 m**;
- diameter: **45 cm**;
- warhead: **~150 kg Type 97 explosive**;
- water speed: **~41-43 kt**;
- nominal run: **~2,000 m**.

Worldline role at 1941 year-end:
- remains serviceable and numerous;
- useful for training, secondary targets and missions where the lighter weapon preserves aircraft fuel/range/deck margin;
- not discarded merely because Mod 2 exists.

### 1.2 Type 91 Mod 2 — principal premium 1941 combat weapon

Historical/service anchor retained:
- total mass: **~935 kg**;
- length: **~5.486 m**;
- warhead: **~205 kg Type 97 explosive**;
- water speed/range remain **~41-43 kt / ~2,000 m**;
- anti-roll stabilization is service-significant.

Worldline qualification inherited from NAVALJETTORP1:
- ordinary low/medium-speed aircraft may continue to release well below the weapon limit;
- **~400-430 km/h** becomes the normal qualified high-speed air-drop band for late-1941 frontline lots;
- **~450 km/h** remains selected/development growth, not a universal fleet release speed;
- no late-war 300/350-knot strengthened Type 91 state is back-ported into 1941.

### 1.3 Warhead energy interpretation

Type 97 explosive is treated as approximately TNT-equivalent for planning; do not apply a hidden large explosive-quality multiplier.

Mod 2 charge mass is **205/150 = 1.367×** Mod 1. Underwater structural damage is not linear with charge mass. Use:
- explosive-energy input: roughly **+37%**;
- characteristic blast/bubble length scale: only about **+11%** (cube-root scaling);
- practical result: materially greater flooding/local structural damage and a better chance of converting a marginal hit into a major casualty, but not a 37% automatic increase in sink probability.

## 2. Release/run reliability closure

These are **planning reliability bands after a technically correct release**, not per-sortie hit rates.

| weapon / release state | successful water entry + stable run | status |
|---|---:|---|
| late Mod 1, ordinary qualified release | **~95-98%** | mature service |
| Mod 2, ordinary B5N/G3M/G4M-speed release | **~96-99%** | mature late-1941 service |
| Mod 2, **400-430 km/h** high-speed qualified release | **~94-97%** | normal high-speed service band |
| Mod 2, selected **~450 km/h** release | **~90-94%** | development/selected unit; not fleet default |

A valid hull impact is assumed to detonate normally unless replay evidence creates a specific lot/fuze defect. Do **not** import the systemic dud/erratic-run behavior of other nations' early-war aerial torpedoes into Type 91 without evidence.

## 3. Why hit accuracy varies so much

Historical calibration anchors deliberately bracket very different target states:

- Pearl Harbor: about **40** Japanese aerial torpedoes were dropped at mostly anchored/restricted-maneuver targets and roughly **half** hit.
- Force Z: about **49** aerial torpedoes produced roughly **8 confirmed hits** on two maneuvering capital ships, or about **16%** overall.

The package therefore rejects one universal Japanese torpedo hit percentage.

### 3.1 Geometry sensitivity

At 42 kt, a Type 91 covers:
- 600 m in ~28 s;
- 800 m in ~37 s;
- 1,000 m in ~46 s;
- 1,200 m in ~56 s.

A 25-knot target moves about:
- ~357 m during a 600 m torpedo run;
- ~476 m during an 800 m run;
- ~595 m during a 1,000 m run.

For a pure broadside crossing solution, a 25-knot target against a 42-knot torpedo requires roughly a **36.5° lead angle**. Therefore gyro/heading setting, target-course estimation, aircraft alignment and release timing matter greatly even when the torpedo itself is perfectly reliable.

## 4. 1941 year-end post-release hit bands

Use these only **after counting valid, normally running torpedoes**. They are H->A planning bands for replay, not guaranteed historical outcomes.

| target / geometry | hit probability per valid running torpedo | interpretation |
|---|---:|---|
| anchored / maneuver severely constrained / surprise | **~45-60%** | Pearl-Harbor-class upper anchor; shallow-water special preparation remains local |
| maneuvering capital ship, coordinated multi-azimuth attack, no effective fighter disruption | **~16-24%** | Force-Z-class baseline with worldline QC/release consistency |
| maneuvering capital ship, alert, mostly single-axis approach | **~10-16%** | target can turn parallel / comb tracks more effectively |
| capital ship already slowed / steering degraded / boxed by crossing attacks | **~25-40%** | later waves exploit damaged geometry |
| maneuvering cruiser/carrier-size target | **~10-18%** | smaller beam, often good speed; carrier maneuver may be constrained by flight ops |
| destroyer / fast light combatant | **~5-12%** | high maneuverability makes aerial torpedo expenditure inefficient unless saturated |
| night / poor-visibility visual attack without strong illumination/contact aid | **~6-15%** vs capital target | training can make attack possible; identification/lead error dominate |

### Important guard

Effective fighter cover, heavy AA, cloud, poor contact reports and formation breakup mostly reduce the **number of valid releases**. Do not multiply these post-release bands again by an arbitrary AA penalty after a torpedo has already entered a normal run.

## 5. Release-distance doctrine bands

Exact unit doctrine remains event/local, but use three modeling bins:

| release bin | approximate water-run start distance | effect |
|---|---:|---|
| close | **~500-800 m** | highest geometric accuracy, highest aircraft exposure / least reaction time |
| normal | **~800-1,200 m** | standard compromise for maneuvering major warships |
| long | **~1,200-1,600 m** | safer aircraft separation but materially more target-motion/lead error |

Historical Force Z releases from roughly the high hundreds to ~1,500 m class validate this order of magnitude. Pearl Harbor's restricted targets allowed much closer solutions.

## 6. Platform employment diversity at 1941 year-end

### 6.1 B5N2 / Type 97 Carrier Attack Aircraft

**Core advantage:** the carrier moves the launch point.

Normal torpedo employment:
- piston airframe remains serial standard;
- practical terminal speed is below the Mod 2 high-speed limit, so the weapon no longer constrains ordinary attack speed;
- 9-aircraft and 18-aircraft carrier strike groupings remain natural planning units;
- carrier strike can combine torpedo axes with D3A dive-bomber/level-bomber/fighter pressure;
- two-axis/pincer attack is preferred when contact geometry and escort allow;
- Mod 2 is preferred for capital ships, but lighter Mod 1 can remain rational when carrier strike radius/deck margin is more valuable than the additional 55 kg warhead charge.

B5N2 remains a highly efficient **mobile torpedo delivery system**, not an obsolete slow weapon merely waiting for B6N.

### 6.2 G3M2 / Type 96 land attack

**Core advantage:** long land-based torpedo radius, ~650-800 km ordinary planning band.

Employment:
- long-range contact-to-attack cycle;
- 9-aircraft elements and multiple sequential waves;
- broad approach-axis choice if reconnaissance/contact quality is good;
- can attack from several bearings, but its lower speed means it must commit earlier and spends longer exposed in the terminal area;
- fatigue/navigation/weather costs are higher on the longest missions;
- Mod 1 remains useful when 151 kg of weapon-mass saving materially extends a marginal long-range mission; Mod 2 is preferred against capital targets when radius permits.

G3M's best use is **reach**, not trying to imitate G4As speed.

### 6.3 G4As1 / Type 0 land attack (E6 Twin JF branch)

**Core advantage:** high-speed positioning before and after the low-level torpedo run.

Employment:
- one Type 91 torpedo;
- ~300-400 km ordinary torpedo radius, favorable growth toward ~350-450 km after drag/load closure;
- sections can remain widely dispersed until comparatively late because high cruise/dash speed buys repositioning time;
- three- or four-aircraft elements can converge from three or four azimuths instead of carrying a large formation on one obvious run-in;
- final deceleration corridor is short; 1941 Mod 2 permits the terminal state to stabilize around **~400-430 km/h** rather than forcing very low attack speed;
- after release, shedding ~0.9 t and using JF low-speed thrust gives unusually rapid egress.

G4As therefore improves **attack-opportunity realization and multi-axis timing**, not the intrinsic hydrodynamic accuracy of a correctly running Type 91.

### 6.4 G4M1 conventional land attack

G4MAUDIT1 now closes the conventional long-range branch:
- one Type 91-class torpedo;
- applicable early-production EX2/QC aircraft **~433-436 km/h class at ~4.2 km**;
- ordinary torpedo radius **~900-1,150 km class**, with ~1,200-1,300 km favorable sensitivity only;
- conventional gasoline architecture remains because serial E6-S-T conversion would cut the reach that justifies the aircraft;
- same Mod 2 stabilization/QC/release-table school.

G4M is therefore the very-long-range conventional branch between mature G3M and short/medium-radius high-speed G4As. Combat attrition and actual 1941 inventory remain replay-local.

### 6.5 B6N design inheritance

B6N is not made operational by this closure. Its design requirement inherits:
- **400-430 km/h** Type 91 release interface from the beginning;
- weapon clearance, sight/release linkage and carrier handling designed around the high-speed standard;
- no requirement to decelerate to B5N-era torpedo fragility limits.

This lets future B6N design optimize the aircraft rather than redesign the torpedo after flight test.

## 7. Mixed attack forms available by 1941 year-end

The Navy can plausibly employ all of the following without inventing a new weapon family:

1. **single-axis mass attack** — simplest, least coordination burden, easiest for target to comb;
2. **two-axis pincer** — classic way to force a ship to expose beam to at least one torpedo track;
3. **sequential waves** — first wave forces turns/damage, second attacks a slower or geometrically constrained target;
4. **three/four-axis late fan-out** — especially suitable to G4As due high pre-terminal reposition speed;
5. **carrier mixed strike** — B5N torpedoes synchronized with D3A dive bombing / fighter strafing to divide AA attention and force maneuver;
6. **land-based mixed-speed attack** — G4As attacks can arrive as a fast geometry-setting wave while G3M/G4M approach from longer-radius axes;
7. **special shallow-water strike** — harbor-tail/stabilizer package; target/site specific, not fleet default;
8. **night/low-light attack** — technically possible with trained crews/contact/illumination but retains a large accuracy penalty and is not a default capital-ship hit-rate baseline.

## 8. Warhead damage ladder for later replay

Use damage-state language before sink probability.

### Mod 1 (~150 kg Type 97)
- destroyer / small transport: one hit commonly catastrophic; sinking or abandonment plausible;
- light cruiser: severe local flooding / propulsion loss possible; one hit often mission-significant;
- heavy cruiser / carrier: serious damage and mission kill possible, but sinking from one hit is not assumed;
- battleship / battlecruiser: major local flooding/shaft/steering casualty possible; one lucky hit can produce disproportionate mobility loss, but one-hit sinking is not a planning norm.

### Mod 2 (~205 kg Type 97)
Raise the damage state by roughly one **severity step in marginal cases**, not by a fixed sink multiplier:
- destroyer/light auxiliary: one hit is usually a catastrophic loss event;
- cruiser: one hit often mission-killing or severely speed-limiting; two hits create high abandonment/sinking risk;
- carrier/heavy cruiser: one hit has a strong mission-kill possibility depending machinery/aviation-fuel/shaft location; two or more are grave;
- modern capital ship: one hit can produce a severe mobility casualty if shaft/steering spaces are struck; **2-3 hits** usually mean major combat ineffectiveness; **~4+ substantial underwater hits** are a credible robust-sinking regime, but location/damage control remain decisive.

Force Z is the key warning against simple hit counting: Prince of Wales' first stern/shaft-area hit had damage far beyond an average hole, while both large ships ultimately required several torpedo hits to sink.

## 9. Formation-size implications for future carrier/land-attack composition

For a maneuvering capital target under the **16-24% valid-running-torpedo band**, expected hits are:

| valid torpedoes | expected hits |
|---:|---:|
| 9 | **~1.4-2.2** |
| 12 | **~1.9-2.9** |
| 18 | **~2.9-4.3** |
| 24 | **~3.8-5.8** |

These are not dispatch requirements. Opposition determines how many launched aircraft actually reach a valid release.

Force-composition implication:
- **9 valid releases** can damage or occasionally mission-kill a major ship but do not make sinking reliable;
- **12 valid releases** are a credible one-ship mission-kill package under favorable geometry;
- **18 valid releases** move into a robust 3-4-hit-class expectation and are a sensible fleet-carrier torpedo-capable strike block;
- **24+ valid releases** or multi-carrier/multi-wave attack materially increases the chance of producing several underwater hits even against maneuvering capital ships.

Therefore future carrier design should not maximize dedicated torpedo aircraft blindly. Dive bombers/fighters that suppress AA, force turns or damage steering **increase torpedo realization** and can be more valuable than replacing every non-torpedo aircraft with another torpedo carrier.

This favors a future attack-aircraft composition in which **roughly 18-24 aircraft per fleet-carrier strike group are torpedo-capable**, without requiring all of them to be torpedo-loaded on every sortie. A later unified B7A-like aircraft becomes especially attractive because weapon load can be chosen after target intelligence is known.

## 10. Type 91 allocation semantics at 1941 year-end

Do not treat Mod 2 as an automatic universal replacement of Mod 1.

Priority logic:
1. capital ship / carrier target within range -> **Mod 2 preferred**;
2. G4As high-speed attack -> **Mod 2 strongly preferred** because its stabilization/high-speed qualification is part of the aircraft concept;
3. B5N carrier strike -> Mod 2 preferred for high-value target, but Mod 1 remains rational when radius/deck weight is binding;
4. G3M very-long-range torpedo mission -> Mod 1 remains useful if 151 kg lighter weapon materially buys fuel/range; Mod 2 when target value outweighs radius loss;
5. training / secondary shipping -> older Mod 1 stock remains useful.

This preserves the **torpedo opportunity-cost problem** for future force planning rather than erasing it with an ahistorical instantaneous inventory conversion.

## 11. Replay guards

- No 1940-41 combat outcome is pre-recorded by this file.
- Historical Pearl Harbor / Force Z results are calibration anchors, not future worldline outcomes.
- Do not assign a universal Japanese torpedo hit percentage.
- Count valid releases first; apply run reliability and target-geometry bands second.
- Fighter/AA/weather effects normally reduce valid releases and aircraft survival, not the post-release geometric hit band.
- Do not equate Mod 2's +37% charge mass with +37% sink probability.
- Do not back-port later-war 300/350-knot Type 91 strengthening.
- G4M performance remains open until its dedicated wash.
- B6N/B7A are inheritance/design implications only unless later replay closes production/service.

## 12. Historical calibration anchors

External anchors used only to calibrate the H->A bands:
- U.S. Naval History and Heritage Command, Pearl Harbor appraisal: roughly 40 torpedo aircraft/torpedoes, about half finding their mark against anchored/restricted targets; release at very low altitude and short range.
- Force Z accounts: roughly 49 aerial torpedoes for about eight confirmed hits on maneuvering Prince of Wales and Repulse; multiple waves/azimuths, no timely fighter cover.
- Type 91 historical data: Mod 1 ~784 kg / 150 kg warhead; Mod 2 ~935 kg / 205 kg warhead, anti-roll stabilizers, 41-43 kt and ~2,000 m run.
- U.S. Navy ordnance assessments: Type 97 explosive is approximately TNT-equivalent for damage-energy planning.
