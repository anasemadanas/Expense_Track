from data.repositories.budget_repo import BudgetRepo
from datetime import datetime
from Services.models.budget import Budget
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PySide6.QtWidgets import QMessageBox
class BudgetService:
    def __init__(self):
        self.repo = BudgetRepo()
        
        
    def deduct_from_budget(self, amount: float, month=None, year=None):
        if month is None:
            month = datetime.now().month
        if year is None:
            year = datetime.now().year

        return self.repo.update_budget_amount(amount, month, year)



    def create_budget(self, amount: float, month: int = None, year: int = None):
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

        now = datetime.now()
        selected = datetime(year, month, 1)
        min_date = datetime(now.year, now.month, 1) - relativedelta(months=6)
        max_date = datetime(now.year, now.month, 1) + relativedelta(years=2)
        
        if selected < min_date or selected > max_date:
            raise ValueError("Date must be within 6 months in the past and 2 years in the future")

        if self.get_budget(month, year):
            result = self.show_update_confirm()
            if result == QMessageBox.StandardButton.Yes:
                return self.repo.create_budget(amount, month, year) 
            else:
                return None 

        return self.repo.create_budget(amount, month, year)


    def get_budget(self, month=None, year=None):
        if month is None:
            month = datetime.now().month
        if year is None:
            year = datetime.now().year
        return self.repo.get_budget(month, year)
        
    def show_update_confirm(self):
        msg = QMessageBox()
        msg.setWindowTitle("Budget Already Exists")
        msg.setText("Budget for this month/year already exists. Do you want to update it?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return msg.exec()
  


    def delete_budget(self, budget_id):
        return self.repo.delete_budget(budget_id)