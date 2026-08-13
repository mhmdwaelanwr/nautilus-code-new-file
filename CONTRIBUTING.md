# Contributing to Nautilus Code New File

Thanks for helping improve the project.

## Development setup

1. Fork or clone the repository.
2. Create a focused branch for your change.
3. Keep changes small and easy to review.
4. Validate Python syntax with:

```bash
python3 -m py_compile nautilus-code-new-file.py
```

5. Validate the installer with:

```bash
bash -n install.sh
```

6. Test the extension in Nautilus before opening a pull request when your change affects menu behavior.

## Adding a new file type

File templates are grouped in the `categories` mapping inside `nautilus-code-new-file.py`. Add a clear menu label and a sensible default filename while keeping the existing category structure readable.

## Pull request checklist

- Explain what changed and why.
- Keep unrelated refactors out of the same pull request.
- Confirm `python3 -m py_compile nautilus-code-new-file.py` passes.
- Confirm `bash -n install.sh` passes when the installer changes.
- Update the README when behavior, installation, or supported file types change.

## Bug reports

Please include your distribution, desktop environment, Nautilus version, steps to reproduce, expected behavior, actual behavior, and any terminal output that helps diagnose the issue.

## License

By contributing, you agree that your contribution will be licensed under the repository's MIT License.
