# Contributing to Nautilus Code New File

Thanks for helping improve the project.

## Development setup

1. Fork or clone the repository.
2. Create a focused branch for your change.
3. Keep changes small and easy to review.

## Project structure

```
nautilus-code-new-file.py   # Nautilus entry point (thin wrapper)
src/
  __init__.py
  extension.py              # Nautilus MenuProvider class
  templates.py              # Template content and category definitions
  file_creator.py           # File creation logic with error handling
tests/
  test_file_creator.py      # Unit tests (no Nautilus required)
  test_imports.py           # Compilation smoke tests
install.sh                  # Installer
uninstall.sh                # Uninstaller
```

## Validation

Before opening a PR, run these checks:

```bash
# Python syntax
python3 -m py_compile nautilus-code-new-file.py
python3 -m py_compile src/extension.py src/templates.py src/file_creator.py

# Shell syntax + lint
bash -n install.sh
bash -n uninstall.sh
shellcheck install.sh
shellcheck uninstall.sh

# Unit tests
python3 -m pytest tests/ -v

# Ruff lint
ruff check src/ tests/ nautilus-code-new-file.py
ruff format --check src/ tests/ nautilus-code-new-file.py
```

## Adding a new file type

1. Add the menu entry in `src/templates.py` under the appropriate category.
2. Optionally add a skeleton template in the `TEMPLATES` dict.
3. Add the default filename to the blank allowlist in `tests/test_file_creator.py` if no template is needed.

## Pull request checklist

- Explain what changed and why.
- Keep unrelated refactors out of the same pull request.
- Confirm all validation steps above pass.
- Update the README when behavior, installation, or supported file types change.

## Bug reports

Please include your distribution, desktop environment, Nautilus version, steps to reproduce, expected behavior, actual behavior, and any terminal output that helps diagnose the issue.

## License

By contributing, you agree that your contribution will be licensed under the repository's MIT License.
