from django.urls import path
from django.conf.urls import url, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
# router.register('station', views.StationViewSet)
# router.register('line/<int:pref_cd>', views.LineViewSet.as_view(), base_name='lines')
urlpatterns = router.urls

app_name = 'ekimei1'

urlpatterns = [
	path('', views.Top.as_view(), name='top'),
	path('list/', views.MovieListView.as_view(), name="list"),
	path('detail/<slug:main_id>/', views.detail_movie, name='detail'),
	path('line/<int:line_cd>/', views.MovieListbyLineView.as_view(), name='line_list'),
	path('station/<int:station_cd>/', views.MovieListbyStationView.as_view(), name='station_list'),
	path('song/<int:id>/', views.MovieListbySongView.as_view(), name='song_list'),
	path('vocal/<int:id>/', views.MovieListbyVocalView.as_view(), name='vocal_list'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('edit/<slug:main_id>/part/', views.part_edit, name='part_edit'),
	path('edit/<slug:main_id>/part/<int:part_num>/', views.station_edit, name='station_edit'),
	path('upload/', views.uploadStation, name='uploadStation'),
	path('uploadline/', views.uploadLine, name='uploadLine'),
	path('uploadpref/', views.uploadPref, name='uploadPref'),
	path('lineprefset/', views.lineprefset, name='lineprefset'),
	url('^api/line/(?P<pref_cd>.+)/$', views.LineViewSet.as_view()),
	url('^api/station/(?P<line_cd>.+)/$', views.StationViewSet.as_view()),
	url('^api/stationsearch/(?P<words>.+)/$', views.StationSearchViewSet.as_view()),
	url('^api/transfer/(?P<station_cd>.+)/$', views.TransferViewSet.as_view()),
	url('^api/partstation/(?P<id>.+)/$', views.PartStationViewSet.as_view()),
	url('api/name/', views.NameViewSet.as_view()),
	url('api/song/', views.SongViewSet.as_view()),
	url('api/vocal/', views.VocalViewSet.as_view()),
	# path('login/', views.Login.as_view(), name='login'),
	# path('logout/', views.Logout.as_view(), name='logout'),
	# path('user_create/', views.UserCreate.as_view(), name='user_create'),
	# path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
	# path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
]