
from Services.models import transaction
from data.repositories.transaction_repo import TransactionRepo
from Services.models.transaction import Transaction
from Services.budget_service import BudgetService


from datetime import datetime

class TransactionService:
    def __init__(self):
        self.repo = TransactionRepo()
        self.budget_service = BudgetService()

    def add_transaction(self, amount_trans, category, month, year):
        budget = self.budget_service.get_budget(month, year)

        if budget is None:
            raise ValueError("No available budget for this month/year")
        if amount_trans > budget.amount:
            raise ValueError(f"Amount exceeds the available budget ({budget.amount})!")
        if amount_trans <= 0:
            raise ValueError("Amount must be greater than 0")
        if year < 2000 or year > 2100:
            raise ValueError("Year must be between 2000 and 2100")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        
        transaction = Transaction(amount=amount_trans, category=category, month=month, year=year)
        self.repo.add_transaction(transaction)
        self.budget_service.deduct_from_budget(amount_trans, month, year)

        return transaction

