# Branch B — Santo 1942-09 Naval Rebuild v003

status: WORKING RESET — prior D-1 night-action result voided pending re-adjudication
scope: 1942-09-21 through D-Day, with direct carryover to New Caledonia
precedence: current Branch MI named lineage + sourcebook 10/30/31/61 + event-local historical availability

## 0. Hard reset

The previously sketched D-1 result (Kongo medium damage / Quincy heavy damage / one U.S. DD sunk) is OPEN again.
Reason: it did not fully implement destroyer class mix, torpedo-reload cycles, staggered attack groups, launch-concealment/decoy maneuver, U.S. Mark 15 reliability, or uneven U.S. SG-radar distribution.

Current hard Branch MI corrections:
- IJN Yudachi sunk at modified MI.
- IJN Natsugumo sunk at modified MI.
- IJN Arashi moderate MI damage, repaired by July.
- IJN Hagikaze light MI damage, repaired by late June/early July.
- IJN Kongo light MI damage, repaired by early-mid July.
- IJN Hiei medium MI damage, repaired by late July.
- USN Benham, Balch, Hammann, Morris, Anderson, Phelps permanently lost at modified MI.
- USN Astoria, Pensacola, Northampton permanently lost at modified MI.
- Genuine Guadalcanal-only losses are not inherited unless recreated.

## 1. IJN destroyer technical state, Sep 1942

### 1.1 Asashio class
Branch sourcebook center:
- trial speed ~34.8 kt;
- 3x2 12.7cm guns;
- 2x4 61cm torpedo tubes + reloads;
- improved steering state from new-build rather than later correction;
- machinery/shafting and damage-control reliability improved, not armor magically increased.

Use: competent fleet destroyer, but torpedo reload/repeatability is below the newest Kagero/Yugumo standard unless individually modernized.

### 1.2 Kagero class
Branch sourcebook center:
- trial 35.4–35.7 kt, loaded practical max ~34.6–34.9 kt;
- range ~5,300 nm / 18 kt;
- 3x2 12.7cm guns;
- 2x4 61cm Type 93 tubes + eight reload torpedoes;
- initial machinery faults -15–25% vs historical class center;
- unscheduled yard days in first two years -10–20%;
- sister-ship speed/fuel variation ~30% narrower.

Torpedo cycle:
- early/mid Kagero, combat undamaged reload: 9–14 min;
- late/mature Kagero: 8–12 min;
- effective first-salvo-to-second-firing-solution cycle: ~13–25 min depending maturity and maneuver.

### 1.3 Yugumo class
Not a higher-speed super-destroyer. It is the mature standardized Kagero water-torpedo system.
- comparable basic speed/range/2x4 Type 93 battery;
- better production tolerances, tube alignment, electrical/communications repeatability, reload-system reliability.
- combat undamaged reload: 7–11 min center;
- first salvo -> second effective firing cycle: 12–20 min.

### 1.4 Type 93 fire control and hit model
Do not use a fixed universal hit percentage.
- 5–12 km: principal precision torpedo band.
- 12–16 km: useful if target course is stable and warning is low.
- >16 km: no longer normal individual precision fire.
- Branch technical improvement is mainly fewer wasted shots from tube/gyro/depth/lot residuals.
- 5–12 km, target unalerted: effective opportunity +5–12% relative vs historical equivalent.
- 12–16 km: +3–8% relative.
- target already maneuvering hard: improvement shrinks toward 0–5%.

### 1.5 Night optics / gunnery
- night binocular low-light identification range +5–12%; useful peripheral field +10–20%.
- normal surface-fire solution convergence ~5–10% faster in applicable conditions.
- normal gun hit probability only modestly higher; do not multiply destroyer gunnery into radar-equivalent performance.

### 1.6 Damage-control tradeoff
Branch DDs have better pump/firemain/steering reliability and are less likely to lose mission function from moderate non-critical damage.
But deck-mounted Type 93 reloads remain a severe hit/fire hazard. A destroyer carrying eight reloads into a gunfight can suffer catastrophic escalation if tube/reload areas are struck.

## 2. U.S. destroyer technical state, Sep 1942

