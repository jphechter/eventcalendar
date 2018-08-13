from django.contrib import admin

from .models import Venue, Event

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','capacity')
    search_fields = ['name']

class EventAdmin(admin.ModelAdmin):
    list_display = ('name','pub_date', 'event_date')
    search_fields = ['name']

admin.site.register(Venue,VenueAdmin)
admin.site.register(Event,EventAdmin)
