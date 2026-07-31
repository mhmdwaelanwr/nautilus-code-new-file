import os
import subprocess
from gi.repository import Nautilus, GObject

class CustomNewFileExtension(GObject.GObject, Nautilus.MenuProvider):
    def get_background_items(self, *args):
        folder = args[-1]
        
        parent_menu = Nautilus.MenuItem(
            name='CustomNewFileMenu',
            label='New Code File...',
            tip='Create a new developer file'
        )
        main_submenu = Nautilus.Menu()
        parent_menu.set_submenu(main_submenu)

        categories = {
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
            ]
        }

        cat_idx = 0
        for category_name, files in categories.items():
            cat_idx += 1
            cat_item = Nautilus.MenuItem(
                name=f'Category_{cat_idx}',
                label=category_name
            )
            cat_submenu = Nautilus.Menu()
            cat_item.set_submenu(cat_submenu)
            main_submenu.append_item(cat_item)

            file_idx = 0
            for label, default_name in files:
                file_idx += 1
                item = Nautilus.MenuItem(
                    name=f'File_{cat_idx}_{file_idx}',
                    label=label
                )
                item.connect('activate', self.create_file, folder, default_name)
                cat_submenu.append_item(item)

        return [parent_menu]

    def create_file(self, menu, folder, default_name):
        try:
            folder_path = folder.get_location().get_path()
        except:
            return

        cmd = [
            'zenity', '--entry',
            '--title=Create New File',
            '--text=Enter filename:',
            f'--entry-text={default_name}'
        ]
        
        res = subprocess.run(cmd, capture_output=True, text=True)
        filename = res.stdout.strip()

        if filename:
            full_path = os.path.join(folder_path, filename)
            if not os.path.exists(full_path):
                with open(full_path, 'w') as f:
                    pass
