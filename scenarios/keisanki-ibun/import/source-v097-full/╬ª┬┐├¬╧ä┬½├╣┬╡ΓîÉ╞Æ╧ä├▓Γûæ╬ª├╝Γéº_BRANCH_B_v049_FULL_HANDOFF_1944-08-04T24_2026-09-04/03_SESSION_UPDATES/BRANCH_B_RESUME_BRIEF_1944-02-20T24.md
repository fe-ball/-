# 計算機異聞 Branch B — 再開ブリーフ

## 1. 正規再開点

- semantic base: **Branch B v048**
- authoritative working frontier: **1944-02-20T24**
- 正規ロード基準: `97_CONTINUATION_MASTER_2026-08-31/MANIFEST/MASTER_LOAD_ORDER_v002.json`
- 旧 `97_CONTINUATION_MASTER_2026-08-30` の 1944-06-15T24 継続は、来歴・参照用に保存されているが **現行結果ではない**。
- 1944-02-20以後の太平洋戦域結果は、現在の因果系列から再計算する。

## 2. モデリング契約の要点

1. Branch B の利得は、前提から自然に累積するなら大きくなってよい。史実に近づけるための人工的な弱体化は行わない。
2. ただし輸送、熟練要員、航続距離、天候、幾何、発着艦サイクル、揚陸処理量、修理能力、通信帯域、弾薬、燃料、意思決定時間などの実在ボトルネックで飽和させる。
3. 未来知識は禁止。観測→認識→説明→決心→命令→実行を分離する。
4. 米軍も日本軍も適応的に行動する。史実行動は参照であって脚本ではない。
5. 必ず分離する勘定:
   - physical / serviceable / mission-ready / committed
   - production / delivery / conversion / frontline-ready / local allocation
   - hull / air group / deck readiness / mission assignment
   - repair/recovery / new production
   - cue / contact / track / weapon-quality fix
   - runway aviation / water aviation
   - direct loss / campaign-out / short repair / recoverable damage
6. fortification はコンクリートだけでなく、基地持続性、sensor/C2、water-air reconnaissance まで含む基地防御システム。
7. 車両の信頼性向上は稼働率・回収・再出現を改善するが、未追跡の車両や戦車を生成しない。
8. 1942-43に成熟parametron計算機を逆投影しない。1944年にType 3 full-logic parametron。
9. 上流の閾値が変わったら、依存する下流イベントは再開する。

## 3. ここまでの再監査で固定された主要結果

- GALVANIC/Tarawaは再走済み。Tarawa組織抵抗崩壊は1943-11-28夕夜、secureは11-29朝。
- Soryuは11-26の損傷が軽く再評価され、1943年12月中旬を中心に第一線復帰。ただし熟練空母航空兵の損耗債務は残る。
- FLINTLOCKでは日本の第一線空母4隻（Shokaku, Zuikaku, Hiryu, Soryu）が戦略的に生存。
- FLINTLOCK D-Dayは1944-02-06、Kwajalein secureは02-09、closeoutは02-10。
- CATCHPOLEには専用の **106 amtracs + 17 amphibian tanks** が存在し、FLINTLOCKのLVTを借りない。
- HAILSTONE主力は **5 CV + 3 CVL**。
- Eniwetokに現地運用レーダーは、輸送traceなしには存在させない。

## 4. Truk / HAILSTONE — 1944-02-20T24

### 米軍
- 主力空母: Wasp, Yorktown, Essex, Intrepid, Bunker Hill + Belleau Wood, Monterey, Cowpens
- **5 CV + 3 CVL**
- raid opening ready aircraft: **445-485、center 465**
- 高速戦艦・巡洋艦の大半は空母スクリーンに残留。価値ある脱出水上目標がない限り史実型leaker-huntは自動発生しない。

### 日本側 Day 1
- strategic surprise: none
- operational surprise: low
- tactical surprise: partial
- 夜明けCAP airborne: **20-24**
- 5分即応: **14-18**
- 10-15分即応: **12-16**
- usable warning: **15-22分**
- 米軍初動F6F sweep: **68-72、center 70**

### 20 Feb 日没時
- 日本 irrecoverable aircraft: **40-50、center 45**
- 米国 irrecoverable aircraft: **24-31、center 27**
- 日本 repairable damaged: **17-25**
- 米国 repairable damaged: **26-38**
- 日本 serviceable fighters: **16-22**
- 日本 attack/recon/water-air night-capable: **13-19**
- immediately relaunchable fighters: **8-12**
- warning/plot throughput: **dawnの50-65%**
- precision AA: 1 channel reliable center、第二はintermittent/local
- airfield: 全主要滑走路がcratered/cycle-limitedだが、少なくとも1本は修理後に小規模緊急発進可能
- communications/power: 局地停止あり。ただし冗長系とalternate powerでlow-bandwidth C2は残存

