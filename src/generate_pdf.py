#!/usr/bin/env python3
"""Fountain台本 → PDF 変換CLI

使い方:
    python generate_pdf.py input.fountain
    python generate_pdf.py input.fountain -o output.pdf
    python generate_pdf.py input.fountain --direction horizontal --orientation portrait
    cat input.fountain | python generate_pdf.py - -o output.pdf
"""

import argparse
import sys
from pathlib import Path

# スクリプト自身のディレクトリをパスに追加（pdf_generator, fountain_utils を import するため）
sys.path.insert(0, str(Path(__file__).parent))

from pdf_generator import generate_script_pdf


def main():
    parser = argparse.ArgumentParser(
        description="Fountain形式の台本テキストをPDFに変換します。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
例:
  %(prog)s script.fountain
  %(prog)s script.fountain -o 出力.pdf
  %(prog)s script.fountain --direction horizontal --orientation portrait
  cat script.fountain | %(prog)s - -o output.pdf

依存ライブラリ (pip install):
  reportlab
  playscript
  fountain-python  (または fountain)
""",
    )

    parser.add_argument(
        "input",
        help="入力Fountainファイルのパス。'-' を指定すると標準入力から読み込みます。",
    )
    parser.add_argument(
        "-o", "--output",
        help="出力PDFファイルのパス（省略時: 入力ファイル名.pdf）",
        default=None,
    )
    parser.add_argument(
        "--direction",
        choices=["vertical", "horizontal"],
        default="vertical",
        help="文字方向: vertical=縦書き（デフォルト）, horizontal=横書き",
    )
    parser.add_argument(
        "--orientation",
        choices=["landscape", "portrait"],
        default="landscape",
        help="用紙の向き: landscape=横向き（デフォルト）, portrait=縦向き",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="入力ファイルの文字コード（デフォルト: utf-8）",
    )

    args = parser.parse_args()

    # 入力読み込み
    if args.input == "-":
        fountain_content = sys.stdin.read()
        default_output = "output.pdf"
    else:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"エラー: ファイルが見つかりません: {args.input}", file=sys.stderr)
            sys.exit(1)
        fountain_content = input_path.read_text(encoding=args.encoding)
        default_output = input_path.with_suffix(".pdf").name

    # 出力パス決定
    output_path = Path(args.output) if args.output else Path(default_output)

    # PDF生成
    try:
        pdf_bytes = generate_script_pdf(
            fountain_content,
            orientation=args.orientation,
            writing_direction=args.direction,
        )
    except Exception as e:
        print(f"エラー: PDF生成に失敗しました: {e}", file=sys.stderr)
        sys.exit(1)

    # 書き出し
    output_path.write_bytes(pdf_bytes)
    print(f"生成完了: {output_path}")


if __name__ == "__main__":
    main()
