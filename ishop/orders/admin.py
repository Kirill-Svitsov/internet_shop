from django.contrib import admin

from orders import models


class OrderItemTabularAdmin(admin.TabularInline):
    model = models.OrderItem
    fields = 'product', 'name', 'price', 'quantity'
    search_fields = (
        'product',
        'name'
    )
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )
    list_display_links = ('id', 'user', 'created_timestamp', 'status')
    search_fields = ('id',)
    readonly_fields = ('created_timestamp',)
    list_filter = [
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    ]
    inlines = (OrderItemTabularAdmin,)


@admin.register(models.OrderItem)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'name', 'price', 'quantity', 'created_timestamp')
    list_display_links = ('id', 'name')
    list_filter = ('quantity', 'created_timestamp', 'price')
    search_fields = ('id', 'order', 'product', 'name')


class OrderTabularAdmin(admin.TabularInline):
    model = models.Order
    fields = (
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )
    search_fields = (
        'requires_delivery',
        'payment_on_get'
    )
    readonly_fields = ('created_timestamp',)
    extra = 0