### 海上・潜水艦
- 高価値移動目標は優先退避。第一線空母、Akashi、主要oiler/tenderを史実HAILSTONEの大量在泊状態に戻さない。
- lagoon day1 merchant/auxiliary loss: **3-5 hulls / 14,000-26,000 GRT**
- 日本潜水艦: TF58近傍 useful nodes **2-4**。昼間に満足な雷撃解なし中心。

### 次の夜間反撃gate
- status: **OPEN**
- available Japanese package: **13-19 aircraft**
- cue: **1-3時間古い submarine / RI/DF / water-air の sector picture**
- exact carrier fixではない
- 米軍は日中戦闘の損害を受け警戒度が高い。fast battleshipsもTF58集中。

## 5. Eniwetok / CATCHPOLE — 1944-02-20T24

### 米軍
- assault personnel: 22nd Marines + 1st/3rd Battalions 106th Infantryほか、約 **8,000-10,000**
- amtracs: **106 physical / center 103 ready**
- amphibian tanks: **17 physical / center 17 ready**
- air: Princeton, Langley + Sangamon, Suwannee, Chenango
- ready aircraft: **145-175**
- fire support: Pennsylvania, Colorado, Tennessee; Indianapolis, Portland, Louisville; destroyers約15相当

### 日本軍
- garrison physical: **3,380-3,540**
- Engebi: **1,240-1,320**
- Eniwetok Island: **790-840**
- Parry: **1,330-1,390**
- Type 95: **9 physical / center 9 serviceable、各主要島3両**
- local radar: **0**
- warning: visual + radio/DF + small air/water recon + external Truk/Ponape/submarine reports
- 20 Feb dusk local air serviceable: **3-5**

### 防御・接近
- 弾薬・水・衛生品の小分散、代替指揮所、runner、戦車のlocal mobile reserve化、再登録射撃、camouflage/decoy/fallbackを実施。
- 深い洞窟・地下要塞網は生成しない。
- passage minefieldにより **2.5-4.0時間** のschedule marginを消費。
- outer artillery isletsは確保され、Engebiへの射撃登録開始。
- **21 Feb Engebi assaultは維持**。

### 20/21 Feb night gate
- Japanese air package possible: **3-5**
- Japanese submarine useful approach nodes: **2-3**
- status: **OPEN**

## 6. 正規の次シミュレーション順序

1. **Truk 20/21 Feb夜間航空反撃**: cue chain、launch decision、route、radar/night-fighter interception、weapon-quality fix、recoveryを別々に判定。
2. 同時間帯の **日本潜水艦 vs TF58 / ASW** を処理。帳尻合わせの命中は禁止。
3. repair parties + night damageを反映して **21 Feb dawn Truk fixed-system state** を再計算。
4. その状態を見て **HAILSTONE Day 2 tasking** を決める。史実コピーは禁止。
5. 並行して **Eniwetok 20/21 night local air/submarine interference** を解く。
6. **21 Feb Engebi assault** を、実際の火力準備、mine/passage delay、106+17 vehicle wallet、3両のType 95、short-warning defenseから実行。
7. Engebi終了後にcapture intelligenceを使い、Eniwetok Island / Parryの順序と日程を決める。

## 7. 現時点で再オープンしないもの

新しい上流事実がない限り、以下は固定:
- FLINTLOCK result
- CATCHPOLE専用106 amtrac + 17 amphibian-tank wallet
- HAILSTONE 5 CV + 3 CVL main-force split
- 日本第一線空母4隻は生存するがTrukへcounter-sortieしない

## 8. 旧データの扱い

- 旧 1944-06-15 frontier と暫定Marianas 16-21 June packageは **quarantined downstream**。
- OOB、doctrine、事故史、感度試験として参照可能。
- ただし現行Pacific resultとしてロードしない。
- Europe/China/Indian Oceanなど無関係な戦域事実は無意味に削除しないが、1944-02-20時点の意思決定に未来状態を持ち込まない。

## 9. 議論再開時の最初の論点

最初に扱うべきなのは、Truk夜間反撃の「13-19機が存在する」ことではなく、
**sector cueから実際に何機をlaunchでき、何機がTF58に接触し、何機がweapon-quality fixを得るか** である。

したがって次の議論は、
- cue age / bearing uncertainty
- usable runway and launch throughput
- aircraft mix and night competence
- route geometry and moon/weather
- US radar/CAP/NF/AA posture
- target acquisition probability
- attack coordination and recovery losses
を順に閉じるのが妥当。
