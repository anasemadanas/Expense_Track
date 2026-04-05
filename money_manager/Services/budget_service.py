from data.repositories.budget_repo import BudgetRepo
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PySide6.QtWidgets import QMessageBox

class BudgetService:
    def __init__(self):
        self.repo = BudgetRepo()
        


    def create_budget(self, amount: float, month: int, year: int):

        self.validate_budget(amount, month, year)
        budget = self.check_budget(month, year)
            
        if budget.id is not None:
            result = self.show_update_confirm(amount, budget)
            if result == QMessageBox.StandardButton.Yes:
                return self.repo.create_budget(amount, month, year)
            else:
                return None

        return self.repo.create_budget(amount, month, year)

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
    
    def show_update_confirm(self, amount, budget):
        msg = QMessageBox()
        msg.setWindowTitle("Budget Already Exists")

        new_total = budget.amount + amount

        msg.setText(
            f"Budget for {budget.month}/{budget.year} already exists.\n"
            f"Do you want to update it?\n"
            f"Current amount: {budget.amount:.2f} and add amount: {amount:.2f}\n"
            f"New amount: {new_total:.2f}"
        )
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return msg.exec()
        
    # ----------------------- check if budget exists ------------------------------------------- ----
    def check_budget(self, month, year):
        return self.repo.check_budget(month, year)
    # ----------------------- update budgets after spending ------------------------------------------- ----
    def deduct_from_budget(self, amount: float, month, year):
        return self.repo.deduct_from_budget(amount, month, year)
    # ----------------------- ------------------------------------------- ----
    

    def delete_budget(self, budget_id):
        return self.repo.delete_budget(budget_id)