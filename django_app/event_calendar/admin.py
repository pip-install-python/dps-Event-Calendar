from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CalendarEvent
# Register your models here.


class Event(SummernoteModelAdmin):
    list_display = ('approved', 'title', 'author', 'color', 'date_created', 'event_start_date', 'event_end_date')
    list_display_links = ('title', 'author',  'date_created')
    list_editable = ('approved', 'color', 'event_start_date', 'event_end_date')
    search_fields = ['approved', 'author', 'title', 'date_created', 'event_start_date', 'event_end_date']

    list_per_page = 25


admin.site.register(CalendarEvent, Event)