from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
        'content': 'Магазин мебели'
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'content_text': 'Парам пам пам',
    }
    return render(request, 'main/about.html', context=context)
