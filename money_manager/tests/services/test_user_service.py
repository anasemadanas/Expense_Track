import pytest

from services.user_service import UserService


class FakeUserRepo:
    def __init__(self, user=None):
        self.user = user

    def find_user(self, username, password):
        return self.user


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
