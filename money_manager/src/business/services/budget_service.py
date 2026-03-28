from src.data.repositories.budget_repo import BudgetRepo

class BudgetService:
    def __init__(self, budget_repo: BudgetRepo):
        self.budget_repo = budget_repo

    def create_budget(self, user_id, name, amount, period):
        if amount <= 0:
            raise ValueError("Budget amount must be positive")
        return self.budget_repo.create_budget(user_id, name, amount, period)

    def get_user_budgets(self, user_id):
        return self.budget_repo.get_budgets_by_user(user_id)

    def update_spent(self, budget_id, spent_amount):
        budget = self.budget_repo.get_budget_by_id(budget_id)
        if budget:
            budget['Spent'] += spent_amount
            self.budget_repo.update_budget(budget_id, budget)