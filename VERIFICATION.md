# Verification

## 実行コマンドと結果

- `markdownlint-cli2` (pass)
- 対象: `TASK.md`, `plain/README.md`, `fastapi/README.md`
- 対象: `streamlit/README.md`, `VERIFICATION.md`
- `uv run ruff check .` (not run: uv/依存が未設定)
- `uv run ruff format --check .` (not run: uv/依存が未設定)
- `uv run mypy .` (not run: uv/依存が未設定)
- `uv run pytest` (not run: uv/依存が未設定)
