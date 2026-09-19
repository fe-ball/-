# Branch B — Aichi B7A Ryusei Full Reaudit
## Engine / Performance / Mission / Compute Effects
### As of 1944-04-25T24 v001

Status: **WORKING TECHNICAL CORRECTION / NEW AUDIT**
Clock advance: **NONE**

Supersedes the numerical portions of:
- `BRANCH_B_RYUSEI_B7A_RECOVERY_CORRECTION_1944-04-25_v001`

Important archive finding:
The detailed active naval-aircraft canon (`52_海軍航空機_艦攻・艦爆・陸攻・大艇.md`) currently stops at D4Y/B6N and does **not** contain a full B7A audit.
The only recovered pre-existing Branch invariant is:

> 流星：初期生産、2月戦闘0。大鳳が最初の全面運用母艦候補。

Therefore previous exact B7A April counts were more certain than the archive justified.
This file performs the missing audit.

---

# 1. Historical design anchor

B7A is not a later improvised bomber.

The Navy's 16-Shi requirement deliberately asks Aichi for a **unified carrier attack aircraft** intended to replace both:
- B6N torpedo-attack role;
- D4Y dive-bombing role.

Historical requirement/design characteristics:
- crew: 2;
- torpedo: one ~800-kg-class external aerial torpedo;
- bombing: internal bomb bay, historically two 250-kg-class bombs or lighter multiples;
- forward armament: two 20-mm cannon;
- rear flexible gun;
- folding wing;
- dive brakes;
- inverted-gull wing / short strong landing gear;
- high speed and long range;
- fighter-like maneuverability requirement.

This requirement remains valid in Branch.
No new doctrine is required to invent the dual-role concept.

---

# 2. Engine decision — HOMARE, not Ha-43

## Production/current B7A
**Nakajima Homare line is the Branch center.**

Historical:
- prototype B7A1: Homare 11 family;
- production B7A2: Homare 12;
- experimental later aircraft: Homare 23;
- proposed B7A3: Mitsubishi MK9 / Ha-43, not built.

## Branch 25-Apr decision
The operational/initial-production Ryusei remains:

**B7A2-class + improved Branch Homare 12-line engine**

Do NOT put Ha-43-powered Ryusei into April 1944 combat strength.

### Why not switch to Ha-43?
1. B7A airframe and engine installation were already designed around Homare.
2. Branch computation improves Homare's lot quality and integration enough to remove part of the historical incentive for an emergency engine change.
3. A Ha-43 change requires:
   - engine mount redesign;
   - cowling/cooling redesign;
   - propeller matching;
   - center-of-gravity work;
   - vibration survey;
   - flight/deck certification.
4. Ha-43 itself is only in 1944-H1 pilot-production maturity in current Branch.
5. Ha-43 is strategically allocated to the Reppu line and future high-power aircraft.
6. The immediate requirement is to put Ryusei into Taiho service, not restart development.

## Future branch
**B7A3 / Ha-43 remains a valid later development branch.**
Because Branch Ha-43 matures earlier than history, a B7A3 study/prototype could occur earlier than historical planning if engine supply allows.

But:
- no Apr-25 combat credit;
- no April production substitution.

---

# 3. Branch Homare input

Current Branch engine audit for 1944 H1:

- selected/test short-time maximum: ~2,000–2,050 hp class;
- standard good production engine: **1,900–2,000 hp class**;
- field median: **1,850–1,950 hp class**;
- useful 5–6 km output: **1,550–1,680 hp class**;
- relative maintenance burden versus Kinsei=1.00: **1.25–1.40**.

Therefore Branch Ryusei is not a 2,200-hp aircraft.

Its advantage over historical B7A2 is:
- fewer weak engines;
- better usable median power;
- lower rejection/exchange rate;
- better cooling/vibration matching;
- more predictable maintenance.

---

# 4. Compute effect — what actually changes

The computer does not invent Ryusei.
It attacks the exact problems created by combining torpedo, dive bombing and carrier landing in one heavy aircraft.

## A. Load-state matrix
Ryusei has radically different structural states:

1. clean / ferry;
2. internal dive-bomb load;
3. external 800-kg torpedo;
4. carrier landing after attack;
5. heavy launch state;
6. emergency asymmetric / damaged state.

Compute-assisted weight/CG tables make these conditions explicit instead of treating one "loaded weight" as the whole aircraft.

## B. Wing / gull-wing / landing gear
Calculations help compare:
- spar bending;
- gull-joint stress;
- landing-gear reaction;
- torpedo ground/propeller clearance;
- folding-wing load;
- carrier-impact loads.

Main benefit:
**fewer late structural surprises and more uniform production aircraft.**

Not:
a magically lighter wing.

## C. Dive bombing
Ryusei combines:
- large wing;
- bomb bay;
- dive brakes;
- high pull-out load;
- heavy carrier structure.

