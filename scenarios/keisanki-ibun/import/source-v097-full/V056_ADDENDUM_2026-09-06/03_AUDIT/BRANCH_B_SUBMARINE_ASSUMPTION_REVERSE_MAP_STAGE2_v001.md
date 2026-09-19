# BRANCH B 潜水艦前提逆引き監査 Stage 2
revision: 2026-09-06-v001
status: audit-only / no numerical correction yet
base: v055 + post-v055 conversation through provisional New Caledonia close
prerequisite: `BRANCH_B_SUBMARINE_CURRENT_STATE_AUDIT_STAGE1_v002.md`

# 0. 目的

このStage 2では潜水艦性能を再評価しない。

行うのは逆向き監査だけである。

> **既に置かれている戦果・配置・敵拘束・戦略判断**
> → **何隻が使えるという前提か**
> → **どの工程の潜水艦改善を食っているか**
> → **現在の権威状態は何か**

を露出させる。

最終的な戦果倍率に上限は置かない。
Stage 3で工程別データを叩き、Stage 4で戦史を再計算する。

---

# 1. 依存タグ

- `AVAIL`：保有→修理/訓練→出撃可能
- `SORTIE`：出撃成立、故障・早期帰投
- `NAV`：航法、哨戒線到着、配置時刻
- `STATION`：on-station艦日、燃料、交代
- `ISR`：索敵、目視/聴音、接触、報告、再配置
- `SHOT`：射点変換、TDC/諸元、発射
- `TORP`：魚雷直進/深度/信管/始動
- `REACQ`：攻撃後再捕捉、第二攻撃
- `SURV`：ASW離脱、生還、次回出撃
- `DOCTRINE`：通商/艦隊/偵察/補給等の任務配分
- `COMSEC`：通信秘匿、敵SIGINT/DFとの相互作用
- `J-ASW`：日本側護衛・対潜改善が米/英潜へ与える逆方向効果
- `GEOMETRY`：Branch戦況そのものによる航路・接触条件。潜水艦性能差ではない。

---

# 2. 既存結果の逆引き

