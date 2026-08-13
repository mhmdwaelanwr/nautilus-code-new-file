# Nautilus Code New File 🛠️

<p align="center">
  <strong>Create developer files directly from the Nautilus right-click menu.</strong><br>
  A lightweight Python extension for Ubuntu/Debian that adds categorized file templates with a quick naming prompt.
</p>

<p align="center">
  <a href="https://github.com/mhmdwaelanwr/nautilus-code-new-file/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/mhmdwaelanwr/nautilus-code-new-file?style=flat-square"></a>
  <a href="https://github.com/mhmdwaelanwr/nautilus-code-new-file/releases"><img alt="GitHub release" src="https://img.shields.io/github/v/release/mhmdwaelanwr/nautilus-code-new-file?style=flat-square"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/github/license/mhmdwaelanwr/nautilus-code-new-file?style=flat-square"></a>
  <img alt="Python" src="https://img.shields.io/badge/Python-Nautilus%20Extension-blue?style=flat-square">
  <img alt="Linux" src="https://img.shields.io/badge/platform-Linux-lightgrey?style=flat-square">
</p>

<p align="center">
  <img src="assets/demo.gif" alt="Nautilus Code New File demo" width="720">
</p>

## Why this project?

Creating a new source file on Linux often means opening a terminal or creating a generic blank file and renaming it manually. **Nautilus Code New File** puts common developer file types directly in the folder context menu, grouped by category, then lets you choose the final filename through Zenity.

## ✨ Features

- Native Nautilus right-click integration.
- Categorized developer file menu instead of one long list.
- Custom filename prompt before creation.
- Common frontend, backend, mobile, scripting, configuration and DevOps file types.
- Lightweight: one Python extension file, with no background service.
- Simple installation and clean uninstall process.

## 🚀 Quick install

Download the installer, review it, then run it:

```bash
curl -fsSL https://raw.githubusercontent.com/mhmdwaelanwr/nautilus-code-new-file/main/install.sh -o /tmp/nautilus-code-new-file-install.sh
less /tmp/nautilus-code-new-file-install.sh
bash /tmp/nautilus-code-new-file-install.sh
```

### Manual installation

```bash
git clone https://github.com/mhmdwaelanwr/nautilus-code-new-file.git
cd nautilus-code-new-file
bash install.sh
```

The installer installs `python3-nautilus`, `zenity` and `curl`, then copies the extension to:

```text
~/.local/share/nautilus-python/extensions/nautilus-code-new-file.py
```

After installation, reopen **Files**, right-click inside a folder, and choose **New Code File...**.

## 📦 Included file types

| Category | Examples |
| --- | --- |
| Documentation & Notes | Markdown, Text |
| Web & Frontend | HTML, CSS, JavaScript, TypeScript, JSX, TSX |
| Mobile & Cross-Platform | Dart, Kotlin, Swift |
| Backend & Languages | Python, Go, Rust, C, C++, Java, PHP |
| Scripts & Automation | Bash, Zsh |
| Data & Configs | JSON, YAML, TOML, XML, `.env`, `.gitignore` |
| DevOps & Containers | Dockerfile, Docker Compose, Makefile |

## 🧩 Requirements

- Linux desktop using **Nautilus / GNOME Files**.
- Debian/Ubuntu-based distribution for the bundled installer.
- `python3-nautilus`.
- `zenity`.

Other distributions can install equivalent dependencies with their package manager and copy `nautilus-code-new-file.py` into the Nautilus extensions directory manually.

## 🗑️ Uninstall

```bash
rm -f ~/.local/share/nautilus-python/extensions/nautilus-code-new-file.py
nautilus -q
```

Then reopen Files/Nautilus.

## 🛠️ Troubleshooting

If the menu does not appear after installation, restart Nautilus:

```bash
nautilus -q
```

Verify the extension exists:

```bash
ls ~/.local/share/nautilus-python/extensions/nautilus-code-new-file.py
```

Verify the Python file has valid syntax:

```bash
python3 -m py_compile ~/.local/share/nautilus-python/extensions/nautilus-code-new-file.py
```

## 📌 Releases

The first stable release is **v1.0.0**. See the [Releases](https://github.com/mhmdwaelanwr/nautilus-code-new-file/releases) page for source snapshots and release notes.

## 🤝 Contributing

Issues, fixes and new file-template ideas are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and pull request checklist.

If this extension saves you time, starring the repository helps other Linux developers discover it.

## 📄 License

Released under the [MIT License](LICENSE).
