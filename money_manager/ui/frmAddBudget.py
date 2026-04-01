
from PySide6 import QtCore, QtGui, QtWidgets
from Services.budget_service import BudgetService
from ui.ui_frmBudget import Ui_AddBudget
from PySide6.QtGui import Qt, QIcon

class AddBudget(QtWidgets.QMainWindow,Ui_AddBudget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.service = BudgetService
        self.btnOkCnacel.clicked.connect(self.close)
        self.setWindowTitle("Budget")
        self.setWindowIcon(QIcon("resources\\icons\\budget.png"))
        
    def save_budget(self):
        print("Budget saved!")