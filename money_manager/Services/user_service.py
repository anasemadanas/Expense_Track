

class UserService:
    
    
    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "1234"
        self.max_attempts = 4
        self.login_attempts = 0

    def CheckLogin (self, username, password):

        if username.lower() == self.admin_username and password == self.admin_password:
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.max_attempts:
                raise Exception("Too many login attempts! Access denied.")
            return False
            
    def login(self, username, password):
        if (self.CheckLogin(username, password)):
            return True
        return False