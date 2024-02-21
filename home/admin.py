from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)