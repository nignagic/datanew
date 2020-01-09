from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Station, Line, StationInMovie, Name, Song, Vocal

class StationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Station
		fields = ('station_name', 'station_cd', 'line_cd')

class LineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Line
		fields = ('line_name', 'line_cd')

# class TransferSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Line
# 		fields = ('line_name', 'line_cd')

class StationSearchSerializer(serializers.ModelSerializer):
	line_name = serializers.CharField(source='line_cd.line_name')
	class Meta:
		model = Station
		fields = ['station_name', 'station_cd', 'line_name']

class StationInMovieSerializer(serializers.ModelSerializer):
	station_g_cd = serializers.IntegerField(source='station_cd.station_g_cd')
	line_cd = serializers.IntegerField(source='station_cd.line_cd.line_cd')
	line_name = serializers.CharField(source='station_cd.line_cd.line_name')
	pref = serializers.CharField(source='station_cd.pref_cd.pref_name')
	class Meta:
		model = StationInMovie
		fields = ['station_name', 'station_cd', 'station_g_cd', 'line_cd', 'line_name', 'pref']

class NameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Name
		fields = ['id', 'name']

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ['id', 'name']

class VocalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vocal
		fields = ['id', 'name']