Computation helps:
- brake-area and left/right balance;
- wing/tail vibration;
- dive-speed limits;
- bomb-door/bomb separation trajectory;
- release altitude;
- pull-out height and G;
- fatigue inspection intervals.

This is one of the largest airframe-level benefits.

## D. Torpedo attack
Computation joins:
- aircraft speed/height;
- torpedo attitude at release;
- water-entry angle;
- gyro/depth settling;
- target lead;
- fuel/return state.

The gain is primarily a **wider reliable release envelope and fewer bad drops**, not a faster aircraft automatically giving a faster torpedo release.

## E. Homare / propeller integration
Branch test-data processing is especially useful for:
- torsional vibration;
- four-blade propeller resonance;
- cylinder-temperature distribution;
- oil pressure/bearing trends;
- supercharger / mixture / ignition;
- cowl/baffle airflow;
- engine-lot correlation.

Again:
the large gain is **production median and availability**, not headline hp.

---

# 5. Performance — 25-Apr working branch values

Historical B7A2 anchor:
- Homare 12 ~1,825 hp;
- max speed ~565–570 km/h class;
- maximum range ~3,000–3,300 km class;
- empty mass ~3.8 t;
- loaded/mission mass roughly 5.6 t and overload up to ~6.5 t.

Branch does not radically change the geometry.

## Weight
Working:
- empty: **3.75–3.90 t**
- standard bombing mission: **5.4–5.8 t**
- standard torpedo mission: **5.8–6.2 t**
- overload / maximum takeoff: **6.3–6.5 t class**

The compute benefit is mostly in structural confidence and tolerance control, not a 300-kg fantasy weight cut.

## Speed
Working 5–7 km altitude:

- selected/test-good: **575–582 km/h**
- production standard: **568–576 km/h**
- field median: **560–570 km/h**

This is consistent with improved Homare altitude output.
Do not credit 590–600 km/h in Apr 1944.

## Climb
Working:
- 6,000 m: **~9 min 40 sec – 10 min 20 sec**

Ryusei is fast for an attack aircraft but not a fighter-climb machine.

## Range
Payload strongly changes the answer.

Working:
- clean / ferry / maximum-range class: **3,100–3,400 km**
- practical dive-bomb strike radius: **~550–700 km**
- practical torpedo strike radius: **~500–650 km**
- upper good-condition torpedo radius can stretch farther, but reserve/recovery margin falls sharply.

Important:
B6N-Mamoru can remain preferable for some very-long-range torpedo missions.
Ryusei does not automatically obsolete B6N on radius alone.

---

# 6. Weapons and actual "multirole" meaning

## Torpedo role
Primary external weapon:
- one ~800-kg-class aerial torpedo.

Mission:
- low-level anti-ship torpedo attack.

## Dive-bomb role
Primary historical-style internal load:
- two ~250-kg-class bombs;
- lighter multiple bombs.

Branch should NOT assume an 800-kg bomb is a standard steep-dive load without a separate separation/structure certification.

A heavy external bomb may be usable for:
- level bombing;
- low-angle attack;
- special anti-ship/land missions;

but it is not automatically the normal full-dive weapon.

## Guns
Forward:
- 20-mm ×2 class.

Rear:
- flexible defensive gun, later 13-mm class.

The forward cannon give:
- strafing;
- self-defense;
- anti-small-ship / soft-target capability.

They do NOT make Ryusei a fighter.

---

# 7. Is it really a multirole bomber?

## YES — at the AIRFRAME / UNIT-LOGISTICS level
Ryusei is a genuine unified torpedo/dive-bomber.

A carrier can maintain:
- one airframe family;
- one engine family;
- one basic deck-handling family;
- one spares system;

then configure sorties for:
- dive bombing;
- torpedo attack.

This is a major organizational advantage.

## NO — at the CREW-SKILL level
Torpedo attack and steep dive bombing remain distinct skills.

Branch operating doctrine should use:
- common aircraft pool;
- crews with a **primary attack qualification**;
- secondary cross-qualification where training hours allow.

A pilot qualified to land Ryusei on Taiho is not automatically equally skilled at:
- torpedo attack;
- 55–65° dive bombing;
- night attack;
- long-range navigation.

The computer can standardize training tables.
It cannot erase practice hours.

---

# 8. Interaction with Branch "cell division"

Ryusei fits the Branch carrier-personnel system extremely well.

## Benefits

### A. fewer airframe families in a future attack group
Instead of separately maintaining:
- D4Y replacement pool;
- B6N replacement pool;

a future Taiho/Unryu cell can use a larger common Ryusei pool.

### B. reserve aircraft become more flexible
A spare Ryusei can replace:
- a lost dive-bomber airframe;
- or a lost torpedo-bomber airframe,

provided an appropriately qualified crew exists.

### C. two-person crew
Ryusei uses **2 crew**, versus B6N's 3.

