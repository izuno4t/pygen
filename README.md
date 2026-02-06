# python-project-boilerplate

Pythonプロジェクトのボイラープレートです。

## 使い方

```bash
./bin/pygen <project-name> \
  [-type <plain|fastapi|streamlit>] \
  [-runtime <python-version>]
```

- `-type` を省略すると `plain` を使用します
- `-runtime` を省略すると `pyenv` のバージョン、なければ `python --version` を使用します
- テンプレートはこのリポジトリのGitHubアーカイブを取得します（git履歴は含みません）
