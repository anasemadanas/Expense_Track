from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget
from src.presentation.controllers.transaction_controller import TransactionController

class TransactionView(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.controller = TransactionController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.category_input = QLineEdit()
        self.add_btn = QPushButton("Add Transaction")
        self.list_widget = QListWidget()

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Amount:"))
        layout.addWidget(self.amount_input)
        layout.addWidget(QLabel("Category:"))
        layout.addWidget(self.category_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)
        self.add_btn.clicked.connect(self.add_transaction)
        self.load_transactions()

    def add_transaction(self):
        name = self.name_input.text()
        amount = float(self.amount_input.text())
        category = self.category_input.text()
        self.controller.add_transaction(name, amount, category, "expense", self.user_id)
        self.load_transactions()

    def load_transactions(self):
        self.list_widget.clear()
        transactions = self.controller.get_transactions_by_user(self.user_id)
        for t in transactions:
            self.list_widget.addItem(f"{t['name']} - {t['amount']} - {t['category']}")