import pytest

from services.user_service import UserService


class FakeUserRepo:
    def __init__(self, user=None):
        self.user = user
        self.created = None
        self.reset_result = True
        self.reset = None
        self.recovery = None

    def find_user(self, username, password):
        return self.user

    def create_user(self, username, password, recovery_key, permissions=7):
        self.created = (username, password, recovery_key, permissions)

    def reset_password(self, username, recovery_key, password):
        self.reset = (username, recovery_key, password)
        return self.reset_result

    def set_recovery_key(self, user_id, recovery_key):
        self.recovery = (user_id, recovery_key)


def test_login_returns_user_and_resets_attempts():
    service = UserService(user_repo=FakeUserRepo({"username": "admin"}))
    service.login_attempts = 3

    user = service.login(" Admin ", " secret ")

    assert user == {"username": "admin"}
    assert service.login_attempts == 0


def test_login_increments_attempts_for_invalid_credentials():
    service = UserService(user_repo=FakeUserRepo(None))

    result = service.login("admin", "wrong")

    assert result is None
    assert service.login_attempts == 1


def test_login_locks_after_max_attempts():
    service = UserService(user_repo=FakeUserRepo(None))
    service.login_attempts = service.max_attempts - 1

    with pytest.raises(Exception, match="Too many login attempts"):
        service.login("admin", "wrong")


def test_register_normalizes_username_and_creates_account():
    repo = FakeUserRepo()
    service = UserService(user_repo=repo)

    service.register(" New.User ", "secret1", "secret1", "recover1")

    assert repo.created == ("new.user", "secret1", "recover1", 7)


def test_reset_password_rejects_unknown_username():
    repo = FakeUserRepo()
    repo.reset_result = False
    service = UserService(user_repo=repo)

    with pytest.raises(ValueError, match="Username or recovery code"):
        service.reset_password("missing", "recover1", "secret1", "secret1")


def test_set_recovery_key_requires_matching_codes():
    repo = FakeUserRepo()
    service = UserService(user_repo=repo)

    with pytest.raises(ValueError, match="Recovery codes do not match"):
        service.set_recovery_key(1, "recover1", "recover2")

    service.set_recovery_key(1, "recover1", "recover1")

    assert repo.recovery == (1, "recover1")
