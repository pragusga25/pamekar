from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from .forms import MyRegistrationForm

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
    form = MyRegistrationForm()
    context = {"page": page, "form": form}

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Account created successfully")
            login(request, user)

            return redirect("profiles")
        else:
            messages.error(request, "Invalid form")

    return render(request, "users/login-register.html", context)