### 2.1 Radar distribution is uneven
Do not model every U.S. destroyer as an SG-radar node.
- Washington is an exceptional SG/radar-gunnery node.
- Helena/selected newer ships can supply high-quality radar contact if assigned.
- many Sep 1942 DDs carry older/less-capable radar sets or air-search sets; CIC integration is immature.
- Fletcher-class lead ship is not available at Santo center: historical Noumea arrival was 5 Oct 1942.

Therefore U.S. formation advantage is:
- early contact at force level where Washington/Helena sees the enemy;
- not automatic real-time distributed precision control on every DD.

### 2.2 U.S. DD guns
5-inch/38 gives high rate of fire, good dual-purpose performance, and strong short/medium-range gun lethality.
In a close destroyer gunfight U.S. ships remain dangerous even without SG on every hull.

### 2.3 U.S. Mark 15 torpedo
Mark 15 still carries major 1942 reliability/exploder/depth problems.
USN DD torpedo attacks must therefore separate:
- correct launch solution;
- track/run;
- depth;
- exploder/function.
A tactical hit opportunity does not guarantee a detonation.

No at-sea reload equivalent to IJN Type 93 reload cycle: U.S. DD first torpedo battery is effectively a one-salvo battle resource.

## 3. Proposed IJN Santo naval OOB — named working center

This is an event OOB, not a claim that these were the historical Sep 24 formations.
The operation has had weeks of preparation and may reassign divisions.

### 3.1 Main carrier force
- Shokaku (damaged D-2 in current provisional air-battle line; result itself retained only until larger reset says otherwise)
- Zuikaku
- carrier heavy screen: Hiei, Kirishima, Tone, Chikuma
- DD screen center: Akizuki, Teruzuki + 4 Yugumo/Kagero-standard DDs
  - Yugumo
  - Makigumo
  - Kazagumo
  - Akigumo (Kagero-derived hull, treated by its actual technical class where needed)

Rationale: preserve high-AA/newer DDs around the carriers rather than spend every best torpedo hull in the night attack.

### 3.2 Bombardment / surface-cover group
Heavy ships:
- Kongo
- Haruna
- Atago
- Takao
- light-cruiser / destroyer command node: Jintsu candidate

#### Torpedo Group A — DesDiv 4 center
- Arashi
- Hagikaze
- Nowaki
- Maikaze

All four are Kagero-class; Branch MI damage to Arashi/Hagikaze is repaired by Sep.
Mission: first torpedo attack / forcing maneuver / withdrawal and reload.

#### Torpedo Group B — DesDiv 16 center
- Yukikaze
- Tokitsukaze
- Amatsukaze
- Hatsukaze

All four Kagero-class.
Mission: maintain optical contact while Group A reloads; attack the target's new course, or fire first if Group A's geometry is poor.

This 4+4 structure is deliberately selected to exploit sourcebook multiple-group time-stagger doctrine.

### 3.3 Transport direct cover
Center 5–6 DD, e.g. surviving Kagero/Shiratsuyu/older fleet DD mix.
Do NOT silently borrow Group A/B DDs into simultaneous transport CAP.
A possible center pool is Kuroshio, Oyashio, Hayashio plus three other available destroyers after exact theater-location audit.

### 3.4 IJN DD count
Center operation-wide unique DD concentration: ~18–20.
- 6 carrier screen
- 8 surface/torpedo attack
- 5–6 transport direct cover
This is below the very large historical late-Aug Solomons concentration and is physically plausible given no Guadalcanal destroyer-attrition chain, but it still consumes substantial fuel/maintenance capacity.

## 4. Proposed USN Santo naval OOB — named working center

### 4.1 Wasp / North Carolina retreat-cover group after D-2 carrier damage
Likely retained around damaged Wasp:
- North Carolina
- San Francisco
- Salt Lake City
- Juneau
- 5–6 DD from Wasp's historical Sep pool, selected among:
  - Aaron Ward
  - Farenholt
  - Buchanan
  - Lansdowne
  - Duncan
  - Lardner
  - Laffey

These cannot all simultaneously reinforce Washington while also escorting a damaged carrier.

