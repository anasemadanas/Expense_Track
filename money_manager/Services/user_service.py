

from data.repositories.user_repo import UserRepo


class UserService:

    def __init__(self, user_repo=None):
        self.user_repo = user_repo or UserRepo()
        self.max_attempts = 4
        self.login_attempts = 0

        
    def CheckLogin(self, username, password):
        username = username.strip().lower()
        password = password.strip()

        if not username or not password:
            return False

        if self.user_repo.find_user(username, password):
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.max_attempts:
                raise Exception("Too many login attempts! Account locked.")
            return False

    def login(self, username, password):
        return self.CheckLogin(username, password)