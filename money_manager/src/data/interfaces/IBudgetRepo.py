from abc import ABC, abstractmethod

class IBudgetRepo(ABC):

    @abstractmethod
    def create_budget(self, name: str, amount: float, user_id: int, period: str = None):
        pass

    @abstractmethod
    def get_budget(self, budget_id: int):
        pass

    @abstractmethod
    def get_budgets_by_user(self, user_id: int):
        pass

    @abstractmethod
    def update_spent(self, budget_id: int, spent: float):
        pass

    @abstractmethod
    def update_budget(self, budget_id: int, name: str = None, amount: float = None, period: str = None):
        pass

    @abstractmethod
    def delete_budget(self, budget_id: int):
        pass