from django.shortcuts import render

from items import models


def catalog(request):
    items = models.Item.objects.all()
    categories = models.Category.objects.all()
    context = {
        'title': 'Каталог',
        'items': items
    }
    return render(request, 'items/catalog.html', context=context)


def item(request):
    return render(request, 'items/item.html')
