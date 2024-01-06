from django import template
from django.utils.http import urlencode

from items import models

register = template.Library()


@register.simple_tag()
def tag_categories():
    return models.Category.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context,  **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
