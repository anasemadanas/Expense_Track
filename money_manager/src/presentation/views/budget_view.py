from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget
from src.presentation.controllers.budget_controller import BudgetController

class BudgetView(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.controller = BudgetController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.name_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.add_btn = QPushButton("Add Budget")
        self.list_widget = QListWidget()

        layout.addWidget(QLabel("Budget Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Amount:"))
        layout.addWidget(self.amount_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)
        self.add_btn.clicked.connect(self.add_budget)
        self.load_budgets()

    def add_budget(self):
        name = self.name_input.text()
        amount = float(self.amount_input.text())
        self.controller.add_budget(name, amount, self.user_id)
        self.load_budgets()

    def load_budgets(self):
        self.list_widget.clear()
        budgets = self.controller.get_budgets_by_user(self.user_id)
        for b in budgets:
            self.list_widget.addItem(f"{b['name']} - {b['amount']} - Spent: {b['spent']}")