from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.utils import get_user_orders


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            # Получаем сессионный ключ, на случай, если юезр добавлял в корзину
            # товары, будучи неавторизованным
            session_key = request.session.session_key
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, вы вошли в аккаунт')
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('users:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            # Получаем сессионный ключ, на случай, если юезр добавлял в корзину
            # товары, будучи неавторизованным
            session_key = request.session.session_key
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, f'{user.username}, вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    orders = get_user_orders(request)
    context = {
        'title': 'Профиль',
        'form': form,
        'orders': orders
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, вы успешно вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')


def users_orders(request):
    return render(request, 'users/user_orders.html')
