# FastAPI Template

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

## 構成パターン

- ファイルタイプ別構成: `src/project_name/`
- ドメイン別構成: `src/project_name_domain/`
