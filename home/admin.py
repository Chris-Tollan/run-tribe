from django.contrib import admin
from .models import ContactUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