### 4.2 Washington night-interception group — center
- Washington
- Atlanta
- Helena (preferred radar-support cruiser if event geometry permits)
- Quincy as additional heavy gun platform candidate
- DD van/screen center:
  - Walke
  - Preston
  - Gwin
  - O'Brien
  - plus 1–2 available DesRon-12 ships only if release from Wasp cover is physically timed

Important Branch collision:
- Benham cannot be used; it was sunk at modified MI.
- Fletcher cannot be used at Sep Santo center; historical South Pacific arrival is 5 Oct.

### 4.3 U.S. radar topology
Center:
- Washington = primary high-confidence surface picture / heavy-gun range source.
- Helena, if assigned = second strong radar source.
- Atlanta and most DDs = useful sensors/communications, but not treated as equivalent SG-CIC nodes.
Thus target information can be delayed or imperfectly propagated down the destroyer line.

## 5. Rebuilt Japanese night-torpedo doctrine for Santo

### 5.1 Do not fire and immediately perform an obvious fleet-wide 180-degree turn
An immediate synchronized reversal is detectable by radar and strongly suggests torpedo launch.
At 8–12 km Type 93 running time leaves the U.S. several minutes to alter future position.

### 5.2 Center attack cycle
1. Group A establishes 5–12 km or favorable 12–16 km solution.
2. Group A fires a controlled broad fan; it does NOT automatically dump all 32 torpedoes if friendly-danger sectors or poor target ID exist.
3. Non-firing ships / Group B maintain gunfire, illumination pressure or parallel course to obscure exact launch moment.
4. Group A makes delayed/split withdrawal into darkness/smoke, then stabilizes for reload.
5. U.S. reaction is observed:
   - no major turn -> Group B may hold fire and improve solution;
   - major turn -> Group B attacks the new course / exit lane;
   - battle line breaks -> surface mission may already be achieved even without hits.
6. Group A reloads in parallel, not sequentially.
7. At ~13–25 min depending ship/damage, surviving Group-A ships become 0/4/8-torpedo second-salvo candidates.
8. A second attack occurs only after re-contact, firing solution, safe sector and mission-value checks.

### 5.3 Deception / forcing maneuver
Torpedo fire can be used for more than direct hit probability.
A deliberately visible partial withdrawal can force Washington's line to turn away, disrupting radar/gun solutions and opening a bombardment-group escape lane.
But the Japanese should not automatically telegraph every first salvo; use mixed behavior by group.

## 6. Rebuilt U.S. response doctrine

Washington/Lee gets first warning more often, but the DD van is vulnerable if pushed forward.
Center response after detecting Japanese DD approach:
- heavy guns engage the largest reliable targets;
- DDs make smoke / screen / limited torpedo attack;
- do not assume U.S. torpedo reliability comparable to Type 93;
- once Japanese torpedo attack is suspected, begin high-amplitude course/speed changes;
- maintain evasive behavior longer than one Type-93 running interval if a second attack is considered possible.

Branch-specific learning caveat:
Santo occurs before historical Cape Esperance/Tassafaronga/Nov Guadalcanal lessons. The U.S. knows Japanese torpedoes are dangerous, but does not yet possess the full historical late-1942 practical appreciation of repeated Long-Lance attack cycles.

## 7. Re-adjudication state

Before resuming D-Day, re-run 24 Sep night in time slices:
- T0: first radar contact / optical contact
- T+0–5: U.S. first gunfire, Japanese dispersion/approach
- T+5–10: Torpedo Group A first salvo decision
- T+10–15: U.S. evasion, Group B solution
- T+15–25: Group-A reload / Group-B attack / gun damage
- T+25–40: possible Group-A second attack or disengagement

For every Japanese DD track separately:
- hull/damage state;
- first-salvo torpedoes fired (0–8);
- reload state (0/4/8);
- fire-control/communications state;
- ability to re-contact;
- deck-reload-fire hazard.

For every U.S. DD:
- radar type / information source;
- gun/torpedo availability;
- Mark 15 run/function outcome separately;
- damage / formation / communications state.

No previous D-1 surface-combat damage result survives this reset until this re-run is completed.
