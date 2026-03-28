import pytest
from src.data.repositories.user_repo import UserRepo
from src.data.repositories.budget_repo import BudgetRepo
from src.data.database import DB_NAME
import sqlite3

@pytest.fixture
def user_repo():
    return UserRepo(DB_NAME)

@pytest.fixture
def budget_repo():
    return BudgetRepo(DB_NAME)

def test_add_and_get_user(user_repo):
    user_id = user_repo.add_user("testuser", "1234", "test@example.com", None, None)
    
    user = user_repo.get_user_by_username("testuser")
    assert user is not None
    assert user["UserName"] == "testuser"

def test_add_and_get_budget(budget_repo):
    budget_id = budget_repo.add_budget("Food", 500, 1, "2026-03")
    
    budgets = budget_repo.get_budgets_by_user(1)
    assert len(budgets) > 0
    assert budgets[0]["Name"] == "Food"