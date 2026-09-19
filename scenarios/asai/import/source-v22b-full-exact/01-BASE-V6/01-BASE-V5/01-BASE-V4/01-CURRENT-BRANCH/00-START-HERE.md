# 浅井世界線 branch reconstruction V1 — 2026-08-30

> **FULL V4 integration note (2026-08-30):** In the integrated handoff, this directory is the active current-branch layer. All pre-8/30 payloads are physically isolated under `../90-SOURCE-QUARANTINE/`. Their presence is source/provenance only and must not be used to auto-promote old terminology or old adoption states. Logical source paths are resolved by `../SOURCE-RESOLUTION-MAP-2026-08-30-FULL-V4.tsv`.


## 目的

旧正本、machine layer、8/29 overlay、archiveされた航空史、8/30会話で再CLOSEした内容が混在し、同じ名称が異なる意味・年次で再利用されている。このパッケージは、**資料そのものの索引**と**現在のbranchで有効な主張の索引**を分離して、再構築の土台を作る。

## 読み順

1. `02-TOPIC-SOURCE-MAP.md` — どの資料層を何に使うか。
2. `03-CURRENT-BRANCH-INDEX.tsv` — 現branchの主張単位の索引。最重要。
3. `04-CURRENT-BRANCH-HISTORY-1903-1937-SUMMER.md` — 祖業から1937夏までの因果史。
4. `05-CURRENT-CLOSED-PRODUCT-WEAPON-LEDGER.tsv` — 現時点でCLOSEDと扱える商品・兵器・実証機。
5. `06-CONFLICT-AND-REVIEW-QUEUE.tsv` — 混乱源、再監査が必要な項目。
6. `01-GLOBAL-RAW-SOURCE-INDEX.tsv` — 元パッケージ856ファイルのraw索引。
7. `07-SESSION-DELTA-2026-08-30.md` — 8/30会話で追加・変更された現在overlay。
8. `08-MILITARY-DELIVERY-LEDGER-1937-SUMMER.md` / `09-MILITARY-DELIVERY-LEDGER-1937-SUMMER.tsv` — 1937夏の軍需納入・採用見込。
9. `10-WEAPON-IMPACT-LEDGER-1937-SUMMER.md` / `.tsv` — 史実兵器の開発・生産・性能への影響走査。
10. `11-MATERIAL-TOOL-WEAPON-IMPACT-AUDIT-1937-SUMMER.md` / `.tsv` — 特殊鋼・工具・材料チャネル監査。
11. `12-MACHINE-INTEGRITY-AUDIT.md` / `.json` — schema、重複、参照、ZIP整合の機械監査。
12. `13-FILE-MANIFEST-SHA256.tsv` — current package各ファイルのchecksum。
13. `14-URANIUM-ROUTE-ECONOMIC-AUDIT-1937.md` / `.tsv` — 旧uranium枝の原料経路、metalization経済性、1937 saleability再監査。
14. `15-URANIUM-TUNGSTEN-DENSE-MATERIALS-AUDIT-1937.md` / `.tsv` — U/W高密度材、価格、WHA、UC棄却の材料監査。
15. `16-DENSE-CORE-AMMUNITION-MILITARY-IMPACT-1937.md` / `.tsv` — dense-core特殊弾の軍事影響。
16. `17-DENSE-MATERIAL-AMMUNITION-SUPPLY-AUDIT-1937.md` / `.tsv` — U/W供給量、弾材配賦、W節約量の監査。
17. `18-1937-07-07-EVENT-GATE.md` / `.tsv` — 1937-07-07の盧溝橋事件発生判定、偶発事象ルール、直後の再シミュレーション開始状態。
18. `19-1937-07-07-08-INITIAL-RESPONSE-GATE.md` / `.tsv` — 7/7夕刻～7/8 05:30の初動event-by-event closure。
19. `20-1937-07-08-FIRST-COMBAT-GATE-0530-0600.md` / `.tsv` — 盧溝橋05:30–06:00最初の火戦micro-gate。
20. `21-1937-07-08-MORNING-GATE-0600-1200.md` / `.tsv` — 06:00–12:00の散発射撃、電話障害、撤退交渉、通州方面増援出発gate。
21. `22-1937-07-08-AFTERNOON-GATE-1200-1830.md` / `.tsv` — 12:00–18:30の増援機動・交渉と18:30自発撤収gate。
22. `23-1937-07-08-09-EVENING-OVERNIGHT-GATE-1830-0210.md` / `.tsv` — 18:30–翌02:10の中央不拡大、天津増援、夜襲意図、撤兵合意gate。
23. `24-1937-07-09-WITHDRAWAL-COMMS-FAILURE-GATE-0210-0710.md` / `.tsv` — 02:10–07:10の撤兵命令伝達failure、05:00再射撃、06:40/07:10再連絡gate。
24. `25-1937-07-09-WITHDRAWAL-SECURITY-FORCE-GATE-0710-1600.md` / `.tsv` — 07:10–16:00の撤退監視、保安隊/変装正規軍誤認衝突、警備引継ぎgate。
25. `26-1937-07-09-10-DEESCALATION-PREPARATION-GATE-1600-1600.md` / `.tsv` — 7/9 16:00–7/10 16:00の局地離隔、第29軍防衛準備、16時再緊張trigger。
26. `27-1937-07-10-LONGWANGMIAO-SECOND-BATTLE-GATE-1600-2115.md` / `.tsv` — 7/10 16:00–21:15の竜王廟再戦、撤収命令と牟田口独断攻撃、21:15再占領gate。

