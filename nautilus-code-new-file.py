"""Thin wrapper that loads the modular extension for Nautilus.

This file stays at the original path so existing installations keep working.
The actual logic lives in src/.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "src")

if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

# Re-export the extension class so Nautilus can discover it.
from extension import CustomNewFileExtension  # noqa: E402, F401
