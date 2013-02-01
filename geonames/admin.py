from django.contrib.gis import admin
from models import Geoname


class GeonameAdmin(admin.OSMGeoAdmin):
    search_fields = ('name',)
    list_display = ('name', 'country', 'admin1',)

admin.site.register(Geoname, GeonameAdmin)
