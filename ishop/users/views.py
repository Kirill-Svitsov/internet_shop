from django.shortcuts import render


# Create your views here.
def login(requset):
    context = {
        'title': 'Авторизация'
    }
    return render(requset, 'users/login.html', context)


def registration(requset):
    context = {
        'title': 'Регистрация'
    }
    return render(requset, 'users/registration.html', context)


def profile(requset):
    context = {
        'title': 'Профиль'
    }
    return render(requset, 'users/profile.html', context)


def logout(requset):
    context = {
        'title': 'Выход'
    }
    return render(requset, 'users/logout.html', context)