27. `28-1937-07-11-LOCAL-SETTLEMENT-CENTRAL-DISPATCH-GATE-0500-2000.md` / `.tsv` — 7/11 05:00–20:00 local settlement vs central dispatch-preparation gate.
28. `29-1937-07-11-13-SETTLEMENT-MOBILIZATION-GATE-2000-2000.md` / `.tsv` — 7/11 night–7/13 mobilization / settlement gate.
29. `30-1937-07-13-17-REINFORCEMENT-LOCAL-CLASH-LUSHAN-GATE-2000-1800.md` / `.tsv` — 7/13–17 reinforcement / local clashes / Lushan gate.
30. `31-1937-07-17-20-LOCAL-COMPLIANCE-RENEWED-FIGHTING-GATE-1800-2100.md` / `.tsv` — 7/17–20 compliance / renewed artillery fighting gate.
31. `32-1937-07-21-22-WITHDRAWAL-RAIL-TRANSPORT-GATE.md` / `.tsv` — 7/21–22 renewed de-escalation, home-division opinion, Chinese rail withdrawal gate.

## 新しい優先規則

主張を勝たせる順は以下。

1. **SESSION-CLOSED**：8/30会話で明示的にCLOSEした内容。
2. **late-8/29 CURRENT overlay**：FULL V3のcurrent state / handoff / overlays。
3. **Marine V10等の現行domain authority**：特定分野の再監査済み技術 authority。
4. **semantic v48 main**：上記で上書きされていないbase正本。
5. **machine v48r3**：索引・chronology。意味論の親ではなく検索・整合補助。
6. **archive / pre-v48**：系譜・旧案の参照。自動復活禁止。

例外：旧archiveにしか残らない項目を8/30会話で明示的に救済した場合は、archiveを「根拠」として使うが、権威はSESSION-CLOSED/WORKINGに置く。

## 主張レコードの必須属性

今後は最低でも次を持つ。

- `claim_id`
- `domain`
- `entity`
- `claim`
- `status`: CLOSED / CLOSED-TECH / WORKING / OPEN / SUPERSEDED
- `authority_layer`
- `effective_branch`
- `source_pointer`
- `supersedes`
- `notes`

「正本」という語だけでは勝たせない。同じ「材一号」でも意味が変われば別claimとして記録する。

## 最新event gate

- `35-1937-07-26-27-GUANGANMEN-CONVOY-DELAY-GATE.md` / `.tsv` — 7月26日広安門事件。26台truck convoyの遅延を「豊台出発遅延」と特定し、浅井車両差で到着を前倒ししない。18:20分断戦闘、22:20攻撃命令、27日04:30一時延期までCLOSED-SAME。
- 次gate: `Q-035` — 7月27日昼→28日攻撃開始。最後通牒/撤兵/居留民退避/総攻撃部署と浅井ready・砲兵計算・航空整備差を監査。

## 次チャットへの引継ぎ

- `99-NEXT-CHAT-HANDOFF.md` — 現在時刻1937-07-27 ~04:30、最新CLOSED gate 35、次のQ-035（27日昼→28日攻撃開始）、浅井差の監査要点を一枚に集約。
