# GALVANIC sortie-start re-audit — mobilization to 1943-11-23 v001

status: CURRENT WORKING REAUDIT NOTE  
ledger: `06_RUNTIME/GALVANIC_SORTIE_MOBILIZATION_LEDGER_1943-11-10_23_v001.json`

## 1. 11/23 is not the sortie start

The 1943-11-23 checkpoint is retained as the first tactical-resolution boundary. Forces do **not** materialize there. The operational prelude is charged from the staggered mobilization/departure window in roughly 8–16 November through 23 November: convoy assembly, carrier departure, AO rendezvous, CAP/ASW, search, drills, maintenance, alert, transit and fatigue.

The old Branch D-Day of 24 November is a planning/comparison datum only until this prelude is closed. A qualitative change can move the later sequence.

## 2. First qualitative deltas

### Junyo

Historical 5 November 1943 damage is not copied automatically. The historical `HALIBUT` interception was Ultra-cued, while Branch B explicitly denies the US historical high-grade short-strategic reconstruction of Japanese operational traffic. Centered Branch line therefore carries **no 5 November torpedo hit on Junyo**. An uncued encounter remains a low-probability sensitivity, not the default.

This matters: secondary-carrier accounting is not cosmetic. A naive historical carry-forward would remove or seriously degrade a deck that Branch B is likely to retain.

### Marshall aircraft / Operation RO

Historical Galvanic entered the fight after 27 aircraft were stripped from the Marshalls on 12 November for Operation RO. That transfer is part of the historical northern-Solomons/Rabaul emergency chain and is not automatically valid in Branch B. Unless an equivalent Branch transfer is found, the Marshall/Gilbert air wallet remains substantially healthier.

### Bunker Hill

Historical Bunker Hill staging through Espiritu Santo and Rabaul combat wear cannot be copied because Espiritu Santo is Japanese-held. The ship remains date-valid, but must use surviving US staging/AO nodes. Centered effect: less acute combat wear than historical, but different transit/rendezvous cost and somewhat less immediate Rabaul seasoning.

## 3. All-carrier-class working wallet at 11/23

### United States fast decks

Centered date-valid set:

- CV: Wasp, Essex, Yorktown (CV-10), Lexington (CV-16), Bunker Hill.
- CVL: Independence, Princeton, Belleau Wood, Cowpens, Monterey.
- Working ready-aircraft class before CAP/search/recovery reservation: about **540–590** across ten fast decks.

Old Lexington/Yorktown/Enterprise/Hornet/Saratoga remain lost. Intrepid and Cabot are not inserted early.

### United States escort carriers

Track separately: Barnes, Chenango, Coral Sea, Corregidor, Liscome Bay, Nassau, Sangamon, Suwanee. Working ready-aircraft class is about **185–215**, but this pool is primarily CAP/ASW/CAS/spotting. It is not added to TF fast-carrier strike strength.

### Japan first-line core

Shokaku / Zuikaku / Hiryu / Soryu remain the conserved first-line core. Working ready-aircraft class is about **270–290**, with low acute fatigue. They do not sortie merely because Tarawa/Makin are threatened; contact freshness, enemy mission-state separation, fuel/escort and recovery geometry remain gates.

### Japan secondary carriers

Centered Bengal hull commitment is **0**. Junyo / Hiyo / Ryujo / Zuiho are treated as a two-ocean mobile reserve that becomes Pacific-priority once the US amphibious signature becomes clear. Routine ferry/patrol/training is charged; heavy Bengal campaign fatigue is not.

Combined working combat-usable air group if all four are released: about **105–130**. This does not mean all four are in one task group or within immediate strike radius on 23 November.

Shoho and Ryuho remain visible background candidates but are **not counted** in the immediate combat wallet until individual location/air-group/deck-readiness trace closes. Their deeper treatment is deferred to the later Eastern Fleet return audit unless GALVANIC itself forces them into relevance.

## 4. Water aviation is now part of the main calculation

Because the historical Operation-RO drain is not copied and the 1943 fielding ledgers are now explicitly runtime-bound, the Gilbert-Marshall network is provisionally carried as:

