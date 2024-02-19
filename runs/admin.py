from django.contrib import admin
from .models import Runs, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Runs)
class RunsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'updated_on')
    search_fields = ['title', 'description']
    list_filter = ('status', 'updated_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'excerpt',)


admin.site.register(Booking)
