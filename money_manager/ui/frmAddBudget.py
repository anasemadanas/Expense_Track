from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon
from Services.budget_service import BudgetService
from ui.ui_frmAddBudget import Ui_AddBudget
from PySide6.QtCore import QDate

class AddBudget(QtWidgets.QDialog, Ui_AddBudget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.service = BudgetService()
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
            
            if amount > 0 and self.service.create_budget(amount, selected_month, selected_year):
                QtWidgets.QMessageBox.information(self, "Success", "Budget saved!")
                self.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
