# 仮想歴史総合

複数の仮想歴史シナリオの**中央ルータ**。

ここで管理するのは、各世界線の本文そのものより、

- どのシナリオが存在するか
- 現在のauthorityは何か
- 歴史時計はどこか
- 時計が進行中か凍結中か
- 次に何を処理するか
- どこから読むか
- 元資料がGitHubへどこまでimportされているか

という「現在地」。

機械可読の正本一覧は [scenarios.yaml](scenarios.yaml)。

## 現在のシナリオ

| Scenario | Status | Authority | Canonical clock | Clock state | Current frontier |
|---|---|---|---|---|---|
| [浅井世界線](scenarios/asai/README.md) | active | V22B | 1944-12-31T24:00級 | 1945へOPEN | 独ソ作戦選択・ソ連応答・日ソ中立条約ゲート |
| [計算機異聞](scenarios/keisanki-ibun/README.md) | active | Branch B v097 | 1944-04-30T24:00 | FROZEN | 航空機processing-history監査 → FORAGER |

## 読み方

1. scenarios.yaml で対象世界線の current authority / clock / frontier を確認。
2. 各 scenarios/<id>/README.md を読む。
3. 各 SCENARIO-RULES.md で、その世界線固有の知識・因果ルールを確認。
4. authority entrypoint から本体へ入る。

**最大version、最新作成日、最も未来の歴史時刻を自動的にcurrentとはみなさない。**

シナリオを将来独立repositoryへ移しても、scenario idは維持し、scenarios.yaml の repository / path を更新する。

## 共通原則

- [Simulation Method](principles/simulation-method.md)
- [Causality](principles/causality.md)
- [Authority / Evidence Status](principles/evidence-status.md)

共通原則と、各シナリオ固有のepistemic ruleを混ぜない。

例:
- 浅井世界線では、正本で認められた先行知識・技術優位の伝播範囲を追う。
- 計算機異聞では未来知識を置かず、計算・測定・試験feedbackの高速化から分岐を導く。

## 永続化ルール

通常の会話・検討は GitHub へ自動反映しない。

ユーザーの「GitHubに投げろ」「ここまでGitHub反映」等を永続化トリガーとする。

詳細:
- [Persistence Policy](conventions/persistence-policy.md)
- [Scenario Status Convention](conventions/scenario-status.md)

AIの推論、ユーザー指定、未確定案、superseded事項を可能な限り区別し、誤解釈が判明した場合は履歴を隠さず修正する。

## ディレクトリ

- scenarios.yaml — 中央registry
- principles/ — 複数シナリオ共通の方法論
- conventions/ — authority / status / persistenceの運用規約
- scenarios/ — 現在のシナリオ配置
