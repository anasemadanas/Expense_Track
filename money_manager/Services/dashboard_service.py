from PySide6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import csv
from data.repositories.transaction_repo import TransactionRepo

class DashBoardService:
    def __init__(self, transaction_repo=None):
        self.transaction_repo = transaction_repo or TransactionRepo()

    # ------------------ Dashboard Actions ------------------------------------------
    def show_about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About This App")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(
            "Expense Manager v1.0\n\n"
            "A simple tool for managing expenses and tracking your budget.\n"
            "Developer: Team Student\n\n"
            "Click below to visit my GitHub page:"
        )
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        btn_link = msg.addButton("Open GitHub", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        msg.exec()
        if msg.clickedButton() == btn_link:
            QtGui.QDesktopServices.openUrl(
                QtCore.QUrl("https://github.com/anasemadanas/Expense_Track")
            )

    def open_guide(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Guide")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Click below to visit my GitHub page:")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        btn_link = msg.addButton("Open Guide", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        msg.exec()
        if msg.clickedButton() == btn_link:
            QtGui.QDesktopServices.openUrl(
                QtCore.QUrl("https://github.com/anasemadanas/Expense_Track/blob/main/docs/project_document.md")
            )

    def save_data(self):
        transactions = self.get_all_transactions()
        if not transactions:
            print("No transactions to save.")
            return

        file, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save Transactions", "Transactions.txt", "Text Files (*.txt);;All Files (*)"
        )
        if not file:
            return

        with open(file, 'w', encoding='utf-8') as f:
            for t in transactions:
                line = " | ".join(f"{k}: {v}" for k, v in t.items())
                f.write(line + "\n")

        print(f"Transactions saved to {file}")

    def export_data(self):
        """Export all transactions to CSV"""
        transactions = self.get_all_transactions()
        if not transactions:
            print("No transactions to export.")
            return

        file, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "Export Data", "Transactions.csv", "CSV Files (*.csv);;All Files (*)"
        )
        if not file:
            return

        keys = transactions[0].keys()
        with open(file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(transactions)

        print(f"Transactions exported to {file}")
    # ----------------------------------------------------------------- ----


    # ------------------ Data Access Methods ------------------------------------------
    def get_all_transactions(self):
        if self.transaction_repo:
            return self.transaction_repo.get_transactions()
        return []

    def get_transactions_for_month(self, month, year):
        if self.transaction_repo:
            return self.transaction_repo.get_transactions_by_month(month, year)
        return []

    def get_current_month_balance(self):
        income = 1200
        expense = 750
        net = income - expense
        return {"income": income, "expense": expense, "net": net}

    def get_available_months(self, transactions=None):
        transactions = transactions or self.get_all_transactions()
        months = set()
        for t in transactions:
            dt = datetime.strptime(t['date'], "%Y-%m-%d")
            months.add(dt.month)
        return sorted(list(months))


    def get_budget_for_category(self, category, year):
        return 500
    
