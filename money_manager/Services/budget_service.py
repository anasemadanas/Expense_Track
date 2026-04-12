from repository.budget_repo import BudgetRepo
from datetime import datetime
from dateutil.relativedelta import relativedelta
from services.IBudgetService import IBudgetService

class BudgetService(IBudgetService):
    def __init__(self):
        self.budget_repo  = BudgetRepo()


    def create_budget(self, amount: float, month: int, year: int):
            self.validate_budget(amount, month, year)
            budget = self.check_budget(month, year)

            if budget and budget.id is not None:
                return {
                    "exists": True,
                    "budget": budget
                }

            new_budget = self.budget_repo.create_budget(amount, month, year)

            return {
                "exists": False,
                "budget": new_budget
            }
  

    def validate_budget(self, amount, month, year):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if month is None:
            month = datetime.now().month
        if year is None:
            year = datetime.now().year
        if year < 2000 or year > 2100:
            raise ValueError("Year must be between 2000 and 2100")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        if amount > 1000000.00:
            raise ValueError("Amount must be less than 1,000,000")
        now = datetime.now()
        selected = datetime(year, month, 1)
        min_date = datetime(now.year, now.month, 1) - relativedelta(months=6)
        max_date = datetime(now.year, now.month, 1) + relativedelta(years=2)
        
        if selected < min_date or selected > max_date:
            raise ValueError("Date must be within 6 months in the past and 2 years in the future")
    

    # ----------------------- check if budget exists and update budgets after spending ------------------------------------------- ----
    def check_budget(self, month, year):
        return self.budget_repo.check_budget(month, year)
    
    def deduct_from_budget(self, amount: float, month, year):
        return self.budget_repo.deduct_from_budget(amount, month, year)
    
    def add_to_budget(self, amount, month, year):
        return self.budget_repo.add_to_budget(amount, month, year)


    # ----------------------- future --------------------------------- ----
    def get_budget_balance(self,  month, year):
        return self.budget_repo.get_budget_balance( month, year)
    
    def delete_budget(self, budget_id):
        return self.budget_repo.delete_budget(budget_id)
    
    def update_budget(self, budget_id, amount):
        return self.budget_repo.update_budget(budget_id, amount)