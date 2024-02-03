from django import template

from users.utils import get_user_orders

register = template.Library()


@register.simple_tag()
def user_orders(request):
    return get_user_orders(request)
