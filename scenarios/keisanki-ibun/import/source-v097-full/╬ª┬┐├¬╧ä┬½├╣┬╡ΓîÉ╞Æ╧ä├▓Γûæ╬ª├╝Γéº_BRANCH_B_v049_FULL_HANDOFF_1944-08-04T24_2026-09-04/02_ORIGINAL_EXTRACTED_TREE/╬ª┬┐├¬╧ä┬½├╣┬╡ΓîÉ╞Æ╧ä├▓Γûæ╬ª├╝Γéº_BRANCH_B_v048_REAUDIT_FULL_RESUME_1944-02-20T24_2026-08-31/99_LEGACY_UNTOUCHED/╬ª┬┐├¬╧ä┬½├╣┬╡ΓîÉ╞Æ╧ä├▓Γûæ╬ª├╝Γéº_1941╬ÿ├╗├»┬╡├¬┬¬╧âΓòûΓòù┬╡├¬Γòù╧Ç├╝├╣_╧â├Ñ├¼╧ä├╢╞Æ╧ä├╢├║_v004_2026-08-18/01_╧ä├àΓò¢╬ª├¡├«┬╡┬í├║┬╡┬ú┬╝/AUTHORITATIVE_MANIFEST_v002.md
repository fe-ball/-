# 1941開戦巻戻し 現行正本マニフェスト v0.02 — 開戦実行可能版

この版は、旧 `AUTHORITATIVE_MANIFEST_v001` の正本群を同一ディレクトリへ展開し、欠損していた machine-readable 会計依存と validator の世代ずれを修復した実行入口である。

## 実行入口

1. `opening_execution_state_v001.json`
2. `opening_state_1941-12-07_v006.json`
3. `MALAYA_PHASE0_OPENING_PACKET_v003.json`
4. `switch_registry_v010.json`
5. `opening_technical_clock_guard_v001.json`
6. `RERUN_GATE_MATRIX_v005.md`

検証は `../02_検証/validate_opening_package_v001.py` を実行する。

## 修復点

- `prewar_concentration_accounting_v001.json` を既存資料の行政集計値から正規化して復元。新規推定値は置いていない。
- `opening_state_validator_v003.py` の旧参照（Phase0 v002 / registry v007）を廃し、v003 / v010 を参照する v004 を追加。
- 12月7日夜の厳密可動数が閉じない部隊は点推定せず区間状態で実行する。
  - 59/75/90戦隊群: `SERVICEABLE_EVE ∈ [53,72]`
  - 64/12/60/98戦隊群: `SERVICEABLE_EVE ∈ [93,149]`
- 集中損失46機と第一補充便148機は未配賦プールのまま。OOBへ直接加減算しない。
- 推力式単排気管は開戦時 `TEST`。1941年量産標準・固定速度ボーナスを禁止し、117監査→v010 registryの時計を優先する。

## 開戦可否

史料未閉鎖値を `UNKNOWN` / 区間として保持することを条件に、1941-11-15の南方航空集中から実行可能。1941-12-07/08にPearl/Philippines/Malayaを同期させる。

未閉鎖項目は後続史料で区間を狭めるための残論点であり、開戦実行を止める blocker ではない。
