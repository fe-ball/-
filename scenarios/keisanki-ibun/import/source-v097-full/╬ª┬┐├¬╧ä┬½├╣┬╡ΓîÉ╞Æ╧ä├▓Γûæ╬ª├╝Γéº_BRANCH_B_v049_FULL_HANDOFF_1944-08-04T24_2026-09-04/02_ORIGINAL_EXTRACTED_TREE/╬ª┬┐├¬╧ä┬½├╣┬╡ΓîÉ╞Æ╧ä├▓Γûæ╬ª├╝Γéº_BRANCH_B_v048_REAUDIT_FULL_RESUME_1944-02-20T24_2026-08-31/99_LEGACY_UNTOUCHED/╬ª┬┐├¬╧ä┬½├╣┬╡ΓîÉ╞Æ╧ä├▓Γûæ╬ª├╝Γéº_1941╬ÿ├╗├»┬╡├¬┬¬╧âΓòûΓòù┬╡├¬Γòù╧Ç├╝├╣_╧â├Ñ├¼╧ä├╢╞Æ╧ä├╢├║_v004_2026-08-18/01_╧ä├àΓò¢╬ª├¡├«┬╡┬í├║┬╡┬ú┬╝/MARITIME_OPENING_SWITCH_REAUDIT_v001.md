# 海上戦・潜水艦 後続スイッチ再監査 v0.01

## 1. 開戦から遡及するMETHOD

- 個艦 `Hull → Availability → Mission`。
- 損傷は「沈没/無傷」の二値ではなく任務機能別。
- 潜水艦は撃沈数だけでなく、出撃成立、戦域到着、哨戒日数、接触、射点変換、再捕捉、再攻撃、情報価値、敵拘束を追跡。
- 水雷戦の第二斉射は、再装填時間だけでなく再捕捉・射点形成が戦闘時計内に成立した場合だけ発生。
- 修理時計・乗員経験・弾薬燃料・次回可動時刻を後続作戦へ継承。

これらは「後年になって発明された能力」ではなく、研究評価方法の不足なので1941年開戦へ遡及適用する。

## 2. 開戦時から存在するが、量・効果を固定しない能力

### 潜水艦任務集合

第6艦隊の開戦命令には、ハワイ/米西岸偵察、敵艦奇襲、海上交通破壊が併存する。

よって `FLEET_INTERCEPT` と `COMMERCE_RAID` を排他的な文明特性のように扱わない。時期・戦域ごとの配当で決める。

### 艦隊・通商用情報

潜水艦の接触報告は、それ自身の撃沈がゼロでも後続艦隊・航空作戦へ価値を持ち得る。通信遅延、位置誤差、敵の変針を含めて別記帳。

## 3. カレンダー固定を解除する後続スイッチ

- Guadalcanal型潜水艦輸送拘束。
- 潜高第3ロット。
- 戦時型駆逐艦量産開始。
- 専用護衛艦優先。
- 局地ASW統合、全国ASW統合。
- 空母追加建造・緊急改装。
- 伊勢日向/千歳千代田/信濃/伊吹等の最終転用判断。
- 1942年以後の潜水艦戦域再配置。
- 遣独潜水艦の航海結果。

必要性・造船余力・敵脅威・観測戦果から再決定する。

## 4. 保持するHARD/PIPELINE

- 開戦前に既に進行した艦艇建造・改装工程。
- 潜高の第一・第二艇で既に消費済みの船台/設計資源（ただし開戦戦力には未就役）。
- 戦前に凍結済みの技術設計・研究時計。
- 戦時標準船Iの設計凍結・生産移行工程。

ただし完成数・配備先・後続ロットは戦況出力。

## 5. 直近の開戦再走査で見る指標

### 潜水艦

- available boats by theater
- boats actually on station
- patrol-days
- contact-days
- firing opportunities
- successful firing-position conversions
- reacquisition
- enemy ASW/search effort induced
- reconnaissance reports delivered in time
- convoy/warship route changes
- return and repair clocks

### 水上艦

- availability by task
- escort requirement and destroyer bind
- damage-function state
- fuel/ammunition/torpedo state
- repair and forward-base support
- transport/landing throughput supported
- enemy force fixed/diverted

## 6. 重要な禁止事項

- 名目在籍艦数をそのまま戦域戦力にしない。
- 後年の戦果から逆算して配備を決めない。
- 性能向上を一律撃沈率倍率にしない。
- 「史実で通商破壊が少なかった」ことを開戦時の選択肢不在へ変換しない。
- 生残艦が増えても、同一艦を同日複数戦域へ配置しない。
