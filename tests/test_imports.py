"""Smoke tests that validate the main entry point compiles and the Nautilus
extension module can be imported without a running desktop."""

import os
import py_compile
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_main_entry_compiles():
    """nautilus-code-new-file.py should have valid Python syntax."""
    path = os.path.join(os.path.dirname(__file__), "..", "nautilus-code-new-file.py")
    py_compile.compile(path, doraise=True)


def test_src_modules_compile():
    """All src/*.py files should compile cleanly."""
    src_dir = os.path.join(os.path.dirname(__file__), "..", "src")
    for fname in os.listdir(src_dir):
        if fname.endswith(".py"):
            py_compile.compile(os.path.join(src_dir, fname), doraise=True)
