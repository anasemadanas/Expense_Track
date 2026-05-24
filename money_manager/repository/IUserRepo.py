from abc import ABC, abstractmethod

class IUserRepo(ABC):

    @abstractmethod
    def find_user(self, username: str, password: str):
        pass

    @abstractmethod
    def create_user(self, username: str, password: str, recovery_key: str, permissions: int = 7):
        pass

    @abstractmethod
    def reset_password(self, username: str, recovery_key: str, password: str):
        pass

    @abstractmethod
    def set_recovery_key(self, user_id: int, recovery_key: str):
        pass
