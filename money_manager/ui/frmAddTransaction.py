
from PySide6 import QtCore, QtGui, QtWidgets
from services.activity_logger import ActivityLogger
from services.transaction_service import TransactionService

from ui.ui_frmAddTransaction import Ui_AddTransaction
from PySide6.QtGui import QDoubleValidator, Qt, QIcon
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate


class AddTransaction(QtWidgets.QDialog,Ui_AddTransaction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.transaction_service = TransactionService()
        
        self.setWindowTitle("Transaction")
        self.setWindowIcon(QIcon("resources\\icons\\transaction.png"))

        now = QDate.currentDate()
        self.dateMonthTransaction.setDate(now)
        self.dateYearTransaction.setDate(now)
        
        self.cmbboxCatagory.setCurrentIndex(0)
        self.txtAmountTransaction.setPlaceholderText("0000.00")
        
        validator = QDoubleValidator(0.00, 999999.99, 2)  
        self.txtAmountTransaction.setValidator(validator)
        
        self.btnSaveTransaction.clicked.connect(self.save_transaction)
        self.btnCloseTransaction.clicked.connect(self.close)
        self.dateMonthTransaction.dateChanged.connect(self.update_budget_balance_label)
        self.dateYearTransaction.dateChanged.connect(self.update_budget_balance_label)
        
        self.update_budget_balance_label()
        self.prompt_for_missing_budget()

    # ---- ------------------------------------------------------------- ----
    def selected_month_year(self):
        return (
            self.dateMonthTransaction.date().month(),
            self.dateYearTransaction.date().year()
        )

    def update_budget_balance_label(self):
        month, year = self.selected_month_year()
        balance = self.transaction_service.get_budget_balance(month, year)
        if balance <= 0:
            self.lblTotalAmountBudget.setText("No budget")
        else:
            self.lblTotalAmountBudget.setText(f"{balance:.2f}")

    def has_budget_for_selected_month(self):
        month, year = self.selected_month_year()
        budget = self.transaction_service.budget_service.check_budget(month, year)
        return budget is not None and budget.id is not None and budget.totalamount > 0

    def prompt_for_missing_budget(self):
        if self.has_budget_for_selected_month():
            return

        month, year = self.selected_month_year()
        msg = QMessageBox(self)
        msg.setWindowTitle("No Budget Found")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(
            f"No budget exists for {month}/{year}.\n"
            "Please add a budget for this month before adding a transaction."
        )
        add_budget_button = msg.addButton("Add Budget", QMessageBox.ButtonRole.AcceptRole)
        msg.addButton(QMessageBox.StandardButton.Cancel)
        msg.exec()

        if msg.clickedButton() == add_budget_button:
            from ui.frmAddBudget import AddBudget

            budget_dialog = AddBudget()
            budget_dialog.exec()
            self.update_budget_balance_label()
            
    def save_transaction(self):
        if self.txtAmountTransaction.text() == "":
            self.show_error("Please enter a valid amount.")
            return
        
        if not self.has_budget_for_selected_month():
            self.prompt_for_missing_budget()
            return
            
        try:
            amount = float(self.txtAmountTransaction.text())
            category = self.cmbboxCatagory.currentText()
            selected_month = self.dateMonthTransaction.date().month()
            selected_year = self.dateYearTransaction.date().year()

            warning_message = self.transaction_service.get_budget_warning(
                amount,
                selected_month,
                selected_year
            )
            if warning_message:
                msg = QMessageBox(self)
                msg.setWindowTitle("Budget Warning")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText(warning_message)
                continue_button = msg.addButton("Continue", QMessageBox.ButtonRole.AcceptRole)
                msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
                msg.exec()

                if msg.clickedButton() != continue_button:
                    return

            self.transaction_service.add_transaction(amount, category, selected_month, selected_year)
            ActivityLogger.log_transaction(amount, category, selected_month, selected_year)
            QtWidgets.QMessageBox.information(self, "Success", "Transaction saved!")
            self.close()
        except ValueError as e:
            self.show_error(str(e))
            return


    def show_error(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()
