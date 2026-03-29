

class UserService:
    login_attempts = 0
    
    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "1234"
        self.max_attempts = 4

    def login(self, username, password):
        if username == self.admin_username and password == self.admin_password:
            UserService.login_attempts = 0
            return True
        else:
            UserService.login_attempts += 1
            if UserService.login_attempts >= self.max_attempts:
                raise Exception("Too many login attempts! Access denied.")
            return False
