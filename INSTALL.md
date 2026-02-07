# Install Guide

`pygen` を GitHub Releases からインストールして利用するための案内です。

## 前提と注意

- 配布元は GitHub Releases（`latest`）
- `install.sh` を1回実行して `~/bin/pygen` を配置
- 起動時に最新版があれば自動で差し替え
- `curl | sh` の実行は内容を理解したうえで行ってください

## Release Assets

- `pygen`（実行ファイル）
- `pygen.sha256`（`pygen` のSHA-256）

## インストール

```bash
curl -fsSL https://github.com/izuno4t/pygen/releases/latest/download/install.sh | sh
```

## 使えないときの確認

- `~/bin` が `PATH` に含まれているか確認  
  例: `echo "$PATH" | tr ":" "\n" | rg -n "$HOME/bin"`
- 含まれていない場合は `.profile`/`.bashrc`/`.zshrc` に次を追加  
  `export PATH="$HOME/bin:$PATH"`
- 反映されない場合はシェルを再起動するか `source ~/.zshrc` を実行

## セキュリティ

- `pygen.sha256` とローカルの SHA-256 を比較して更新判断します
- 取得した `pygen` は `pygen.sha256` で検証します
