# Streamlit Template Guide

## セットアップ

```bash
uv sync --dev
uv run pre-commit install
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

## 起動

```bash
make run
```

## よく使うコマンド

```bash
make taplo
```

## CI（任意）

CIを導入する場合は、`**/*.toml` の変更時に `taplo fmt --check` と `taplo lint` を実行することを推奨します。
