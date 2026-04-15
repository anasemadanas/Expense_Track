# theme_manager.py
import json
import os
from PySide6.QtWidgets import QColorDialog, QFontDialog

THEME_FILE = "theme.json"


class ThemeManager:

    def __init__(self, app):
        self.app = app
        self.theme = self.load_theme()

    def choose_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.theme["bg"] = color.name()
            self.theme["mode"] = "custom"
            self.save_theme()
            self.app.setStyleSheet("")
            self.apply_theme()



    def get_text_color(self, bg):
        bg = bg.lstrip("#")
        r = int(bg[0:2], 16)
        g = int(bg[2:4], 16)
        b = int(bg[4:6], 16)

        brightness = (r * 299 + g * 587 + b * 114) / 1000

        return "#000000" if brightness > 128 else "#ffffff"

    def apply_theme(self):
        mode = self.theme.get("mode", "default")

        self.app.setStyle("Fusion")

        if mode == "default":
            self.app.setStyleSheet("")
            return

        bg = self.theme.get("bg", "#f5f5f5")
        accent = self.theme.get("accent", "#2d89ef")

        if not bg or bg == "#000000":
            bg = "#f5f5f5"

        text_color = self.get_text_color(bg)

        self.app.setStyleSheet(f"""
            QWidget {{
                background-color: {bg};
                color: {text_color};
            }}

            QPushButton {{
                background-color: {accent};
                color: white;
                border-radius: 8px;
                padding: 6px;
            }}

            QLineEdit, QComboBox {{
                background-color: white;
                color: black;
            }}

            QTableWidget {{
                background-color: white;
                color: black;
            }}
        """)

    def save_theme(self):
        with open(THEME_FILE, "w") as f:
            json.dump(self.theme, f)

    def load_theme(self):
        if os.path.exists(THEME_FILE):
            with open(THEME_FILE, "r") as f:
                return json.load(f)

        return {
            "mode": "default"
        }

    def reset_theme(self):
        self.theme["mode"] = "default"
        self.save_theme()
        self.app.setStyleSheet("")
        self.apply_theme()
        