| ID | 時期/事象 | 現在置かれている結果 | 主依存 | 権威状態 | Stage 4扱い |
|---|---|---|---|---|---|
| S2-01 | 開戦～MI前 日本潜 | 旧85：追加大型商船/タンカー+1中心、0～3、約8,000GRT中心 | SHOT/TORP/SORTIE | **LEGACY**。Q2再決算で再掲なし | 再計算 |
| S2-02 | Saratoga 1942-01被雷 | I-6による史実被雷・長期修理を旧線で維持 | GEOMETRY/史実基準 | **イベント基準として存在**。Branch改善戦果ではない | 個艦時計と新Q2空母線に整合確認 |
| S2-03 | MI日本潜水艦配備 | Q2現行：約19隻級を中央太平洋 | AVAIL/DOCTRINE | **CURRENT Q2** | 個艦availabilityで再構築 |
| S2-04 | MI哨戒線時刻 | 一週間級早い前方線。ただし「性能で早くなる」のではなくAL分離・敵空母撃滅優先の作戦設計 | DOCTRINE/GEOMETRY、NAVは補助 | **CURRENT Q2** | 原則KEEP、個艦到着時計を再検算 |
| S2-05 | MI空母戦で日本潜が米空母撃沈 | 現行Q2では主役にせず直接大型艦戦果を付与していない | — | **CURRENT negative result** | 重複加算禁止 |
| S2-06 | 山本主力前進 | 「潜水艦偶発損失リスク低下」を小さな補助因 | J-ASW/COMSEC | **CURRENT Q2だが弱依存** | J-ASW/COMSEC再検証後に補助因の大きさだけ確認 |
| S2-07 | Midway占領後 米潜阻止 | Q2：夏の局地船腹/護衛負担+15～25%、3か月で輸送/補助艦1～3隻＋損傷数隻暫定 | 米AVAIL/SHOT/TORP + J-ASW + GEOMETRY | **CURRENT PROVISIONAL Q2** | 米潜性能・Mark14・日本ASWで再裁定 |
| S2-08 | 旧MI攻略船団への即時米潜攻撃 | 旧85：有力接触3～5、発射2～4、有効命中1～2、1隻全損/揚陸不能中心 | 米ISR/SHOT/TORP/J-ASW | **LEGACY**。Q2再決算で同じ形を再掲せず | 再計算、旧値を入力にしない |
| S2-09 | Hawaii外周 | 旧23：Midway前進支援でon-station艦日+15～25% | STATION/NAV/SORTIE/基地支援 | **LEGACY/REOPENED** | Midway基地能力＋艇型別燃料/補給でfresh計算 |
| S2-10 | Sydney特殊潜航艇 | 1942年史実イベント自体は存在するが、現行Branchで成功率/損害差を独立監査していない | 母潜NAV/ISR、甲標的固有性能、豪ASW | **GAP** | Stage 4で必須 |
| S2-11 | Diego Suarez甲標的 | Ramillies/British Loyalty被雷を現行世界検討で史実同様残す方向 | 母潜NAV/発進同期、甲標的、港湾ASW | **CURRENT historical-center in RN audit**、Branch能力差未監査 | Stage 3/4で「同じ結果を維持できるか」確認 |
| S2-12 | Mozambique Channel初期作戦 | 史実の成功狩場を基礎として使用 | GEOMETRY/史実基準 | **基準事実**。Branch差は未fresh算出 | 基準戦果とBranch追加を分離 |
| S2-13 | 豪州東岸6～8月 | 旧23：追加4～6隻、2～3.5万GRT | SORTIE/NAV/STATION/SHOT/TORP/敵適応 | **LEGACY**。Q2後は再計算対象 | fresh patrol ledger |
| S2-14 | Ro-33 1942-08生残 | 旧23：PMが日本側なので史実任務/喪失geometry消滅、9月生存へ | GEOMETRY | **LEGACYだが因果は能力非依存** | 新PM/SW Pacific任務割当で再確認 |
| S2-15 | Aleutians 米潜 | 旧86：7月前半～中旬に日本DD1隻級喪失中心 | 米GEOMETRY/SHOT/TORP | **LEGACY**。Q2後のALは再計算対象 | 個艦配置から再裁定 |
| S2-16 | Addu発見 | 旧82/23：1942-06-25±10日に主要用途をほぼ確信 | NAV/STATION/ISR/通信整理＋航空偵察 | **LEGACY/REOPENED**。Q2後Indian Ocean再計算対象 | discovery processを別立て |
| S2-17 | Indian Ocean投入 | 旧23：7→12月 6/8/10/10/9/8、計51艇月、43実効艇月、約1320艦日 | AVAIL/SORTIE/STATION/DOCTRINE | **LEGACY/REOPENED** | 全個艦patrol-day再構築 |
| S2-18 | Indian Ocean直接追加戦果 | 旧23：+14～20隻、8～13万GRT。後発RN監査：Branch固有直接追加 **50～90k GRT working**、net Allied差40～80k級 | S2-17全部＋SHOT/TORP＋敵適応 | **CURRENT REOPENED BAND = 50～90k GRT**。隻数未確定 | Stage 4で最重要 |
| S2-19 | Addu情報による純増 | 旧23/82：5～7隻、3～5万GRT | ISR/NAV/STATION/DOCTRINE | **LEGACY** | Addu発見時計確定後に再計算 |
| S2-20 | Indian Ocean日本潜損失 | 旧23：0～2喪失、中心1＋1長期修理 | SURV/敵ASW/活動量 | **LEGACY** | 活動量に応じ再計算 |
| S2-21 | Indian Ocean shipping tax | 旧82：全体2～4%、危険区間6～9%→年末3～5% | 戦果＋航路迂回/船団/港待ち | **LEGACY working**。後発RN監査は%を固定せず | ship-dayモデルで再計算 |
| S2-22 | 英護衛拘束 | 旧23/82：8～12 escorts + 2～3長距離哨戒飛行隊。後発RN監査：1942H2 **5～8 escort/ASW hull-equivalents continuously** | 潜水艦接触密度＋脅威認識 | **CURRENT RN band = 5～8 hull-eq**。2～3飛行隊はOPEN | 英艦日/航空隊日で再計算 |
| S2-23 | Guadalcanal潜輸送拘束消滅 | 旧23：「史実16隻級補給任務を丸ごと消す」→他戦域へ再配置 | DOCTRINE/GEOMETRY | **RESET SWITCH**。自動入力禁止 | 実際のBranch孤立拠点/輸送需要から再トリガー |
| S2-24 | 1942末日本潜現存差 | 旧23：Ro-33等で史実比+2中心、+1～3 | SURV/GEOMETRY/再配置 | **LEGACY** | 1942全損失イベント再走査後に決める |
| S2-25 | South Pacific割当 | 旧23：9～12月10～14/月、実働7～10 | S2-23 + AVAIL/SORTIE/STATION | **LEGACYだがv050が再利用** | **authority seam**。fresh ledger必須 |
| S2-26 | South Pacific直接追加 | 旧23：+4～6隻、2.5～4万GRT、別3～5損傷 | S2-25＋SHOT/TORP | **LEGACY** | 再計算 |
| S2-27 | Santo外周線 | v050：South Pacific既存10～14/7～10を入力に、Santo戦6～8 effective boats | AVAIL/STATION/配置 | **LOCAL CURRENTだが入力seamあり** | 6～8を守らずfresh算出 |
| S2-28 | Santo撤収阻止 | v050 D+2：outer-screen/submarine contactで回避・遅延、major sinkingなし | ISR/NAV/STATION/GEOMETRY | **CURRENT EVENT** | 潜水艦配置が変われば接触確率再評価。結果0沈は先験固定しない |
| S2-29 | SantoのWasp追跡 | 旧86：潜水艦進出するが有効接触なし | ISR/GEOMETRY | **LEGACY**、v050 Santo戦に自動継承しない | 必要なら新時系列で再計算 |
| S2-30 | NC侵攻前潜水艦wallet | v050：critical period 8～11 effective | AVAIL/SORTIE/STATION/DOCTRINE | **LOCAL CURRENTだがS2-25 seam依存** | 最優先fresh ledger |
| S2-31 | NC潜水艦任務分化 | fast-BB/carrier contact、Australia–Noumea、Efate reinforcement、tanker/crippled ship、outer reporting | DOCTRINE/ISR | **CURRENT v050 concept** | 艦数再計算後も任務集合はKEEP候補 |
| S2-32 | NC連合軍情報 | 米側が日本潜水艦の配置/接触geometryをNC目標判定材料の一つに使う | 日本配置＋米ISR/COMINT | **CURRENT v050 info environment** | 艦数/線が変わればwarning confidence再計算 |
| S2-33 | 歴史的I-19 Wasp/NC geometry | v050はhistorical 9/15 I-19 geometryをコピーせず、North CarolinaをNC前にhealthyとする | GEOMETRY | **CURRENT negative/absence result** | 新しい潜水艦接触が発生しない限り史実命中を復活させない |
| S2-34 | NC本戦で日本潜が大型艦を雷撃 | 現行v050-v055戦闘結果では固定命中なし | — | **CURRENT negative result** | 能力改善を理由に後付け命中禁止 |
| S2-35 | NC撤退航路 日本潜 | post-v055会話：3～5隻散開、接触2回級、1中型輸送船に1本命中、約700～900乗船、120～220死亡/MIA級 | AVAIL/STATION/ISR/SHOT/TORP/米護衛 | **PROVISIONAL / NOT ARTIFACTED** | Stage 4で全面再裁定 |
| S2-36 | NC撤退throughput低下 | 上記接触/潜水艦脅威で大型船撤収が遅延・分散 | 脅威認識＋S2-35 | **PROVISIONAL** | ship-night/escort-nightで再計算 |
| S2-37 | Santo–NC補給線への米潜 | NC占領後、固定需要点・タンカーを米潜が狙うことを戦略上想定 | 米AVAIL/Mark14/ISR + J-ASW/COMSEC | **GAP：まだ実イベント未裁定** | 1942-11末～12月の必須監査 |
| S2-38 | 米Mark 14修正時計 | 攻撃機会増→不発/深度異常サンプル増なら前倒し可能 | 敵適応 | **OPEN SWITCH P-SS06** | 実発射/回収/報告サンプルから決定 |
| S2-39 | 日本focused convoy ASW | 第一射は消さず、再捕捉+20～35%、米潜二回目以降攻撃機会-15～30%、重大損傷相対+20～40%という技術帯 | J-ASW | **CURRENT TECH BAND / FIELDING OPEN** | 各航路で護衛数・装備・組織を実在させてから適用 |
| S2-40 | 高級暗号による米潜待伏せ抑制 | 旧70のblanket unreadabilityは撤回。v050 Santo/NCだけ個別にexact objective等を読めない裁定 | COMSEC | **GLOBAL OPEN / LOCAL v050 CURRENT** | 戦域ごとの情報生成を再構築 |

