from django.contrib import admin

from .models import Railway_type, Company, Line, Station

class StationAdmin(admin.ModelAdmin):
	list_display = ('id', 'station_code', 'station_name', 'line_code')

admin.site.register(Railway_type)
admin.site.register(Company)
admin.site.register(Line)
admin.site.register(Station)