This slightly reduces:
- carrier attack-aircrew headcount;
- third-seat radio/gunner demand.

But:
- navigation/radio/observer burden becomes concentrated in the second crewman;
- skilled two-man crew pairing remains a bottleneck.

### D. maintenance cell commonality
One Homare/Ryusei maintenance nucleus can support both attack missions.

This strengthens the new-carrier shadow-cell model.

---

# 9. Why D4Y and B6N still remain

Ryusei does NOT erase both predecessor families immediately.

## D4Y remains useful for
- high-speed reconnaissance;
- lighter deck footprint;
- existing trained units;
- older/secondary carrier use;
- missions where dive specialization matters.

## B6N remains useful for
- longer-range torpedo missions;
- existing large production/training pool;
- secondary carriers;
- units not yet converted to Ryusei;
- lower-risk continuity while Ryusei/Homare matures.

Thus April 1944 is a **three-type transition period**:
- D4Y;
- B6N;
- B7A.

Future new-carrier groups may become Ryusei-dominant faster than veteran groups.

---

# 10. Carrier compatibility

Ryusei is heavy.

The key states are not:
"6.5 t aircraft fits / does not fit."

A carrier handles several different weights:

1. elevator / hangar transfer:
   - no torpedo;
   - limited fuel;
   - under ~5 t where possible.

2. deck completion:
   - fuel;
   - torpedo/bombs;
   - final arming.

3. landing:
   - weapon expended;
   - much fuel consumed;
   - landing mass substantially below takeoff overload.

This is similar in principle to the current Branch B6N handling rule, but Ryusei is still more demanding.

## Apr-25 certification
**Taiho: full operational-candidate / first full-use carrier.**

Veteran four:
- trial/cross-deck familiarization plausible;
- full Ryusei combat-group certification remains OPEN pending arresting/recovery-fit trace.

Do not place a full B7A unit on Shokaku/Zuikaku/Hiryu/Soryu merely because the aircraft physically fits.

## Unryu / Amagi
They should incorporate Taiho's Ryusei handling data into work-up planning.
This is one reason Ryusei is strategically more important than its April aircraft count.

---

# 11. April-25 quantity — REOPENED and re-estimated conservatively

Pre-existing Branch invariant:
- initial production;
- no Feb combat;
- Taiho first full-operation candidate.

No recovered detailed production ledger yet fixes exact April quantity.

Therefore the previous:
- national 25–40;
- Taiho mission-ready 12–20

should NOT be treated as hard.

## Current conservative working range pending production-line audit

National B7A physical including production-standard aircraft:
**~20–32**

Serviceable / work-up usable:
**~15–24**

Taiho-associated physical/work-up:
**~12–20**

Taiho mission-ready:
**~8–14**

Additional prototype/test/training aircraft may exist outside this band depending whether prototypes are counted separately.

These numbers are **PROVISIONAL**.

---

# 12. Operational effect in the April five-carrier package

Because Ryusei numbers are still small:

- it does not replace the bulk D4Y/B6N force;
- it does not change the five-carrier 210–245 one-cycle total;
- it creates a **high-value Taiho sub-cell**.

Best use:
1. trained homogeneous Ryusei section/squadron;
2. selected high-value anti-ship target;
3. mission selected before launch as dive or torpedo;
4. avoid mixing every Ryusei crew into a different attack technique on the same day.

The initial operational benefit is:
**flexibility + speed + commonality + survivability of the future system**, not mass.

---

# 13. Hit-rate / compute-effect guard

Existing Branch generic technical effects remain applicable when the relevant crew is trained:

- moving-ship dive bombing: roughly **10–25% relative** hit-rate improvement versus historical-equivalent technical procedure;
- aerial torpedo attack: roughly **10–25% relative** improvement.

These are NOT:
- +10–25 percentage points;
- automatic Ryusei-specific bonuses;
- stackable with every other doctrine/QC improvement.

For Ryusei specifically, the compute system's special value is that **both mission envelopes can be certified on one airframe without one role corrupting the other**, while keeping release tables and structural limits consistent.

Actual combat result still depends on:
- CAP;
- AA;
- formation disruption;
- weather;
- crew experience;
- target maneuver;
- approach geometry.

---

# 14. Current decision

As of 25 Apr 1944 Branch B:

**Engine:** improved Homare-12 line.  
**Ha-43:** future B7A3 branch only, combat credit 0.  
**Role:** genuine unified carrier torpedo/dive attack aircraft.  
**Not:** fighter-bomber or universal replacement aircraft.  
**Performance:** historical B7A concept, modestly better median speed/climb/availability rather than fantasy horsepower.  
**Compute effect:** development convergence, structural/dive/torpedo envelope certification, engine-lot reliability and carrier handling.  
**First operational carrier:** Taiho.  
**April quantity:** small initial operational cell; exact production count reopened pending line audit.
