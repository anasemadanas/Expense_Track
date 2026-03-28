import os
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

CURRENT = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT)))
DB_PATH = os.path.join(PROJECT_ROOT, "Database", "money_manager_DB.db")
DB_PATH = os.path.normpath(DB_PATH)


class Ui_AddBudget(object):

    def setupUi(self, AddBudget):
        AddBudget.setObjectName("AddBudget")
        AddBudget.resize(520, 620)
        AddBudget.setWindowTitle("New Budget")

        # ── Title ─────────────────────────────────────────────────────────────
        self.lblNewBudget = QtWidgets.QLabel(AddBudget)
        self.lblNewBudget.setGeometry(QtCore.QRect(130, 20, 260, 55))
        font_title = QtGui.QFont()
        font_title.setFamily("MV Boli")
        font_title.setPointSize(22)
        self.lblNewBudget.setFont(font_title)
        self.lblNewBudget.setStyleSheet("color: rgb(170, 0, 255);")
        self.lblNewBudget.setObjectName("lblNewBudget")

        # ── Shared fonts ──────────────────────────────────────────────────────
        font_lbl = QtGui.QFont()
        font_lbl.setPointSize(13)
        font_lbl.setBold(True)

        font_inp = QtGui.QFont()
        font_inp.setFamily("Segoe UI")
        font_inp.setPointSize(12)

        lbl_style  = "color: rgb(60, 60, 60);"
        inp_style  = (
            "background-color: #f9f9f9;"
            "border: 1px solid #aaa;"
            "border-radius: 6px;"
            "padding: 4px 8px;"
        )

        # ── helper: make label ────────────────────────────────────────────────
        def make_label(text, x, y, w=110, h=30):
            lbl = QtWidgets.QLabel(AddBudget)
            lbl.setGeometry(QtCore.QRect(x, y, w, h))
            lbl.setFont(font_lbl)
            lbl.setStyleSheet(lbl_style)
            lbl.setText(text)
            return lbl

        # ── helper: make line edit ────────────────────────────────────────────
        def make_input(x, y, w=220, h=36, placeholder=""):
            inp = QtWidgets.QLineEdit(AddBudget)
            inp.setGeometry(QtCore.QRect(x, y, w, h))
            inp.setFont(font_inp)
            inp.setStyleSheet(inp_style)
            inp.setPlaceholderText(placeholder)
            return inp

        # ── Row: Budget name ──────────────────────────────────────────────────
        make_label("Budget",   70, 100)
        self.txtBudget = make_input(200, 95, placeholder="Budget name...")

        # ── Row: Amount ───────────────────────────────────────────────────────
        make_label("Amount",   70, 165)
        self.txtAmount = make_input(200, 160, placeholder="0.00")

        # ── Row: Spent ────────────────────────────────────────────────────────
        make_label("Spent",    70, 230)
        self.txtSpent  = make_input(200, 225, placeholder="0.00 (optional)")

        # ── Row: Period ───────────────────────────────────────────────────────
        make_label("Period",   70, 295)
        self.txtPeriod = make_input(200, 290, placeholder="e.g. Monthly, Weekly...")

        # ── Status label ──────────────────────────────────────────────────────
        self.lblStatus = QtWidgets.QLabel(AddBudget)
        self.lblStatus.setGeometry(QtCore.QRect(50, 510, 420, 25))
        self.lblStatus.setText("")

        # ── Buttons ───────────────────────────────────────────────────────────
        font_btn = QtGui.QFont()
        font_btn.setFamily("Segoe UI")
        font_btn.setPointSize(13)

        btn_style_save = (
            "background-color: #4CAF50; color: white;"
            "border-radius: 8px; padding: 6px;"
        )
        btn_style_cancel = (
            "background-color: #e74c3c; color: white;"
            "border-radius: 8px; padding: 6px;"
        )

        self.btnSave = QtWidgets.QPushButton("  Save", AddBudget)
        self.btnSave.setGeometry(QtCore.QRect(100, 550, 140, 50))
        self.btnSave.setFont(font_btn)
        self.btnSave.setStyleSheet(btn_style_save)

        self.btnCancel = QtWidgets.QPushButton("  Cancel", AddBudget)
        self.btnCancel.setGeometry(QtCore.QRect(280, 550, 140, 50))
        self.btnCancel.setFont(font_btn)
        self.btnCancel.setStyleSheet(btn_style_cancel)

        # ── Signals ───────────────────────────────────────────────────────────
        self.btnSave.clicked.connect(self.save_budget)
        self.btnCancel.clicked.connect(AddBudget.close)

        self.AddBudget = AddBudget
        QtCore.QMetaObject.connectSlotsByName(AddBudget)

    # ── Save budget ───────────────────────────────────────────────────────────
    def save_budget(self):
        name     = self.txtBudget.text().strip()
        amount   = self.txtAmount.text().strip()
        spent    = self.txtSpent.text().strip() or "0"
        period   = self.txtPeriod.text().strip()

        # ── Validation ────────────────────────────────────────────────────────
        if not name:
            self._set_status("Budget name is required.", error=True)
            return
        try:
            amount_val = float(amount)
            if amount_val <= 0:
                raise ValueError
        except ValueError:
            self._set_status("Amount must be a positive number.", error=True)
            return
        try:
            spent_val = float(spent)
        except ValueError:
            self._set_status("Spent must be a number.", error=True)
            return

        try:
            os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

            conn = sqlite3.connect(DB_PATH)
            cur  = conn.cursor()

            cur.execute("""
                INSERT INTO Budget (Name, Amount, Spent, Period)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, amount_val, spent_val, period))
            conn.commit()
            conn.close()

            self._set_status("Budget saved successfully!", error=False)
            self.clear_fields()

        except Exception as e:
            self._set_status(f"Error: {e}", error=True)

    # ── Helpers ───────────────────────────────────────────────────────────────
    def clear_fields(self):
        self.txtBudget.clear()
        self.txtAmount.clear()
        self.txtSpent.clear()
        self.txtPeriod.clear()

    def _set_status(self, message, error=False):
        color = "red" if error else "green"
        self.lblStatus.setStyleSheet(f"color: {color};")
        self.lblStatus.setText(message)

