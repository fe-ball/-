# GALVANIC sortie-start audit — 2026-08-28

## Scope

Re-open Operation GALVANIC from mobilization/departure rather than from the previous tactical result. Preserve strategic 1944-01-01 frontier while treating the old detailed GALVANIC settlement as comparison-only until the causal chain is re-adjudicated.

## User-approved centered assumptions now recorded

- Japanese secondary carriers are explicitly tracked; Bengal hull commitment centered at 0.
- Junyo/Hiyo/Ryujo/Zuiho form the mandatory secondary-carrier trace; routine ferry/patrol/training fatigue is paid, Bengal combat exhaustion is not.
- Shoho/Ryuho remain visible background traces and will be reopened in depth for the later Eastern Fleet return unless GALVANIC forces earlier relevance.
- Main carriers are not the sole carrier wallet: US CVL/CVE and Japanese secondary/light decks remain separate mission systems.
- Night confidence may rise for prepared one-pass torpedo attack/withdrawal, not prolonged SG/CIC gun duels.
- Water aviation (Kyofu/Zuiun plus legacy reconnaissance/seaplane network) is a mandatory local allocation and information-cycle input.

## Qualitative causal guards

- Junyo 1943-11-05 historical HALIBUT damage is not inherited on the centered line because the historical interception depended on Ultra cueing unavailable under Branch-B high-grade Japanese COMSEC divergence.
- Historical Operation-RO stripping of Marshall aircraft is not inherited absent a Branch-equivalent transfer.
- Historical Bunker Hill Espiritu Santo/Rabaul wear/staging is not inherited because Branch-B geography differs.

## Runtime data repair

The 1943-11-23 re-audit checkpoint originally listed late-1943 aircraft/carrier/seaplane/surface ledgers only as source pointers. `build_event_handout_v012.py` therefore resolved AIR_PLATFORM and SENSOR_SEARCH state from WARSTART fallback.

Repair applied to `CHECKPOINT_1943-11-23T00_BRANCH_B_GALVANIC_REAUDIT_v001.json`:

- explicit ledger fields for aircraft, seaplane doctrine, surface combatants, carriers and sortie mobilization;
- sortie/seaplane ledgers added to `state_sources`;
- checkpoint-local `weapons`, `japan_naval_posture`, `US_information_state`, and `maturation_deltas` summaries added.

Post-repair CARRIER_BATTLE handout resolution:

- AIR_PLATFORM: CHECKPOINT_LOCAL
- AIR_WEAPONS: CHECKPOINT_LOCAL
- CARRIER: CHECKPOINT_LOCAL
- SENSOR_SEARCH: CHECKPOINT_LOCAL
- SIGINT_COMINT: CHECKPOINT_LOCAL
- PERSONNEL_READINESS_STATE: CHECKPOINT_LOCAL
- AIR_FORCE_STATE: CHECKPOINT_LOCAL
- CARRIER_FORCE_STATE: CHECKPOINT_LOCAL
- INFORMATION_STATE: CHECKPOINT_LOCAL

No mandatory domain/state requirement uses WARSTART fallback.

## Current boundary

Mobilization/warning prelude is closed provisionally through 1943-11-23T00 with transit/alert fatigue paid. Next adjudication is the first external contact / first light-night surface opportunity. Do not release weapons until local air OOB, submarine patrol-day trace, named light group, US screen/route geometry, weather/moon/visibility, and actual equipped sensor/ESM units close.
