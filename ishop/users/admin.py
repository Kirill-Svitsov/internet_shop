from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users import models


@admin.register(models.User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_display_links = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('id', 'username', 'first_name', 'last_name', 'email')
    inlines = [CartTabAdmin, OrderTabularAdmin]
