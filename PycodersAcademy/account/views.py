from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import RegisteredUser

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            register_user = RegisteredUser(
                Fullname=fullname,
                Email=email
            )
            register_user.save()
            user1 = authenticate(request, username=username, password=password1)
            login(request, user1)
            return redirect('home')
        else:
            messages.error("The two Password doesn't match")
            return redirect('register')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error("Incorrect Username or Password")
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

