from abc import ABC, abstractmethod


class IBudgetService(ABC):

    @abstractmethod
    def create_budget(self, amount: float, month: int, year: int):
        pass

    @abstractmethod
    def validate_budget(self, amount, month, year):
        pass

    @abstractmethod
    def check_budget(self, month, year):
        pass

    @abstractmethod
    def deduct_from_budget(self, amount: float, month, year):
        pass

    @abstractmethod
    def add_to_budget(self, amount, month, year):
        pass

    @abstractmethod
    def get_budget_balance(self, month, year):
        pass

    @abstractmethod
    def delete_budget(self, budget_id):
        pass

    @abstractmethod
    def update_budget(self, budget_id, amount):
        pass