from django.contrib import admin
from .models import Runs, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Runs)
class RunsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'updated_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'runs', 'approved')
    list_filter = ('approved', 'runs')
    search_fields = ('user__username', 'runs__title', 'approved')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
