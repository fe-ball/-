# NEXT SESSION HANDOFF REFACTOR v023

## Start here
1. Current time is **1943-10-01T00:00**.
2. Runtime restart is `CHECKPOINT_1943-09-30T24_v001`; do not use the former 1944 restart.
3. Load `BRANCH_INVARIANT_GUARD_1943-10-01_v001.json` before any historical comparison.

## Anti-handback items
- Midway is Japanese-held at restart. A US recapture must be freshly adjudicated; the old Sep-1943 result is provisional.
- New Caledonia ownership is split: Japanese military/traffic control, Vichy nominal sovereignty.
- US carrier losses Lexington/Yorktown/Enterprise/Hornet/Saratoga and British Indomitable/Formidable stay paid. Wasp survives; new Essex/CVL power is additive.
- Japanese hull/commander fates are branch-specific. Four-carrier core survives; historical Guadalcanal/Vengeance loss dates do not auto-apply.
- Load TECH v006 combat and SIGINT/COMINT effects. No historical JN-25 plaintext shortcut.
- China: Hanzhong endpoint settled; Sichuan Phase III HOLD. Burma allocations consume China consolidation margin.

## October order
1. Branch-geography-based US fast-carrier pressure/raid direction.
2. Japanese first-line carrier + surface allocation and actual surviving hull readiness.
3. SEAC/Bengal land-air concentration.
4. Cox's/Teknaf contested coastal throughput and landing hull/escort readiness.
5. Shinshu Maru / Nisshin / DD / CA / kaibokan individual closure.
6. India late-Oct/early-Nov GO/NO-GO.

Use `python 98_TOOLS/validate_refactor_v011.py` before advancing if any runtime/control file is edited.
