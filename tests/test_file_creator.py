"""Unit tests for file_creator and templates modules.

These tests do NOT require Nautilus or a running desktop environment.
They exercise the pure-Python logic only.
"""

import os
import sys

import pytest

# Adjust path so we can import src modules without installing the package.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.file_creator import _is_safe_name, create_file  # noqa: E402
from src.templates import CATEGORIES, TEMPLATES, get_template  # noqa: E402

# ---------------------------------------------------------------------------
# Template tests
# ---------------------------------------------------------------------------


class TestTemplates:
    def test_all_category_files_have_template_or_are_blank(self):
        """default_name must have a template or be in the blank allowlist."""
        blank_ok = {".env", "notes.txt", "config.toml"}
        for _cat, files in CATEGORIES.items():
            for _label, default_name in files:
                tpl = get_template(default_name)
                assert tpl is not None or default_name in blank_ok, (
                    f"No template for '{default_name}' and not in blank allowlist"
                )

    def test_templates_are_strings(self):
        for name, content in TEMPLATES.items():
            assert isinstance(content, str), f"Template '{name}' is not a string"

    def test_get_template_returns_none_for_unknown(self):
        assert get_template("unknown_file.xyz") is None


# ---------------------------------------------------------------------------
# Path safety tests
# ---------------------------------------------------------------------------


class TestIsSafeName:
    @pytest.mark.parametrize(
        "name",
        [
            "file.txt",
            "my-file.py",
            "dir/file.ts",
            ".env",
            "a/b/c.js",
        ],
    )
    def test_safe_names(self, name):
        assert _is_safe_name(name) is True

    @pytest.mark.parametrize(
        "name",
        [
            "../file.txt",
            "../../etc/passwd",
            "~/file.sh",
            "dir/../../secret",
            "../",
        ],
    )
    def test_unsafe_names(self, name):
        assert _is_safe_name(name) is False


# ---------------------------------------------------------------------------
# create_file tests
# ---------------------------------------------------------------------------


class TestCreateFile:
    def test_creates_blank_file(self, monkeypatch, tmp_path):
        """Zenity returning a valid filename creates a blank file."""
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 0, "stdout": "test.txt"})(),
        )
        result = create_file(str(tmp_path), "notes.txt")
        assert result is True
        assert (tmp_path / "test.txt").exists()

    def test_creates_file_with_template(self, monkeypatch, tmp_path):
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 0, "stdout": "main.py"})(),
        )
        result = create_file(str(tmp_path), "main.py")
        assert result is True
        content = (tmp_path / "main.py").read_text()
        assert "def main()" in content

    def test_cancel_returns_false(self, monkeypatch, tmp_path):
        """User pressing Cancel returns False without writing anything."""
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 1, "stdout": ""})(),
        )
        result = create_file(str(tmp_path), "file.txt")
        assert result is False
        assert list(tmp_path.iterdir()) == []

    def test_empty_filename_returns_false(self, monkeypatch, tmp_path):
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 0, "stdout": "   \n"})(),
        )
        result = create_file(str(tmp_path), "file.txt")
        assert result is False
        assert list(tmp_path.iterdir()) == []

    def test_traversal_blocked(self, monkeypatch, tmp_path):
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 0, "stdout": "../evil.txt"})(),
        )
        result = create_file(str(tmp_path), "file.txt")
        assert result is False
        assert list(tmp_path.iterdir()) == []

    def test_existing_file_returns_false(self, monkeypatch, tmp_path):
        (tmp_path / "already.txt").touch()
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 0, "stdout": "already.txt"})(),
        )
        result = create_file(str(tmp_path), "file.txt")
        assert result is False

    def test_permission_error(self, monkeypatch, tmp_path):
        import builtins

        real_open = builtins.open

        def deny_open(*args, **kwargs):
            if "file_creator" in str(args[0]) or str(tmp_path) in str(args[0]):
                raise PermissionError("denied")
            return real_open(*args, **kwargs)

        monkeypatch.setattr("builtins.open", deny_open)
        monkeypatch.setattr(
            "src.file_creator.subprocess.run",
            lambda *a, **kw: type("R", (), {"returncode": 0, "stdout": "secret.txt"})(),
        )
        result = create_file(str(tmp_path), "file.txt")
        assert result is False
