from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Profile
from django.contrib.auth.models import User

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


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            print("Username doesnt exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            print("Username or password is incorrect")

    return render(request, "users/login-register.html")
