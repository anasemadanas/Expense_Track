import pytest
from typing import cast, Any
from models.budget import Budget
from services.transaction_service import TransactionService


class FakeBudgetService:
    def __init__(self, budget=None):
        self.budget = budget

    def check_budget(self, month, year):
        return self.budget


def make_service():
    service = TransactionService.__new__(TransactionService)
    return service


def test_get_budget_warning_returns_none_below_threshold():
    service = make_service()
    budget = Budget(amount=90, totalamount=100, month=4, year=2026, id=1)

    service.budget_service = cast(Any, FakeBudgetService(budget))
    service.validate_transaction = TransactionService.validate_transaction.__get__(service, TransactionService)

    warning = service.get_budget_warning(10, 4, 2026)

    assert warning is None


def test_get_budget_warning_returns_message_at_or_above_80_percent():
    service = make_service()
    budget = Budget(amount=30, totalamount=100, month=4, year=2026, id=1)

    service.budget_service = cast(Any, FakeBudgetService(budget))
    service.validate_transaction = TransactionService.validate_transaction.__get__(service, TransactionService)

    warning = service.get_budget_warning(10, 4, 2026)

    assert warning is not None
    assert "80.0%" in warning
    assert "Do you want to continue?" in warning


def test_validate_transaction_rejects_missing_budget():
    service = make_service()

    with pytest.raises(ValueError, match="No budget found"):
        service.validate_transaction(10, 4, 2026, None)


def test_validate_transaction_rejects_amount_over_budget():
    service = make_service()
    budget = Budget(amount=20, totalamount=100, month=4, year=2026, id=1)

    with pytest.raises(ValueError, match="Amount exceeds the available budget"):
        service.validate_transaction(25, 4, 2026, budget)
