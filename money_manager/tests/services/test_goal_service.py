import pytest
from typing import cast, Any

from services.goal_service import GoalService


class FakeGoalRepo:
    def __init__(self):
        self.created = None
        self.saved = None
        self.deleted = None

    def create_goal(self, name, target_amount, initial_saved):
        self.created = (name, target_amount, initial_saved)

    def add_savings(self, goal_id, amount):
        self.saved = (goal_id, amount)

    def delete_goal(self, goal_id):
        self.deleted = goal_id


def make_service():
    service = GoalService.__new__(GoalService)
    service.goal_repo = cast(Any, FakeGoalRepo())
    return service


def test_add_goal_creates_goal_when_input_is_valid():
    service = make_service()

    service.add_goal("Emergency Fund", 1000, 200)

    assert cast(Any, service.goal_repo).created == ("Emergency Fund", 1000, 200)


@pytest.mark.parametrize(
    ("name", "target_amount", "initial_saved", "message"),
    [
        ("   ", 1000, 0, "Goal name cannot be empty."),
        ("Emergency Fund", 0, 0, "Target amount must be greater than 0."),
        ("Emergency Fund", 1_500_000, 0, "Target amount must be less than 1,000,000."),
        ("Emergency Fund", 1000, -1, "Initial savings cannot be negative."),
        ("Emergency Fund", 1000, 1500, "Initial savings cannot exceed the target amount."),
    ],
)
def test_add_goal_rejects_invalid_input(name, target_amount, initial_saved, message):
    service = make_service()

    with pytest.raises(ValueError, match=message):
        service.add_goal(name, target_amount, initial_saved)


def test_add_savings_requires_positive_amount():
    service = make_service()

    with pytest.raises(ValueError, match="Amount must be greater than 0."):
        service.add_savings(1, 0)


def test_delete_goal_calls_repo():
    service = make_service()

    service.delete_goal(7)

    assert cast(Any, service.goal_repo).deleted == 7
