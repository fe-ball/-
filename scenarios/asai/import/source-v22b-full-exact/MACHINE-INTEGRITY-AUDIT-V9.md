# MACHINE INTEGRITY AUDIT — V9 SESSION CLOSE / TECHCLOSE4

- status: **PASS**
- package: `ASAI-WORLDLINE-HANDOFF-2026-09-05-FULL-V9-NOMONHAN-CLOSED-CHINA-JUN20`
- datafix: **V9-TECHCLOSE4**
- total files: **662**
- manifest SHA targets: **658**
- manifest errors / validation errors: **0**
- current state pointer: **PASS**
- index/authority pointer validation: **PASS**
- TSV rectangularity: **PASS**
- inventory membership: **PASS**
- session issue history rows: **12**
- active session queue rows: **7**
- technical issue rows: **26**
- cheat-rule index rows: **32**
- technical-stage taxonomy rows: **53**
- China current replay clock: **1939-06-20 24:00**
- Nomonhan: **CLOSED through 1939-08-31 stabilization/central stop**
- next gate: **1939-06-21 Shantou/Swatow**

## TECHCLOSE4 closure checks
- G3M Chongqing EX state: **CLOSED-CONTROL**
- Nomonhan AT-37/TANK-37 production-inspection-forwarding: **CLOSED-LOWER-BOUND-FLOW**
- Nomonhan aviation stock-flow: **CLOSED-CAMPAIGN-SUFFICIENT**
- uranium strategic-system balance: **CLOSED-SCENARIO-MACRO**
- RIKEN isotope research: **CLOSED-THROUGH-AUG1939**

V9 manifest/SHA/audit files are excluded from the content manifest to avoid self-hash recursion. `PACKAGE-INVENTORY-V9.tsv` is included in the content manifest but excludes itself and the four recursion-control files from its membership list.
