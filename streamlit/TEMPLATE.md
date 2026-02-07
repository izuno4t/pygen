# Streamlit Template Guide

このテンプレートは「Streamlitによるアプリ開発の基本形」を目的にしています。シンプルなUIとデータ表示を想定した構成です。

## このテンプレートでできること

- `uv` による依存管理と再現性のある環境構築
- `ruff` / `mypy` / `pytest` による品質チェックの標準化
- `pre-commit` を使ったローカル自動チェック
- `Makefile` での開発コマンド一元化
- Streamlitアプリの起動

## ディレクトリ構成

- **`src` レイアウト**: 実行時とテスト時のimport解決を一致させ、配布対象外のファイルが混入しないようにします。
- **`pages` / `components`**: ページとUI部品を分離します。
- **`.streamlit/`**: Streamlit設定とシークレットを管理します。
- **`.python-version`**: テンプレート利用時にPythonバージョンを明示できるようにします。

```text
streamlit/
├── src/
│   └── project_name/
│       ├── app.py                # Streamlitアプリの入口
│       ├── pages/                # ページ
│       ├── components/           # UI部品
│       ├── services/             # ロジック
│       └── utils/                # ユーティリティ
├── tests/
│   ├── unit/
│   └── integration/
├── .streamlit/
│   └── secrets.toml.example
├── .pre-commit-config.yaml
├── .python-version
├── Makefile
├── pyproject.toml
└── README.md
```

## 設定ポリシー

- **Ruff / mypy / pytest / coverage** を `pyproject.toml` に集約
- **pre-commit** で自動チェックを標準化
- **Makefile** に開発コマンドを集約

## セットアップ

```bash
uv sync --extra dev
uv run pre-commit install
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

## Makeターゲット

| コマンド | 内容 |
| --- | --- |
| `make help` | コマンド一覧を表示 |
| `make install` | 本番依存のインストール |
| `make dev` | 開発依存のインストールとpre-commit設定 |
| `make test` | テスト実行 |
| `make lint` | リント実行 |
| `make format` | 自動整形 |
| `make typecheck` | 型チェック |
| `make check` | lint/typecheck/test をまとめて実行 |
| `make run` | アプリ起動 |
| `make run-dev` | 保存時に自動再実行 |
| `make clean` | キャッシュ/生成物の削除 |

## CI（任意）

CIを導入する場合の基本チェックは以下を推奨します。

- `make lint`
- `make format`
- `make typecheck`
- `make test`
- `uv run bandit -c pyproject.toml -r src/`

TOMLが変更された場合は以下も実行します。

- `make taplo`
