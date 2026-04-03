
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
        
        self.budget_service = BudgetService()

        budget_amount = self.budget_service.get_budget_amount(month, year)
        
        if budget_amount is None:
            raise ValueError("No budget found for this month/year")
        if amount_trans >  budget_amount :
                raise ValueError(f"Amount exceeds the available budget ({budget_amount})!")
        if amount_trans <= 0:
            raise ValueError("Amount must be greater than 0")
        if year < datetime.now().year or year > datetime.now().year + 5:
            raise ValueError("Year must be between the current year and 5 years in the future")
        
        transaction = Transaction(amount_trans, category, month, year)
        self.repo.add_transaction(transaction)

        self.budget_service.deduct_from_budget(amount_trans, month, year)
        return transaction



    def get_transactions(self):
        return self.repo.get_transactions()
    
    