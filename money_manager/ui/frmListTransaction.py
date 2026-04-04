
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QTableWidgetItem, QVBoxLayout, QMenu, QMessageBox
from PySide6 import QtCore, QtGui, QtWidgets

from Services.transaction_service import TransactionService
from ui.ui_frmListTransaction import Ui_ListTransaction  

class ListTransaction(QtWidgets.QDialog, Ui_ListTransaction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.service = TransactionService()
        
        self.setWindowTitle("List Transactions")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))
        self.btnSaveList.setText("Export")
        self.btnSaveList.clicked.connect(self.save_list)
        self.btnCloseList.clicked.connect(self.close)
        self.tableWidgetTransaction.customContextMenuRequested.connect(self.show_menu)
        self.tableWidgetTransaction.setContextMenuPolicy(Qt.CustomContextMenu)
        self.load_data()
    # ---- ------------------------------------------------------------- ----

    def save_list(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Transactions exported successfully!")
        msg.exec()



    def show_menu(self, position):
        menu = QMenu()
        edit_action = menu.addAction("Edit")
        delete_action = menu.addAction("Delete")
        action = menu.exec(self.tableWidgetTransaction.viewport().mapToGlobal(position))

        if action == edit_action:
            print("Edit clicked")
        elif action == delete_action:
            row = self.tableWidgetTransaction.currentRow()
            transaction_id_item = self.tableWidgetTransaction.item(row, 0)
            if transaction_id_item:
                transaction_id = int(transaction_id_item.text())
                self.delete_transaction(transaction_id)

            
    def load_data(self):
       
        results = self.service.get_transactions()

        self.tableWidgetTransaction.setRowCount(0)
        self.tableWidgetTransaction.setColumnCount(7)
        self.tableWidgetTransaction.setHorizontalHeaderLabels([
            "Transaction ID", "Amount", "Category",
            "Month", "Year", "Budget ID", "Total Amount"
        ])
        for row_num, row_data in enumerate(results):
            self.tableWidgetTransaction.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.tableWidgetTransaction.setItem(row_num, col_num, item)


    def delete_transaction(self, transaction_id):
        from data.repositories.transaction_repo import TransactionRepo
        repo = TransactionRepo()
        repo.delete_transaction(transaction_id)
        self.load_data()  