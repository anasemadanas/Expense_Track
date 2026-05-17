from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="budgets")
    month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2100)])
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "month", "year"], name="uniq_budget_user_month_year"),
        ]
        indexes = [
            models.Index(fields=["user", "year", "month"]),
        ]

    def __str__(self) -> str:
        return f"Budget({self.user_id}) {self.month}/{self.year}"


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=64)
    occurred_at = models.DateField(default=timezone.now)
    note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["user", "occurred_at"]),
            models.Index(fields=["user", "category"]),
        ]
        ordering = ["-occurred_at", "-id"]

    def __str__(self) -> str:
        return f"Txn({self.user_id}) {self.category} {self.amount}"


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="goals")
    name = models.CharField(max_length=120)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["user", "name"]),
        ]

    @property
    def is_complete(self) -> bool:
        return self.saved_amount >= self.target_amount

    def __str__(self) -> str:
        return f"Goal({self.user_id}) {self.name}"
