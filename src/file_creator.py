"""File creation logic with validation, error handling, and Zenity feedback."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from .templates import get_template

# Maximum allowed filename length (most filesystems support 255 bytes).
_MAX_NAME_LEN = 255

# Dangerous path components that could escape the target directory.
_DANGEROUS_PATTERNS = ("..", "~")


def _is_safe_name(name: str) -> bool:
    """Return True if *name* contains no path-traversal components."""
    return all(part not in _DANGEROUS_PATTERNS for part in Path(name).parts)


def _zenity_error(message: str) -> None:
    """Show a Zenity error dialog."""
    subprocess.run(
        ["zenity", "--error", "--title=Error", f"--text={message}", "--width=360"],
        capture_output=True,
        check=False,
    )


def _zenity_info(message: str) -> None:
    """Show a Zenity info/success dialog."""
    subprocess.run(
        ["zenity", "--info", "--title=Success", f"--text={message}", "--width=360"],
        capture_output=True,
        check=False,
    )


def create_file(folder_path: str, default_name: str) -> bool:
    """Prompt for a filename via Zenity and create the file.

    Returns True when a file was successfully created, False otherwise.
    """
    cmd = [
        "zenity",
        "--entry",
        "--title=Create New File",
        "--text=Enter filename:",
        f"--entry-text={default_name}",
    ]

    res = subprocess.run(cmd, capture_output=True, text=True, check=False)

    # User pressed Cancel or closed the dialog.
    if res.returncode != 0:
        return False

    filename = res.stdout.strip()

    # Empty filename after trimming.
    if not filename:
        _zenity_error("Filename cannot be empty.")
        return False

    # Length check.
    if len(filename) > _MAX_NAME_LEN:
        _zenity_error(
            f"Filename too long ({len(filename)} chars, max {_MAX_NAME_LEN})."
        )
        return False

    # Path-traversal check.
    if not _is_safe_name(filename):
        _zenity_error(
            f"Invalid filename: '{filename}'\n\n"
            "Filenames cannot contain '..' or '~' path components."
        )
        return False

    # Null byte check.
    if "\x00" in filename:
        _zenity_error("Filename contains illegal characters.")
        return False

    full_path = os.path.join(folder_path, filename)

    # File already exists.
    if os.path.exists(full_path):
        _zenity_error(f"File already exists:\n{filename}")
        return False

    # Determine content from templates.
    content = get_template(default_name)

    try:
        with open(full_path, "w", encoding="utf-8") as fh:
            if content is not None:
                fh.write(content)
            # else: blank file (empty write)
    except PermissionError:
        _zenity_error(
            f"Permission denied:\n{full_path}\n\n"
            "Check directory permissions or run as appropriate user."
        )
        return False
    except OSError as exc:
        _zenity_error(f"I/O error creating file:\n{exc}")
        return False
    except Exception as exc:  # noqa: BLE001
        _zenity_error(f"Unexpected error:\n{exc}")
        return False

    _zenity_info(f"Created {filename}")
    return True