- land fighters capable of Gilbert reaction: roughly 80–95 physical-class across the Marshall network before suppression, with lower event-ready count;
- attack aircraft: roughly 35–45 physical-class, only a subset night-qualified;
- legacy recon/flying-boat/floatplane core: roughly 15–20 physical-class;
- Kyofu: working local allocation 12–20 physical / 8–16 ready across priority lagoon nodes;
- Zuiun: working first-detachment allocation 5–9 physical / 4–7 ready on Marshall-side nodes by 23 November.

The Zuiun is not scored as a small bombing squadron. Its first-order value is contact freshness: search, revisit, fast confirmation and handoff. Kyofu does not defeat F6F sweeps; it makes `runway suppressed = air activity ended` invalid for some time by preserving a water-based local layer.

These are working local-allocation bands, not final OOB. Base-by-base placement must close before the first Marshall air strike.

## 5. Paid mobilization sequence

**8–12 Nov:** US slow/assault echelons, oilers, escorts and carrier formations begin distributed assembly/departure. Japan gets a growing major-operation signature from traffic/DF/recon/submarine observation and missing shipping, but no magic target identification.

**13–16 Nov:** the amphibious character becomes more likely than a pure raid. Japanese secondary carriers cut nonessential routine tasks, take maintenance/rest and begin Pacific-priority movement where geography permits. First-line carriers raise readiness without automatic GO.

**17–20 Nov:** route and suppression activity increasingly indicate the Gilbert-Marshall axis. Japan raises Marshall/Gilbert search, CAP, dispersion, submarine and light-surface readiness. Since no Operation-RO stripping is paid, this alert also burns more Japanese fuel, engine-hours and crew rest than the historical depleted force did.

**21–23 Nov:** US fast decks divide effort among suppression, fleet defense, search and assault support. Japan tightens target inference and enters the external-contact chain with submarines, water aviation and light night forces. By 23 November both sides have **paid transit/alert fatigue**.

## 6. Runtime data repair

`CHECKPOINT_1943-11-23T00_BRANCH_B_GALVANIC_REAUDIT_v001.json` listed the October aircraft/carrier/seaplane/surface ledgers only in `state_sources`. The event-handout generator therefore failed to bind them and fell back to opening-war state for parts of AIR_PLATFORM and SENSOR_SEARCH.

The checkpoint now explicitly binds:

- `AIRCRAFT_FIELDING_LEDGER_1943-10-01_v001.json`
- `SEAPLANE_TACTICS_LEDGER_1943-10-01_v001.json`
- `SURFACE_COMBATANT_CAPABILITY_LEDGER_1943-10-01_v001.json`
- `CARRIER_CAPABILITY_LEDGER_1943-10-01_v001.json`
- this sortie-mobilization ledger.

The direct file pointers alone were not sufficient, because `build_event_handout_v012.py` resolves runtime state through checkpoint-local state paths. The checkpoint was therefore also repaired with explicit `weapons`, `japan_naval_posture`, `US_information_state`, and `maturation_deltas` summaries whose evidence is the above ledgers.

Verification after repair: all mandatory CARRIER_BATTLE domains — AIR_PLATFORM, AIR_WEAPONS, CARRIER, SENSOR_SEARCH and SIGINT_COMINT — resolve as `CHECKPOINT_LOCAL`; AIR_FORCE_STATE, CARRIER_FORCE_STATE, PERSONNEL_READINESS_STATE and INFORMATION_STATE also resolve locally. No WARSTART fallback remains in those mandatory domains/state requirements. `validate_refactor_v016.py` returns `ERRORS=0 WARNINGS=0`.

## 7. Next tactical boundary

Next resolution is **first Japanese external contact / first light-night surface opportunity**, not D-Day. Before weapon release close:

- Marshall/Gilbert ready aircraft by base and type;
- submarine on-station hulls and patrol days;
- named light-surface group and readiness;
- US assault convoy screen/route geometry;
- weather/moon/visibility;
- actual ESM/radar-equipped units.

Then use the EM warning → bearing history/preparation → contact → track → weapon-quality ladder. Japanese night confidence may rise for a one-pass torpedo ambush and withdrawal; it does not become confidence in a prolonged SG/CIC gun duel.
