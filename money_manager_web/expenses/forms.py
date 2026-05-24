from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import Budget, Goal, Transaction

User = get_user_model()


class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or email",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "autocomplete": "username",
                "placeholder": "Username or email",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update(
            {
                "autocomplete": "current-password",
                "placeholder": "Password",
            }
        )

    def clean(self):
        identity = (self.cleaned_data.get("username") or "").strip()

        if "@" in identity:
            usernames = list(
                User.objects.filter(email__iexact=identity, is_active=True)
                .values_list("username", flat=True)[:2]
            )
            if len(usernames) == 1:
                self.cleaned_data["username"] = usernames[0]

        return super().clean()


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"placeholder": "Username"})
        self.fields["email"].widget.attrs.update(
            {"autocomplete": "email", "placeholder": "Email"}
        )
        self.fields["password1"].widget.attrs.update({"placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm password"})

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email

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
