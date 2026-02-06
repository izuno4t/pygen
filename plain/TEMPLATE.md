# Plain Template Guide

このテンプレートは「フレームワークに依存しないPythonプロジェクトの基本形」を目的にしています。最小限の構成で、後からFastAPI/Streamlit等へ拡張できる前提です。

## このテンプレートでできること

- `uv` による依存管理と再現性のある環境構築
- `ruff` / `mypy` / `pytest` による品質チェックの標準化
- `pre-commit` を使ったローカル自動チェック
- `Makefile` での開発コマンド一元化
- `src` レイアウトにより拡張しやすい構成

## ディレクトリ構成

- **`src` レイアウト**: 実行時とテスト時のimport解決を一致させ、配布対象外のファイルが混入しないようにします。
- **`tests/unit` / `tests/integration`**: テストの粒度を最初から区別できるようにします。
- **`utils` のみ**: 最小構成として必要最低限に絞っています。
- **`py.typed`**: 型情報を配布する前提で、型チェックの精度を上げます。
- **`.python-version`**: テンプレート利用時にPythonバージョンを明示できるようにします。

```text
plain/
├── src/
│   └── project_name/
│       ├── __main__.py           # `python -m project_name` の入口
│       ├── py.typed              # 型情報を配布するためのマーカー
│       └── utils/                # 汎用ユーティリティ
├── tests/
│   ├── unit/                     # ユニットテスト
│   └── integration/              # 統合テスト
├── .env.example                  # 環境変数テンプレート
├── .pre-commit-config.yaml       # pre-commit設定
├── .python-version               # Pythonバージョン指定
├── Makefile                      # 開発コマンド集約
├── pyproject.toml                # プロジェクト設定
└── README.md
```

## 設定ポリシー

- **Ruff / mypy / pytest / coverage** を `pyproject.toml` に集約
- **pre-commit** で自動チェックを標準化
- **Makefile** に開発コマンドを集約

## セットアップ

```bash
uv sync --dev
uv run pre-commit install
```

## Makeターゲット

| コマンド | 内容 |
| --- | --- |
| `make help` | コマンド一覧を表示 |
| `make install` | 本番依存のインストール |
| `make dev` | 開発依存のインストールとpre-commit設定 |
| `make test` | テスト実行 |
| `make test-cov` | カバレッジ付きテスト |
| `make lint` | リント実行 |
| `make format` | 自動整形 |
| `make typecheck` | 型チェック |
| `make check` | lint/typecheck/test をまとめて実行 |
| `make taplo` | TOMLの整形とlint |
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
