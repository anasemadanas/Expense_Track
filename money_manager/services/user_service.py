from repository.user_repo import UserRepo
from services.IUserService import IUserService


class UserService(IUserService):
    def __init__(self, user_repo=None):
        self.user_repo = user_repo or UserRepo()
        self.login_attempts = 0
        self.max_attempts = 4

    def login(self, username, password):
        username = username.strip().lower()
        user = self.user_repo.find_user(username, password)
        if user:
            self.login_attempts = 0
            return user 
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.max_attempts:
                raise Exception("Too many login attempts! Account locked.")
            return None

    def register(self, username, password, confirm_password, recovery_key):
        username = self._validate_username(username)
        password = self._validate_new_password(password, confirm_password)
        recovery_key = self._validate_recovery_key(recovery_key)
        self.user_repo.create_user(username, password, recovery_key)
        return True

    def reset_password(self, username, recovery_key, password, confirm_password):
        username = self._validate_username(username)
        password = self._validate_new_password(password, confirm_password)
        recovery_key = self._validate_recovery_key(recovery_key)
        if not self.user_repo.reset_password(username, recovery_key, password):
            raise ValueError("Username or recovery code is incorrect.")
        self.login_attempts = 0
        return True

    def set_recovery_key(self, user_id, recovery_key, confirm_recovery_key):
        if recovery_key != confirm_recovery_key:
            raise ValueError("Recovery codes do not match.")
        recovery_key = self._validate_recovery_key(recovery_key)
        self.user_repo.set_recovery_key(user_id, recovery_key)
        return True

    @staticmethod
    def _validate_username(username):
        username = username.strip().lower()
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters.")
        if not all(ch.isalnum() or ch in "._-" for ch in username):
            raise ValueError("Username may contain letters, numbers, '.', '_' and '-'.")
        return username

    @staticmethod
    def _validate_new_password(password, confirm_password):
        if password != confirm_password:
            raise ValueError("Passwords do not match.")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters.")
        return password

    @staticmethod
    def _validate_recovery_key(recovery_key):
        if len(recovery_key.strip()) < 6:
            raise ValueError("Recovery code must be at least 6 characters.")
        return recovery_key
