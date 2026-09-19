# GALVANIC negative-delta / no-change revalidation — 2026-08-29

status: AUTHORITATIVE_CLOSEOUT_AUDIT
scope: Every major current GALVANIC result that could otherwise survive by inertia.
rule: “UNCHANGED” is valid only if the final input has no causal path to the node, or the causal threshold is explicitly re-evaluated and does not cross.

## Classification key

- `RECALCULATED_SAME_ROUTE_QUANT_DELTA`: direct recomputation changes center/quantity but not route.
- `THRESHOLD_RECHECKED_NO_CROSS`: affected by the new input, but the qualitative state transition remains on the same side of the threshold.
- `DEPENDENCY_INDEPENDENT_RECONFIRMED`: the newly corrected factor cannot causally reach this node; its existing adjudication was re-opened only to confirm independence.
- `ALREADY_RERUN_CURRENT_BRANCH`: this node had already been causally rerun during the v028-v029 GALVANIC re-audit rather than inherited from old v001.

## Major-node audit

| Node | Final classification | Revalidation result |
|---|---|---|
| Nauru 11/23 suppression and two-peaked Japanese warning picture | DEPENDENCY_INDEPENDENT_RECONFIRMED + ALREADY_RERUN_CURRENT_BRANCH | Fighter microprofile cannot change whether Wasp/Princeton strike Nauru or the fact that Japan observes separate carrier groups. No route change. |
| 11/23 Japanese torpedo strike / Independence CVL-22 campaign-out | DEPENDENCY_INDEPENDENT_RECONFIRMED + ALREADY_RERUN_CURRENT_BRANCH | Strike is land-based and precedes the 11/26 carrier Kinsei allocation. One-torpedo centered hit remains. |
| Liscome Bay survival on 11/24 | DEPENDENCY_INDEPENDENT_RECONFIRMED + ALREADY_RERUN_CURRENT_BRANCH | Survival follows D-Day alert/screen geometry and the absence of the historical D+4 temporary-screen gap, not Kinsei performance. Old sinking remains blocked. |
| Tarawa tide window / measured-lane landing / final US capture | DEPENDENCY_INDEPENDENT_RECONFIRMED + ALREADY_RERUN_CURRENT_BRANCH | Tide date, ground force composition, logistics and fire-control dependencies are unchanged. Capture route remains; casualty/timing bands already use the current rerun. |
| Makin final capture 11/27 | DEPENDENCY_INDEPENDENT_RECONFIRMED | No carrier-fighter micro dependency reaches the ground-force ratio/support state enough to alter organized-resistance end date band. |
| Japanese 11/26 first-strike escort exchange | RECALCULATED_SAME_ROUTE_QUANT_DELTA | Re-profiled F6F-3/Kinsei/Zuisei simulation. Actual 13/48 Kinsei mix reduces Japanese escort-fighter loss about 7% (~1 aircraft in six-pass diagnostic) vs all-Zuisei and raises US fighter loss ~0.6. |
| Lexington CV-16 mission-kill | THRESHOLD_RECHECKED_NO_CROSS | The corrected fighter delta is too small to change the centered number of effective attack releases enough to erase the one-torpedo + 1-2 bomb hit state. Mission-kill remains centered. |
| Yorktown CV-10 temporary damage | THRESHOLD_RECHECKED_NO_CROSS | Small fighter-survival delta remains within attack-distribution noise; temporary deck damage remains centered. |
| Cowpens CVL-25 no major damage | THRESHOLD_RECHECKED_NO_CROSS | Extra effective release sensitivity is bounded to 0-2 aircraft; it does not make a Cowpens major hit the center. Upward branch remains possible but non-centered. |
| US counterstrike fighter escort vs Japanese CAP | RECALCULATED_SAME_ROUTE_QUANT_DELTA | Actual 7/52 Kinsei CAP mix saves <1 Japanese fighter in the mission-window diagnostic. |
| Soryu mission-kill | THRESHOLD_RECHECKED_NO_CROSS | <1-fighter CAP improvement does not remove sufficient US attack aircraft to cross the two-bomb mission-kill threshold. |
| Shokaku / Zuikaku / Hiryu remain operational | THRESHOLD_RECHECKED_NO_CROSS | Counterstrike release count changes negligibly. Major-damage branches remain stochastic tails, not centered states. |
| Both carrier forces disengage after one major exchange | THRESHOLD_RECHECKED_NO_CROSS | Japan still pays large experienced strike-cadre loss; US still has major deck damage and uncertainty over surviving Japanese carriers. No second all-out strike becomes positive-EV. |
| Secondary carriers remain rear-deck/regeneration pool rather than first-strike additions | DEPENDENCY_INDEPENDENT_RECONFIRMED | Kinsei performance does not create dated location/readiness to teleport Junyo/Hiyo/Ryujo/Zuiho into the 11/26 first strike. Their post-battle shock-absorber role remains. |
| 11/26-27 Hatsuzuki/Suzutsuki/Hamakaze/Fujinami stand-off raid / Franks loss / Fujinami damage | DEPENDENCY_INDEPENDENT_RECONFIRMED + ALREADY_RERUN_CURRENT_BRANCH | Surface-force arrival, air cueing and SG/Type-93 geometry are independent of the carrier-fighter micro correction. Named outcome remains. |
| 11/27 I-175 -> Pierce APA-50 | DEPENDENCY_INDEPENDENT_RECONFIRMED | Submarine patrol/screen geometry unaffected by Kinsei/F6F micro result. Named damage state remains. |
| 12/4 historical mass Kwajalein/Roi raid does not recur | THRESHOLD_RECHECKED_NO_CROSS | Surviving Shokaku/Zuikaku/Hiryu, US Lexington/Independence absence, Yorktown recovery, Japanese air dispersion and US meta-cognition still favor limited outer-Marshalls pressure/recon under strong cover. The ~few-aircraft micro delta is far below this decision threshold. |
| Independence repair clock | DEPENDENCY_INDEPENDENT_RECONFIRMED | Damage state occurred 11/23; no dependency on 11/26 fighter correction. |
| Lexington repair clock | THRESHOLD_RECHECKED_NO_CROSS | Hit state unchanged, therefore repair schedule unchanged. |
| Yorktown repair clock | THRESHOLD_RECHECKED_NO_CROSS | Hit state unchanged, therefore near-normal deck cycle ~11/29 remains. |
| Soryu repair clock | THRESHOLD_RECHECKED_NO_CROSS | Hit state unchanged, therefore Truk emergency repair -> home yard and late-Jan/early-Feb trial band remain. |
| 1944-01-01 carrier availability state | THRESHOLD_RECHECKED_NO_CROSS | Independence/Lexington/Soryu unavailable; Yorktown/Cowpens/Liscome Bay and Shokaku/Zuikaku/Hiryu operational remains the year-end state. |

## Accumulated quantitative changes

The new fighter re-profile does not reset the operation to an earlier narrative estimate. It is layered on top of all prior v028-v029 deltas: Nauru sortie expenditure, absence of historical Operation-RO depletion, tide-date change, US experience correction, Japanese crew survival, D4Y/B6N maturity, secondary-carrier reserve, land-based air, night attack, surface/submarine actions and repair debt.

The cumulative current macro aircraft-loss adjudication is:
- Japan 60-75 irrecoverable, working center ~67;
- United States 40-50, working center ~44.

These centers are intentionally not treated as exact Monte Carlo results. Their purpose is to ensure subsequent crew/airframe regeneration begins from a single consistent point.

## Final conclusion

No new qualitative branch is triggered by the corrected Kinsei-vs-F6F-3 simulation. This is a **real negative result produced by revalidation**, not an assumption of invariance. The GALVANIC route remains closed, while its quantitative fighter-loss center and Japanese fighter doctrine are refined.
