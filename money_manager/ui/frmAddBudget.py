from PySide6 import QtCore, QtGui, QtWidgets
from common.activity_logger import ActivityLogger
from PySide6.QtGui import QIcon
from services.budget_service import BudgetService

from ui.ui_frmAddBudget import Ui_AddBudget
from PySide6.QtCore import QDate
from common.utils import resource_path

class AddBudget(QtWidgets.QDialog, Ui_AddBudget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.budget_service = BudgetService()
        self.btnCloseBudget.clicked.connect(self.close)
        self.btnSaveBudget.clicked.connect(self.save_budget)

        self.setWindowTitle("Add Budget")

        self.setWindowIcon(QIcon(resource_path("resources/icons/budget.png")))
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
                new_total = budget.totalamount + amount

                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Budget Already Exists")
                msg.setText(
                    f"Budget for {budget.month}/{budget.year} already exists.\n"
                    f"Do you want to update it?\n"
                    f"Current Total: {budget.totalamount:.2f}\n"
                    f"Add: {amount:.2f}\n"
                    f"New Total: {new_total:.2f}"
                )
                msg.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Yes |
                    QtWidgets.QMessageBox.StandardButton.No
                )

                if msg.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                    self.budget_service.increase_budget_total(amount, selected_month, selected_year)
                    ActivityLogger.log_budget(amount, selected_month, selected_year, "budget_updated")
                    QtWidgets.QMessageBox.information(self, "Updated", "Budget updated!")
                    self.close()

            else:
                ActivityLogger.log_budget(amount, selected_month, selected_year, "budget_created")
                QtWidgets.QMessageBox.information(self, "Success", "Budget saved!")
                self.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
            