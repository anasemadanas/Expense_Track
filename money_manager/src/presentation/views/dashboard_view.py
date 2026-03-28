from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from src.presentation.controllers.transaction_controller import TransactionController
from src.presentation.controllers.budget_controller import BudgetController

class DashboardView(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.trans_controller = TransactionController()
        self.budget_controller = BudgetController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.income_label = QLabel()
        self.expense_label = QLabel()
        self.balance_label = QLabel()

        layout.addWidget(self.income_label)
        layout.addWidget(self.expense_label)
        layout.addWidget(self.balance_label)

        self.setLayout(layout)
        self.refresh_dashboard()

    def refresh_dashboard(self):
        transactions = self.trans_controller.get_transactions_by_user(self.user_id)
        total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
        total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
        balance = total_income - total_expense

        self.income_label.setText(f"Total Income: {total_income}")
        self.expense_label.setText(f"Total Expenses: {total_expense}")
        self.balance_label.setText(f"Balance: {balance}")