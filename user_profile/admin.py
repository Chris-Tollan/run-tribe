from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserUpdate


@admin.register(UserUpdate)
class UserUpdateAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
