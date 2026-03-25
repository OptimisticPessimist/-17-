# 修正箇所の確認 (Walkthrough)

## 概要
Fountain 形式のファイルを PDF に変換する CLI ツールを `src/pdf_converter.py` に実装しました。

## 変更内容
### `src/pdf_converter.py`
- `argparse` を導入し、コマンドライン引数で入出力を制御できるようにしました。
- 入力ファイルが存在しない場合のエラーチェックを追加しました。
- 出力先ディレクトリが未作成の場合に自動作成する機能を追加しました。
- `str(output_dir)` による型安全性の確保（lint対策）を行いました。

## 使い方
CLI から以下のように実行できます。

### 基本的な実行
入力ファイルを指定します（出力ファイル名は自動的に `.pdf` に変換されます）。
```bash
python src/pdf_converter.py books/scenario.fountain
```

### 出力先を指定して実行
`-o` または `--output` オプションで出力パスを指定できます。
```bash
python src/pdf_converter.py books/scenario.fountain -o out/my_script.pdf
```

### ヘルプの表示
```bash
python src/pdf_converter.py --help
```

## 注意事項
- `playscript` および `fountain` ライブラリの依存関係が作業環境の Python にインストールされている必要があります。
- Windows の場合、`python` または `py` コマンドで実行してください。
