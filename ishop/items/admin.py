from django.contrib import admin

from items import models


@admin.register(models.Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    search_fields = ('id', 'name', 'slug')


@admin.register(models.Item)
class ItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    search_fields = ('id', 'name', 'slug')
