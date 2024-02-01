from django.contrib import admin

from items import models


@admin.register(models.Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(models.Item)
class ItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'quantity', 'price', 'discount')
    list_display_links = ('id', 'name')
    list_editable = ('discount',)
    list_filter = ('discount', 'quantity', 'category')
    search_fields = ('name', 'description')
    fields = (
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity'
    )
