# Branch B — 中国陸軍・南京政権・重慶政権の差分因果回収 1937–1942 v001

Status: **RECOVERED CAUSAL BASELINE / CATEGORY-SPECIFIC, NO BLANKET MULTIPLIER**  
Current application clock: **1942-07-30 00:00**

## 0. 結論

以前のBranchで使われた「日本陸軍は史実より良い／南京側は史実より良い／重慶側は史実より悪い」は、三つの独立した差の合成だった。

1. **日本陸軍の装備・整備・計画の中央値が少し良い。**
2. **1937–38の局地戦でその差が時間差を作り、中国の工場・機械・技能者・車両・在庫の内遷をやや悪化させる。**
3. **その後の戦局認識・占領地行政・財政差が、南京政権の後方代替能力を上げ、重慶の軍再建/財政/輸送能力を下げる。**

戦車の砲・装甲が突然強くなったことが、直接「南京強化/重慶弱体化」を生んだわけではない。

## 1. 1937–38 戦車・車両再監査の回収値

旧`CHINA_1937_38_SYSTEMIC_ARMOR_RETRO_AUDIT`のworking first-pass:

- Japanese combat-effective AFV-days: **+8–15%** relative to same historical-quality OOB.
- 主因: mechanical dropout低下、parts/recovery改善。gun/armor unchanged.
- 日本不可逆AFV損失差: **-7～-15 hulls** working cumulative.
- 日本人員K/W/M差: **-300～-650** working.
- 中国人員K/W/M差: **+500～+1,100** working.
- 中国側追加の砲/MG/strongpoint損失: **10～25 equivalent** working.
- 日本燃料消費: **+6～12%**。
- 日本tank ammunition: **+8～15%**。

この数字自体はLOW～MEDIUM confidenceであり、戦略地図を単独で変える倍率ではない。

### 本当に重要な効果

- あるstrongpoint/道路軸が数時間早く崩れる;
- 次の線への追撃が予定通り発生する率が上がる;
- 日本側の壊れた車両/砲/トラックを回収しやすい;
- 中国側は道路/倉庫/車両を回収・破壊・移送する時間を少し失う。

これが複数戦役で累積する。

## 2. 日本陸軍が「史実より良い」の意味

### 車両・戦車
- 同じType 89/95/97等の砲・装甲を別兵器にしない。
- reliability, clutch/transmission/cooling, running gear, spare allocation, failure statistics, recoveryが改善。
- 強みはphysical hull数より **dispatchability / reappearance / recovery**。

### 砲兵
- firing tables;
- met/charge correction;
- lot/砲身摩耗管理;
- survey/registration;
- ammunition expenditure control。

### 工兵/輸送
- bridge/road repair sequencing;
- truck/tractor uptime;
- rail schedules;
- depot accounting;
- workshop throughput;
- recovery priority。

### 指揮・計画
- 前提値、輸送量、燃料・弾薬、日程、故障率を比較しやすい;
- 「この条件では成立しない」を工兵/輸送側が文書化しやすい;
- ただし精神論・政治命令を自動排除しない。

このため日本陸軍は、**同じ編制・同じ武器をより高い実用中央値で使う軍**であり、別世界の重装甲軍ではない。

## 3. 早期戦況差 → 中国の内遷損失

1937–38の中国側戦時工業は、沿海/華中の工場・機械・技術者をWuhan経由でSichuan等へ移すことで後方工業基盤を構築した。

Branch causal ruling:
- 日本の局地突破・追撃が少し早い;
- 中国軍部隊崩壊/後退の時計が一部早まる;
- 疎開命令、解体、積出、鉄道/船舶積替えの余裕が減る;
- 軍用輸送との競合が強まる;
- 工場本体だけでなく、機械、工具、予備品、発電機、車両、熟練工、技術官僚の一部が取り残される/分散する。

重要: 日本軍が意図的に「工場疎開要員を狙う」設定ではない。**時間窓の短縮による二次効果**。

旧legacy文書は「重慶基準で数割弱い」という粗い表現を置いていたが、現行ではその一律倍率を採用しない。

現行はカテゴリ別:
- industrial machinery/repair depth: worse;
- skilled-worker retention: worse;
- truck/transport equipment: worse;
- ammunition/heavy-weapon replacement: worse;
- fiscal/tax/credit resilience: worse;
- long-distance operational mobility: worse;
- raw manpower/geographic retreat space: broadly still large。

## 4. 重慶側が「史実より悪い」因果

### 4.1 産業・修理
初期内遷で取りこぼした設備・技能者が、後年まで累積する。

結果:
- 部隊が生き残っても装備再建に時間;
- 砲/車両/無線/機関の修理capacityが薄い;
- depot stockが不足しやすい;
- 抽象的な「師団数」より sustained effective divisions が減る方向。

