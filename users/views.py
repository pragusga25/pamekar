from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profile.objects.get(pk=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills,
    }
    return render(request, "users/user-profile.html", context)


def loginUser(request):
    page = "login"
    context = {"page": page}

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "users/login-register.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")


def registerUser(request):
    page = "register"
    form = UserCreationForm()
    context = {"page": page, "form": form}

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        confirmPassword = request.POST["password2"]

        if password != confirmPassword:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        try:
            user = User.objects.get(username=username)
            messages.error(request, "Username already exists")
            return redirect("register")

        except:
            user = User.objects.create_user(username, password=password)
            user.save()
            messages.success(request, "Registered successfully")
            return redirect("profiles")

    return render(request, "users/login-register.html", context)
