# 計算機異聞 BRANCH B v056 START HERE

revision: 2026-09-06
status: audit-only overlay / NO submarine capability canon overwrite
base: v055

## Purpose

v056 is a submarine-audit checkpoint only. It does **not** change submarine performance, patrol allocations, combat results, or New Caledonia outcomes.

The user-mandated audit order is:

1. Inventory the current submarine data.
2. Reverse-map current results that were placed because submarines were assumed stronger, and identify submarine-relevant gaps through the provisional end of New Caledonia.
3. Only then externally revalidate submarine data.
4. Re-adjudicate 1941 opening through end-1942 / provisional NC close.

## Included audits

- `03_AUDIT/BRANCH_B_SUBMARINE_CURRENT_STATE_AUDIT_STAGE1_v002.md`
- `03_AUDIT/BRANCH_B_SUBMARINE_ASSUMPTION_REVERSE_MAP_STAGE2_v001.md`

## Key authority findings

- The technical submarine input files remain current inputs pending Stage 3 validation.
- Old 1942H2 patrol-allocation and combat-result ledgers were reopened by the 1941/Q2 rollback and must not be treated as immutable canon.
- The largest authority seam is the old South Pacific `10–14 allocated / 7–10 effective` wallet, later reused by v050 to support Santo `6–8 effective` and New Caledonia `8–11 effective`. Those local scenario results remain current scenario text, but their submarine wallet must be rebuilt fresh before final canonization.
- The latest Indian Ocean working audit is not the old `+14–20 ships / 80–130k GRT` line. The later RN audit reopens 1942H2 Branch-specific direct extra loss at approximately `50–90k GRT`, with `5–8 escort/ASW hull-equivalents` continuously required; both remain Stage-3/4 recheck inputs rather than protected answers.
- No aggregate multiplier cap exists. Stage-wise changes may yield 2x/3x aggregate results if the causal chain supports it. Blanket whole-weapon multipliers remain prohibited.
- Allied submarine models, especially U.S. 1942 patrol cycle/Mark 14 and British Indian Ocean submarines, are not yet modeled to the same depth as Japanese submarines. Stage 3 must correct this asymmetry.

## Next gate

Do not advance the world clock or further canonize NC submarine effects before Stage 3 historical/technical validation and Stage 4 re-adjudication.
