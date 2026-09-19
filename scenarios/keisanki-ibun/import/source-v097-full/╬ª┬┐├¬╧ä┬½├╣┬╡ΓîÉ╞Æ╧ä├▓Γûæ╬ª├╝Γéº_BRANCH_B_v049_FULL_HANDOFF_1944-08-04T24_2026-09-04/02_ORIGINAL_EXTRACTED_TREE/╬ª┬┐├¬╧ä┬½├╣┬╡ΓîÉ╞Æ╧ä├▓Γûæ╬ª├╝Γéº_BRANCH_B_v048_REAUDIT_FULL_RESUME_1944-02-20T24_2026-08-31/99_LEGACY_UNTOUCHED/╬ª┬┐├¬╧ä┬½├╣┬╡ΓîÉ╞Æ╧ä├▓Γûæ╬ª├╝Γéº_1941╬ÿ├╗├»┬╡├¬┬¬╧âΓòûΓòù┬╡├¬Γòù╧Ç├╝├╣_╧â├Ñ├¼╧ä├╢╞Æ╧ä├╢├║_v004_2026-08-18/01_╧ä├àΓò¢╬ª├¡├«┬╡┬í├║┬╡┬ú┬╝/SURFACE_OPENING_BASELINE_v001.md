# 水上艦 開戦再走査基準 v0.01

## 0. 目的

開戦時の日本水上艦を「艦級の性能倍率」ではなく、実際の任務可能性へ戻す。

`Hull → Availability → Mission set → Coordination → Situation → Damage state → Repair/next mission`

を1941年12月から適用する。

## 1. 開戦前から保持する物理差

現行10/11/30/31で1934～41年に成立済みとされたものは、戦史巻き戻しで消さない。

- 友鶴・第四艦隊事件後の重量/復原性/強度監査。
- 朝潮型以後の設計・標準化・公試残差の戻し。
- 金剛型等の改装で得た実用速力、燃費、故障・整備の再現性。
- 最上型等の重量・射撃I/Oの成熟差。
- 九三式魚雷・射撃指揮・再装填の物理時計。
- 大和で設計時に準備済みの電力/配線/将来改装余地。

ただし、後年艦の改善を開戦艦へ逆流させない。

## 2. 開戦後の出力として再計算するもの

- 各艦の戦闘損傷・沈没・修理。
- 生残艦の再配置。
- 空母・戦艦・巡洋艦・駆逐艦の任務配分。
- 駆逐艦を艦隊戦/護衛/輸送/局地任務のどこへ割くか。
- 1942～43年の建造・改装優先。
- 戦時型駆逐艦/専用護衛艦需要。
- 空母追加建造・緊急改装。
- 生残旧艦の `現役 / 小改装 / 任務転換 / 予備 / 練習試験 / 除籍`。

## 3. 解除する旧「安全な史線」

61/62の後期追加では、旧85～89で再走査した1942～43年結果を保持し、1944年6月10日までを安全な継続点としていた。

今回の巻き戻しではこの前提を解除する。

理由：

- 潜水艦の開戦配置と任務価値を再評価する。
- 航空の生残者・練度・基地機動を開戦前集中から追う。
- 水上艦のAvailabilityと任務配分を開戦から追う。
- これらがMO/MI/Guadalcanal相当の発生・損耗・必要建造を変え得る。

したがって、1942年夏以後の「Guadalcanal型大量損耗なし」を入力にしない。結果としてそうなった場合だけ再び成立する。

## 4. 開戦時の大分類

### Main Body / First Fleet

戦艦群は、存在するだけで南方上陸作戦へ自動投入しない。高速/低速、燃費、基地、敵主力の位置、抑止任務を分ける。

### Second Fleet / Southern support

重巡・水雷戦隊は南方攻略で直接使われるため、個艦燃料・魚雷・損傷・夜戦後の再出撃時計を継承する。

### Third Fleet

フィリピン攻略部隊。潜水戦隊、巡洋艦、駆逐隊、基地部隊と同一時計で扱う。

### Fourth Fleet

Wake/Guam/南洋方面。第一回Wake失敗のような局地結果が、増援潜水艦・追加空母/艦艇の配当を変える。

### First Air Fleet escorting surface force

空母そのものと艦載機を分離し、母艦Hull、航空隊、護衛駆逐艦を別stateとして持つ。

## 5. 最初の戦役で取る状態

Pearl/Malaya/Philippines/DEIで各艦について：

- actual location
- mechanical availability
- fuel/endurance margin
- ammunition/torpedo state
- crew fatigue
- mission assignment
- sortie/escort days
- enemy contact
- damage/function state
- repair location and duration
- next mission ready date

これが後のMO/MIへ直接渡る。

## 6. 後続判断の再発火条件

### 戦時型駆逐艦

`DD losses + escort burden + convoy loss + fleet-screen requirement + shipyard capacity` が閾値を越えた時。

### 専用護衛艦

`submarine pressure + shipping value at risk + fleet DD opportunity cost + ASW sensor/weapon maturity`。

### 空母追加/改装

`carrier hull losses + surviving air groups + pilot pipeline + deck demand + shipyard opportunity cost`。

### 旧式艦転用

`surviving hull life + mission gap + conversion duration + dock/equipment/crew opportunity cost`。

カレンダー日付だけでは発火しない。
