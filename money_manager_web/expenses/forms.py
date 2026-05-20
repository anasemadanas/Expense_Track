from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Budget, Goal, Transaction


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"placeholder": "Username"})
        self.fields["email"].widget.attrs.update({"placeholder": "Email (optional)"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm password"})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")


class TransactionForm(forms.ModelForm):
    kind = forms.ChoiceField(
        choices=(("expense", "Expense"), ("income", "Income")),
        initial="expense",
    )

    class Meta:
        model = Transaction
        fields = ("amount", "category", "occurred_at", "note")
        widgets = {
            "occurred_at": forms.DateInput(attrs={"type": "date"}),
            "note": forms.Textarea(attrs={"rows": 3}),
        }


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ("total_amount",)


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ("name", "target_amount", "saved_amount")