---

# 3. 「潜水艦が強いから」と見えて実は別因子のもの

能力再検証で誤って強化しないため、以下は明確に分離する。

## 3.1 作戦枝・地理が主因
- Ro-33史実喪失の消滅候補：PM/任務geometryの変更。
- historical I-19のWasp/North Carolina命中消滅：Guadalcanal convoy geometryがない。
- Saratoga 8/31 I-26史実イベント：現行Q2ではSaratoga自体がMIで喪失しているため成立不能。
- S-44によるKako等、Guadalcanal/Savo後の史実潜水艦イベント：対応する水上戦sequenceが違うなら自動コピー禁止。
- MI前方哨戒線早期化：作戦設計変更が主因。

## 3.2 doctrine/配当が主因
- Indian Oceanへ艇を残す。
- South Pacificへ艇を増す。
- 通商攻撃を増す。
- Guadalcanal補給へ艇を使わない。

これらは艇性能が高いから自動的に成立しない。
戦略目的、孤立基地、敵交通、燃料、整備、他戦域価値から毎回決める。

## 3.3 敵適応が主因
- Mark 14修正前倒し。
- 英船団化/航路変更。
- ASW航空増強。
- 日本局地護衛指揮所の強度。

戦果増が大きければ適応も早くなり得るので、Stage 4では内生化する。

