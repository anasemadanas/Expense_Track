from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon
from Services.budget_service import BudgetService
from ui.ui_frmAddBudget import Ui_AddBudget
from PySide6.QtCore import QDate

class AddBudget(QtWidgets.QDialog, Ui_AddBudget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.budget_service = BudgetService()
        self.btnCloseBudget.clicked.connect(self.close)
        self.btnSaveBudget.clicked.connect(self.save_budget)

        self.setWindowTitle("Add Budget")
        self.setWindowIcon(QIcon("resources\\icons\\budget.png"))

        self.txtAmountBugdet.setValidator(QtGui.QDoubleValidator(0.00, 999999.99, 2))
        self.txtAmountBugdet.setPlaceholderText("0000.00")
        
        now = QDate.currentDate()
        self.dateMonthBugdet.setDate(now)
        self.dateYear.setDate(now)
    # ---- ------------------------------------------------------------- ----
        
    def save_budget(self):
        amount_text = self.txtAmountBugdet.text().strip()

        if not amount_text:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter amount")
            return

        try:
            amount = float(amount_text)
            selected_month = self.dateMonthBugdet.date().month()
            selected_year = self.dateYear.date().year()

            result = self.budget_service.create_budget(amount, selected_month, selected_year)

  
            if result["exists"]:
                budget = result["budget"]
                new_total = budget.amount + amount

                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Budget Already Exists")
                msg.setText(
                    f"Budget for {budget.month}/{budget.year} already exists.\n"
                    f"Do you want to update it?\n"
                    f"Current: {budget.amount:.2f}\n"
                    f"Add: {amount:.2f}\n"
                    f"New: {new_total:.2f}"
                )
                msg.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Yes |
                    QtWidgets.QMessageBox.StandardButton.No
                )

                if msg.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                    self.budget_service.add_to_budget(amount, selected_month, selected_year)
                    QtWidgets.QMessageBox.information(self, "Updated", "Budget updated!")
                    self.close()

            else:
                QtWidgets.QMessageBox.information(self, "Success", "Budget saved!")
                self.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
            
