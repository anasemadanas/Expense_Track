from abc import ABC, abstractmethod

class IUserRepo(ABC):

    @abstractmethod
    def create_user(self, username: str, password: str, phone: str = None, email: str = None, currency_id: int = None):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        pass

    @abstractmethod
    def update_user(self, user_id: int, username: str = None, password: str = None,
                    phone: str = None, email: str = None, currency_id: int = None):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass