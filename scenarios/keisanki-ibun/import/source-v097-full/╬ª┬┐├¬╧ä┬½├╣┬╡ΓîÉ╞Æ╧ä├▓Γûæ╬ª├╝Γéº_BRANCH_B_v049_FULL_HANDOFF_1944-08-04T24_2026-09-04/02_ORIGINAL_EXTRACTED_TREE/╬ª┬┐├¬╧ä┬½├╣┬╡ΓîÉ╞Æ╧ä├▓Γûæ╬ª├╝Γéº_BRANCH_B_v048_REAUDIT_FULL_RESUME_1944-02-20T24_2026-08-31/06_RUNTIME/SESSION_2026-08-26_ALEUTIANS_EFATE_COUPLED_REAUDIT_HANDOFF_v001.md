# 2026-08-26 session handoff — 1943春 Aleutians / Efate coupled re-audit

Status: **CURRENT REAUDIT HANDOFF / CLOCK REOPENED / DOWNSTREAM RESULTS PROVISIONAL**

This file records the deliberate rollback made after the 1943 spring South Pacific / Efate audit noticed that the Aleutians had not been integrated into the same force-allocation clock. The correct continuation is **not** to force the previously simulated May Efate operation forward. Re-audit the North Pacific first, then rebuild the May South Pacific OOB from the resulting allocations.

## 1. Restart boundary

Restart at approximately **1943-03-26T00:00**, immediately before the Battle of the Komandorski Islands / the critical Attu resupply decision.

Required sequence:

1. Komandorski Islands battle re-audit.
2. Determine what Japanese convoy / fast-transport supply actually reaches Attu afterward.
3. Determine what the United States can infer about that resupply and the true Attu garrison/logistics state.
4. Re-evaluate US Attu/Kiska invasion timing, target choice, force allocation, and willingness to divert ships while Efate is becoming a dangerous exposed forward base.
5. Re-evaluate Japanese strategic warning of an Aleutians landing and the resulting rescue / reinforcement / abandonment policy.
6. Fix Attu campaign outcome and Kiska policy.
7. Only then rebuild the May 1943 Efate air/naval OOB and decide whether/when the Japanese limited neutralization strike occurs.
8. Only after the North/South Pacific allocation is closed should the post-Efate Indian Ocean option be reopened.

## 2. Why the rollback is mandatory

The prior Efate discussion implicitly treated several ships and support assets as if the Aleutians were not simultaneously consuming them. That is unsafe.

At the same time, the correction is **not** "Aleutians consume X ships, therefore Efate loses X ships" by default. This branch has qualitatively different Japanese navigation, propulsion reliability, ship survival, transport hull availability, and transport design. A limited northern supply effort may therefore be materially cheaper and more weather-capable than its historical analogue.

The core question is a coupled information-and-logistics problem:

- US: Efate is growing under immediate Japanese pressure from Santo and New Caledonia. Does Washington/Nimitz still commit a northern amphibious operation, and with which categories of ships?
- Japan: Efate is an obvious emerging threat, but US activity around Adak/Amchitka makes an Aleutians move increasingly plausible. How much northern insurance is required before the Navy can exploit the southern offensive window?
- Neither side knows the other's exact allocation. Strategic warning may exist without precise target/date/OOB knowledge.

## 3. Branch-specific capability changes that must be applied in the Aleutians

### 3.1 Japanese navigation / weather / propulsion

Do not model the branch improvement as a cosmetic +speed percentage only. In the Aleutians, the important outputs are event probabilities:

- probability a convoy maintains planned speed in cold rough weather;
- probability ships reach rendezvous on time in fog;
- probability an engine casualty forces mission abort;
- probability a fast transport reaches/clears the unloading area inside one weather window;
- probability a force keeps cohesion when visibility and dead-reckoning error are poor;
- probability a damaged ship can still withdraw without becoming a second rescue problem.

The existing naval machinery/navigation/operational-reliability ledgers must be queried before adjudication.

### 3.2 "Mouse transport" is not historical by default

The branch's destroyer / fast transport / specialized transport force has materially different weather tolerance and operational reliability. Re-audit the actual hulls and designs available in spring 1943 rather than importing the historical Tokyo Express template.

