from django.contrib import admin
from trips.models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'start', 'finish', 'date']

admin.site.register(Trip,TripAdmin)