---

# 4. 1942年末までに「潜水艦が出るのに未検証」のイベント候補

Stage 4で歴史線を再走査する際、少なくとも以下を明示的にYES/NO判定する。

## 日本側
1. 1941-12～42Q1 Hawaii/US West Coast commerce patrols。
2. Saratoga I-6 attackのBranch geometry/戦果が本当に史実維持か。
3. DEI/Java/Australia周辺の各哨戒と主要個艦戦果。
4. Sydney midget attack。
5. Diego Suarez midget attack。
6. Mozambique Channel初期5隻級作戦。
7. Addu発見・追跡。
8. 豪州東岸通商破壊。
9. Aleutians/北太平洋への日本潜配置。
10. Midway/Hawaii外周。
11. Santo作戦前後。
12. NC準備・本戦・撤収。
13. 11～12月Santo–NC占領補給線防衛/米潜反撃。
14. 史実Guadalcanal潜輸送に相当するBranch孤立拠点輸送が別地域で発生しないか。

## 米側
1. Midway侵攻/占領後の補給線攻撃。
2. Aleutiansでの日本DD/輸送船攻撃。
3. Rabaul–PM、Truk–Rabaul、Rabaul–Santo等の新しい固定需要線。
4. Savo/Guadalcanal不発生で消える史実個艦遭遇（Kako等）の整理。
5. Mark 14不良サンプルの蓄積と修正時期。
6. Santo/NC補給線へのBrisbane/Pearl側からの再配分。
7. 日本focused convoy ASWによる二撃目阻止と米潜損失。
8. 日本高級暗号/通信量変化によるULTRA/DF待伏せ精度。

## 英・蘭側
1. Indian Ocean/Bay of Bengal/Malayaの英潜水艦活動。
2. 日本のPenang/Andaman/Madagascar圧力で英潜の配分が変わるか。
3. British/Dutch submarinesによる日本タンカー・輸送船への1942損失。
4. 日本側ASW/COMSEC改善がこれらへ与える効果。

---

# 5. Stage 2で確定した重要問題

## 5.1 最大の入力汚染は「South Pacific 10～14 / effective 7～10」

これは旧23のGuadalcanal非発生配当から来たlegacy帯であり、
rollback後は本来再トリガー対象。

ところがv050 Santo/NCは、
- Santo 6～8 effective
- NC 8～11 effective

へこのwalletを実質継承している。

従ってSanto/NCの潜水艦**戦果そのものより先に、艇walletを作り直す必要がある。**

## 5.2 Indian Oceanは旧23値を守る作業ではない

最新RN監査自身が直接追加損失を50～90k GRTへ再オープンしている。

したがってStage 3/4で、
- 30kへ落ちてもよい
- 150kへ上がってもよい
- 戦果隻数よりescort/ship-day taxが大きくなってもよい

工程因果が通るなら旧レンジに拘束されない。

## 5.3 Allied submarine modelが不足

日本潜水艦は20/21/22/31でかなり詳細だが、
1942米潜はMark 14と個別戦史、英潜はさらに断片的。

よってStage 3を「日本潜だけの性能再検証」にすると非対称になる。
少なくとも比較基準として、
- 米Gato/Tambor/S-classのavailability/patrol cycle
- Mark 14
- 米TDC/レーダー/SD・SJ導入時計
- 英T-class等Indian Ocean潜水艦
- 日英米の1942ASW
を同じ表に載せる。

---

# 6. 次段階へのgate

Stage 3は以下の順で行う。

1. 史実日本潜水艦の**艇型別実測性能**。
2. 史実の**故障・早期帰投・修理・patrol cycle**。
3. 潜望鏡/TDC/魚雷の実攻撃律速。
4. 航法・通信・報告・再配置。
5. 史実日本潜水艦の任務 doctrine と、Branchで自然に変わる範囲。
6. 米潜/Mark14と英国潜水艦を比較基準化。
7. 日本ASW・連合ASWを同じ工程へ接続。
8. その後にのみStage 4の1942全戦史を再計算。

**旧レンジを守ることはStage 3/4の目的ではない。**
