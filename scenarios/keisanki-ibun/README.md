# 計算機異聞

Status: **active**

Authority: **Branch B v097**

Canonical clock: **1944-04-30T24:00**

Clock state: **FROZEN**

Current frontier: **aircraft processing-history audit → pre-FORAGER OOB → Saipan/FORAGER**

## Scenario rule

最初に [SCENARIO-RULES.md](SCENARIO-RULES.md) を確認する。

この世界線には未来知識を置かない。計算機は大量反復計算、設計探索、公差評価、試験feedbackを加速するが、材料・工場・熟練・耐久試験時間を無料で作らない。

## Authority

v096 FULL package is the base authority/provenance layer.  
v097 is the newest authority overlay for points explicitly settled or corrected through 2026-09-19.

WORKING / OPEN / PROVISIONAL は hard canon として扱わない。

後の歴史時刻まで進んだ旧枝が存在しても、v097の1944-04-30 clock freezeを自動的に上書きしない。

## Current frontier

FORAGER / Saipan battle resolutionへ進む前に、航空機processing historyを機種・世代ごとに監査する。

requirement → prototype iterations → engine generation → airframe/drag/weight → weapons/protection/radio → production blocks → field feedback → maturity → serviceability → political allocation.

Recent conversational June-Marianas aircraft projections are quarantined until this audit is closed.

## Reading order

1. [v097 current read-first](current/00_CURRENT_AUTHORITY/00_READ_FIRST_CURRENT_V097_2026-09-19.md)
2. [v097 handoff](current/V097_ADDENDUM_2026-09-19/00_HANDOFF/00_READ_FIRST_V097_FULL_HANDOFF.md)
3. [v097 supersession/status map](current/V097_ADDENDUM_2026-09-19/01_AUTHORITY/V097_SUPERSESSION_AND_STATUS_MAP.md)
4. [v097 next frontier](current/V097_ADDENDUM_2026-09-19/04_RESUME/NEXT_FRONTIER_1944-04-30_AIRCRAFT_HISTORY_FIRST.md)
5. [v096 base handoff](current/00_CURRENT_AUTHORITY/00_READ_FIRST_V096_FULL_HANDOFF.md)
6. [v096 supersession map](current/00_CURRENT_AUTHORITY/02_SUPERSESSION_MAP_V096_FULL.md)

## Aircraft-audit source anchors

- [Army/Navy aviation master canon](current/00_CURRENT_AUTHORITY/05_CLEAN_CANONICAL_REFERENCES/50_航空機研究_陸海軍総合正本.md)
- [Army aircraft design / engines / timing](current/00_CURRENT_AUTHORITY/05_CLEAN_CANONICAL_REFERENCES/51_陸軍航空機_機種別設計・発動機・日程.md)
- [Navy attack / dive / land attack / flying boats](current/00_CURRENT_AUTHORITY/05_CLEAN_CANONICAL_REFERENCES/52_海軍航空機_艦攻・艦爆・陸攻・大艇.md)
- [Navy fighters / air-cooled engines / jet aviation](current/00_CURRENT_AUTHORITY/05_CLEAN_CANONICAL_REFERENCES/53_海軍戦闘機・空冷発動機・噴進航空.md)
- [B7A Ryusei full reaudit](current/00_CURRENT_AUTHORITY/05_CLEAN_CANONICAL_REFERENCES/BRANCH_B_B7A_RYUSEI_FULL_REAUDIT_1944-04-25_v001.md)

## Import status

- [Source package](import/SOURCE-PACKAGE.md)
- [Import status](import/IMPORT-STATUS.md)

The provided FULL HANDOFF ZIP contains 2,520 entries and a deep supersession chain. GitHub promotes the current v097 overlay, required v096 authority, and current-aircraft-audit source anchors into the main reading path; legacy branches remain source-package provenance unless explicitly re-imported with their original status.
