# psc_pdf — Fountain台本 → PDF 変換CLI

Fountain形式の台本テキストファイルをPDFに変換するスタンドアロンCLIツールです。

## ファイル構成

```
psc_pdf/
  generate_pdf.py    # CLIエントリポイント
  pdf_generator.py   # PDF生成コアロジック
  fountain_utils.py  # Fountain前処理ユーティリティ
  requirements.txt   # 依存ライブラリ
  fonts/             # (オプション) カスタムフォントを配置する場合
```

## セットアップ

```bash
pip install -r requirements.txt
```

依存ライブラリ:

| ライブラリ | 用途 |
|---|---|
| `reportlab` | PDF描画エンジン |
| `playscript` | 台本オブジェクトモデル |
| `fountain-python` | Fountain形式パーサー |

## 使い方

```bash
python generate_pdf.py <input.fountain> [オプション]
```

### オプション

| オプション | デフォルト | 説明 |
|---|---|---|
| `input` | (必須) | 入力Fountainファイル。`-` で標準入力 |
| `-o`, `--output` | 入力ファイル名.pdf | 出力PDFファイルのパス |
| `--direction` | `vertical` | 文字方向: `vertical`（縦書き）/ `horizontal`（横書き） |
| `--orientation` | `landscape` | 用紙の向き: `landscape`（横向き）/ `portrait`（縦向き） |
| `--encoding` | `utf-8` | 入力ファイルの文字コード |

### 実行例

```bash
# 縦書き・横向きA4（デフォルト）
python generate_pdf.py script.fountain

# 出力ファイルを指定
python generate_pdf.py script.fountain -o 台本.pdf

# 横書き・縦向きA4
python generate_pdf.py script.fountain --direction horizontal --orientation portrait

# 縦書き・縦向きA4
python generate_pdf.py script.fountain --direction vertical --orientation portrait

# 標準入力から読み込み
cat script.fountain | python generate_pdf.py - -o output.pdf

# Shift-JISファイルを変換
python generate_pdf.py script.fountain --encoding shift-jis -o output.pdf
```

## フォントについて

デフォルトでは ReportLab 組み込みの CID フォント `HeiseiMin-W3`（平成明朝）を使用します。

カスタムフォント（ShipporiMincho など）を使用したい場合は、TTFファイルを以下のいずれかに配置してください。スクリプト起動時に自動で読み込まれます。

```
psc_pdf/fonts/ShipporiMincho-Regular.ttf
psc_pdf/ShipporiMincho-Regular.ttf
```

## Fountain書式リファレンス（簡易）

```
Title: タイトル
Author: 作者名
Date: 2026-03-17

# 登場人物

太郎　主人公

# あらすじ

ある日、太郎は旅に出る。

# 第一場

INT. 家の中 - 昼

!太郎が荷物をまとめている。

@太郎
今日こそ旅立つぞ。
```

- `#` — セクション見出し（H1）
- `##` — サブセクション（H2）
- `INT.` / `EXT.` — シーン見出し
- `!` — ト書き（強制）
- `@名前` — セリフの話者
- `=` — あらすじマーカー
