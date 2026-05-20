class Goal:
    def __init__(self, name: str, target_amount: float, saved_amount: float = 0.0, id=None):
        self.id = id
        self.name = name
        self.target_amount = target_amount
        self.saved_amount = saved_amount

    @property
    def progress_percent(self) -> int:
        if self.target_amount <= 0:
            return 0
        return min(int(self.saved_amount / self.target_amount * 100), 100)

    @property
    def is_complete(self) -> bool:
        return self.saved_amount >= self.target_amount
