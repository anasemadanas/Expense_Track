from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.home, name="home"),

    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="auth/password_reset_form.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"), name="password_reset_complete"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("transactions/", views.transaction_list, name="transactions"),
    path("transactions/new/", views.transaction_create, name="transaction_new"),

    path("budgets/", views.budget_manage, name="budgets"),

    path("goals/", views.goal_list, name="goals"),
    path("goals/<int:goal_id>/edit/", views.goal_edit, name="goal_edit"),

    path("settings/", views.settings_page, name="settings"),
]
