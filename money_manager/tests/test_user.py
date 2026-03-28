import unittest
from src.business.services.user_service import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()

    def test_create_user(self):
        user = self.user_service.create_user("testuser", "pass123")
        self.assertEqual(user.username, "testuser")


if __name__ == "__main__":
    unittest.main()