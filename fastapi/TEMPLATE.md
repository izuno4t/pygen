# FastAPI Template Guide

## セットアップ

```bash
uv sync --dev
uv run pre-commit install
cp .env.example .env
```

## 開発サーバー起動

```bash
make run
```

## よく使うコマンド

```bash
make taplo
```

## 構成パターン

- ファイルタイプ別構成: `src/project_name/`
- ドメイン別構成: `src/project_name_domain/`

## CI（任意）

CIを導入する場合は、`**/*.toml` の変更時に `taplo fmt --check` と `taplo lint` を実行することを推奨します。
