# Import Status — 完全取り込み確認 2026-09-20

指定された原本ZIPと、その全ファイルをGit管理対象に取り込みました。

- 原本: [ZIP](archives/計算機異聞_BRANCH_B_v097_FULL_HANDOFF_1944-04-30T2400_AIRCRAFT_HISTORY_NEXT_2026-09-19(1).zip)（27,078,890 bytes）
- SHA-256: `29e2d71e234cfdfab108b15054c3ad1014c6f68ad7778d67d591d110950e40fb`
- 展開保存先: [source-v097-full/](source-v097-full/)
- ファイル: **2,071 / 2,071**
- 展開後容量: 51,813,460 bytes
- ZIP CRC検査: 全件合格
- 原本ZIPコピーおよび展開ファイル: 全件SHA-256一致
- [ファイル別パス・サイズ・SHA-256一覧](FULL-IMPORT-MANIFEST-2026-09-20.tsv)
- [検証結果](FULL-IMPORT-AUDIT-2026-09-20.json)

## 保存範囲と現行正本

旧版、監査履歴、バイナリ、入れ子ZIPを含め、元ZIP直下の全ファイルを保存しています。
入れ子ZIPはファイルとして原寸保存し、再帰展開はしていません。空ディレクトリの記録も原本ZIPに残ります。
展開時はZIP内の名前をそのまま使用し、元から含まれる文字化け名を推測で修正していません。
元ZIPから保存先への対応はmanifestに記録しています。

現行authorityは **Branch B v098** のままです。`current/` の本文・時計・frontierは今回変更していません。
旧資料の収録はCANONへの昇格を意味しません。各資料のsupersession・WORKING・OPEN・ARCHIVE等の状態を維持します。
現行の読み始めは [シナリオREADME](../README.md) を参照してください。
