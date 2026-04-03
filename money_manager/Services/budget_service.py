from data.repositories.budget_repo import BudgetRepo
from datetime import datetime
from Services.models.budget import Budget

class BudgetService:
    def __init__(self):
        self.repo = BudgetRepo()
        
        
    def deduct_from_budget(self, amount: float, month=None, year=None):
        if month is None:
            month = datetime.now().month
        if year is None:
            year = datetime.now().year

        budget = self.get_budget(month, year)
        if not budget:
            return None
        new_amount = budget.amount - amount
        if new_amount < 0:
            new_amount = 0
            
        return self.repo.update_budget_amount(new_amount, month, year)


    def create_budget(self, amount: float, month: int = None, year: int = None):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if month is None:
            month = datetime.now().month

        if year is None:
            year = datetime.now().year
        return self.repo.create_budget(amount, month, year)

    def get_budget(self, month=None, year=None):
        if month is None:
            month = datetime.now().month
        if year is None:
            year = datetime.now().year
            
        return self.repo.get_budget(month, year)

    def get_budget_amount(self, month=None, year=None):
        budget = self.get_budget(month, year)
        if budget is None:
            return 0  
        return budget.amount 



    def delete_budget(self, budget_id):
        return self.repo.delete_budget(budget_id)