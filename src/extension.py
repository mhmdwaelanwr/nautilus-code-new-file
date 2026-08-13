"""Nautilus extension: adds 'New Code File...' to the folder context menu."""

from __future__ import annotations

from gi.repository import GObject, Nautilus

from .file_creator import create_file
from .templates import CATEGORIES


class CustomNewFileExtension(GObject.GObject, Nautilus.MenuProvider):
    """Provides a right-click menu to create developer files."""

    def get_background_items(self, *args):  # noqa: ANN002, ANN201
        folder = args[-1]

        parent_menu = Nautilus.MenuItem(
            name="CustomNewFileMenu",
            label="New Code File...",
            tip="Create a new developer file",
        )
        main_submenu = Nautilus.Menu()
        parent_menu.set_submenu(main_submenu)

        for cat_idx, (category_name, files) in enumerate(CATEGORIES.items(), start=1):
            cat_item = Nautilus.MenuItem(
                name=f"Category_{cat_idx}",
                label=category_name,
            )
            cat_submenu = Nautilus.Menu()
            cat_item.set_submenu(cat_submenu)
            main_submenu.append_item(cat_item)

            for file_idx, (label, default_name) in enumerate(files, start=1):
                item = Nautilus.MenuItem(
                    name=f"File_{cat_idx}_{file_idx}",
                    label=label,
                )
                item.connect("activate", self._on_activate, folder, default_name)
                cat_submenu.append_item(item)

        return [parent_menu]

    # ------------------------------------------------------------------
    # Internal callbacks
    # ------------------------------------------------------------------

    @staticmethod
    def _on_activate(_menu, folder, default_name: str) -> None:
        try:
            folder_path = folder.get_location().get_path()
        except Exception:  # noqa: BLE001
            return
        if folder_path is None:
            return
        create_file(folder_path, default_name)
