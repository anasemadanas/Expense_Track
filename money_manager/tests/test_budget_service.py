import pytest
from src.business.services.budget_service import BudgetService
from src.data.repositories.budget_repo import BudgetRepo


repo = BudgetRepo()
service = BudgetService(repo)

def test_add_budget():
    user_id = 1
    name = "Food"
    amount = 500
    
    budget = service.add_budget(name, amount, user_id)
    
    assert budget['name'] == name
    assert budget['amount'] == amount
    assert budget['user_id'] == user_id

def test_get_budgets_by_user():
    user_id = 1
    budgets = service.get_budgets_by_user(user_id)
    assert isinstance(budgets, list)