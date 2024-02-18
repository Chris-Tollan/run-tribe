from django.contrib import admin
from .models import UserUpdate
from django_summernote.admin import SummernoteModelAdmin

@admin.register(UserUpdate)
class UserUpdateAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

