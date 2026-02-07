# pygen

Pythonプロジェクト用のジェネレーターです。
`plain` / `fastapi` / `streamlit` / `lib` の4種類のテンプレートを提供し、`bin/pygen` で生成します。

## 特徴

- 4種類のテンプレート（`plain` / `fastapi` / `streamlit` / `lib`）
- `pyproject.toml` を中心にした構成
- テンプレート仕様書を `docs/` に同梱
- 生成時に `project-name` / `project_name` を自動置換
- 生成時に `.python-version` を作成

## 必要なもの

- Bash
- `curl`
- `tar`
- Python（`python` または `python3`）
- `pyenv`（任意。導入済みなら優先的に使用）

## インストール

```bash
curl -fsSL https://github.com/izuno4t/pygen/releases/latest/download/install.sh | bash
```

`install.sh` が `PATH` を設定します。シェルを再読み込みするか、新しいターミナルを開いてください。

## クイックスタート

```bash
./bin/pygen my-app -type plain
```

## 使い方

```bash
pygen [project-name] [-type <plain|fastapi|streamlit|lib>] \
  [-runtime <python-version>] [--dest <dir>]
```

例:

```bash
# plain テンプレート（デフォルト）
./bin/pygen my-app

# fastapi テンプレート + ランタイム指定
./bin/pygen my-api -type fastapi -runtime 3.11.6

# streamlit テンプレート
./bin/pygen my-dashboard -type streamlit

# lib テンプレート
./bin/pygen my-lib -type lib
```

### オプション

- `-type` : テンプレート種別（`plain` / `fastapi` / `streamlit` / `lib`）。省略時は `plain`
- `-runtime` : `.python-version` に書き込むPythonバージョン
- `--dest` : 出力先ディレクトリ（省略時はプロジェクト名）

### ランタイム検出ルール

`-runtime` を省略した場合の取得順:

1. `pyenv version-name`
2. `python --version`
3. `python3 --version`

## テンプレート一覧

| テンプレート | 用途 | 仕様書 |
| --- | --- | --- |
| `plain` | 汎用Pythonプロジェクト | `docs/PYTHON-PROJECT-SPEC.md` |
| `fastapi` | FastAPIアプリ | `docs/PYTHON-FASTAPI-SPEC.md` |
| `streamlit` | Streamlitアプリ | `docs/PYTHON-STREAMLIT-SPEC.md` |
| `lib` | PyPI向けライブラリ | `library/` |

## 生成時の挙動

- テンプレートはGitHubのアーカイブから取得されます（git履歴は含まれません）。
- `project-name` / `project_name` は、指定したプロジェクト名に合わせて置換されます。
- `.python-version` が生成されます。

## 仕組み

`bin/pygen` は以下の流れでプロジェクトを生成します。

1. GitHubのアーカイブを取得して、指定テンプレートの中身だけを展開
2. Pythonで `project-name` / `project_name` / `project_name_domain` をプロジェクト名に置換
3. `src/project_name` などのディレクトリをリネーム
4. `.python-version` を生成

## 仕様書

- `docs/PYTHON-PROJECT-SPEC.md`
- `docs/PYTHON-FASTAPI-SPEC.md`
- `docs/PYTHON-STREAMLIT-SPEC.md`

## ライセンス

MIT License
