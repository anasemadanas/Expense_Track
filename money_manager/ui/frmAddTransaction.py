
from PySide6 import QtCore, QtGui, QtWidgets
from Services.transaction_service import TransactionService
from ui.ui_frmTransaction import Ui_AddTransaction
from PySide6.QtGui import Qt, QIcon
class AddTransaction(QtWidgets.QMainWindow,Ui_AddTransaction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.service = TransactionService
        self.btnClose.clicked.connect(self.close)
        self.setWindowTitle("Transaction")
        self.setWindowIcon(QIcon("resources\\icons\\transaction.png"))


