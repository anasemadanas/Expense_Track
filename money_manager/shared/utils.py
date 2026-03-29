import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    return True
    