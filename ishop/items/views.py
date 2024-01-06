from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from items import models

ITEMS_ON_PAGE = 3


def catalog(request, category_slug):
    if category_slug == 'all':
        items = models.Item.objects.all()
    else:
        items = get_list_or_404(models.Item, category__slug=category_slug)
    page = request.GET.get('page', 1)
    paginator = Paginator(items, ITEMS_ON_PAGE)
    current_page = paginator.page(int(page))
    context = {
        'title': 'Каталог',
        'items': current_page,
        'slug_url': category_slug
    }
    return render(request, 'items/catalog.html', context=context)


def item(request, item_slug):
    item = models.Item.objects.get(slug=item_slug)
    context = {
        'item': item
    }
    return render(request, 'items/item.html', context=context)
