# Combat Adjudication Context v002

Load this compact instruction layer before resolving combat, interception, raid, convoy, amphibious action, base defense, special strike, major operational gate, or any event introducing a branch-specific/new weapon.

## Mandatory procedure

1. Resolve the current checkpoint first. Load every pointer under `combat_resolution_support`, including the factor index/matrix and the weapon/platform capability index/matrix/novel-weapon policy.
2. `EVENT_RELEVANCE_PROFILES` selects normal TECH domains; the combat-factor matrix checks non-platform completeness; the platform matrix independently forces platform-class review. None substitutes for the others.
3. For every mandatory combat factor, emit an explicit resolution. Omission is never a zero modifier.
4. For every mandatory platform class, read its capability dimensions, anti-underestimate rules, active TECH candidates and indexed branch systems. Match these to actual participants; an index entry is not proof of presence.
5. Submarines: evaluate sortie availability, station time, information age, underwater repositioning, attack opportunity, survival/re-sortie and enemy diversion. Do not reduce to torpedo hit rate or historical Japanese submarine results.
6. Surface combatants: evaluate practical speed/range, reliability, damage-control state transitions, sensor/optical tracking, gunfire, torpedo first/second-salvo cycle, formation support and re-entry. Do not reduce to gun caliber, paper speed or initial tube count.
7. Any `AHISTORICAL_NEW`, `AHISTORICAL_TIMING`, `DIVERGENT_VARIANT` or `UNKNOWN` event-local system must have a capability record, maturity/readiness and provenance. Do not force it into the nearest historical platform and do not assume superiority merely because it is new.
8. Event-local actual strength, fatigue, damage, intelligence age, sortie cycle, geometry, weather, terrain, concentration and abort/withdrawal thresholds remain mandatory where the factor matrix says so.
9. Separate existence → production → allocation → serviceability → crew workup → mission availability → mission effectiveness.
10. If a mandatory factor/platform/novel-system record is materially unresolved, carry a bounded branch or stop final combat adjudication.

`build_event_handout_v007.py` emits `combat_factor_resolution`, `platform_capability_resolution` and `novel_weapon_review`. Final combat/gate output requires both factor completeness and weapon/platform completeness; the combined flag is `combat_resolution_ready`.
