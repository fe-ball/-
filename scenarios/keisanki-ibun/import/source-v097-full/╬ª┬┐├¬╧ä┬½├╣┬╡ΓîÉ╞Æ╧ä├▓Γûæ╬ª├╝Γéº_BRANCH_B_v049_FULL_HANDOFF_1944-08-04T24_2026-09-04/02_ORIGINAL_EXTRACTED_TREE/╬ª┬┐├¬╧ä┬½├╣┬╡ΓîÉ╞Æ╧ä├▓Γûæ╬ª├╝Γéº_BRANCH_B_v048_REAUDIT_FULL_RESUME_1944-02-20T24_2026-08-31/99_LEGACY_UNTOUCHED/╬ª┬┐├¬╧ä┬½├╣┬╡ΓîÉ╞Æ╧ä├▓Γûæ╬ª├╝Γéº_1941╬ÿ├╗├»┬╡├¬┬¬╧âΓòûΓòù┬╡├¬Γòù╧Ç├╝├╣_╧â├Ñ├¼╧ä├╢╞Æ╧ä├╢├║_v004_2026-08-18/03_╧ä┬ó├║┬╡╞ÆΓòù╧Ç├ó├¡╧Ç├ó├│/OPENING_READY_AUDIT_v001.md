# 開戦実行可能化 監査メモ v0.01

## 判定

`OPENING_GATE = PASS` を得ることを機械条件とする。

## blockerとして処理したもの

- 正本machine-readableファイルが表層正本フォルダに無く、原アーカイブ内にしか存在しなかった問題: 本パッケージで同一正本ディレクトリへ展開。
- `opening_state_validator_v003.py` が存在しない `prewar_concentration_accounting_v001.json`、旧 `MALAYA_PHASE0_OPENING_PACKET_v002.json`、旧 `switch_registry_v007.json` を参照する問題: 会計JSONを既存値から復元し、v004 validatorへ更新。
- 推力式単排気管の旧時計が51に残る問題: 開戦入力では117系監査を優先し `TEST` 固定。1941量産標準化と固定性能加算は禁止。

## 開戦を止めない残論点

46機損失内訳、148機補充配賦、各戦隊の厳密serviceability、搭乗員経験核実数、12th/10th Air Brigadeの一部OOBは未閉鎖。ただし既知出撃下限と名目上限の区間状態で矛盾なく前進できる。

この処理では、史料に存在しない中心値・生存数・補充配賦を新規に作っていない。
