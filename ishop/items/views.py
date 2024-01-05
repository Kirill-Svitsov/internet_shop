from django.shortcuts import render, get_list_or_404

from items import models


def catalog(request, category_slug):
    if category_slug == 'all':
        items = models.Item.objects.all()
    else:
        items = get_list_or_404(models.Item, category__slug=category_slug)
    context = {
        'title': 'Каталог',
        'items': items
    }
    return render(request, 'items/catalog.html', context=context)


def item(request, item_slug):
    item = models.Item.objects.get(slug=item_slug)
    context = {
        'item': item
    }
    return render(request, 'items/item.html', context=context)
