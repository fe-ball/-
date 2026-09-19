# 計算機異聞 Branch B — v094 FULL HANDOFF

version: v094
package_date: 2026-09-15
current_cutoff: 1943-11-21T10:20
status: CURRENT AUTHORITY
next_session_frontier: FORGOTTEN_TECHNOLOGY_AUDIT

## 0. 最初に読む順番

1. `00_CURRENT_AUTHORITY/00_READ_FIRST_V094_FULL_HANDOFF.md`（本書）
2. `00_CURRENT_AUTHORITY/CURRENT_BRANCH_B_V094_COMPACT_ACTIVE_CONTEXT_1943-11-21T1020.md`
3. `00_CURRENT_AUTHORITY/CURRENT_BRANCH_B_V094_STATE_1943-11-21T1020.json`
4. `00_CURRENT_AUTHORITY/02_SUPERSESSION_MAP_V094_FULL.md`
5. `04_RESUME_FRONTIER/00_RESUME_V094_TECH_AUDIT_FRONTIER.md`
6. `CURRENT_1943-11-21_UPDATES/12_NEXT_SESSION_TECH_AUDIT_REGISTER.md`

GALVANICの詳細を読む場合：
- `CURRENT_1943-11-21_UPDATES/07_GALVANIC_CURRENT_STATE_1943-11-21T1020.md`
- `CURRENT_1943-11-21_UPDATES/08_GALVANIC_FIRST_STRIKE_TECH_AND_RESULT.md`
- `CURRENT_1943-11-21_UPDATES/09_SUPPORT_FORCE_ROLES_1943-11-21.md`

## 1. 現行線の要約

現在時刻は1943-11-21 10:20（GALVANIC D+1）。
日本第一機動部隊（翔鶴・瑞鶴・飛龍・蒼龍）は21日朝、米Makin側高速空母群（Essex / Belleau Wood / Monterey）へ140機第一波を実施。
結果：
- Essex：500kg級爆弾2＋航空魚雷1。沈没せず、戦役mission-kill。暫定修理6～10週。
- Belleau Wood：爆弾1＋魚雷1。沈没せず、重mission-kill。暫定修理4～6か月。
- Monterey：爆弾1。6～10時間級飛行作業停止、1～2日級で全戦闘サイクル復帰候補。
- 日本第一波：38機不可逆、搭乗員55～70名級不可逆/行方不明、17～23機損傷帰投。
- 日本4空母船体は無傷。即応/短時間即応は戦闘機55～62、攻撃機23～30級。
- 第二波は即時発進せず、西～北西へ変針して米反撃に備える。

この空母戦は「4CV vs 6CV」だけで裁定しない。
米CVE8隻がTarawa/MakinのCAP/CAS/ASWを維持し、米高速空母を対艦戦へ解放する。
日本の二級空母6隻は即時主力戦へ足さず、後方CAP・補充・回送・受け甲板・第二線打撃層として機能する。

## 2. 現行の重要な世界差

- Midway：日本保持。旧1943年第二次Midway枝は失効。
- Port Moresby / Santo / New Caledonia戦略域：日本保持。
- Attu / Kiska：米側。ただし日本は守備隊を大規模に回収して北方戦を早期閉鎖。
- 中国：西安・宝鶏・略陽・漢中を日本が確保。四川第三期はHOLD。
- 日本海軍：猿ガッソー旧枝の飛鷹沈没等は失効。戦闘用空母10船体が生存（主力4＋二線6）。
- 陸奥事故は発生しない。戦艦12船体。
- 重巡18船体、既成重巡沈没0。
- 商船500GRT+は1943-10-31中心5.89～5.94百万GRT級。タンカー実用能力は史実比+8～13%級の作業帯。
- 1943H2は海防艦・東海・COMSEC・護衛運用が質的に成熟しつつある。

## 3. v093からの最大の上書き

v093内の `CURRENT_1943-11-05_UPDATES/` は、当時の別の進行線を含む。
v094では、1943年夏以降の進行を再構成したため、以下は現行では自動採用しない：
- 猿ガッソー由来の二線空母損耗
- 旧1943年第二次Midway / Midway raid / post-Midway gate
- 旧Five-Go Phase IIIA Guangyuan進攻（現行はHanzhong HOLD）
- 旧GALVANICのD-Day、OOB、戦果、艦艇損害
- 旧Wake/Gilberts/Marcus相当の戦果（v094で再裁定済）

技術正本 `31 / 50 / 51 / 52 / 53 / 61` は、v094で明示修正していない部分は参照可能。ただし次回はこれらの「1943-11時点への適用漏れ」を総点検する。

## 4. 次回開始点

**戦闘を即再開しない。最初に技術論点の取りこぼし監査を行う。**

P0は：
- 1943-11時点の日本艦隊レーダー/戦闘機誘導/CAP統制
- 日本空母のダメコン・防火・航空燃料安全・AA射撃指揮
- 二級空母6隻の新型機適合性/甲板循環/受け甲板能力
- 空地分離・搭乗員/整備員/補充機の再配分
- 米残存6高速空母の11月21日反撃機種・航空隊構成
- 金星零戦改、疾風/誉、Ha43、烈風/紫電改の11月実態
- 海防艦/東海/カ号/ASWセンサーの11月実数・即応
- DD/海防艦/タンカー/AOの実竣工・修理・利用可能艦日

技術監査後の運用ゲートは、**米残存6高速空母の索敵・反撃 vs 日本4正規空母**。
