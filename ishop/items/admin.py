from django.contrib import admin

from items import models


@admin.register(models.Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Item)
class ItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
