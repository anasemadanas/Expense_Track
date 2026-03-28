class User:
    def __init__(self, user_id: int, username: str, password: str, email: str, phone: str = None, currency_id: int = None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.currency_id = currency_id