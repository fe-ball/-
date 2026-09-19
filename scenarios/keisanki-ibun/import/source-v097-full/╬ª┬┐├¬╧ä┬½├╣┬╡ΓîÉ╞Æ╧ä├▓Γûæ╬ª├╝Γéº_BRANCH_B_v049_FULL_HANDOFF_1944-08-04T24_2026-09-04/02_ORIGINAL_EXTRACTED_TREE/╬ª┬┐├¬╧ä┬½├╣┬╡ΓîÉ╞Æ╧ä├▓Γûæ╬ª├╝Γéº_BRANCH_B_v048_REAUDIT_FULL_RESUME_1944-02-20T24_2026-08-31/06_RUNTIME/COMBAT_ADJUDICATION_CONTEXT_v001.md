# Combat Adjudication Context v001

This file is a compact, reusable adjudication instruction layer. Load it before resolving any combat, interception, raid, convoy, amphibious action, base defense, special strike, or major operational gate.

## Mandatory procedure

1. Resolve the current checkpoint first. Then load `COMBAT_CAPABILITY_FACTOR_INDEX_v001.json` and `COMBAT_EVENT_FACTOR_MATRIX_v001.json` from the checkpoint `combat_resolution_support` pointer.
2. Use `EVENT_RELEVANCE_PROFILES` for technical-domain selection, but use the combat-factor matrix for completeness. They solve different problems.
3. For every `mandatory_factor`, write one resolution: `CHECKPOINT_EVIDENCE`, `TECH_EVIDENCE`, `MIXED_EVIDENCE`, `RUNTIME_INPUT`, `RUNTIME_AND_ARCHIVE_EVIDENCE`, `RUNTIME_INPUT_REQUIRED`, `UNKNOWN`, or `NOT_APPLICABLE`. Never omit a factor and never convert absence into a zero modifier.
4. Event-local variables override generic assumptions where appropriate. In particular, actual committed strength, fatigue, current damage, contact age/surprise, sortie cycle, mission geometry, weather/visibility, terrain/base condition, formation/concentration and abort/withdrawal thresholds must be supplied for final combat adjudication when the profile marks them runtime-required.
5. Separate existence → availability → readiness → mission set → mission effectiveness → allocation. Do not skip stages.
6. Integrate effects by causal stage. Do not multiply two labels that describe the same intermediate state.
7. If a mandatory factor is unknown and materially outcome-sensitive, carry a bounded branch/sensitivity band or stop final result adjudication.

## Compact pre-result checklist

Before announcing a combat result, verify: actual force; crew quality; fatigue/cohesion; platform performance; weapon suitability; prior damage; maintenance/serviceability; search/tracking; intelligence/surprise; C2/coordination; doctrine/ROE; fuel/ammo/supply; sortie/attack cycle; range/payload/route; weather/visibility/sea state; terrain/base condition if relevant; concentration/mutual support; enemy countermeasures/adaptation; objective/abort/withdrawal; post-contact regeneration.

`build_event_handout_v006.py` emits this checklist as `combat_factor_resolution` and sets `combat_resolution_ready=false` until all runtime-required mandatory factors have event-local input. Structural baseline errors remain under `execution_blocked`; incompleteness of combat-local inputs is deliberately a separate flag.
