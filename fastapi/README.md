# FastAPI Project

FastAPI を使った API プロジェクトのテンプレートです。

## 特徴

- FastAPI + Uvicorn を前提にした構成
- `pyproject.toml` に設定を集約
- `Makefile` で主要コマンドを短縮
- `.env` による設定管理を想定

## 必要なもの

- Python（`python` または `python3`）
- `uv`
- `newman`（Postman CLI。`make api-test` で使用）

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
make run       # 開発サーバー起動
make run-prod  # 本番サーバー起動
make test      # テスト
make lint      # リント
make format    # フォーマット
make typecheck # 型チェック
make api-test  # Postman APIテスト
```

### 追加設定

- `.env.example` をコピーして `.env` を作成
- DB を使う場合は `alembic` を有効化

## 仕様書

- `docs/PYTHON-FASTAPI-SPEC.md`
- `fastapi/postman/`

## ライセンス

MIT License
