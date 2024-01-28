from django.shortcuts import render, redirect

from carts.models import Cart
from items.models import Item
from users.models import User


def cart_add(request, product_slug):
    product = Item.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass


def cart_remove(request, product_slug):
    pass
