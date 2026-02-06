# Streamlit Project

Streamlit を使ったアプリケーションのテンプレートです。

## 特徴

- Streamlit のページ構成に対応
- `pyproject.toml` に設定を集約
- `Makefile` で主要コマンドを短縮
- `.streamlit/secrets.toml` を想定

## 必要なもの

- Python（`python` または `python3`）
- `uv`

## インストール

```bash
uv sync --dev
```

## クイックスタート

```bash
make run
```

## 使い方

```bash
make run      # アプリ起動
make run-dev  # 保存時に自動再実行
make test     # テスト
make lint     # リント
make format   # フォーマット
make typecheck # 型チェック
```

### 追加設定

- `.streamlit/secrets.toml.example` をコピーして
  `.streamlit/secrets.toml` を作成

## 仕様書

- `docs/PYTHON-STREAMLIT-SPEC.md`

## ライセンス

MIT License
