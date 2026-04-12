from abc import ABC, abstractmethod


class IDashboardService(ABC):

    @abstractmethod
    def show_about(self):
        pass

    @abstractmethod
    def open_guide(self):
        pass

    @abstractmethod
    def save_data(self, month, year):
        pass

    @abstractmethod
    def export_data(self, month, year):
        pass

    @abstractmethod
    def get_all_transactions(self):
        pass

    @abstractmethod
    def get_transactions_for_month(self, month, year):
        pass

    @abstractmethod
    def get_current_month_balance(self):
        pass

    @abstractmethod
    def get_balance_for_month(self, month, year):
        pass

    @abstractmethod
    def get_budget_summary(self, month, year):
        pass

    @abstractmethod
    def get_budget_for_category(self, month, year):
        pass