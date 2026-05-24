from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Goal, Transaction

User = get_user_model()


class AccountTests(TestCase):
    password = "WellChosenPassword123!"

    def test_signup_creates_user_with_normalized_email_and_logs_in(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "alice",
                "email": "Alice@Example.COM",
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        user = User.objects.get(username="alice")
        self.assertEqual(user.email, "alice@example.com")
        self.assertEqual(self.client.session["_auth_user_id"], str(user.pk))

    def test_signup_rejects_duplicate_email_case_insensitively(self):
        User.objects.create_user(
            username="alice",
            email="alice@example.com",
            password=self.password,
        )

        response = self.client.post(
            reverse("signup"),
            {
                "username": "second-alice",
                "email": "ALICE@example.com",
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An account with this email already exists.")
        self.assertFalse(User.objects.filter(username="second-alice").exists())

    def test_login_accepts_email_address(self):
        user = User.objects.create_user(
            username="alice",
            email="alice@example.com",
            password=self.password,
        )

        response = self.client.post(
            reverse("login"),
            {"username": "ALICE@EXAMPLE.COM", "password": self.password},
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(self.client.session["_auth_user_id"], str(user.pk))


class UserDataIsolationTests(TestCase):
    password = "WellChosenPassword123!"

    @classmethod
    def setUpTestData(cls):
        cls.alice = User.objects.create_user(
            username="alice",
            email="alice@example.com",
            password=cls.password,
        )
        cls.bob = User.objects.create_user(
            username="bob",
            email="bob@example.com",
            password=cls.password,
        )
        Transaction.objects.create(
            user=cls.alice,
            amount=Decimal("-25.00"),
            category="Alice groceries",
            occurred_at=date(2026, 5, 5),
        )
        Transaction.objects.create(
            user=cls.bob,
            amount=Decimal("-900.00"),
            category="Bob private purchase",
            occurred_at=date(2026, 5, 5),
        )
        cls.bob_goal = Goal.objects.create(
            user=cls.bob,
            name="Bob private goal",
            target_amount=Decimal("800.00"),
            saved_amount=Decimal("10.00"),
        )

    def setUp(self):
        self.client.force_login(self.alice)

    def test_dashboard_shows_only_signed_in_users_transactions(self):
        response = self.client.get(reverse("dashboard"), {"month": 5, "year": 2026})

        self.assertContains(response, "Alice groceries")
        self.assertNotContains(response, "Bob private purchase")

    def test_transaction_create_assigns_signed_in_user(self):
        response = self.client.post(
            reverse("transaction_new"),
            {
                "kind": "expense",
                "amount": "12.50",
                "category": "Lunch",
                "occurred_at": "2026-05-06",
                "note": "",
            },
        )

        self.assertRedirects(response, reverse("transactions"))
        transaction = Transaction.objects.get(category="Lunch")
        self.assertEqual(transaction.user, self.alice)
        self.assertEqual(transaction.amount, Decimal("-12.50"))

    def test_user_cannot_edit_another_users_goal(self):
        response = self.client.post(
            reverse("goal_edit", args=[self.bob_goal.pk]),
            {
                "name": "Changed by Alice",
                "target_amount": "1.00",
                "saved_amount": "1.00",
            },
        )

        self.assertRedirects(response, reverse("goals"))
        self.bob_goal.refresh_from_db()
        self.assertEqual(self.bob_goal.name, "Bob private goal")
