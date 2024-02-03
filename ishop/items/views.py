from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_list_or_404

from items import models
from items.utils import q_search

ITEMS_ON_PAGE = 6


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    # Проверяем, что параметр page не пустой
    if not page:
        page = 1
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    if category_slug == 'all':
        items = models.Item.objects.all()
    elif query:
        items = q_search(query)
    else:
        items = models.Item.objects.filter(category__slug=category_slug)
    if on_sale:
        items = items.filter(discount__gt=0)
    if order_by and order_by != "default":
        items = items.order_by(order_by)
    paginator = Paginator(items, ITEMS_ON_PAGE)
    try:
        current_page = paginator.page(int(page))
    except (EmptyPage, PageNotAnInteger):
        current_page = paginator.page(1)
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
