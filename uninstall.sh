#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="$HOME/.local/share/nautilus-python/extensions"
TARGET_FILE="$TARGET_DIR/nautilus-code-new-file.py"
SRC_DIR="$TARGET_DIR/nautilus_code_new_file"

echo "Uninstalling Nautilus Code New File..."

removed=0

if [[ -f "$TARGET_FILE" ]]; then
  rm -f "$TARGET_FILE"
  echo "  Removed $TARGET_FILE"
  removed=1
fi

if [[ -d "$SRC_DIR" ]]; then
  rm -rf "$SRC_DIR"
  echo "  Removed $SRC_DIR"
  removed=1
fi

if [[ "$removed" -eq 0 ]]; then
  echo "Nothing to remove — extension not found."
  exit 0
fi

nautilus -q >/dev/null 2>&1 || true

echo "Uninstall complete. Reopen Files/Nautilus to apply changes."
