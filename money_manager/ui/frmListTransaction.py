
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QInputDialog, QTableWidgetItem, QVBoxLayout, QMenu, QMessageBox
from PySide6 import QtCore, QtGui, QtWidgets
from services.transaction_service import TransactionService
from ui.ui_frmListTransaction import Ui_ListTransaction
from services.dashboard_service import DashBoardService
from common.utils import resource_path

class ListTransaction(QtWidgets.QDialog, Ui_ListTransaction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.transaction_service = TransactionService()
        self.dashboard_service = DashBoardService()
        self.setWindowTitle("List Transactions")
        self.setWindowIcon(QIcon(resource_path("resources/icons/transaction.png")))
        self.btnSaveList.setText("Export")
        self.btnSaveList.clicked.connect(self.save_list)
        self.btnCloseList.clicked.connect(self.close)
        self.tableWidgetTransaction.customContextMenuRequested.connect(self.show_menu)
        self.tableWidgetTransaction.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.load_data()
    # ---- ------------------------------------------------------------- ----

    def save_list(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Export Transactions",
            "Transactions.csv",
            "CSV Files (*.csv)"
        )

        if not file_path:
            return

        import csv

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            headers = []
            for col in range(self.tableWidgetTransaction.columnCount()):
                headers.append(self.tableWidgetTransaction.horizontalHeaderItem(col).text())

            writer.writerow(headers)


            for row in range(self.tableWidgetTransaction.rowCount()):
                row_data = []
                for col in range(self.tableWidgetTransaction.columnCount()):
                    item = self.tableWidgetTransaction.item(row, col)
                    row_data.append(item.text() if item else "")
                writer.writerow(row_data)

        QMessageBox.information(self, "Success", "Transactions exported successfully!")



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
            month_item = self.tableWidgetTransaction.item(row, 3)
            year_item = self.tableWidgetTransaction.item(row, 4)
            
            if any(x is None for x in [id_item, amount_item, month_item, year_item]):
                QMessageBox.warning(self, "Error", "Missing data in row!")
                return

            assert id_item is not None and amount_item is not None and month_item is not None and year_item is not None

            try:
                tid = int(id_item.text())
                old_amount = float(amount_item.text())
                month = int(month_item.text())
                year = int(year_item.text())
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
            
            id_item = self.tableWidgetTransaction.item(row, 0)
            amount_item = self.tableWidgetTransaction.item(row, 1)
            month_item = self.tableWidgetTransaction.item(row, 3)
            year_item = self.tableWidgetTransaction.item(row, 4)
            
            if any(x is None for x in [id_item, amount_item, month_item, year_item]):
                QMessageBox.warning(self, "Error", "Missing data in row!")
                return
            
            assert id_item is not None and amount_item is not None and month_item is not None and year_item is not None
            
            transaction_id = int(id_item.text())
            amount = float(amount_item.text())
            month = int(month_item.text())
            year = int(year_item.text())
            
            self.delete_transaction(transaction_id, amount, month, year)
            
    # ------------------- Call -------------------
    def edit_transaction(self, tid, old_amount, month, year):
        new_amount, ok = QInputDialog.getDouble(self, "Edit", "New amount:", old_amount)
        if not ok:
            return
        if new_amount == old_amount:
                QMessageBox.information(self, "Info", "No Change")  
                return
        warning = self.transaction_service.get_transaction_warning(old_amount, new_amount)

        if warning:
            reply = QMessageBox.question(
            self,
            "Confirm Change",
            warning,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
            )

            if reply != QMessageBox.StandardButton.Yes:
                return
        try:
            self.transaction_service.edit_transaction(tid, new_amount, month, year)
            
            QMessageBox.information(self, "Success", "Transaction updated!")
            self.load_data()
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
            
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

        QMessageBox.information(self, "Deleted", "Transaction successfully deleted!")
        self.load_data()
            
    # ------------------------ Refresh ------------------------------------
    def load_data(self):
        results = self.transaction_service.get_transactions() or []

        self.tableWidgetTransaction.setRowCount(len(results))
        self.tableWidgetTransaction.setColumnCount(5)
        self.tableWidgetTransaction.setHorizontalHeaderLabels([
            "Transaction ID", "Amount", "Category", "Month", "Year"
        ])
        for row, record in enumerate(results):
            for col, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidgetTransaction.setItem(row, col, item)
