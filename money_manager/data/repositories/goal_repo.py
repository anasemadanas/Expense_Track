from Services.models.goal import Goal
from data.database import DatabaseConnection
from data.interfaces.IGoalRepo import IGoalRepo


class GoalRepo(IGoalRepo):
    def __init__(self):
        self.db = DatabaseConnection()

    def create_goal(self, name: str, target_amount: float, initial_saved: float = 0.0):
        self.db.execute(
            "INSERT INTO goals (name, target_amount, saved_amount) VALUES (?, ?, ?)",
            (name, target_amount, initial_saved)
        )

    def get_all_goals(self):
        rows = self.db.execute("SELECT id, name, target_amount, saved_amount FROM goals ORDER BY id", fetch="all")
        if not rows:
            return []
        return [Goal(id=row[0], name=row[1], target_amount=row[2], saved_amount=row[3]) for row in rows]

    def add_savings(self, goal_id: int, amount: float):
        self.db.execute(
            "UPDATE goals SET saved_amount = saved_amount + ? WHERE id = ?",
            (amount, goal_id)
        )

    def delete_goal(self, goal_id: int):
        self.db.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
