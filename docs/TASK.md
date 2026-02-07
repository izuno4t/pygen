# TASKS

マイルストーン: M1
ゴール: 3種テンプレートが各SPECに完全準拠する

## ワークフロールール

- タスク着手時にステータスを 🚧 に更新する
- タスク完了時にステータスを ✅ に更新する
- DependsOn のタスクがすべて ✅ でないタスクには着手しない

## ステータス表記ルール

| Status | 意味 |
| ---- | ----- |
| ⏳ | 未着手、TODO |
| 🚧 | 作業中、IN_PROGRESS |
| 🧪 | 確認待ち、REVIEW |
| ✅ | 完了、DONE |
| 🚫 | 中止、CANCELLED |

## タスク一覧

| ID | ステータス | 概要 | 依存関係 |
| --- | --- | --- | --- |
| TASK-001 | ✅ | テンプレート共通の基本構成を整備する | - |
| TASK-002 | ✅ | 共通のpyproject設定と品質設定を実装する | TASK-001 |
| TASK-003 | ✅ | 共通のツール設定と開発補助を整備する | TASK-002 |
| TASK-004 | ✅ | plainテンプレートの骨格とサンプルを実装する | TASK-003 |
| TASK-005 | ✅ | fastapiテンプレートの構成と実装を整備する | TASK-003 |
| TASK-006 | ✅ | streamlitテンプレートの構成と実装を整備する | TASK-003 |
| TASK-007 | ✅ | デプロイ関連サンプルを追加する | TASK-004,TASK-005,TASK-006 |
| TASK-008 | ✅ | テンプレート別セットアップ文書を整備する | TASK-004,TASK-005,TASK-006 |
| TASK-009 | ✅ | 仕様準拠の検証手順と結果をまとめる | TASK-007,TASK-008 |
| TASK-010 | ✅ | 共通必須ファイルをFastAPI/Streamlitに追加する | TASK-003 |
| TASK-011 | ✅ | FastAPIのルーターと依存性の実装例を追加する | TASK-005 |
| TASK-012 | ✅ | FastAPIのスキーマとサービス層の例を追加する | TASK-011 |
| TASK-013 | ✅ | FastAPIの設定例と環境変数を拡充する | TASK-011 |
| TASK-014 | ✅ | Streamlitの状態管理とキャッシュ例を追加する | TASK-006 |
| TASK-015 | ✅ | StreamlitのUIコンポーネント例を拡充する | TASK-006 |
| TASK-016 | ✅ | Streamlitの推奨ナビゲーション実装を追加する | TASK-006 |
| TASK-017 | ✅ | FastAPI不足項目の対応を完了させる | TASK-010,TASK-011,TASK-012,TASK-013 |
| TASK-018 | ✅ | Streamlit不足項目の対応を完了させる | TASK-010,TASK-014,TASK-015,TASK-016 |
| TASK-019 | ✅ | 仕様準拠の検証記録を更新する | TASK-017,TASK-018 |
| TASK-020 | ✅ | plainの不足ファイルを追加する | TASK-004 |
| TASK-021 | ✅ | Streamlitの不足コンポーネントを追加する | TASK-006 |
| TASK-022 | ✅ | Streamlitのサービス層実装例を追加する | TASK-006 |
| TASK-023 | ✅ | 仕様準拠の検証記録を再更新する | TASK-020,TASK-021,TASK-022 |

## タスク詳細（補足が必要な場合のみ）

### TASK-001

- 補足: `plain/fastapi/streamlit` の3フォルダにsrc layoutを作成する
- 注意: 仕様にある構成要素のみを対象にする

### TASK-002

- 補足: Ruff/mypy/pytest/coverage/bandit設定を含める
- 注意: 仕様に記載のバージョン/ルールを反映する

### TASK-003

- 補足: pre-commit、.gitignore、.python-version、Makefile、devcontainerを含める
- 注意: オプション要素はテンプレートに同梱する

### TASK-004

- 補足: `core/domain/infrastructure/utils` とテスト雛形を含める
- 注意: 命名規則とサンプルコードに準拠する

### TASK-005

- 補足: 構成パターン（ファイルタイプ別/ドメイン別）を用意する
- 注意: `main.py`、`routers/`、`schemas/`、`core/config.py` 等を含める

### TASK-006

- 補足: `.streamlit/` 設定、`app.py`、`pages/`、`components/` を含める
- 注意: `secrets.toml.example` とセッション管理の雛形を含める

### TASK-007

- 補足: FastAPI/Streamlit向けDockerとcompose例を追加する
- 注意: 仕様のポート/起動コマンドに合わせる

### TASK-008

- 補足: テンプレートごとのREADME/セットアップ手順を記載する
- 注意: SPECの手順に沿った最小手順にする

### TASK-009

- 補足: lint/test/typecheck/formatの実行確認を含める
- 注意: 実行できない場合は理由と代替確認を記録する

### TASK-010

- 補足: `__main__.py` と `py.typed` を `fastapi` / `streamlit` に追加する
- 注意: 既存のplain構成と整合させる

### TASK-011

- 補足: `routers/users.py`、`routers/items.py`、`dependencies.py` を追加する
- 注意: 依存性注入の例を含める

### TASK-012

- 補足: `schemas/` と `services/` の具体例を追加する
- 注意: テスト用の利用が可能な粒度にする

### TASK-013

- 補足: `.env.example` に `SECRET_KEY` 等を追加する
- 注意: 仕様の項目を過不足なく反映する

### TASK-014

- 補足: `utils/state.py` と `utils/cache.py` に例を実装する
- 注意: `st.session_state` と `@st.cache_data` の使用例を含める

### TASK-015

- 補足: `components/charts.py` 等に具体例を追加する
- 注意: 仕様例の最低限を満たす

### TASK-016

- 補足: `st.navigation` / `st.Page` を使った例を追加する
- 注意: 既存 `app.py` を置き換える

### TASK-017

- 補足: FastAPI向け不足項目の残対応を集約する
- 注意: 仕様のサンプル実装が揃っていること

### TASK-018

- 補足: Streamlit向け不足項目の残対応を集約する
- 注意: 仕様のサンプル実装が揃っていること

### TASK-019

- 補足: `VERIFICATION.md` を更新する
- 注意: 実行可否の理由を明記する

### TASK-020

- 補足: `plain/.env.example` を追加する
- 注意: 仕様の位置に合わせる

### TASK-021

- 補足: `components/forms.py` と `components/sidebar.py` の例を追加する
- 注意: 既存のcomponents構成に揃える

### TASK-022

- 補足: `services/data_service.py` と `services/api_client.py` の例を追加する
- 注意: 最低限の呼び出し例を含める

### TASK-023

- 補足: `VERIFICATION.md` を更新する
- 注意: 実行可否の理由を明記する
