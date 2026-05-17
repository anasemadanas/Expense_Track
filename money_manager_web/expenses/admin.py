from django.contrib import admin

from .models import Budget, Goal, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "occurred_at", "category", "amount")
    list_filter = ("category", "occurred_at")
    search_fields = ("user__username", "category", "note")


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "month", "year", "total_amount", "updated_at")
    list_filter = ("year", "month")
    search_fields = ("user__username",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "saved_amount", "target_amount", "updated_at")
    search_fields = ("user__username", "name")
