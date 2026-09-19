# Topic / source map

## A. 現在branchの入口

FULL V4では、current namespaceを8/30 reconstruction layerへ一本化する。

- `03-CURRENT-BRANCH-INDEX.tsv` — current claimの主索引。
- `07-SESSION-DELTA-2026-08-30.md` — 8/30で追加・修正・再CLOSEしたoverlay。
- `06-CONFLICT-AND-REVIEW-QUEUE.tsv` — 未解決・再監査項目。
- `99-NEXT-CHAT-HANDOFF.md` — 現在のsimulation位置と次gate。

8/29の `CURRENT-STATE-*`, `CURRENT-HANDOFF-NOTES-*`, `CURRENT-PRECEDENCE-*` は、FULL V4では `../90-SOURCE-QUARANTINE/2026-08-29-FULL-V3/` 配下の**source layer**として保持する。late-8/29 authorityは優先規則上なお有効だが、旧用語や旧stateをcurrent namespaceへ自動流入させない。

## B. 会社起源・因果史

第一親：
- `nested/.../main/asai-works-business-origin-diversification-1903-30.md`
- `nested/.../main/asai-works-timeline-1920s.md`
- `nested/.../main/asai-works-timeline-1930s.md`
- `nested/.../main/asai-works-company-structure.md`

読み方：1903の織機・一般機械を祖業とし、輸入途絶を特殊鋼・工具・工作機械の内製化へ変換。GT研究は最初から本業ではなく赤字研究。排気ターボが先に商品として成功し、GTを育て返す。

## C. GT / ターボ

上流authority：
- `main/asai-works-engine-capability-core-e1-e9.md`
- `main/asai-works-e4-e5-*-rebaseline-1931-37.md`
- outer `ASAI-GT-FRONT-SCALE-RATING-PRODUCTS-V14-COST.xlsx`

商品・顧客：
- `main/asai-works-product-availability-ledger-1903-41.md`
- `main/asai-works-gt-first-customers.md`
- `main/asai-works-diesel-turbo-1930s.md`

Marine large-coreはMarine V10を優先。

## D. 計算機・設計文化

- `main/asai-works-computation-origin-business.md`
- `main/asai-works-engine-computation-internal-1923-28.md`
- `main/asai-works-engine-computation-externalization-1928-34.md`
- `main/asai-works-engine-computation-maturation-1934-37.md`

現在の方法論は「計算集計機使用文化」。O0–O3、D/T/Sで効果を分ける。計算機が事故や設計基準の誤りを魔法的に消す扱いは禁止。

## E. 材料・エポキシ・植物FRP

- `main/asai-works-materials-resin.md`
- `main/asai-works-frp-manufacturing.md`
- outer `ASAI-EPOXY-FRP-CAPABILITY-LEDGER-V2-COST.xlsx`

現時点の材料境界：エポキシ社内合成1931–33、30年代半ば少量商品。1937夏には植物繊維＋エポキシ、紙ハニカム、接着構造の**部分航空構造**は技術的に成立域。ただし主桁等の一次主荷重経路へ全面昇格しない。連続ガラスは1938以降。

## F. 航空

v48で旧採用史はarchiveへ隔離：
- `main/asai-works-aviation-reconstruction-framework-v48.md`
- `archive/aviation-pre-v48/v46-main/*`

したがって旧Ki-40、凱風、霹靂、旧STOL採用史等は自動復活しない。ただし8/30会話で救済された**1937夏までの開発史・実証史**は `07-SESSION-DELTA` を権威とする。

## G. 地上

late-8/29 overlay優先：
- `overlays/GROUND-DUST-CLOSURE-DELTA-2026-08-29.tsv`
- `CURRENT-HANDOFF-NOTES...` 地上・舟艇節

Type 97までの普通戦車、1938 GT戦車の技術評価、舟艇diesel本流などが現在の閉鎖。

## H. 海軍・商船

- late-8/29 `overlays/NAVAL-COMMERCIAL-INTEGRATION-OVERLAY-V1.md`
- Marine V10 technical authority
- 8/30会話で新型推進実験船の籍別・名称方針を追加CLOSE

## I. archiveの使い方

archiveは次の用途に限定する。

1. 記憶している旧案の所在確認。
2. 現branchで救済する候補の技術根拠。
3. 名称の意味変遷の追跡。

archive内の「採用済み」「就役済み」「量産済み」は、現branchでは原則無効。
