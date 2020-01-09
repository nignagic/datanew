from django.contrib import admin

from .models import Prefecture, Line, Station, Category, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie

class StationAdmin(admin.ModelAdmin):
	list_display = ('id', 'station_cd', 'station_name', 'line_cd', 'add', 'e_sort')
	list_editable = ['e_sort']
	search_fields = ['station_name']

class StationInMovieAdmin(admin.ModelAdmin):
	list_display = ('id', 'id_in_movie', 'station_cd', 'station_name')
	search_fields = ['station_name']

class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'channel', 'main_id', 'published_at', 'is_collab')

admin.site.register(Prefecture)
admin.site.register(Line)
admin.site.register(Station, StationAdmin)
admin.site.register(Category)
admin.site.register(Creator)
admin.site.register(YoutubeChannel)
admin.site.register(Name)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Vocal)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Part)
admin.site.register(StationInMovie, StationInMovieAdmin)