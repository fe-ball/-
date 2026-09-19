# 計算機異聞 refactor v004 — closeout

この版でリファクタリングの締め工程を完了した。新しい概念層は追加せず、v003の骨格を実行用に閉じた。

## 現在の正規入口

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v004.md`
2. `05_WARTIME/CHECKPOINT_INDEX_v003.json`
3. `05_WARTIME/CHECKPOINT_1942-05-06T24_v001.json`
4. `06_RUNTIME/EVENT_RELEVANCE_PROFILES_v002.json`
5. `98_TOOLS/build_event_handout_v004.py`

## 完了した締め工程

- 旧188ファイル全体の残滓・版系列・重複監査。旧ファイルは無変更。
- WARSTARTの全ドメインを、確定・bounded・conditional・event-resolution-requiredのいずれかへ明示。点推定の捏造はしない。
- 7代表イベントでTECH/STATE検索漏れ試験。mandatory domainの無参照は0。
- 1942-05-06 24:00を現行の正式restart boundaryとして作成。5/7戦闘は未実行。
- COMINT旧再抽選規則と後発handoffの衝突を明示し、現行branch overrideとして分離。旧規則自体は保存。

詳細は `95_AUDIT/REFACTOR_CLOSEOUT_AUDIT_v001.json` を参照。
