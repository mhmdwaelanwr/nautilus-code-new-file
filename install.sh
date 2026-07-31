#!/bin/bash

echo "🚀 Installing Nautilus New Code File Extension..."

# 1. Install required packages
sudo apt update && sudo apt install -y python3-nautilus zenity

# 2. Create the target extensions directory
TARGET_DIR="$HOME/.local/share/nautilus-python/extensions"
mkdir -p "$TARGET_DIR"

# 3. Copy the extension script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cp "$SCRIPT_DIR/nautilus-code-new-file.py" "$TARGET_DIR/"

# 4. Restart Nautilus
nautilus -q

echo "✅ Installation complete! Right-click inside any folder to see 'New Code File...' menu."
