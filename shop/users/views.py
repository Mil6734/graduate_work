from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import UserLogin, UserRegister
from orders.models import Order
from .models import EmailVerify, User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login/')
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
            messages.success(request, 'Подтвердите регистрацию на почте')
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


def email_verify(request, code, email):
    user = User.objects.get(email=email)
    email_verification = EmailVerify.objects.filter(user=user, code=code)

    if email_verification.exists() and not email_verification.first().is_expired():
        user.is_verify_email = True
        user.save()
        context = {'title': 'Подтверждение электронной почты'}

        return render(request, 'users/email_verify.html', context)
    else:
        return redirect('index')


@login_required(login_url='/users/login/')
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'users/user_orders.html', context)
