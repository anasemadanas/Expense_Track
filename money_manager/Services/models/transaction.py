class Transaction:
    def __init__(self, amount: float, category: str, month: int, year: int, id=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.month = month
        self.year = year