The question is not merely "how many destroyers can be spared?" but:

- payload per sortie;
- loading/unloading time;
- fuel cost;
- escort requirement;
- weather cancellation rate;
- machinery casualty rate;
- probability of arrival before Allied air reaction;
- whether purpose-built / altered transport hulls can carry ammunition, food, engineering stores, radios, medical stores, and small AA weapons more efficiently than destroyer-only runs.

### 3.3 Ship-count divergence matters

Both sides have different survivor ledgers from history.

Japan has avoided much of the historical Solomon Islands destroyer/cruiser attrition, though alternate Midway and New Caledonia generated their own losses/damage. The exact spring-1943 northern deployable DD/CL/CA count must be drawn from the branch ledger, not historical OOB.

The United States likewise avoided much Guadalcanal surface attrition but suffered heavier alternate Midway losses. Old battleships, CVEs, cruisers, destroyers, amphibious lift, and fleet oilers must be allocated from one common wallet between North and South Pacific.

## 4. US decision problem to adjudicate

Do **not** assume historical LANDCRAB automatically occurs on 1943-05-11 with the historical force.

Arguments favoring an Aleutians attack:

- It can use old battleships, CVE/CAS, land-based air, and North Pacific infrastructure rather than scarce fast carriers.
- South Pacific may be too dangerous for a major amphibious offensive, making Attu one of the few politically visible places where the US can still take the initiative.
- Amchitka/Adak infrastructure already creates pressure toward a western move.
- Taking Attu can isolate Kiska and remove a Japanese North American foothold.

Arguments against / for delay:

- Efate is an exposed forward base sitting between Japanese Santo and New Caledonia and is being expanded under immediate threat.
- Amphibious shipping, DD escorts, oilers, AA assets, engineering units, and some cruisers are not free resources even if fast CVs are not required.
- A better-supplied Attu may look more expensive if US intelligence notices reinforcement.
- If Japanese northern naval activity is interpreted as a serious counter-intervention threat, the US may increase escort strength, postpone, or change the target rather than simply execute the historical plan.

Must distinguish:

- fast CV / fast BB allocation;
- old BB / CVE allocation;
- cruisers/DD;
- amphibious lift;
- oilers/tenders;
- land-based air;
- engineers / base construction;
- what can be moved north without degrading Efate's survival probability.

## 5. Japanese warning / response problem

Japan should not receive exact knowledge of LANDCRAB by fiat.

Likely warning sources to audit:

- US build-up at Adak / Amchitka;
- increased bombing and reconnaissance tempo;
- submarine / seaplane / weather-station observations;
- merchant and naval radio traffic trends;
- unusual amphibious shipping concentrations;
- escort and tanker movement;
- Komandorski itself as evidence that the US intends to interdict the supply line before a larger move.

Likely output should separate:

- probability of "an Aleutians landing is coming this spring";
- probability of correctly identifying Attu vs Kiska;
- estimated timing window;
- confidence in US force size;
- whether the evidence is strong enough to alter carrier/surface deployment.

Japan's response menu must remain open until this is calculated:

- one more conventional convoy;
- fast-transport / weather-window resupply;
- submarine resupply;
- local air / seaplane reconnaissance reinforcement;
- surface-force insurance without full carrier commitment;
- second-line carrier contingency;
- full rescue attempt;
- planned abandonment / later Kiska evacuation.

## 6. Komandorski / Attu supply is the first concrete adjudication

The next session should begin with the exact 1943-03-26 OOB and branch-specific readiness.

Do not pre-assume the historical sequence "surface battle -> Hosogaya turns back -> Attu receives nothing substantial afterward."

Key questions:

1. Does the improved Japanese fleet execute the same contact geometry?
2. How do better machinery condition, navigation, fire-control consistency, and surviving trained crews affect the battle without erasing US advantages?
3. When does the Japanese commander decide that further pursuit is no longer worth the risk?
4. Is "stop pursuit" still automatically equivalent to "cancel the transport mission"?
5. Can the convoy separate, hide in weather, re-form, or make a second approach?
6. What cargo actually reaches Attu, and how much of it is combat ammunition vs food/engineering/medical/radio stores?
7. Does a later fast-transport run occur before the US landing?
8. What does US intelligence actually observe about these deliveries?

