
from PySide6 import QtCore, QtGui, QtWidgets
from Services.transaction_service import TransactionService
from ui.ui_frmTransaction import Ui_AddTransaction
from PySide6.QtGui import QDoubleValidator, Qt, QIcon
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate


class AddTransaction(QtWidgets.QMainWindow,Ui_AddTransaction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.transaction_service = TransactionService()
        
        self.setWindowTitle("Transaction")
        self.setWindowIcon(QIcon("resources\\icons\\transaction.png"))


        now = QDate.currentDate()
        self.dateMonthTransaction.setDate(now)
        self.dateYearTransaction.setDate(now)
        
        self.chkboxCatagory.setCurrentIndex(0)
        self.txtAmountTransaction.setPlaceholderText("0000.00")
        
        validator = QDoubleValidator(0.00, 999999.99, 2)  
        self.txtAmountTransaction.setValidator(validator)
        
        self.btnSaveTransaction.clicked.connect(self.save_transaction)
        self.btnCloseTransaction.clicked.connect(self.close)
        
    def save_transaction(self):
        if self.txtAmountTransaction.text() == "":
            self.show_error("Please enter a valid amount.")
            return

        try:
            amount = float(self.txtAmountTransaction.text())
            category = self.chkboxCatagory.currentText()
            selected_month = self.dateMonthTransaction.date().month()
            selected_year = self.dateYearTransaction.date().year()


            self.transaction_service.add_transaction(amount, category, selected_month, selected_year)
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
