from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLogin, UserRegister


def profile(request):
    context = {
        'title': 'Профиль'
    }
    return render(request, 'users/profile.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('home')
    else:
        form = UserLogin()

    context = {
        'title': 'Логин',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegister(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegister()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')

