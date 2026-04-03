from PySide6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import random

class DashBoardService:
    def __init__(self):
        pass


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

    def save_data(self):
        print("Saving…")

    def open_guide(self):
        url = QtCore.QUrl("https://github.com/anasemadanas/Expense_Track")
        QtGui.QDesktopServices.openUrl(url)

    def export_data(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Export Data",
            "Summary_Budget.csv",
            "CSV Files (*.csv);;All Files (*)"
        )
        if file:
            print("Export to:", file)




    def get_current_month_balance(self):

        income = 1200
        expense = 750
        net = income - expense

        return {
            "income": income,
            "expense": expense,
            "net": net
        }

    def get_spending_by_category(self):

        return [
            {"category": "Food", "total": 200},
            {"category": "Transport", "total": 150},
            {"category": "Shopping", "total": 300},
            {"category": "Bills", "total": 100},
        ]

    def get_budget_vs_actual(self):

        return [
            {"category": "Food",      "budget": 300, "actual": 200},
            {"category": "Transport", "budget": 200, "actual": 150},
            {"category": "Shopping",  "budget": 400, "actual": 300},
        ]

    def get_monthly_spending_saving(self):

        months = ["Jan","Feb","Mar","Apr","May","Jun",
                  "Jul","Aug","Sep","Oct","Nov","Dec"]

        rows = []
        for m in months:
            expense = random.randint(200, 600)
            saving  = random.randint(100, 500)
            rows.append({
                "month": m,
                "expense": expense,
                "saving": saving
            })

        return rows
    
    def get_available_months(self, transactions: list):
  
        months = set()

        for t in transactions:
            dt = datetime.strptime(t['date'], "%Y-%m-%d")
            months.add(dt.month)

        return sorted(list(months))
    