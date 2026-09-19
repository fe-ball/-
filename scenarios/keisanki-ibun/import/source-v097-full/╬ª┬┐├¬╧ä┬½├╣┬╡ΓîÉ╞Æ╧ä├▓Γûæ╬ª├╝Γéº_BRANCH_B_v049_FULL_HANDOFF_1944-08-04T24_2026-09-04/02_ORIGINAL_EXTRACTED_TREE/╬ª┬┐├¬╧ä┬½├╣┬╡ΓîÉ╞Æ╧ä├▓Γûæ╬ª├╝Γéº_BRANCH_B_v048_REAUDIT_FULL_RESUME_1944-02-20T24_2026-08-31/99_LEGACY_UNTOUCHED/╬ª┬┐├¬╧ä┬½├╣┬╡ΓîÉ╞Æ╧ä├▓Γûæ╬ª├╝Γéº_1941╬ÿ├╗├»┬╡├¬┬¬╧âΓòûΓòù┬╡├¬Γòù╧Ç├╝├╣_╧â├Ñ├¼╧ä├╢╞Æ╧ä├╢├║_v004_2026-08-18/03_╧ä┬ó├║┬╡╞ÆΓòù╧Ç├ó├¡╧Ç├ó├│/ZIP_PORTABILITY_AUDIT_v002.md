# ZIP portability audit v0.02

v001 ZIPは内容検証自体はPASSしていたが、ZIP entryの日本語パスがUTF-8フラグなしで格納されており、Unix系の標準展開でディレクトリ名が文字化けしvalidatorが `01_現行正本` を発見できない問題があった。

v002は正規Unicodeパスから再梱包し、非ASCII entryのUTF-8 flagを検査する。
