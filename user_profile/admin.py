from django.contrib import admin
from .models import UserUpdate


@admin.register(UserUpdate)
class UserUpdateAdmin(admin.ModelAdmin):
    """
    registers user update app in admin
    """

    list_display = ('message', 'read',)
