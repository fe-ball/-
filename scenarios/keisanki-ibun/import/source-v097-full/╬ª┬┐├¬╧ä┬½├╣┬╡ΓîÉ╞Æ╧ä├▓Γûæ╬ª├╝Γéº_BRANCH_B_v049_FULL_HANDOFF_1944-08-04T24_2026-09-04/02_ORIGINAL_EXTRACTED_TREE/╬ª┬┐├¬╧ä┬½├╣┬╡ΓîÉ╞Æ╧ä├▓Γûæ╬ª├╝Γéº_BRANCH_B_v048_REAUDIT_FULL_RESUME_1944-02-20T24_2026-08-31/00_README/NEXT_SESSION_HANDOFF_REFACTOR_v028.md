# NEXT SESSION HANDOFF — v028 / GALVANIC full re-audit

Strategic year-end frontier remains **1944-01-01 00:00**, but GALVANIC has been reopened as a causal dependency after the Axis submarine-tech / electronic-warfare audit.

**Analytical restart:** `CHECKPOINT_1943-11-23T00_BRANCH_B_GALVANIC_REAUDIT_v001`.

Do not jump to the 11/26 carrier strike. Start with actual force commitment/sortie state and carry forward prior damage, repair debt, aircrew/airframe fatigue, fuel, transit and readiness.

Mandatory Japanese carrier audit includes **Shokaku, Zuikaku, Hiryu, Soryu plus Junyo, Hiyo, Ryujo, Zuiho**. Trace actual location/readiness/air group/deck/fuel/escort and why each does or does not participate. Do the same for date-valid US CV/CVL groups under Branch old-carrier losses.

New technology/doctrine rules:
- I-30 returns in late Oct 1942; subsequent hull fate must be propagated, not assumed.
- 1943 metric ESM/RWR, ESM-cued search, precision-track/calibration, base control cells, electronics field service, Giman-shi/RCM, EMCON/radar survivability and Bold-type decoys are staged capabilities in `TECH_INDEX_v009`.
- Use `EM warning -> bearing/battle preparation -> sensor contact -> track -> weapon-quality` rather than a single 'sees first' statement.
- Selected Japanese night forces may prepare a Long-Lance ambush before own target-quality contact; US SG/CIC weapon-quality track advantage remains. Night confidence may rise for one-pass torpedo action, not prolonged radar gun duels.
- Tool-driven organizational changes matter: island sensor lines, fighter readiness states, base repair/calibration and cue-to-confirm reconnaissance.

Future technology guards: I-34 return, I-29 Singapore-to-Japan physical cargo, RO-501 and I-52 are unresolved future gates. German Naxos/Type-XXI/Jumo/HWK physical effects cannot be back-ported.

If the reconstructed GALVANIC changes qualitatively, follow that branch and propagate it into the 1944-01-01 year-end checkpoint before resuming FLINTLOCK/Eastern Fleet work.

## 2026-08-28 sortie-start closure

The re-audit has now been pushed backward from the 11/23 tactical checkpoint into the **11/08–23 mobilization / departure / warning prelude**. Current working ledger: `06_RUNTIME/GALVANIC_SORTIE_MOBILIZATION_LEDGER_1943-11-10_23_v001.json`; narrative: `06_RUNTIME/GALVANIC_SORTIE_START_REAUDIT_1943-11-10_23_v001.md`.

Centered secondary-carrier posture is now explicit: Bengal hull commitment **0**; Junyo/Hiyo/Ryujo/Zuiho were retained as a two-ocean reserve, did routine ferry/patrol/training/qualification work, then shifted Pacific-priority as US amphibious pressure became clear and took pre-operation rest/maintenance. Shoho/Ryuho stay visible for later Eastern Fleet re-audit but count zero in the immediate GALVANIC combat wallet until individually traced.

Do **not** inherit Junyo's historical 1943-11-05 HALIBUT torpedo damage on the centered line: that interception was historically Ultra-cued, while Branch B denies that US high-grade short-strategic Japanese traffic reconstruction. Keep an uncued submarine encounter only as sensitivity.

Do **not** inherit the historical 12 Nov Operation-RO draw of 27 Marshall aircraft unless a Branch-equivalent transfer is independently proven. This is a potentially qualitative GALVANIC delta. Bunker Hill likewise cannot inherit historical Espiritu Santo/Rabaul staging/wear because Espiritu Santo is Japanese-held in Branch B.

Water aviation is mandatory runtime state, not color text. By 11/23 Kyofu is material and Zuiun is in the first combat-capable-detachment window. Separate existence/production/delivery from local allocation; use the matured search cycle `broad search -> suspicious contact -> re-search -> fast confirmation -> track -> handoff`.

The 11/23 checkpoint had a data-binding defect: late-1943 ledgers were only source pointers, so the event-handout generator fell back to WARSTART state for AIR_PLATFORM/SENSOR_SEARCH. The checkpoint now contains the required local state summaries and direct ledger bindings. Re-test shows all mandatory CARRIER_BATTLE domains and mandatory state requirements resolve `CHECKPOINT_LOCAL`; validator passes with zero errors/warnings.

**Next boundary:** first Japanese external contact / first light-night surface opportunity. Close base-by-base Marshall/Gilbert ready aircraft, submarine on-station hulls/patrol-days, named light-surface group/readiness, US convoy screen/route geometry, weather/moon/visibility, and actual ESM/radar-equipped units before weapon release.

Master post-v027 audit context: `06_RUNTIME/SESSION_2026-08-28_MASTER_AUDIT_DELTA_v001.md`.

## 2026-08-28 first-contact closure

First-contact ledger: `06_RUNTIME/GALVANIC_FIRST_CONTACT_LEDGER_1943-11-22_23_v001.json`; narrative: `06_RUNTIME/GALVANIC_FIRST_CONTACT_REAUDIT_1943-11-22_23_v001.md`.

Centered line now closes the contact ladder through **first firm Japanese external sensor contact / partial operational track** on the morning of 1943-11-23, centered about **0630 local**. Late 11/22 passive/DF evidence gives warning/bearing only; dawn cue-assisted air search then visually confirms one US carrier-cover formation. The report does not identify the whole US CV/CVL disposition or the assault convoy and is not weapon-quality.

Zuiun/D4Y are used at the correct causal stage: broad-ocean detection remains the legacy long-range search system's job; scarce faster aircraft improve revisit/re-search/contact freshness after a suspicious or firm contact exists. US radar/CAP can break continuous shadowing without automatically preventing the initial report.

Environmental center: favorable trade-weather band for dawn search; 23/24 Nov is a dark waning-crescent night near new moon. The exact shifted Branch date is not assigned the historical 20 Nov weather observation as a hard fact, only as a fallback regime.

**Qualitative branch gate crossed:** the old detailed settlement's first major Marshall night-air action occurred after the Branch landings. The re-audit now has a credible firm carrier contact on D-1 while the Marshall air wallet is healthier and the 23/24 night is very dark. Therefore do not jump back to 11/24-25. Resolve a pre-D-day recontact/strike decision first.

**Next boundary:** 1943-11-23 afternoon/night. Close base-by-base attack/recon aircraft and night-qualified crews, named light-surface group, submarine patrol-day roster, US screen/route geometry, actual unit sensor/ESM fits, and event cloud/recovery-base state. Then adjudicate whether Japan can maintain/reacquire a fresh enough track for a night land-air strike and/or one-pass light-surface probe. No weapon result has yet been awarded.
