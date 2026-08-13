#!/usr/bin/env bash
set -euo pipefail

REPO_RAW_URL="https://raw.githubusercontent.com/mhmdwaelanwr/nautilus-code-new-file/main"
TARGET_DIR="$HOME/.local/share/nautilus-python/extensions"
TARGET_FILE="$TARGET_DIR/nautilus-code-new-file.py"
SRC_DIR="$TARGET_DIR/nautilus_code_new_file"

echo "Installing Nautilus Code New File..."

if ! command -v apt-get >/dev/null 2>&1; then
  echo "This installer currently supports Debian/Ubuntu-based systems with apt." >&2
  exit 1
fi

sudo apt-get update
sudo apt-get install -y python3-nautilus zenity curl

mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
LOCAL_EXTENSION="${SCRIPT_DIR}/nautilus-code-new-file.py"
LOCAL_SRC="${SCRIPT_DIR}/src"

if [[ -n "$SCRIPT_DIR" && -f "$LOCAL_EXTENSION" && -d "$LOCAL_SRC" ]]; then
  install -m 0644 "$LOCAL_EXTENSION" "$TARGET_FILE"
  rm -rf "$SRC_DIR"
  mkdir -p "$SRC_DIR"
  cp "${LOCAL_SRC}/__init__.py" "${LOCAL_SRC}/templates.py" \
     "${LOCAL_SRC}/file_creator.py" "${LOCAL_SRC}/extension.py" \
     "$SRC_DIR/"
else
  curl -fsSL "$REPO_RAW_URL/nautilus-code-new-file.py" -o "$TARGET_FILE"
  chmod 0644 "$TARGET_FILE"
  rm -rf "$SRC_DIR"
  mkdir -p "$SRC_DIR"
  for f in __init__.py templates.py file_creator.py extension.py; do
    curl -fsSL "$REPO_RAW_URL/src/$f" -o "${SRC_DIR}/${f}"
  done
fi

python3 -m py_compile "$TARGET_FILE"
for f in "$SRC_DIR"/*.py; do
  python3 -m py_compile "$f"
done

nautilus -q >/dev/null 2>&1 || true

echo "Installation complete. Reopen Files/Nautilus, then right-click inside a folder and choose 'New Code File...'."
