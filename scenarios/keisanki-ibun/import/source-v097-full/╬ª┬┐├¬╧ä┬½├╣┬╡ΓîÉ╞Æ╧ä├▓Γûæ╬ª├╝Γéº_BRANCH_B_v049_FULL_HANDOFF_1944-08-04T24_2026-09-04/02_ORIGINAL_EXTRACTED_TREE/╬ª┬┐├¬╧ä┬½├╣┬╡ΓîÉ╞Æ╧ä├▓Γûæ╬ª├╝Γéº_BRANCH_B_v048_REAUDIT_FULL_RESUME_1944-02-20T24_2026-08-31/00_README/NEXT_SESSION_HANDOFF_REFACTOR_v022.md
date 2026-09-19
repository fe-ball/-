# 次回引継ぎ — refactor v022

## CURRENT
- 同期時刻: **1943-09-30T24 / 1943-10-01T00:00**
- モード: `GLOBAL_1943_AUTUMN_SYNCHRONIZED_ADVANCE`
- 直前まで: Aleutians/Attu/Kiska → June Efate → Five-Go Phase II → Jul-Sep India/Burma coastal-operation study → Europe/Eastern Front Q3 resync を閉じた。
- India/Burma沿岸打通案: `ADVANCED_OPERATIONAL_STUDY / PREPARATION_AUTHORIZED`、**まだGOではない**。

## 最初に読む
1. `06_RUNTIME/CURRENT_BRANCH_STATE_v004.json`
2. `06_RUNTIME/SESSION_2026-08-26_1943Q3_SYNCHRONIZED_HANDOFF_v001.md`
3. `06_RUNTIME/INDIAN_OCEAN_BURMA_COASTAL_OPERATION_STUDY_1943-06_09_v001.md`
4. `06_RUNTIME/JAPAN_AMPHIBIOUS_NAVAL_WALLET_1943-07_09_v001.json`
5. `06_RUNTIME/GLOBAL_1943Q3_SYNCHRONIZATION_LEDGER_v001.md`
6. `06_RUNTIME/EFATE_LIMITED_NEUTRALIZATION_1943-06_SETTLEMENT_v001.md`
7. `06_RUNTIME/ALEUTIANS_ATTU_KISKA_REAUDIT_1943-03_07_SETTLEMENT_v001.md`

## 次の処理順
1. 1943年10月のPacific米新空母群の実際の圧力・作戦方向を枝地理から裁定。史実Marcus/Gilbertsを自動コピーしない。
2. 日本第一線空母4隻をPacific fleet-in-beingとしてどこまで拘束するか更新。
3. Mountbatten/SEACの現地実体化と、英国がIndia防御・Assam/Hump・Arakanへどの程度資源を回せるかを能力ベースで更新。
4. India沿岸打通案について、Bengal陸上航空の集中速度、Naf/Teknaf/Cox's敵前最終区間、Akyab/Port Blair基地航空、特殊揚陸船/大発/海防艦の実配備可能量を詰める。
5. 陸軍側は五号第二期後の工兵・自動車・航空燃料・参謀余力を更新し、India案の実施時期を10月末～11月前半候補としてGate判定。
6. Bose/INAは一般蜂起を0として計画。確認済み連絡網・英印軍離反工作・情報協力だけを算入。
7. Eastern Fleetは「弱いから必ず来る」としない。上陸救援のためBayへ出た場合のみ別紙機会計画で捕捉撃滅を狙う。
8. 英国が低確率で無理な反攻を先打ちする可能性はbranchとして残すが、中央線に固定しない。発生なら防御配置・船腹・航空集中から因果を引く。

## India案の現在Gate
- 第一波上陸能力: GREEN寄り
- 初期艦砲支援: GREEN
- Cox's継続LOC: AMBER（敵前最終区間込みの中央150–220t/day）
- Bengal陸上航空: AMBER、最大の局地リスク
- Eastern Fleet即応: 現時点GREEN寄り（日本側に有利）だが時間経過で悪化
- INA/国内協力: AMBER-LOW～AMBER。大蜂起は不算入
- Pacific: RED寄りAMBER。第一線正規空母西送は中央NO

## 重要な方法論
- hard fact / branch assumption / working estimate / realized central outcomeを混ぜない。
- 最頻値を常に選ぶ決定論にしない。接触、天候、認知、反応は分布から実現を引く。
- substitute lossesと敵adaptationを必ず引く。
- 海軍「両取り」は主目的ではない。陸軍上陸・LOCが英艦隊不出撃でも成立することが先。Eastern Fleet撃滅は出てきた場合の追加収益。
- 空中投下補給は小粒の野戦保険。主LOCの成立判定に足さない。
