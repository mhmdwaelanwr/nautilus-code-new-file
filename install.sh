#!/usr/bin/env bash
set -euo pipefail

REPO_RAW_URL="https://raw.githubusercontent.com/mhmdwaelanwr/nautilus-code-new-file/main"
TARGET_DIR="$HOME/.local/share/nautilus-python/extensions"
TARGET_FILE="$TARGET_DIR/nautilus-code-new-file.py"

echo "🚀 Installing Nautilus Code New File..."

if ! command -v apt-get >/dev/null 2>&1; then
  echo "❌ This installer currently supports Debian/Ubuntu-based systems with apt." >&2
  exit 1
fi

sudo apt-get update
sudo apt-get install -y python3-nautilus zenity curl

mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd || true)"
LOCAL_EXTENSION="${SCRIPT_DIR}/nautilus-code-new-file.py"

if [[ -n "$SCRIPT_DIR" && -f "$LOCAL_EXTENSION" ]]; then
  install -m 0644 "$LOCAL_EXTENSION" "$TARGET_FILE"
else
  curl -fsSL "$REPO_RAW_URL/nautilus-code-new-file.py" -o "$TARGET_FILE"
  chmod 0644 "$TARGET_FILE"
fi

python3 -m py_compile "$TARGET_FILE"
nautilus -q >/dev/null 2>&1 || true

echo "✅ Installation complete. Reopen Files/Nautilus, then right-click inside a folder and choose 'New Code File...'."
