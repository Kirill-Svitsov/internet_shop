from django import template

from items import models

register = template.Library()


@register.simple_tag()
def tag_categories():
    return models.Category.objects.all()
