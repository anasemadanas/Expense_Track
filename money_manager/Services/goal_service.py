from data.repositories.goal_repo import GoalRepo


class GoalService:
    def __init__(self):
        self.goal_repo = GoalRepo()

    def add_goal(self, name: str, target_amount: float, initial_saved: float = 0.0):
        name = name.strip()
        if not name:
            raise ValueError("Goal name cannot be empty.")
        if target_amount <= 0:
            raise ValueError("Target amount must be greater than 0.")
        if target_amount > 1_000_000:
            raise ValueError("Target amount must be less than 1,000,000.")
        if initial_saved < 0:
            raise ValueError("Initial savings cannot be negative.")
        if initial_saved > target_amount:
            raise ValueError("Initial savings cannot exceed the target amount.")
        self.goal_repo.create_goal(name, target_amount, initial_saved)

    def get_all_goals(self):
        return self.goal_repo.get_all_goals()

    def add_savings(self, goal_id: int, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.goal_repo.add_savings(goal_id, amount)

    def delete_goal(self, goal_id: int):
        self.goal_repo.delete_goal(goal_id)
