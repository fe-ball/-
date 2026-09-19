# GALVANIC fighter microcombat re-audit — 1943-11

status: AUTHORITATIVE_DIAGNOSTIC_INPUT
purpose: Rebuild the Kinsei Zero / late-Zuisei Zero / F6F-3 comparison with the current HARD performance clocks before closing GALVANIC negative-delta revalidation.

## 1. What was wrong with the inherited microcombat result

The retained WIP microcombat engine and profiles were real, but the saved headline comparison was against F6F-5 (WEP), not the 1943-11 F6F-3. More importantly, the old Kinsei profile climbed to 6,000 m in roughly 6.1 minutes, faster than the current audited early-unit GALVANIC center. The old result therefore remains useful as provenance only.

This re-audit keeps the legacy v04 interaction kernel for relative diagnostics but replaces the performance clocks with current event values:
- late Zuisei Zero: peak about 564 km/h, 6,000 m about 7:25;
- early-unit Kinsei Zero: peak about 590 km/h, 6,000 m about 6:45;
- F6F-3: peak about 605 km/h near 7,100 m, 20,000 ft climb center about 7:00.

## 2. Equal-geometry result

At equal altitude / equal initial speed the F6F-3 remains favored at 3, 5 and 7 km. Kinsei narrows the gap substantially but does not erase it.

At 5 km, co-altitude/equal-speed pairwise diagnostic:
- late Zuisei: JP kill 0.0187, US kill 0.0645, first-shot JP/US 0.369/0.617;
- Kinsei: JP kill 0.0248, US kill 0.0434, first-shot JP/US 0.435/0.552.

The high-altitude penalty remains strong: at 7 km, co-altitude F6F-3 advantage expands again.

## 3. Geometry dominates aircraft substitution

At 5 km, if Japan begins 1,000 m below the F6F, Kinsei remains clearly disadvantaged. At the same altitude it substantially narrows the gap. If Japan begins 1,000 m above, Kinsei reverses the local pairwise kill odds; late Zuisei improves but does not fully reverse them.

Therefore the primary lesson is not “Kinsei beats Hellcat.” It is: **Kinsei converts a favorable warning/height state into combat value much better than late Zuisei, but US radar/CIC/fighter direction can still deny that state.**

The GALVANIC US-CIC external geometry prior is 55% F6F +1,000 m, 35% co-altitude, 10% Japan +1,000 m. Under that prior, weighted 5-km pairwise values remain F6F-favored:
- late Zuisei JP/US kill 0.0183/0.0680;
- Kinsei JP/US kill 0.0251/0.0499.

## 4. Group and mission-window effect

A pure all-Kinsei counterfactual materially improves Japanese fighter exchange. That counterfactual is not available in November 1943.

For the actual first strike, 13 Kinsei + 35 late Zuisei escorts against 60 F6F CAP in the longer six-pass diagnostic gives:
- all-Zuisei counterfactual: Japanese fighter loss mean 14.85, US 4.24;
- actual mix: Japanese 13.74, US 4.81;
- all-Kinsei counterfactual: Japanese 11.16, US 6.02.

Thus the actual 13/48 Kinsei mix saves about 1.1 Japanese fighters in this window and costs the US about 0.6 additional fighters relative to the erroneous all-Zuisei assumption. This is real but not battle-transforming.

For Japanese defensive CAP against the US counterstrike, 7 Kinsei + 45 late Zuisei saves about 0.7 fighter in the same diagnostic. This is far too small to erase the centered Soryu mission-kill.

## 5. Crew experience

The Branch Japanese carrier force has a higher experienced leader density than historical late 1943 because the historical Guadalcanal/Solomons attrition chain did not occur. The US force has strong standardized training and raid experience but not a prior equal-carrier fleet battle in this Branch.

The model applies only a small experience sensitivity, not an ace multiplier. Its effect is much smaller than CIC/altitude geometry. This prevents “veteran crew” from becoming an unbounded hit-rate bonus.

## 6. GALVANIC reinjection

The new microcombat result changes the **center** slightly, not the route:
- Japanese irrecoverable aircraft remains 60-75; working center about 67;
- US remains 40-50; working center about 44;
- first-strike Kinsei effect is fighter-loss reduction on the order of one aircraft plus modest extra CAP pressure;
- any improvement in attack-aircraft weapon-release survival is bounded to roughly 0-2 aircraft relative to the all-Zuisei assumption and is not directly claimed by the fighter kernel;
- Lexington mission-kill remains centered; Yorktown temporary damage remains centered; Cowpens major damage remains outside the center;
- Soryu mission-kill remains centered; Shokaku/Zuikaku/Hiryu remain centered operational.

The broad v029 aircraft-loss bands already contained this corrected center. The prior qualitative wording overstated the magnitude of the 20-aircraft Kinsei component and is superseded by this report.

## 7. Operational lesson

Kinsei should be prioritized where F6F contact is likely and where warning can create a height/closure advantage. Late Zuisei remains superior for longer escort radius, lower landing speed, mature deck routines and small-deck operations. Full conversion is neither available nor desirable at this date.

The highest-payoff improvement revealed by the simulation is not another 10-20 km/h of airframe speed. It is **warning, vectoring, section leadership and preserving initial energy state**.

Reproducible files are retained under `98_TOOLS/GALVANIC_AIR_MICRO_v001/`.
