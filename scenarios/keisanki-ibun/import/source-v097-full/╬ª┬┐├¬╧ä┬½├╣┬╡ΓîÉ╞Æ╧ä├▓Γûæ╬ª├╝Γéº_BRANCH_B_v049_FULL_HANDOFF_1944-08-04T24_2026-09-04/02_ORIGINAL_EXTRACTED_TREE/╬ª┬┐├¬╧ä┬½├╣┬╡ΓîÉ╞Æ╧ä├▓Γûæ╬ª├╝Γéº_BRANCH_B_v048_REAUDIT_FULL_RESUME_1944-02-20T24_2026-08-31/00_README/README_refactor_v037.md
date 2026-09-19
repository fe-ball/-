# 計算機異聞 refactor v037 — Raiden interceptor-system re-audit working full package

CURRENT authority remains unchanged at 1944-01-01 (`CURRENT_BRANCH_STATE_v012`, checkpoint v004, overrides v012). The WORKING discussion clock remains 1944-01-28.

v037 does not advance the war clock. It closes the Raiden/J2M question from airframe through base-defense coordination so later B-24/B-29 and Marianas calculations do not treat a national ready count as a homogeneous high-altitude interception force.

Closed in v037:
- Standard Raiden production median is centered at 590–600 km/h near 5.4–5.8 km and 6,000 m climb 5:35–5:55; the old 5:20-class figure is retained only as a good-aircraft/prototype tail, not the fleet median.
- A limited high-altitude mechanically-supercharged Kasei subset is split from the standard aircraft; 14–22 serviceable nationwide is a Jan-28 working band inside total Raiden inventory. Exhaust-turbo aircraft remain test-only with combat count 0.
- Four-20-mm armament is dominant by Jan 1944, but mixed Type-99 ballistic sets remain; full four-Model-2-equivalent unification is not granted to every frontline aircraft.
- Raiden is modeled as a warning/plot/radio-vector interceptor system. A-grade bases gain staged readiness and better initial geometry but do not receive US-style continuous precision GCI/CIC.
- GALVANIC losses remain locked. A dated post-GALVANIC exchange-transition ledger records only subsequent procedural learning: fixed-base maturity improves through Dec-Jan and falls back if radar/plot/radio is suppressed.
- Marshall totals are unchanged. v002 places 12–18 serviceable Raiden, center 16, inside the existing 72 fighter/local-cover slots, centered Taroa 10 / Roi 6.
- The future 4/30 `Raiden ready 260–300` line is now explicitly inventory-only; future B-29 calculations must split standard/high-alt/turbo-test variants first.

Start with `00_README/CURRENT_DISCUSSION_FRONTIER_v006.json`, then `06_RUNTIME/RAIDEN_INTERCEPTOR_SYSTEM_1943Q4_1944Q1_WORKING_v001.json`, `06_RUNTIME/AIR_DEFENSE_EXCHANGE_TRANSITION_POST_GALVANIC_1943-11_1944-01_WORKING_v001.json`, and `06_RUNTIME/MARSHALL_AIR_OOB_1944-01-28_WORKING_v002.json`.
