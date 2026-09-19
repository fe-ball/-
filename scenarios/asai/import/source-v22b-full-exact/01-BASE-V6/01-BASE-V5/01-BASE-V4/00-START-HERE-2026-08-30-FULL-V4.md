# 浅井世界線 — FULL HANDOFF 2026-08-30 V4

## これは何か

2026-08-29 FULL V3 と 2026-08-30 BRANCH RECONSTRUCTION V1 を統合した、**自己完結型のFULL handoff**。

今回の統合では、旧用語・旧採用史・archive claimがcurrent branchへ混ざることを防ぐため、pre-8/30 payloadを `90-SOURCE-QUARANTINE/` へ物理隔離した。隔離層は削除ではなくsource/provenance保存であり、現行claimから明示参照して使える。

## 最初に読む

1. `CURRENT-STATE-2026-08-30-FULL-V4.json`
2. `01-CURRENT-BRANCH/00-START-HERE.md`
3. `01-CURRENT-BRANCH/03-CURRENT-BRANCH-INDEX.tsv`
4. `TERMINOLOGY-AND-SUPERSESSION-GUARD.tsv`
5. `01-CURRENT-BRANCH/06-CONFLICT-AND-REVIEW-QUEUE.tsv`
6. `01-CURRENT-BRANCH/99-NEXT-CHAT-HANDOFF.md`

旧資料へ遡る必要があるときだけ `SOURCE-RESOLUTION-MAP-2026-08-30-FULL-V4.tsv` と `90-SOURCE-QUARANTINE/` を使う。

## 混濁防止規則

- current claimの意味・statusは `03-CURRENT-BRANCH-INDEX.tsv` が入口。
- 同名でも意味が変わったものは別claim。名前一致だけで統合しない。
- `SUPERSEDED`, archive, pre-v48, old adoption wordingをcurrentへ自動復活させない。
- 旧層の「採用済み」「量産済み」「就役済み」は、current indexで明示的に再CLOSEされていない限り現行branchの事実にしない。
- late-8/29 overlayやMarine V10等はsource authorityとして有効な場合がある。**quarantineはauthority剥奪ではなくnamespace隔離**。
- 旧語と新語がぶつかったら `TERMINOLOGY-AND-SUPERSESSION-GUARD.tsv` → current claim → source pointer の順に確認する。

## 前パッケージからの機械修理

- RECONSTRUCTION V1の監査文にあった `FULL-HANDOFF ZIP rebuilt` は、実体がthin reconstruction packageだったため不正確だった。V4では実際にFULL V3 source layerを内包して再構築した。
- 8/29 resume documentsをcurrent entry pointから外し、source quarantineへ移した。これにより旧用語がcurrent namespaceへ検索上・読順上で流入しにくくした。
- 856 raw-source recordsに対し、V4内の実ファイルまたはnested ZIP memberへのresolution mapを付与した。
- current TSV schema、claim/review/event ID重複、source pointer解決、JSON、manifest SHA256、nested ZIP CRC、final ZIP CRCを再監査する。

## 現在位置

- branch time: **1937-07-27 ~04:30**
- latest CLOSED gate: `35-1937-07-26-27-GUANGANMEN-CONVOY-DELAY-GATE.md`
- next: **Q-035 — 1937-07-27 daytime → 1937-07-28 attack opening**
