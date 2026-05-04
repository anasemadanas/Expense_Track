from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")



def logout_view(request):
    logout(request)
    return redirect("login")



@login_required(login_url="login")
def dashboard(request):

    context = {
        "username": request.user.username,

        "month": 5,
        "year": 2026,
        "month_name": "May",

        "balance": {
            "income": 1200,
            "expense": 800,
            "net": 400
        },

        "budget": {
            "total": 1000,
            "spent": 700,
            "remaining": 300,
            "percent": 70
        },

        "transactions": [
            {"category": "Food", "amount": -50},
            {"category": "Salary", "amount": 1000},
        ],

        "goals": [
            {
                "name": "Buy Laptop",
                "saved_amount": 300,
                "target_amount": 1000,
                "progress_percent": 30,
                "is_complete": False
            }
        ],
    }

    return render(request, "dashboard.html", context)