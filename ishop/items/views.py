from django.shortcuts import render


def catalog(request):
    return render(request, 'items/catalog.html')


def item(request):
    return render(request, 'items/item.html')
