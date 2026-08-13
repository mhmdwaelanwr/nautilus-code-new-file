"""File template definitions for Nautilus Code New File.

Each template maps a (label, default_filename) pair to an optional content
string. When content is None the file is created empty (blank file).
"""

# ---------------------------------------------------------------------------
# Category mapping used by the Nautilus menu
# ---------------------------------------------------------------------------

CATEGORIES: dict[str, list[tuple[str, str]]] = {
    "Documentation & Notes": [
        ("Markdown (.md)", "README.md"),
        ("Text (.txt)", "notes.txt"),
    ],
    "Web & Frontend": [
        ("HTML (.html)", "index.html"),
        ("CSS (.css)", "style.css"),
        ("JavaScript (.js)", "app.js"),
        ("TypeScript (.ts)", "app.ts"),
        ("React/Vue (.jsx)", "Component.jsx"),
        ("React (.tsx)", "Component.tsx"),
    ],
    "Mobile & Cross-Platform": [
        ("Dart (.dart)", "main.dart"),
        ("Kotlin (.kt)", "Main.kt"),
        ("Swift (.swift)", "Main.swift"),
    ],
    "Backend & Languages": [
        ("Python (.py)", "main.py"),
        ("Go (.go)", "main.go"),
        ("Rust (.rs)", "main.rs"),
        ("C++ (.cpp)", "main.cpp"),
        ("C (.c)", "main.c"),
        ("Java (.java)", "Main.java"),
        ("PHP (.php)", "index.php"),
    ],
    "Scripts & Automation": [
        ("Bash Script (.sh)", "script.sh"),
        ("Zsh Script (.zsh)", "script.zsh"),
    ],
    "Data & Configs": [
        ("JSON (.json)", "data.json"),
        ("YAML (.yaml)", "config.yaml"),
        ("TOML (.toml)", "config.toml"),
        ("XML (.xml)", "data.xml"),
        ("Env File (.env)", ".env"),
        ("Git Ignore (.gitignore)", ".gitignore"),
    ],
    "DevOps & Containers": [
        ("Docker (Dockerfile)", "Dockerfile"),
        ("Docker Compose (.yaml)", "docker-compose.yaml"),
        ("Makefile", "Makefile"),
    ],
}

# ---------------------------------------------------------------------------
# Skeleton templates keyed by default filename
# ---------------------------------------------------------------------------

TEMPLATES: dict[str, str] = {
    # Web & Frontend
    "index.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Hello</h1>
</body>
</html>
""",
    "style.css": """\
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: system-ui, sans-serif;
}
""",
    "app.js": """\
'use strict';

function main() {
  console.log('Hello');
}

main();
""",
    "app.ts": """\
function main(): void {
  console.log('Hello');
}

main();
""",
    "Component.jsx": """\
export default function Component() {
  return <div>Component</div>;
}
""",
    "Component.tsx": """\
import React from 'react';

interface ComponentProps {}

export default function Component({}: ComponentProps) {
  return <div>Component</div>;
}
""",
    # Backend & Languages
    "main.py": """\
def main():
    print("Hello")


if __name__ == "__main__":
    main()
""",
    "main.go": """\
package main

import "fmt"

func main() {
\tfmt.Println("Hello")
}
""",
    "main.rs": """\
fn main() {
\tprintln!("Hello");
}
""",
    "main.cpp": """\
#include <iostream>

int main() {
\tstd::cout << "Hello" << std::endl;
\treturn 0;
}
""",
    "main.c": """\
#include <stdio.h>

int main(void) {
\tprintf("Hello\\n");
\treturn 0;
}
""",
    "Main.java": """\
public class Main {
\tpublic static void main(String[] args) {
\t\tSystem.out.println("Hello");
\t}
}
""",
    "index.php": """\
<?php
echo "Hello";
""",
    "main.dart": """\
void main() {
\tprint('Hello');
}
""",
    "Main.kt": """\
fun main() {
\tprintln("Hello")
}
""",
    "Main.swift": """\
import Foundation

print("Hello")
""",
    # Scripts
    "script.sh": """\
#!/usr/bin/env bash
set -euo pipefail

echo "Hello"
""",
    "script.zsh": """\
#!/usr/bin/env zsh
set -euo pipefail

echo "Hello"
""",
    # DevOps
    "Dockerfile": """\
FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python3", "main.py"]
""",
    "docker-compose.yaml": """\
services:
  app:
    build: .
    ports:
      - "8000:8000"
""",
    "Makefile": """\
.PHONY: help
help:
\t@echo "No targets defined"
""",
    # Data & Configs
    "data.json": """\
{
}
""",
    "config.yaml": """\
---
""",
    "config.toml": """\
""",
    "data.xml": """\
<?xml version="1.0" encoding="UTF-8"?>
<root>
</root>
""",
    ".env": """\
""",
    ".gitignore": """\
__pycache__/
*.pyc
node_modules/
.env
""",
    "README.md": """\
# Project

Description.
""",
    "notes.txt": """\
""",
}


def get_template(default_name: str) -> str | None:
    """Return skeleton content for *default_name*, or None for blank files."""
    return TEMPLATES.get(default_name)
