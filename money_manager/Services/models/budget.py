class Budget:
    def __init__(self, budget_id: int, name: str, amount: float, spent: float = 0, period: str = None, user_id: int = None):
        self.budget_id = budget_id
        self.name = name
        self.amount = amount
        self.spent = spent
        self.period = period
        self.user_id = user_id