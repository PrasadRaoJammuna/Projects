from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

#from django.contrib.gis.admin import OSMGeoAdmin
from .models import City


class CityAdmin(LeafletGeoAdmin):
    list_display = ('name','country','temperature','humidity')


admin.site.register(City,CityAdmin)

