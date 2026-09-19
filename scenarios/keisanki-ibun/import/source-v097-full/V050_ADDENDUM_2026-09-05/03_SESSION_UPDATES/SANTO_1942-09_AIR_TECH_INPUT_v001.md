# Branch B — Santo 1942-09 Air Technology Input v001

status: WORKING_INPUT_FROM_CANONICAL_AIR_MASTERS
clock_advance: false
operation_window: 1942-09-21 -- 1942-10 (revised Santo branch)

## Authority / precedence

Use current aviation master `50_航空機研究_陸海軍総合正本.md` first; use `52_海軍航空機_艦攻・艦爆・陸攻・大艇.md`, `53_海軍戦闘機・空冷発動機・噴進航空.md`, `31_魚雷・水雷戦...md` as canonical detail references. The old authoritative `SANTO_1942-08_TECH_STACK_REAUDIT_v001.md` remains authoritative for the technology stack but not for its old dates/outcome, which are reopened by the Madagascar delay.

## Japanese types actually applicable in late Sep 1942

### Fighter
- Main type: Zusei-21-series Zero; 1942 quantitative frontline main type.
- Working performance from master: roughly 545–552 km/h max for the Zusei-21 stage; production-median/reliability benefit matters more than peak speed.
- Do **not** universal-backport the later 52-equivalent 560–568 km/h / 1943 protection package to Sep 1942.
- Late-1942 refinements (high-speed handling, radio, exhaust/cowling/structural work) may exist in transition/selected lots, not as fleetwide finished 1943 standard.

### Carrier torpedo bomber
- Main type: late B5N with Zusei 15, not B6N.
- Working performance: 391–397 km/h max, torpedo mission radius 500–620 km.
- Partial fire/protection package: fuel shutoff, firewall, extinguisher, piping separation/local fire protection, small rear armor; not full self-sealing protection.
- B6N: trial / pre-initial-unit stage; not counted as Santo main-force torpedo bomber.

### Carrier dive bomber
- Main type: D3A 1941-late standard, 394–400 km/h max.
- Standardized dive envelope and release/structure repeatability reduce bad dives, release accidents and aircraft-to-aircraft variance.
- D4Y bomber is **not** a mass frontline type at Santo.

### Carrier reconnaissance
- Limited D4Y reconnaissance aircraft are valid from 1942H1.
- Working performance: 557–567 km/h unit median, reconnaissance endurance/range 2,200–2,450 km class.
- Use as scarce fast search/recontact asset; do not convert into mass dive-bomber strength.

### Land attack aircraft
- G4M late-1941 standard: 444–451 km/h max, unit median 437–446 km/h; torpedo practical radius 900–1,100 km.
- Partial protection/segmentation reduces immediate fire/mission loss from light single hits, but repeated .50-cal / 20mm hits in wing fuel remain dangerous.
- Lunga–Santo is ~1,030 km one-way: G4M strike is feasible near the edge of practical torpedo radius, but route/loiter/fuel margins are tight.

### Flying boats
- H8K1 combat-usable from early 1942; working max 440–446 km/h, patrol radius 1,800–2,200 km.
- H6K5 remains useful but slower/more vulnerable.
- Forward H8K/H6K detachments are primarily search, contact, weather, rescue and relay assets; do not use H8K as routine low-altitude torpedo attack against defended fleets.

## Japanese technical combat modifiers (same-opportunity relative modifiers)

These are relative changes, never percentage-point bonuses and never substitutes for geometry, CAP interception, target maneuver or crew quality.

- fighter fixed gun vs fighter: +10% to +25% relative hit probability.
- fixed gun vs bomber / ground target: +20% to +40% relative.
- level bombing vs point target: +15% to +35% relative.
- level bombing vs area target: +5% to +20% relative.
- dive bombing vs fixed target: +15% to +30% relative.
- dive bombing vs moving ship: +10% to +25% relative.
- aerial torpedo attack: +10% to +25% relative under same tactical conditions.

Aerial torpedo improvement comes from reduced technical dispersion, better drop/entry envelope, lot control and normal-run probability; torpedo nominal speed/warhead is not magically increased.

## Readiness / navigation / search

- Navigation/reporting: standardized time/position/wind/fuel/contact reporting; less information leakage.
- Search doctrine: broad search -> suspicious-contact revisit -> fast confirmation -> tracking/recontact is increasingly mature through 1942 and reinforced by Operation C/MO/MI lessons.
- Production median/reliability: benefit appears in ready rate, abort rate, accident loss, handling repeatability and maintenance burden, not just top speed.
- Opening-master anchors: navigation/mission abort leakage down roughly 15–30%, non-combat loss 15–25% in the early-war comparison. Do **not** multiply these mechanically on every Sep-1942 sortie; use them as sortie-generation/mission-completion inputs.

## Personnel / organization in late Sep 1942

- MI after-action policy expands training throughput without yet shortening first-line carrier qualification.
- Shokaku/Zuikaku frontline groups receive a concentrated veteran-survivor nucleus.
- Medium/light carriers are new/old mixed and should not receive the same quality scalar as frontline fleet carriers.
- 1942H2 air-ground separation is at the major-base trial stage: a flying unit plus direct maintenance detachment can be ferried/rebased between Rabaul and Lunga, but this is not instant movement and requires pre-positioned fuel, munitions, base maintenance and weather support.

## Lunga–Santo escort correction

Great-circle distance is ~1,030 km / 556 nm one-way.

- This is inside/near G4M practical strike radius but above the master's normal/safe Zero combat/escort radius.
- A Zero escort can still be attempted using maximum-range/drop-tank practice, as historically Rabaul–Guadalcanal-class extreme missions demonstrated, but it has very little loiter/fighting margin and high sensitivity to detours, weather, combat and damaged-aircraft recovery.
- Therefore use Lunga as a **limited timed reinforcement / coordinated strike source**, not an all-day fighter umbrella over Santo.
- Working operational rule: at most one major long-range escorted Lunga strike window in a day under favorable conditions; frequent multi-wave escort is not the center line.

## U.S. side — no technology discount

The old Santo tech settlement explicitly preserves historical 1942 U.S. F4F, PBY/B-17, warning/radar and Wasp fleet operation. Extend that rule to SBD/TBF in the revised Sep battle.

- F4F: historical armor/self-sealing, heavy .50-cal armament, radio/team tactics; Branch Japanese improvements do not discount it.
- SBD-3: historical ruggedness, armor/self-sealing and very effective steep dive attack; remains the principal U.S. anti-ship strike aircraft.
- TBF-1: available, but the 1942 Mk 13 torpedo remains historically unreliable. Do not give U.S. aerial torpedo attacks Japanese Type-91 reliability.
- PBY: strong search asset but vulnerable when intercepted.
- B-17: useful for tracking, disruption and fixed/area targets; high-altitude attacks on maneuvering ships retain low absolute hit probability.

## Consequence for revised Santo D-3 onward

1. Japanese search quality is materially stronger than historical single-pass practice because H8K/H6K + scarce D4Y recon + E13A/floatplanes + multi-layer recontact can be combined.
2. Japanese carrier strike hit probability is modestly but materially higher once a valid attack geometry is achieved.
3. The largest Japanese advantage is not a universal hit-rate multiplier: it is fewer aborts, better recontact, more repeatable weapon release, and preservation of first-line crew quality.
4. Lunga contributes timed G4M/Zero pressure, but cannot maintain continuous CAP over Santo.
5. U.S. SBD/F4F quality and Wasp radar/air warning remain fully historical; U.S. Mk 13 aerial torpedo weakness remains.
