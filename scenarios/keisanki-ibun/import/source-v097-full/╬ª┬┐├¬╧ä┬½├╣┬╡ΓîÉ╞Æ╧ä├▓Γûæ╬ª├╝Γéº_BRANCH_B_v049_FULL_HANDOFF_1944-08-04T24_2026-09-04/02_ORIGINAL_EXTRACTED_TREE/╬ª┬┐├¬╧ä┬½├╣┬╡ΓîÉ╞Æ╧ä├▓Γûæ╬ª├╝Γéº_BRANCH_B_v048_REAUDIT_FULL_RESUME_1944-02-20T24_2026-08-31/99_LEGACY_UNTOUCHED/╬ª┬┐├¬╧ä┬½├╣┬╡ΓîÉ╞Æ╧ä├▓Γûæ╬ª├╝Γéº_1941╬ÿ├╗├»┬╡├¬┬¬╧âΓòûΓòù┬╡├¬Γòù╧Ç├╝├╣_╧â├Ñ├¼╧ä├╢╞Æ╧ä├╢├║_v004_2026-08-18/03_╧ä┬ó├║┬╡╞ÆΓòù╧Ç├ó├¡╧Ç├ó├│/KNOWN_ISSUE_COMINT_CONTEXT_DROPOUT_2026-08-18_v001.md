# KNOWN ISSUE — COMINT CONTEXT DROPOUT 2026-08-18

Severity: HIGH
Status: IDENTIFIED / CONTAINED / INDEX-LEVEL REMEDIATION PENDING

## 症状

会話圧縮サマリーに高等暗号条件が残らず、史実の米側JN-25 COMINTがシミュレーションへ再流入した。

## 原因

原本欠落ではなく、実行時コンテキストの不完全な縮約。

## 影響範囲

主として1942年3月後半以降のMO情報戦・空母配置判断。物理戦闘結果は情報依存性を個別判定して保持／再計算する。

## 恒久対策案

次回、シナリオ全体の改変項目を機械可読な execution index に束ね、戦闘前に関連switchを自動列挙する方式を議論する。

## ゲート

`1942-05-07` より先へ進む前に、少なくとも航空機・艦艇純性能、基地、暗号、偵察、航空人事、戦術時計の関連設定を再ロードする。
