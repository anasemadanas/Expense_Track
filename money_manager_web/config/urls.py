from django.contrib import admin
from django.urls import path
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.home, name="home"),

    path("login/", views.home, name="login"),

    path("dashboard/", views.dashboard, name="dashboard"),
    
    path("logout/", views.logout_view, name="logout"),
]