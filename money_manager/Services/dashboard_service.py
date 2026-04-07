from PySide6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import csv
from data.repositories.transaction_repo import TransactionRepo
from data.repositories.budget_repo import BudgetRepo
class DashBoardService:
    def __init__(self):
        self.transaction_repo =  TransactionRepo()
        self.budget_repo = BudgetRepo()
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



    # ------------------ Data Access Methods ------------------------------------------
    def get_all_transactions(self):
        return self.transaction_repo.get_transactions()


    def get_transactions_for_month(self, month, year):
        return self.transaction_repo.get_transactions_by_month(month, year)


    def get_current_month_balance(self):
        now = datetime.now()
        return self.get_balance_for_month(now.month, now.year)

    def get_balance_for_month(self, month, year):
        transactions = self.get_transactions_for_month(month, year)
        income = sum(t['amount'] for t in transactions if t['amount'] > 0)
        expense = sum(-t['amount'] for t in transactions if t['amount'] < 0)
        net = income - expense
        return {"income": income, "expense": expense, "net": net}

    def get_budget_for_category(self, month, year):
        return self.budget_repo.get_budget(month, year)
        

