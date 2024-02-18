from django.contrib import admin
from .models import ContactUs, UserUpdate
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)


@admin.register(UserUpdate)
class UserUpdateAdmin(admin.ModelAdmin):

    list_display = ('message', 'read')
