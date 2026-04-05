
from data.repositories.transaction_repo import TransactionRepo
from Services.models.transaction import Transaction
from Services.budget_service import BudgetService
from data.repositories.budget_repo import BudgetRepo

class TransactionService:
    def __init__(self):
        self.repo = TransactionRepo()
        self.budget_service = BudgetService()
        self.budget_repo = BudgetRepo()

    # ----------------------- add transaction ------------------------------------------- ----
    def add_transaction(self, amount_trans, category, month, year):
        # Check if budget exists for the month and year
        budget = self.budget_service.check_budget(month, year)
        # Validate transaction against the budget
        self.validate_transaction(amount_trans, month, year, budget)
        # Create and add the transaction
        transaction = Transaction(amount_trans, category, month, year)
        self.repo.add_transaction(transaction)
        # Deduct the transaction amount from the budget
        self.budget_service.deduct_from_budget(amount_trans, month, year)
        return transaction
    
    def validate_transaction(self, amount_trans, month, year, budget):
        if amount_trans <= 0:
            raise ValueError("Amount must be greater than 0")
        if year < 2000 or year > 2100:
            raise ValueError("Year must be between 2000 and 2100")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        if amount_trans > budget.amount:
            raise ValueError(f"Amount exceeds the available budget ({budget.amount})!")
    
    
    # ----------------------- ------------------------------------------- ----
    def get_transactions(self):
        return self.repo.get_transactions()

    def get_budget_balance(self, month, year):
        row = self.budget_repo.get_budget_balance(month, year)
        if row:
            return row[0] 
        return 0