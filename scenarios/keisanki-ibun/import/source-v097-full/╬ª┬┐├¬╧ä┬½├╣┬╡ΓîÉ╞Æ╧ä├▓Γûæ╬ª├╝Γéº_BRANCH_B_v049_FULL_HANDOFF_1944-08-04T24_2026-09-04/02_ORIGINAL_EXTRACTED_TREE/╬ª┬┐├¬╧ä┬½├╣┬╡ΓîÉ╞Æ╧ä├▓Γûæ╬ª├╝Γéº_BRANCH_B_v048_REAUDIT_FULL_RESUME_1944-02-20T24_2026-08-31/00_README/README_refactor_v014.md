# 計算機異聞 refactor v014 — 2026-08-24 data-normalized continuation package

v014 is a data-sanitization release derived from v013. Scenario adjudication is unchanged; machine-readable continuation metadata is normalized so that CURRENT state is unambiguous.

## Canonical machine entrypoint

1. `06_RUNTIME/CURRENT_BRANCH_STATE_v001.json`
2. `06_RUNTIME/CURRENT_ANALYSIS_FRONTIER_1944SPRING_REAUDIT_v001.json`
3. `06_RUNTIME/SESSION_2026-08-24_ROLLBACK_PACIFIC_CHINA_SETTLEMENT_v001.md`
4. `00_CONFIG/current_branch_overrides_v004.json`

## Normalization applied

- Spring re-audit frontier is the sole `CURRENT_SESSION_FRONTIER`.
- Summer v012 frontier is retained but marked `RETAINED_REFERENCE_NOT_CURRENT`.
- The v012 `CHECKPOINT_1944-04-30T24_v004` pointer is no longer exposed as an active/canonical restart checkpoint for the current branch.
- Active restart is explicitly `1944-04-11T00:00`, narrative-frontier mode, with no active checkpoint.
- Package ZIP is regenerated with UTF-8 filenames and the UTF-8 filename flag set.

## Current branch

Current analysis frontier: **1944-04-11, post re-audited HAILSTONE-equivalent**.

Next adjudication: **CATCHPOLE / Eniwetok, working window 1944-04-18 to 1944-04-22**.

The later Saipan/July and China/August files remain reference/provisional material only.
