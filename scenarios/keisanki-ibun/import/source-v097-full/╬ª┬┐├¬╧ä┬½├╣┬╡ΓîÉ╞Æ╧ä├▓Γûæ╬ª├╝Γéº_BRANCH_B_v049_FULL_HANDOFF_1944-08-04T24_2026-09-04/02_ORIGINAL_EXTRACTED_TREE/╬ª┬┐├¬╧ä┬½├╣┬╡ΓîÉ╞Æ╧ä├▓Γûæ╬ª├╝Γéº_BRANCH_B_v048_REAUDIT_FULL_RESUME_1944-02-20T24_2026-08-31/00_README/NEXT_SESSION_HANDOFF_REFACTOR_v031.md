# NEXT SESSION HANDOFF v031 — Indian Ocean / Japanese wallet

Branch B authoritative time: **1944-01-01T00:00**.
GALVANIC: **CLOSED**, including negative-delta revalidation. Do not reopen it without a new upstream dependency.

## Load first
1. `06_RUNTIME/CURRENT_BRANCH_STATE_v012.json`
2. `05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v004.json`
3. `00_CONFIG/current_branch_overrides_v012.json`
4. `06_RUNTIME/JAPAN_HULL_RECONCILIATION_1944-01-01_WORKING_v003.json`
5. `06_RUNTIME/JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_v004.json`
6. `95_AUDIT/JAPAN_INDIAN_OCEAN_ORIGIN_ROUTE_AUDIT_1944-01_WORKING_v001.md`
7. `06_RUNTIME/GALVANIC_DAMAGE_REPAIR_REGEN_LEDGER_1943-11_1944Q1_v002.json`

## What has been reconciled in working state
- Branch-specific narrative-only hull damage slots from Midway/New Caledonia/Efate/Bengal/GALVANIC are named/booked in the working ledger.
- Modern fleet DD center is rebuilt hull-by-hull rather than inheriting historical Solomon losses: **81 physical**, **70–75 ready band, center 72**.
- Light cruisers: **21 physical**, **18–20 ready/near-ready**. Absent Solomon loss chains restore Yura/Jintsu/Sendai and remove historical Agano Rabaul-damage inheritance.
- Submarine physical center is rebuilt to **103 (102–104)**, with **82–89 combat-usable center 86** and **63–71 ocean-patrol-ready/near-ready center 67**. This supersedes earlier undercounting that implicitly retained historical H2-1943 submarine losses.
- Warship-construction delta is modest for fleet surface hulls (Yugumo 3–5%, Akizuki 2–4% schedule improvement); the large 1944 advantage is survival/availability, not mass extra construction.
- Taiho remains a **Feb-1944 completion + work-up** gate, not a January asset.

## Initial Indian-Ocean reinforcement screen (WORKING, not yet ordered)
Preferred first mobile group after high-confidence RN eastbound confirmation:
- `Oyodo`
- `Teruzuki`
- `Takanami`
- `Makinami`
- `Kiyonami`

Working origin: Truk / Combined-Fleet mobile pool.
Route center: Truk → Palau → Balikpapan/Tarakan fuel gate → Singapore/Lingga.
Movement clock: **6–8 days** center; Jan 11–12 GO implies about Jan 18–21 arrival.
Mission: contact-plot fusion, ISR/logistics escort, one-pass Type-93 strike on fresh contact; avoid sustained daylight/radar gunnery against the RN battle line.

Second gate if Eastern Fleet sorties east from Ceylon:
- `Noshiro` center (keep Agano Pacific unless separately freed),
- `Niizuki`,
- 2–3 DD from `Onami / Suzunami / Hayanami`,
- activate `I-27 / I-37`; aim about 7 active/outbound conventional boats.

Third gate if RN enters Bay/Andaman approach:
- `Suzuya + Kumano`, plus the required DD screen debit.

## Local submarine clock
Jan 1 on-station: `I-162`, `I-166`.
Forward ready/near-ready: `RO-110`, `I-165`, `I-27`, `I-37`, `RO-111`.
En route south: `RO-112`.
Do **not** count `I-8 / I-10 / I-29 / I-34 / I-175 / I-30` as immediate local combat availability for this problem.
Sentaka: **0 initial transfer**; 1–2 only if stale/fresh-contact geometry specifically rewards sprint/recontact.
German Monsun boats: sector-level information handoff only, no unified tactical control.

## Next exact action
Open the Eastern Fleet indication timeline from late Dec 1943 / early Jan 1944. At each evidence gate (departure preparation → Gibraltar/Med transit → visual confirmation → Aden departure → Ceylon arrival → Ceylon eastbound sortie), do four things together:
1. update Japanese confidence and observation/DF/search sectors;
2. issue or withhold actual surface/submarine movement orders;
3. debit the Central-Pacific opportunity cost explicitly;
4. update the RN estimate of Japanese redeployment from its own SIGINT/recon/submarine observations.

Observation network itself is still an open quantitative node: Branch logic supports higher priority-theater availability, DF/ESM cueing and integrated plot cells, but exact Jan-1944 Andaman–Arakan station count has not yet been promoted. Rebuild that before resolving first weapon-quality contact.