### 4.2 財政・通貨
史実でも重慶政府は戦費赤字・インフレ・輸送不足に苦しむ。
Branchでは:
- 占領地の税源/人口/産業基盤をより早く/確実に失う;
- 内遷工業の実力がやや薄い;
- 部隊再建・長距離輸送コストが上がる;
- 法幣での兵士給与・食料調達・地方輸送協力を維持しにくい。

### 4.3 軍
弱体化の主対象:
- equipped effective division count;
- heavy artillery/ammunition;
- vehicles;
- aviation;
- communications;
- workshop/repair;
- long-distance concentration。

弱体化させないもの:
- 中国全土の人的プールを一律倍率で削らない;
- 地理的撤退余地は残る;
- 地方軍閥/共産軍/地域政治は残る;
- 政権が軍事劣勢だけで自動崩壊しない。

## 5. 南京側が「史実より良い」の意味

ここでいう「南京」は主に **南京国民政府/占領地域の行政・治安・物流代替機能**。

「南京軍が日本師団並みに強い」という意味ではない。

### 5.1 物理的な土台
- 日本軍の車両・工兵・鉄道運用が少し安定;
- 占領主要鉄道/倉庫/都市の稼働を維持しやすい;
- 日本正規軍の局地損耗/機械的消耗が史実より若干軽い;
- 現行BranchではGuadalcanal/New Guinea緊急転用鎖がなく、1942後半に中国から第6・第41・第51等を急いで南東へ抜く圧力が弱い。

### 5.2 政治・信用のramp
南京側改善は1944数字を1942へteleportしない。

入力:
- 日本がMI/FSで史実より強い戦局認識を与える;
- 日本占領域が持続する;
- 重慶のインフレ・支払/調達問題が悪化;
- 将来Five-Goが成功すれば西方安全神話がさらに崩れる。

その結果として徐々に:
- local police/security reliability;
- rail/warehouse staff retention;
- labor/cart/animal mobilization;
- food/fodder/tax procurement;
- Nanjing-linked payment/contract acceptance;
- sabotage reporting;
が改善する。

政治カテゴリは混在する:
- sincere collaborators;
- opportunistic hedgers;
- coerced compliance;
- hostile but passive;
- active Chongqing/CCP networks。

### 5.3 日本軍への実効配当
最も価値があるのは**静的任務代替**。

- city/rail/warehouse guard;
- local police;
- anti-guerrilla/local sweep;
- tax/fodder collection;
- secondary road/bridge protection。

日本軍はstrategic nodeにcadre/rapid-response nucleusを残す。
南京軍に独立した重火器突破戦・大規模機動予備を任せない。

後年旧枝の1944 working snapshotが示した「日本静的任務3–3.8 division-equivalent release」は、こうしたrampが十分進んだ場合の**downstream validation**であり、1942の現在値ではない。

## 6. 「南京良化」と「重慶悪化」は同じものではない

両者をゼロサム倍率にしない。

南京側の改善:
- 占領地を使う行政コスト低下;
- 日本正規軍の静的拘束低下;
- local logistics/credit/security改善。

重慶側の悪化:
- 工場/技能者/輸送設備の内遷不足;
- fiscal/monetary strain;
- heavy weapon/vehicle/repair不足;
- long-range concentration能力低下。

中国の全人口や全ての地方社会が南京へ転向するわけではない。

## 7. Five-Goとの接続

この差分がFive-Goで効く場所:

### 日本側
- rear securityに必要なregular workloadが少し軽い;
- rail/warehouse/food procurementがやや安定;
- 同じ師団/砲/車両の実働日数が増える;
- damage→repair returnが多い;
- 五号用の29–31万人級集中を中国正面内部で成立させやすい。

### 中国側
- 大部隊を集めても砲・車両・通信・弾薬の同期が弱い;
- retreatした師団が「6,000人残ったから即6,000 effective」に戻らない;
- 西安/宝鶏/漢中のstock/node喪失が、その後のreconstitutionへ長く効く;
- Humpは高価値物資を補えるが、bulk transport/food/road/whole-army repairを即代替しない。

## 8. Current 1942-07-30 ruling

現時点で確定してよいのは方向と因果:

**Japanese Army:** modestly better practical readiness, recovery, planning and combined-arms synchronization.  
**Nanjing/occupied rear:** gradually more usable and politically credible than historical, especially if Japan keeps winning.  
**Chongqing/National Government:** less industrial/transport/repair/fiscal depth than historical, but still large, resilient and politically alive.

まだ閉じないもの:
- 1942 Nanjing軍 exact headcount / trustworthy pool;
- 中国軍 national effective division count;
- exact factory/tonnage evacuation delta;
- exact inflation percentage delta;
- Five-Go launch tank OOB;
- political surrender probability。

これらはFive-Go exact OOB/China mirrorを作る時に個別に閉じる。
