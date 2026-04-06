
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QInputDialog, QTableWidgetItem, QVBoxLayout, QMenu, QMessageBox
from PySide6 import QtCore, QtGui, QtWidgets
from Services.transaction_service import TransactionService
from ui.ui_frmListTransaction import Ui_ListTransaction  
from Services.budget_service import BudgetService

class ListTransaction(QtWidgets.QDialog, Ui_ListTransaction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.transaction_service = TransactionService()
        self.budget_service = BudgetService()
        
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
        
        row = self.tableWidgetTransaction.currentRow()
        if row < 0:
            return
        # ------------------- EDIT -------------------
        if action == edit_action:
            id_item = self.tableWidgetTransaction.item(row, 0)
            amount_item = self.tableWidgetTransaction.item(row, 1)

            if id_item:
                try:
                    tid = int(id_item.text())
                    old_amount = float(amount_item.text())
                    month = int(self.tableWidgetTransaction.item(row, 3).text())
                    year = int(self.tableWidgetTransaction.item(row, 4).text())
                except ValueError:
                    QMessageBox.warning(self, "Error", "Invalid data in selected row!")
                    return

                self.edit_transaction(tid, old_amount, month, year)
                self.load_data()

        # ------------------- DELETE -------------------
        if action == delete_action:
            row = self.tableWidgetTransaction.currentRow()
            if row < 0:
                return

            transaction_id = int(self.tableWidgetTransaction.item(row, 0).text())
            amount = float(self.tableWidgetTransaction.item(row, 1).text())
            month = int(self.tableWidgetTransaction.item(row, 3).text())
            year = int(self.tableWidgetTransaction.item(row, 4).text())

            self.delete_transaction(transaction_id, amount, month, year)

    def delete_transaction(self, transaction_id, amount, month, year):
        msg = QMessageBox()
        msg.setWindowTitle("Confirm Delete")
        msg.setText("Are you sure you want to delete this transaction?")
        msg.setIcon(QMessageBox.Icon.Warning)
        delete_btn = msg.addButton("Delete", QMessageBox.ButtonRole.AcceptRole)
        cancel_btn = msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
        msg.setDefaultButton(cancel_btn)
        msg.exec()

        if msg.clickedButton() != delete_btn:
            return  
        
        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            "Deleting this transaction cannot be undone.\nProceed with delete?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return

        self.transaction_service.delete_transaction(transaction_id)
        self.budget_service.add_to_budget(amount, month, year)

        QMessageBox.information(self, "Deleted", "Transaction successfully deleted!")

        self.load_data()
            

    def edit_transaction(self, tid, old_amount, month, year):
        new_amount, ok = QInputDialog.getDouble(self, "Edit", "New amount:", old_amount)
        if not ok:
            return
        try:
            self.transaction_service.edit_transaction(tid, new_amount, month, year)
            QMessageBox.information(self, "Success", "Transaction updated!")
            self.load_data()
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def load_data(self):
        results = self.transaction_service.get_transactions()

        self.tableWidgetTransaction.setRowCount(0)
        self.tableWidgetTransaction.setColumnCount(5)
        self.tableWidgetTransaction.setHorizontalHeaderLabels([
            "Transaction ID", "Amount", "Category",
            "Month", "Year"
        ])
        for row_num, row_data in enumerate(results):
            self.tableWidgetTransaction.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.tableWidgetTransaction.setItem(row_num, col_num, item)


