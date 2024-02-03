from django.db.models import Prefetch

from orders.models import Order, OrderItem


def get_user_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related(
        Prefetch(
            'orderitem_set',
            queryset=OrderItem.objects.select_related('product'),
        )
    ).order_by('-id')
    return orders
