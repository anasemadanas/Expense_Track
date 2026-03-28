from src.data.database import DatabaseConnection
from src.data.interfaces.IBudgetRepo import IBudgetRepo


class BudgetRepo(IBudgetRepo):

    def __init__(self):
        self.db = DatabaseConnection()

    def add_budget(self, budget):
        query = """
            INSERT INTO Budget (Name, Amount, Spent, period, User_ID)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (budget.name, budget.amount, budget.spent, budget.period, budget.user_id)
        return self.db.execute(query, params)

    def get_budget_by_id(self, budget_id: int):
        query = "SELECT * FROM Budget WHERE Budget_ID = ?"
        return self.db.fetch_one(query, (budget_id,))

    def get_budgets_by_user(self, user_id: int):
        query = "SELECT * FROM Budget WHERE User_ID = ? ORDER BY period DESC"
        return self.db.fetch_all(query, (user_id,))

    def update_budget(self, budget):
        query = """
            UPDATE Budget
            SET Name = ?, Amount = ?, Spent = ?, period = ?
            WHERE Budget_ID = ?
        """
        params = (budget.name, budget.amount, budget.spent, budget.period, budget.id)
        return self.db.execute(query, params)

    def delete_budget(self, budget_id: int):
        query = "DELETE FROM Budget WHERE Budget_ID = ?"
        return self.db.execute(query, (budget_id,))

    def add_spent_amount(self, budget_id: int, amount: float):
        query = "UPDATE Budget SET Spent = Spent + ? WHERE Budget_ID = ?"
        return self.db.execute(query, (amount, budget_id))