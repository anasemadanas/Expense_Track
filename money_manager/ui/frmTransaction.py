import os
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

CURRENT = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT)))
DB_PATH = os.path.join(PROJECT_ROOT, "Database", "money_manager_DB.db")
DB_PATH = os.path.normpath(DB_PATH)


class Ui_AddTransaction(object):

    def setupUi(self, AddTransaction):
        AddTransaction.setObjectName("AddTransaction")
        AddTransaction.resize(566, 680)
        AddTransaction.setWindowTitle("New Transaction")

        # ── Shared font ───────────────────────────────────────────────────────
        font = QtGui.QFont()
        font.setPointSize(14)

        # ── Title label ───────────────────────────────────────────────────────
        self.lblNewTransaction = QtWidgets.QLabel(AddTransaction)
        self.lblNewTransaction.setGeometry(QtCore.QRect(130, 15, 291, 51))
        font_title = QtGui.QFont()
        font_title.setFamily("MV Boli")
        font_title.setPointSize(20)
        self.lblNewTransaction.setFont(font_title)
        self.lblNewTransaction.setStyleSheet("color: rgb(170, 0, 255);")
        self.lblNewTransaction.setObjectName("lblNewTransaction")

        # ── Budget (read-only display) ────────────────────────────────────────
        self.lblBudgetTransaction = QtWidgets.QLabel(AddTransaction)
        self.lblBudgetTransaction.setGeometry(QtCore.QRect(69, 67, 131, 51))
        self.lblBudgetTransaction.setFont(font)
        self.lblBudgetTransaction.setObjectName("lblBudgetTransaction")

        self.lblBudget_ = QtWidgets.QLabel(AddTransaction)
        self.lblBudget_.setGeometry(QtCore.QRect(210, 80, 200, 25))
        self.lblBudget_.setFont(font)
        self.lblBudget_.setStyleSheet("color: rgb(0, 128, 0); font-weight: bold;")
        self.lblBudget_.setObjectName("lblBudget_")

        # ── Transaction name ──────────────────────────────────────────────────
        self.lblTransaction = QtWidgets.QLabel(AddTransaction)
        self.lblTransaction.setGeometry(QtCore.QRect(69, 120, 131, 51))
        self.lblTransaction.setFont(font)
        self.lblTransaction.setObjectName("lblTransaction")

        self.txtTransaction = QtWidgets.QLineEdit(AddTransaction)
        self.txtTransaction.setGeometry(QtCore.QRect(210, 128, 281, 36))
        self.txtTransaction.setFont(font)
        self.txtTransaction.setPlaceholderText("Transaction name...")
        self.txtTransaction.setObjectName("txtTransaction")

        # ── Amount ────────────────────────────────────────────────────────────
        self.lblAmount = QtWidgets.QLabel(AddTransaction)
        self.lblAmount.setGeometry(QtCore.QRect(70, 180, 131, 51))
        self.lblAmount.setFont(font)
        self.lblAmount.setObjectName("lblAmount")

        self.txtAmount = QtWidgets.QLineEdit(AddTransaction)
        self.txtAmount.setGeometry(QtCore.QRect(210, 190, 161, 36))
        self.txtAmount.setFont(font)
        self.txtAmount.setPlaceholderText("0.00")
        self.txtAmount.setObjectName("txtAmount")

        # ── Category ──────────────────────────────────────────────────────────
        self.lblCatagory = QtWidgets.QLabel(AddTransaction)
        self.lblCatagory.setGeometry(QtCore.QRect(70, 240, 131, 51))
        self.lblCatagory.setFont(font)
        self.lblCatagory.setObjectName("lblCatagory")

        self.txtCatagory = QtWidgets.QLineEdit(AddTransaction)
        self.txtCatagory.setGeometry(QtCore.QRect(210, 248, 161, 36))
        self.txtCatagory.setFont(font)
        self.txtCatagory.setPlaceholderText("e.g. Food, Rent...")
        self.txtCatagory.setObjectName("txtCatagory")

        # ── Date ──────────────────────────────────────────────────────────────
        self.lblDate = QtWidgets.QLabel(AddTransaction)
        self.lblDate.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.lblDate.setFont(font)
        self.lblDate.setObjectName("lblDate")

        self.DateTransaction = QtWidgets.QDateEdit(AddTransaction)
        self.DateTransaction.setGeometry(QtCore.QRect(210, 310, 171, 41))
        font_date = QtGui.QFont()
        font_date.setPointSize(12)
        self.DateTransaction.setFont(font_date)
        self.DateTransaction.setCalendarPopup(True)
        self.DateTransaction.setDate(QtCore.QDate.currentDate())
        self.DateTransaction.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.DateTransaction.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.DateTransaction.setDisplayFormat("dd-MMM-yyyy")
        self.DateTransaction.setObjectName("DateTransaction")

        # ── Type ──────────────────────────────────────────────────────────────
        self.lblType = QtWidgets.QLabel(AddTransaction)
        self.lblType.setGeometry(QtCore.QRect(80, 360, 111, 51))
        self.lblType.setFont(font)
        self.lblType.setObjectName("lblType")

        self.txtType = QtWidgets.QComboBox(AddTransaction)
        self.txtType.setGeometry(QtCore.QRect(210, 370, 161, 36))
        self.txtType.setFont(font)
        self.txtType.addItems(["Expense", "Income"])
        self.txtType.setObjectName("txtType")

        # ── Currency ──────────────────────────────────────────────────────────
        self.lblCurrency = QtWidgets.QLabel(AddTransaction)
        self.lblCurrency.setGeometry(QtCore.QRect(70, 420, 111, 51))
        self.lblCurrency.setFont(font)
        self.lblCurrency.setObjectName("lblCurrency")

        self.lblCurrency_ = QtWidgets.QComboBox(AddTransaction)
        self.lblCurrency_.setGeometry(QtCore.QRect(210, 430, 161, 36))
        self.lblCurrency_.setFont(font)
        self.lblCurrency_.addItems(["USD", "JOD", "EUR", "GBP", "SAR"])
        self.lblCurrency_.setObjectName("lblCurrency_")

        # ── Note ──────────────────────────────────────────────────────────────
        self.lblNoteTransaction = QtWidgets.QLabel(AddTransaction)
        self.lblNoteTransaction.setGeometry(QtCore.QRect(40, 490, 111, 51))
        self.lblNoteTransaction.setFont(font)
        self.lblNoteTransaction.setStyleSheet("color: rgb(0, 150, 0);")
        self.lblNoteTransaction.setObjectName("lblNoteTransaction")

        self.txtNote = QtWidgets.QTextEdit(AddTransaction)
        self.txtNote.setGeometry(QtCore.QRect(160, 493, 341, 91))
        font_note = QtGui.QFont()
        font_note.setFamily("Segoe UI")
        font_note.setPointSize(11)
        self.txtNote.setFont(font_note)
        self.txtNote.setPlaceholderText("Optional note...")
        self.txtNote.setObjectName("txtNote")

        # ── Status label ──────────────────────────────────────────────────────
        self.lblStatus = QtWidgets.QLabel(AddTransaction)
        self.lblStatus.setGeometry(QtCore.QRect(60, 590, 450, 25))
        self.lblStatus.setStyleSheet("color: green;")
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")

        # ── Buttons ───────────────────────────────────────────────────────────
        font_btn = QtGui.QFont()
        font_btn.setFamily("Nirmala UI Semilight")
        font_btn.setPointSize(14)

        self.btnSave = QtWidgets.QPushButton(AddTransaction)
        self.btnSave.setGeometry(QtCore.QRect(100, 620, 151, 51))
        self.btnSave.setFont(font_btn)
        self.btnSave.setObjectName("btnSave")

        self.btnClose = QtWidgets.QPushButton(AddTransaction)
        self.btnClose.setGeometry(QtCore.QRect(310, 620, 151, 51))
        self.btnClose.setFont(font_btn)
        self.btnClose.setObjectName("btnClose")

        # ── Signals ───────────────────────────────────────────────────────────
        self.btnSave.clicked.connect(self.save_transaction)
        self.btnClose.clicked.connect(AddTransaction.close)

        self.AddTransaction = AddTransaction
        self.retranslateUi(AddTransaction)
        QtCore.QMetaObject.connectSlotsByName(AddTransaction)

    # ── Translations ──────────────────────────────────────────────────────────
    def retranslateUi(self, AddTransaction):
        _translate = QtCore.QCoreApplication.translate
        AddTransaction.setWindowTitle(_translate("AddTransaction", "New Transaction"))
        self.lblNewTransaction.setText(_translate("AddTransaction", "New Transaction"))
        self.lblBudgetTransaction.setText(_translate("AddTransaction", "Budget"))
        self.lblBudget_.setText(_translate("AddTransaction", "—"))
        self.lblTransaction.setText(_translate("AddTransaction", "Transaction"))
        self.lblAmount.setText(_translate("AddTransaction", "Amount"))
        self.lblCatagory.setText(_translate("AddTransaction", "Category"))
        self.lblDate.setText(_translate("AddTransaction", "Date"))
        self.lblType.setText(_translate("AddTransaction", "Type"))
        self.lblCurrency.setText(_translate("AddTransaction", "Currency"))
        self.lblNoteTransaction.setText(_translate("AddTransaction", "Note"))
        self.btnSave.setText(_translate("AddTransaction", "Save"))
        self.btnClose.setText(_translate("AddTransaction", "Close"))

    # ── Save transaction to DB ────────────────────────────────────────────────
    def save_transaction(self):
        name     = self.txtTransaction.text().strip()
        amount   = self.txtAmount.text().strip()
        category = self.txtCatagory.text().strip()
        date     = self.DateTransaction.date().toString("yyyy-MM-dd")
        t_type   = self.txtType.currentText()
        currency = self.lblCurrency_.currentText()
        note     = self.txtNote.toPlainText().strip()

        # ── Basic validation ──────────────────────────────────────────────────
        if not name:
            self._set_status("Transaction name is required.", error=True)
            return
        try:
            amount_val = float(amount)
            if amount_val <= 0:
                raise ValueError
        except ValueError:
            self._set_status("Amount must be a positive number.", error=True)
            return
        if not category:
            self._set_status("Category is required.", error=True)
            return

        # ── Save to database ──────────────────────────────────────────────────
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Transactions (
                    Trans_ID   INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name       TEXT    NOT NULL,
                    Amount     REAL    NOT NULL,
                    Category   TEXT,
                    Date       TEXT,
                    Type       TEXT,
                    Currency   TEXT,
                    Note       TEXT
                )
            """)
            cur.execute("""
                INSERT INTO Transactions (Name, Amount, Category, Date, Type, Currency, Note)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, amount_val, category, date, t_type, currency, note))
            conn.commit()
            conn.close()
            self._set_status("Transaction saved successfully!", error=False)
            self.clear_fields()
        except Exception as e:
            self._set_status(f"DB Error: {e}", error=True)

    # ── Helpers ───────────────────────────────────────────────────────────────
    def clear_fields(self):
        self.txtTransaction.clear()
        self.txtAmount.clear()
        self.txtCatagory.clear()
        self.txtNote.clear()
        self.DateTransaction.setDate(QtCore.QDate.currentDate())
        self.txtType.setCurrentIndex(0)
        self.lblCurrency_.setCurrentIndex(0)

    def _set_status(self, message, error=False):
        color = "red" if error else "green"
        self.lblStatus.setStyleSheet(f"color: {color};")
        self.lblStatus.setText(message)


