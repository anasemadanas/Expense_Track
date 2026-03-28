import pytest
from src.business.services.transaction_service import TransactionService
from src.data.repositories.transaction_repo import TransactionRepo
from src.data.database import DB_NAME

@pytest.fixture
def transaction_service():
    repo = TransactionRepo(DB_NAME)
    service = TransactionService(repo)
    return service

def test_add_transaction(transaction_service):
    tx = transaction_service.add_transaction(
        name="Salary",
        amount=2000,
        type="income",
        category="Job",
        user_id=1,
        budget_id=None,
        family_id=None,
        currency_id=1
    )
    assert tx["Name"] == "Salary"
    assert tx["Amount"] == 2000
    assert tx["Type"] == "income"

def test_get_transactions_by_user(transaction_service):
    transactions = transaction_service.get_transactions_by_user(1)
    assert isinstance(transactions, list)
    if transactions:
        assert "Name" in transactions[0]
        assert "Amount" in transactions[0]