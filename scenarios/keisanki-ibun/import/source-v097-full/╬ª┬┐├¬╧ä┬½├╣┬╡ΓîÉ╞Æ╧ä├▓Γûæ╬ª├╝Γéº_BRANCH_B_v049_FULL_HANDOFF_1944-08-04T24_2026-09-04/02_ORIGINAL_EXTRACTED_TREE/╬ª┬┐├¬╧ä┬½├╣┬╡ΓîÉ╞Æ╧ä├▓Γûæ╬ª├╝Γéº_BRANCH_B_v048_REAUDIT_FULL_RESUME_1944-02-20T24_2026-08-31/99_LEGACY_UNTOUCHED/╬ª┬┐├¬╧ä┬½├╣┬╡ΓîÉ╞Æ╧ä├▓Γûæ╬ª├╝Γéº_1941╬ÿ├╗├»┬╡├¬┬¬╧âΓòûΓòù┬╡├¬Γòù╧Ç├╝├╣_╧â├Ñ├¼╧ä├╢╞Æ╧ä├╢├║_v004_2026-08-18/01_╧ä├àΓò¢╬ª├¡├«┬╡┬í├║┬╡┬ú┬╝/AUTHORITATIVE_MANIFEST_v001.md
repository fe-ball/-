# 1941開戦巻戻し 現行正本マニフェスト v0.01

## 現行入口

今後の再走査は次を正本入口とする。旧途中版から数値・スイッチ状態を自動継承しない。

- `OPENING_RERUN_PACKET_1941_v006.md`
- `opening_state_1941-12-07_v006.json`
- `switch_registry_v010.json`
- `MASTER_SWITCH_AUDIT_v010.md`
- `MASTER_SWITCH_AUDIT_v010.csv`
- `RERUN_GATE_MATRIX_v005.md`
- `CONDITIONAL_POLICY_RESET_LEDGER_v001.md`
- `LATER_SWITCH_PROVENANCE_AND_RELEASE_v007.md`
- `SWITCH_AUDIT_COVERAGE_v001.md`
- `MALAYA_PHASE0_OPENING_PACKET_v003.json`
- `OPENING_DIVERGENCE_LEDGER_1941-12-07_08_v001.md`
- `opening_divergence_ledger_1941-12-07_08_v001.json`
- `MALAYA_OPENING_OOB_BASELINE_v001.md`
- `malaya_opening_oob_baseline_v001.json`
- `MALAYA_EVE_STATE_DERIVATION_v001.md`
- `MALAYA_DEC8_LOWER_BOUND_CONSTRAINTS_v001.md`
- `malaya_dec8_lower_bound_constraints_v001.json`
- `PRECOMBAT_DIVERGENCE_ELIGIBILITY_MATRIX_v001.md`
- `precombat_divergence_eligibility_v001.json`
- `PREWAR_SOUTHERN_AIR_CONCENTRATION_1941-11-15_12-07_v001.md`
- `prewar_southern_air_concentration_v001.json`
- `MALAYA_PHASE1_1941-12-08_15_STATE_TRANSITION_v001.md`
- `malaya_phase1_state_schema_v001.json`
- `malaya_phase1_events_v001.json`
- `state_transition_validator_v001.py`
- `opening_state_validator_v003.py`
- `PEARL_STATE_TRANSITION_v001.md`
- `pearl_state_transition_v001.json`
- `SUBMARINE_OPENING_OOB_1941-12-08_v001.md`
- `submarine_opening_oob_1941-12-08_v001.json`
- `SURFACE_OPENING_BASELINE_v001.md`
- `FLEET_ROSTER_SOURCE_AUDIT_v001.md`
- `MARITIME_OPENING_SWITCH_REAUDIT_v001.md`
- `_later_switch_candidates.txt`

## 旧版の扱い

- `OPENING_STATE_1941-12-07_v001..v005.md`：履歴のみ。
- `opening_state_1941-12-07_v001.json`：旧machine state。使用禁止。
- `switch_registry_v003..v009.json`：監査履歴。現行はv010。
- `SWITCH_LEDGER_v001..v005.md`：監査履歴。
- `RERUN_GATE_MATRIX_v001..v004.md`：監査履歴。現行ゲートはv005。

旧ファイルに残る `+15–25%`、`+20–35%`、MI後固定日付等をscenario inputへ復帰させない。

## 次の実行ゲート

1. 1941-11-15～12-07南方航空集中。
2. 1941-12-07/08 Pearl/Philippines/Malayaを実時間同期。
3. Malaya 12-08～15の日次状態遷移。
4. 必要になった水上艦だけ個艦Availabilityを閉じる。
5. 初期潜水艦戦は個艦mission-dayへ展開。

UNKNOWNを旧総量で埋めず、閉じた状態だけを次へ渡す。
