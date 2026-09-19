# 計算機異聞 refactor v022 — 2026-08-26 1943春～秋 同期再監査固定

v022は、v021で1943-03-26 Komandorski直前まで戻したAleutians/Efate再監査を閉じ、Attu/Kiska、6月Efate限定無力化、五号第二期、1943年夏のIndian Ocean/Burma偵察・沿岸打通研究、欧州/地中海/東部戦線の同期差分を1943-09-30T24まで再統合する。

## Canonical machine entrypoint
1. `06_RUNTIME/CURRENT_BRANCH_STATE_v004.json`
2. `06_RUNTIME/SESSION_2026-08-26_1943Q3_SYNCHRONIZED_HANDOFF_v001.md`
3. `06_RUNTIME/ALEUTIANS_ATTU_KISKA_REAUDIT_1943-03_07_SETTLEMENT_v001.md`
4. `06_RUNTIME/EFATE_LIMITED_NEUTRALIZATION_1943-06_SETTLEMENT_v001.md`
5. `06_RUNTIME/INDIAN_OCEAN_BURMA_COASTAL_OPERATION_STUDY_1943-06_09_v001.md`
6. `06_RUNTIME/JAPAN_AMPHIBIOUS_NAVAL_WALLET_1943-07_09_v001.json`
7. `06_RUNTIME/GLOBAL_1943Q3_SYNCHRONIZATION_LEDGER_v001.md`
8. `00_CONFIG/current_branch_overrides_v006.json`

## Current synchronized frontier
**1943-09-30T24 / 1943-10-01T00:00.**

次に裁定するのは1943年10月。India/Burma沿岸打通案は `ADVANCED_OPERATIONAL_STUDY / PREPARATION_AUTHORIZED` まで進んだが、まだGOではない。Pacificで米新空母群が実戦化したため、第一線正規空母4隻を西へ出す中央案は凍結されている。

## 1943春～秋で新たに固定した大枠
- Komandorskiの史実型海戦は中央実現では発生しない。日本のAttu補給船団はSanko Maru型低速船を主船団から外し、3月27～28日にAttuへ到達。
- Yamasakiは約6週早くAttuへ入り、4月にも小規模補給が続く。5月LANDCRABは実施されるが、日本側は5月26～27夜に一度だけ限定救出。Attu最終抵抗は6月4日前後、Kiskaは7月27～28日級に撤収。
- Yamamotoは1943-04-18に死亡しない。高級暗号の枝差とGuadalcanal/P-38配置差によりOperation Vengeanceの歴史的kill-chainが成立しない。
- Efateは6月8～9日に大兵力・限定目的の中立化襲撃。第一線空母3隻が東方圧力、Soryuは秘匿予備。Waspは誘いに乗らず健在。基地稼働は6月9日に22～30%まで落ちるが、4～6日で重度抑圧を脱し、約2週で60～70%以上へ回復。
- 日本はEfate占領を狙わず、Santo/New Caledonia/東方空母群による三方向圧力を利用して米基地運用を一時麻痺させる。
- 五号第二期は6月10日開始、Hanzhongは7月21日前後、掃討7月22～23日。四川第三期は自動継続しない。
- India/Burmaは「史実U-Goを実施しない」だけでなく、Arakan沿岸＋Bay of Bengal＋Assam偵察を一つの外線圧迫候補として研究する。Cox's Bazar陸海打通が最低成功、Chittagongは条件付きexploit。
- 一般的な印度大蜂起は作戦戦力に算入しない。INA正規部隊・情報部・確認済み連絡先のみを台帳化し、全国蜂起は上振れ。
- Adduは直接攻撃目標ではなく受動情報源。Chittagongは能動偵察（pokeして応答を見る）に向く。Myitkyina/Bhamo系はHump/Upper Assamの拡張を写真・交通量で追う。
- 1943夏のCox's系沿岸LOC研究は、海上/陸上本線だけで成立判定する。空中投下は弾薬・医療・通信など小粒の数日保険であり、主LOC能力には加算しない。
- 英国のBurma反攻増勢は公理ではない。Indomitable/Formidable追加喪失、Mediterranean/Home Fleet競合、Indian Ocean船腹/乗員摩擦により、海上攻勢よりIndia内陸防御・航空・AA・工兵・Assam/Humpへ資源を寄せる中央線。
- 米国はIndiaを航空・工兵・輸送機で助けられるが、Pacificの新空母戦力をBay of Bengalへ大規模転用する中央線ではない。間接救援としてPacific圧力を上げる方が自然。
- 欧州ではEl Alamein/TORCH/Stalingrad/Kurskを反転させない。Tunisia終結5/22–26、HUSKY 7/10強行、Sicily 8/20–23、Italy休戦ほぼ史実週、Salerno 9/9前後だが英国は史実よりbufferを削り追加損耗を負う。

## 絶対に自動継承しないもの
- 「Guadalcanalで学んだから泥縄補給を避ける」という因果。この枝に史実型Guadalcanal戦役はない。泥縄補給は一般に計算すれば見えるアンチパターンとして扱う。
- 「英国は史実計画通り必ずBurmaへ反攻する」。目的と能力を分離する。
- 「Eastern Fleetが弱いから必ず決戦に出てくる」。出てこないこと自体が日本の海上利用権を作る。
- 「India作戦には第一線空母4隻が必要」。9月末中央案では0隻。
- 「Cox's LOC 200t/dayを空輸で補えば成立」。航空投下はshock absorberのみ。

## Downstream provisional
1943-10以後、1944 China/Pacific/CBI settlementは削除せず参照用PROVISIONALとして残す。v022 current stateが到達するまでは、旧ファイルの日付・損害・OOBを自動的な現行史実として扱わない。
