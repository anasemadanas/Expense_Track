class Transaction:
    def __init__(self, transaction_id: int, name: str, amount: float, type_: str, category: str = None,
                 user_id: int = None, budget_id: int = None, family_id: int = None, currency_id: int = None,
                 date=None):
        self.transaction_id = transaction_id
        self.name = name
        self.amount = amount
        self.type_ = type_
        self.category = category
        self.user_id = user_id
        self.budget_id = budget_id
        self.family_id = family_id
        self.currency_id = currency_id
        self.date = date