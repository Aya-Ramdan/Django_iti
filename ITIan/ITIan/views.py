from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "base.html")  # Adjust to correct template path


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


def user_login(request):
    return render(request, "auth/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
