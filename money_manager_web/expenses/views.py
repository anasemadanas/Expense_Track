from __future__ import annotations

from datetime import date

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import BudgetForm, GoalForm, SignupForm, TransactionForm
from .models import Budget, Goal, Transaction


def _period_from_request(request):
    now = timezone.localdate()

    try:
        month = int(request.GET.get("month") or now.month)
        year = int(request.GET.get("year") or now.year)
    except (TypeError, ValueError):
        month = now.month
        year = now.year

    if not (1 <= month <= 12):
        month = now.month
    if not (2000 <= year <= 2100):
        year = now.year

    start = date(year, month, 1)
    end = date(year + (month // 12), ((month % 12) + 1), 1)

    years = list(range(now.year - 3, now.year + 2))
    months = [{"num": i, "name": date(year, i, 1).strftime("%B")} for i in range(1, 13)]

    return {
        "now": now,
        "month": month,
        "year": year,
        "start": start,
        "end": end,
        "month_name": date(year, month, 1).strftime("%B"),
        "months": months,
        "years": years,
    }


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignupForm()

    return render(request, "auth/signup.html", {"form": form})



@login_required
def dashboard(request):
    period = _period_from_request(request)

    qs = Transaction.objects.filter(
        user=request.user,
        occurred_at__gte=period["start"],
        occurred_at__lt=period["end"],
    )
    income = qs.filter(amount__gt=0).aggregate(total=Sum("amount"))["total"] or 0
    expense = qs.filter(amount__lt=0).aggregate(total=Sum("amount"))["total"] or 0
    expense_abs = -expense
    net = income - expense_abs

    budget = Budget.objects.filter(user=request.user, month=period["month"], year=period["year"]).first()
    budget_total = budget.total_amount if budget else 0
    spent = expense_abs
    remaining = budget_total - spent if budget_total else 0
    percent = int((spent / budget_total) * 100) if budget_total else 0

    goals = Goal.objects.filter(user=request.user).order_by("name")[:10]

    context = {
        "username": request.user.username,
        "role": "Member",

        "month": period["month"],
        "year": period["year"],
        "month_name": period["month_name"],
        "months": period["months"],
        "years": period["years"],

        "balance": {
            "income": income,
            "expense": expense_abs,
            "net": net,
        },

        "budget": {
            "total": budget_total,
            "spent": spent,
            "remaining": remaining,
            "percent": percent,
        },

        "transactions": [
            {
                "category": t.category,
                "amount": t.amount,
                "month": t.occurred_at.month,
                "year": t.occurred_at.year,
            }
            for t in qs.select_related(None)[:10]
        ],
        "goals": [
            {
                "name": g.name,
                "saved_amount": g.saved_amount,
                "target_amount": g.target_amount,
                "progress_percent": int((g.saved_amount / g.target_amount) * 100) if g.target_amount else 0,
                "is_complete": g.is_complete,
            }
            for g in goals
        ],
    }

    return render(request, "dashboard.html", context)


@login_required
def transaction_list(request):
    period = _period_from_request(request)

    qs = (
        Transaction.objects.filter(
            user=request.user,
            occurred_at__gte=period["start"],
            occurred_at__lt=period["end"],
        )
        .order_by("-occurred_at", "-id")
    )

    income = qs.filter(amount__gt=0).aggregate(total=Sum("amount"))["total"] or 0
    expense = qs.filter(amount__lt=0).aggregate(total=Sum("amount"))["total"] or 0

    return render(
        request,
        "transactions/list.html",
        {
            "month": period["month"],
            "year": period["year"],
            "month_name": period["month_name"],
            "months": period["months"],
            "years": period["years"],
            "transactions": list(qs[:200]),
            "income": income,
            "expense": -expense,
        },
    )


@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            txn = form.save(commit=False)
            txn.user = request.user
            kind = form.cleaned_data.get("kind") or "expense"
            amount = txn.amount
            try:
                amount_abs = abs(amount)
            except TypeError:
                amount_abs = amount
            txn.amount = -amount_abs if kind == "expense" else amount_abs
            txn.save()
            return redirect("transactions")
    else:
        form = TransactionForm()

    return render(request, "transactions/new.html", {"form": form})


@login_required
def budget_manage(request):
    period = _period_from_request(request)

    existing = Budget.objects.filter(user=request.user, month=period["month"], year=period["year"]).first()

    if request.method == "POST":
        form = BudgetForm(request.POST, instance=existing)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.month = period["month"]
            budget.year = period["year"]
            try:
                budget.save()
                return redirect(f"{request.path}?month={period['month']}&year={period['year']}")
            except IntegrityError:
                form.add_error(None, "A budget for this month already exists. Please refresh and try again.")
    else:
        form = BudgetForm(instance=existing)

    qs = Transaction.objects.filter(
        user=request.user,
        occurred_at__gte=period["start"],
        occurred_at__lt=period["end"],
    )
    expense = qs.filter(amount__lt=0).aggregate(total=Sum("amount"))["total"] or 0
    spent = -expense
    total = existing.total_amount if existing else 0
    remaining = total - spent if total else 0
    percent = int((spent / total) * 100) if total else 0

    return render(
        request,
        "budgets/manage.html",
        {
            "month": period["month"],
            "year": period["year"],
            "month_name": period["month_name"],
            "months": period["months"],
            "years": period["years"],
            "form": form,
            "has_budget": existing is not None,
            "spent": spent,
            "remaining": remaining,
            "percent": percent,
        },
    )


@login_required
def goal_list(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect("goals")
    else:
        form = GoalForm()

    goals_qs = Goal.objects.filter(user=request.user).order_by("name", "id")
    goals = [
        {
            "id": g.id,
            "name": g.name,
            "saved_amount": g.saved_amount,
            "target_amount": g.target_amount,
            "is_complete": g.is_complete,
            "progress_percent": int((g.saved_amount / g.target_amount) * 100) if g.target_amount else 0,
        }
        for g in goals_qs
    ]

    return render(request, "goals/list.html", {"goals": goals, "form": form})


@login_required
def goal_edit(request, goal_id: int):
    goal = Goal.objects.filter(user=request.user, id=goal_id).first()
    if not goal:
        return redirect("goals")

    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goals")
    else:
        form = GoalForm(instance=goal)

    return render(request, "goals/edit.html", {"form": form, "goal": goal})


@login_required
def settings_page(request):
    return render(
        request,
        "settings/index.html",
        {
            "username": request.user.username,
            "email": getattr(request.user, "email", ""),
        },
    )
