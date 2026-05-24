from abc import ABC, abstractmethod


class IUserService(ABC):

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def register(self, username, password, confirm_password, recovery_key):
        pass

    @abstractmethod
    def reset_password(self, username, recovery_key, password, confirm_password):
        pass

    @abstractmethod
    def set_recovery_key(self, user_id, recovery_key, confirm_recovery_key):
        pass
