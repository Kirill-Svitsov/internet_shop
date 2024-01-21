from django.contrib import admin

from users import models


@admin.register(models.User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_filter = ('username',)
    search_fields = ('id', 'username')
