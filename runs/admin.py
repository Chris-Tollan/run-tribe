from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Runs, Booking


@admin.register(Runs)
class RunsAdmin(SummernoteModelAdmin):
    """
    registers runs model in admin
    """

    list_display = ('title', 'slug', 'status', 'updated_on')
    search_fields = ['title', 'description']
    list_filter = ('status', 'updated_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'excerpt',)


admin.site.register(Booking)
