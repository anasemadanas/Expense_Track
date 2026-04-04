class Transaction:
    def __init__(self, amount, category, month, year, id=None):
        self.amount = amount
        self.category = category
        self.month = month
        self.year = year
        self.id = id