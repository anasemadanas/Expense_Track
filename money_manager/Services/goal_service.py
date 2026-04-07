from data.repositories.goal_repo import GoalRepo


class GoalService:
    def __init__(self):
        self.goal_repo = GoalRepo()

    def add_goal(self, name: str, target_amount: float):
        name = name.strip()
        if not name:
            raise ValueError("Goal name cannot be empty.")
        if target_amount <= 0:
            raise ValueError("Target amount must be greater than 0.")
        if target_amount > 1_000_000:
            raise ValueError("Target amount must be less than 1,000,000.")
        self.goal_repo.create_goal(name, target_amount)

    def get_all_goals(self):
        return self.goal_repo.get_all_goals()

    def add_savings(self, goal_id: int, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.goal_repo.add_savings(goal_id, amount)

    def delete_goal(self, goal_id: int):
        self.goal_repo.delete_goal(goal_id)
