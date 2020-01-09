from django import template
from ekimei1.models import Station
register = template.Library()

@register.filter(name='get_station_cd')
def get_station_cd(value):
	return Station.objects.get(station_cd=value)