The Attu garrison figure must be **derived from these answers**, not assumed in advance.

## 7. Efate status: retain the problem, rollback the result

The following strategic premises remain useful:

- Port Moresby is Japanese and burdens North Queensland / SWPA allocation.
- Santo is Japanese.
- New Caledonia is Japanese/Vichy-administered under the branch settlement and is becoming a substantial air/logistics/industrial base.
- Efate has multiple airfields / PBY facilities and is becoming a dangerous exposed Allied forward base.
- Japan has a real incentive to neutralize Efate before US new-carrier mass arrives.
- Five-Go creates a political gate: a Navy-led limited neutralization strike is easier to approve after the first phase is visibly stable; occupation/Fiji continuation remains much harder.

However, the previously simulated **1943-05-24 to 05-26 Efate battle is NOT CURRENT SETTLEMENT** pending the Aleutians allocation re-audit.

Do not automatically inherit:

- 1943-05-24 as the attack date;
- the exact Efate aircraft count;
- the exact US BB/CVE/CA/DD screen;
- Denver being torpedoed;
- Wasp receiving a mission-kill;
- the Japanese carrier-strike timing;
- the exact Japanese loss totals;
- the conclusion that four old US battleships are simultaneously available at Efate.

These remain useful **scenario probes**, not settled history.

## 8. Surface-force ledger notes from the session

The session also developed provisional hull-name assignments for alternate Midway surface losses and Japanese damage. These are useful but should be ledger-checked before promotion into hard CURRENT state.

US provisional assignment discussed:
- CA Astoria, Pensacola, Northampton sunk;
- CA Portland, Vincennes badly damaged but later repaired;
- DD Hammann, Morris, Anderson, Balch, Benham, Phelps sunk;
- additional DD damage slots.

Japanese provisional assignment discussed:
- CA Chokai badly damaged;
- Hiei medium damage, Kongo light damage;
- DD Yudachi and Natsugumo sunk;
- additional DD damage;
- Fubuki proposed as the New Caledonia surface-battle DD loss.

Treat these as **ledger patch candidates**, not as permission to double-count or silently overwrite older settlement files.

## 9. Post-Aleutians strategic branch to reopen later

Only after the northern decision and revised Efate outcome are fixed should the Navy's post-Efate temptation be adjudicated:

- push farther in the South Pacific;
- keep the four core carriers as Pacific fleet-in-being;
- use second-line carriers / transports / cruisers for an Indian Ocean pressure operation;
- retain a northern contingency for Kiska / Aleutians.

The intended conceptual point is that Japan may desire an Indian Ocean operation while simultaneously watching for a US move elsewhere. The tradeoff need not be one-for-one because this branch's shipping/transport/weather reliability is different, but it must be paid from real hulls, crews, fuel, aircraft, and maintenance cycles.

## 10. First files to consult next session

- `06_RUNTIME/1942H2_STRATEGIC_SETTLEMENT_v001.md`
- `06_RUNTIME/ALLIED_LOGISTICS_FLEET_AXIS_EFFECTS_1942H2_v001.md`
- `06_RUNTIME/1942Q2_OPERATION_C_MO_MI_REAUDIT_SETTLEMENT_v001.md`
- `06_RUNTIME/PACIFIC_MIDWAY_CONTINUOUS_CAMPAIGN_REAUDIT_1943-07_10_v001.md`
- `06_RUNTIME/SANTO_1942-08_TECH_STACK_REAUDIT_v001.md`
- `06_RUNTIME/NEW_CALEDONIA_1942-10_SETTLEMENT_v001.md`
- `06_RUNTIME/CHINA_FIVEGO_POLITICAL_IMPLEMENTATION_1942Q4_v001.md`
- relevant naval propulsion/navigation/torpedo/transport TECH ledgers and weapon-platform indices

Next concrete event: **Battle of the Komandorski Islands, 1943-03-26**, followed immediately by Attu resupply adjudication.
