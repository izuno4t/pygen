#!/usr/bin/env sh
set -eu

BASE="https://github.com/izuno4t/pygen/releases/latest/download"

BIN_DIR="${HOME}/bin"
BOOT="${BIN_DIR}/pygen"

fetch() { curl -fsSL "$1" -o "$2"; }
sha256_verify() {
  file="$1"
  sum="$2"
  if command -v shasum >/dev/null 2>&1; then
    echo "${sum}  ${file}" | shasum -a 256 -c >/dev/null
  elif command -v sha256sum >/dev/null 2>&1; then
    echo "${sum}  ${file}" | sha256sum -c >/dev/null
  else
    echo "sha256 verifier not found (shasum/sha256sum)." >&2
    exit 1
  fi
}

mkdir -p "$BIN_DIR"

if ! echo "$PATH" | tr ":" "\n" | grep -qx "$BIN_DIR"; then
  add_path() {
    target="$1"
    line='export PATH="$HOME/bin:$PATH"'
    if [ -f "$target" ]; then
      if ! grep -Fqx "$line" "$target"; then
        printf "\n%s\n" "$line" >> "$target"
      fi
    else
      printf "%s\n" "$line" >> "$target"
    fi
  }

  add_path "$HOME/.profile"
  add_path "$HOME/.bashrc"
  add_path "$HOME/.zshrc"
  export PATH="$HOME/bin:$PATH"
fi

tmp="$(mktemp)"
sum_tmp="$(mktemp)"
fetch "${BASE}/pygen" "$tmp"
fetch "${BASE}/pygen.sha256" "$sum_tmp"
sha256_verify "$tmp" "$(cat "$sum_tmp")"
chmod +x "$tmp"
mv "$tmp" "$BOOT"

echo "Installed: $BOOT"
echo ""
echo "Next:"
echo "  1) Ensure PATH includes: $BIN_DIR"
echo "  2) Then run:"
echo "     pygen ..."
