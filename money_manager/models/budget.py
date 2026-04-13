from typing import Optional

class Budget:
    def __init__(self, amount: float,totalamount: float, month: int, year: int, id: Optional[int] = None):
        self.id = id
        self.amount = amount
        self.totalamount = totalamount
        self.month = month
        self.year = year