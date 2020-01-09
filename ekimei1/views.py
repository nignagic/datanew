from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from . import serializer
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

from .models import Prefecture, Line, Station, Station2, Category, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie
from . import forms

import csv
from io import TextIOWrapper

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import (
# 	LoginView, LogoutView
# )
# from .forms import LoginForm

class Top(generic.TemplateView):
	template_name = 'ekimei1/top.html'

# class Login(LoginView):
# 	form_class = LoginForm
# 	template_name = 'ekimei1/login.html'

# class Logout(LoginRequiredMixin, LogoutView):
# 	template_name = 'ekimei1/top.html'

class MovieListView(generic.ListView):
	template_name = 'ekimei1/moviebycreator.html'
	context_object_name = 'latest_movie_list'

	def get_queryset(self):
		return Movie.objects.all().order_by('channel').order_by('-published_at')

class MovieListbyStationView(generic.ListView):
	model = Station
	template_name = 'ekimei1/moviebystationlist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		station = Station.objects.get(station_cd=self.kwargs['station_cd'])
		stations = Station.objects.filter(station_g_cd=station.station_g_cd)
		movies = []
		for station in stations:
			movies.append([])
			stationinmovies = StationInMovie.objects.filter(station_cd=station)
			for stationinmovie in stationinmovies:
				movies[-1].append(stationinmovie.movie_part.movie)
		movies_unique_order = []
		for movie in movies:
			movies_unique_order_one = sorted(set(movie), key=movie.index)
			movies_unique_order.append(movies_unique_order_one)

		context = {
			'stations': stations,
			'movies': movies_unique_order
		}
		return context

class MovieListbyLineView(generic.ListView):
	model = Line
	template_name = 'ekimei1/moviebylinelist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		stations = Station.objects.filter(line_cd=self.kwargs['line_cd'])
		movies = []
		for station in stations:
			stationinmoviefilter = StationInMovie.objects.filter(station_cd=station)
			for stationinmovie in stationinmoviefilter:
				movies.append(stationinmovie.movie_part.movie)
		movies_unique_order = sorted(set(movies), key=movies.index)

		line = Line.objects.get(line_cd=self.kwargs['line_cd'])
		context = {
			'line': line,
			'movies': movies_unique_order
		}
		return context

class MovieListbySongView(generic.ListView):
	model = Song
	template_name = 'ekimei1/moviebysonglist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		parts = Part.objects.filter(song=self.kwargs['id'])
		movies = []
		for part in parts:
			movies.append(part.movie)
		movies_unique_order = sorted(set(movies), key=movies.index)

		song = Song.objects.get(pk=self.kwargs['id'])
		context = {
			'song': song,
			'movies': movies_unique_order
		}
		return context

class MovieListbyVocalView(generic.ListView):
	model = Vocal
	template_name = 'ekimei1/moviebyvocallist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		movies = Movie.objects.filter(vocal=self.kwargs['id']).order_by('-published_at')

		vocal = Vocal.objects.get(pk=self.kwargs['id'])
		context = {
			'vocal': vocal,
			'movies': movies
		}
		return context

def detail_movie(request, main_id):
	movie = get_object_or_404(Movie, main_id=main_id)
	parts = Part.objects.filter(movie=movie).order_by('part_num')
	# stations = []
	# lines = []
	# beforeline = 0
	# for part in parts:
	# 	lines.append([])
	# 	stations.append([])
	# 	stationinpart = StationInMovie.objects.filter(movie_part=part)
	# 	for station in stationinpart:
	# 		line = station.station_cd.line_cd
	# 		lines[-1].append(line)
	# 		if (beforeline != line):
	# 			stations[-1].append([])
	# 		stations[-1][-1].append(station)
	# 		beforeline = line

	context = {
		'movie': movie,
		'parts': parts,
		# 'lines': lines,
		# 'stations': stations
	}

	return render(request, 'ekimei1/detail_design1.html', context)

class MovieRegisterView(generic.CreateView):
	template_name = 'ekimei1/register.html'
	model = Movie
	form_class = forms.MovieRegisterForm
	def get_success_url(self):
		return reverse_lazy('ekimei1:part_edit', kwargs={'main_id': self.object.main_id})

def part_edit(request, main_id):
	movie = get_object_or_404(Movie, main_id=main_id)
	form = forms.MovieUpdateForm(request.POST or None, instance=movie)
	formset = forms.PartEditFormset(request.POST or None, instance=movie)
	if request.method == 'POST' and form.is_valid() and formset.is_valid():
		# parts = Part.objects.filter(movie=movie)
		# parts.delete()
		form.save()
		formset.save()
		queryset = Part.objects.filter(movie=main_id, part_num=1)
		if queryset.first() is None:
			return redirect('ekimei1:detail', main_id=main_id)
		else:
			return redirect('ekimei1:station_edit', main_id=main_id, part_num=1)

	context = {
		'movie': movie,
		'form': form,
		'formset': formset,
	}

	return render(request, 'ekimei1/part_edit.html', context)

def station_edit(request, main_id, part_num):
	part = get_object_or_404(Part, movie=main_id, part_num=part_num)
	formset = forms.StationInMovieEditFormset(request.POST or None, instance=part)
	if request.method == 'POST' and formset.is_valid():
		stations = StationInMovie.objects.filter(movie_part=part)
		stations.delete()
		formset.save()
		queryset = Part.objects.filter(movie=main_id, part_num=part_num+1)
		if queryset.first() is None:
			return redirect('ekimei1:detail', main_id=main_id)
		else:
			return redirect('ekimei1:station_edit', main_id=main_id, part_num=part_num+1)

	context = {
		'part': part,
		'formset': formset,
	}

	return render(request, 'ekimei1/station_edit.html', context)
# class StationCreate(generic.CreateView):
# class StationCreatebyLine(generic.CreateView):
# class LineCreate(generic.CreateView):
# class SongCreate(generic.CreateView):
# class ArtistCreate(generic.CreateView):
# class PopupArtistCreate(ArtistCreate):
# class VocalCreate(generic.CreateView)
# class PopupVocalCreate(VocalCreate):
# def update_movie(request, main_id):

def uploadStation(request):
	if 'csv' in request.FILES:
		stations = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			station_cd = line[0]
			station_g_cd = line[1]
			station_name = line[2]
			station_name_k = line[3]
			station_name_r = line[4]
			line_cd = Line.objects.get(line_cd=line[5])
			pref_cd = Prefecture.objects.get(pref_cd=line[6])
			post = line[7]
			add = line[8]
			lon = line[9]
			lat = line[10]
			if line[11] != '':
				open_ymd = line[11]
			else:
				open_ymd = None;
			if line[12] != '':
				close_ymd = line[12]
			else:
				close_ymd = None;
			e_status = line[13]
			e_sort = line[14]

			station = Station(station_cd=station_cd, station_g_cd=station_g_cd, station_name=station_name, station_name_k=station_name_k, station_name_r=station_name_r, line_cd=line_cd, pref_cd=pref_cd, post=post, add=add, lon=lon, lat=lat, open_ymd=open_ymd, close_ymd=close_ymd, e_status=e_status, e_sort=e_sort)
			stations.append(station)
		Station.objects.bulk_create(stations)

		return render(request, 'ekimei1/upload.html')

	else:
		return render(request, 'ekimei1/upload.html')

def uploadLine(request):
	if 'csv' in request.FILES:
		lines = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			line_cd = line[0]
			company_cd = line[1]
			line_name = line[2]
			line_name_k = line[3]
			line_name_h = line[4]
			line_color_c = line[5]
			line_color_t = line[6]
			line_type = line[7]
			lon = line[8]
			lat = line[9]
			zoom = line[10]
			e_status = line[11]
			e_sort = line[12]
			l = Line(line_cd=line_cd, company_cd=company_cd, line_name=line_name, line_name_k=line_name_k, line_name_h=line_name_h, line_color_c=line_color_c, line_color_t=line_color_t, line_type=line_type, lon=lon, lat=lat, zoom=zoom, e_status=e_status, e_sort=e_sort)
			lines.append(l)
		Line.objects.bulk_create(lines)

		return render(request, 'ekimei1/upload.html')

	else:
		return render(request, 'ekimei1/upload.html')

def uploadPref(request):
	if 'csv' in request.FILES:
		prefectures = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			pref_cd = line[0]
			pref_name = line[1]
			pref = Prefecture(pref_cd=pref_cd, pref_name=pref_name)
			prefectures.append(pref)
		Prefecture.objects.bulk_create(prefectures)

		return render(request, 'ekimei1/upload.html')
	else:
		return render(request, 'ekimei1/upload.html')

def lineprefset(request):
	stations = Station.objects.all()
	for station in stations:
		line = station.line_cd
		pref = station.pref_cd
		line.pref_cds.add(pref)

	return render(request, 'ekimei1/lineprefset.html')

class StationViewSet(generics.ListAPIView):
	serializer_class = serializer.StationSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['line_cd']
		return Station.objects.filter(line_cd=query_my_name)

class LineViewSet(generics.ListAPIView):
	serializer_class = serializer.LineSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['pref_cd']
		return Line.objects.filter(pref_cds=query_my_name)

class StationSearchViewSet(generics.ListAPIView):
	serializer_class = serializer.StationSearchSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['words']
		return Station.objects.filter(station_name__contains=query_my_name)

class TransferViewSet(generics.ListAPIView):
	serializer_class = serializer.LineSerializer
	def get_queryset(self):
		station = Station.objects.get(station_cd=self.kwargs['station_cd'])
		stations = Station.objects.filter(station_g_cd=station.station_g_cd)
		lines = []
		for station in stations:
			lines.append(station.line_cd)
		return lines

class PartStationViewSet(generics.ListAPIView):
	serializer_class = serializer.StationInMovieSerializer
	def get_queryset(self):
		stations = StationInMovie.objects.filter(movie_part=self.kwargs['id'])
		return stations

class NameViewSet(generics.ListAPIView):
	serializer_class = serializer.NameSerializer
	def get_queryset(self):
		names = Name.objects.all()
		return names

class SongViewSet(generics.ListAPIView):
	serializer_class = serializer.SongSerializer
	def get_queryset(self):
		songs = Song.objects.all()
		return songs

class VocalViewSet(generics.ListAPIView):
	serializer_class = serializer.VocalSerializer
	def get_queryset(self):
		vocals = Vocal.objects.all()
		return vocals