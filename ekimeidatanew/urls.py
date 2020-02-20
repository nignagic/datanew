from django.urls import path
from django.conf.urls import url, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
# router.register('station', views.StationViewSet)
# router.register('line/<int:pref_cd>', views.LineViewSet.as_view(), base_name='lines')
urlpatterns = router.urls

app_name = 'ekimeidatanew'

urlpatterns = [
	path('line/<int:line_code>/', views.StationListbyLineView.as_view(), name='stationlistbylineview'),
	path('lineservice/<slug:line_service_code>/', views.StationServiceListbyLineView.as_view(), name='stationservicelistbylineview'),
	path('linelist/', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompanyview'),
	path('stationsearch/', views.StationSearchView.as_view(), name='stationsearchview'),
	path('upload/', views.uploadStation, name='uploadStation'),
	path('uploadline/', views.uploadLine, name='uploadLine'),
	path('uploadcompany/', views.uploadCompany, name='uploadCompany'),
	path('uploadrailwaytype/', views.uploadRailwayType, name='uploadRailwayType'),
	path('uploadstationservice/', views.uploadStationService, name='uploadStationService'),
	path('uploadlineservice/', views.uploadLineService, name='uploadLineService'),
	path('stationdelete/', views.StationDelete, name='StationDelete'),
	path('linedelete/', views.LineDelete, name='LineDelete'),
	path('companydelete/', views.CompanyDelete, name='CompanyDelete'),
	path('stationservicedelete/', views.StationServiceDelete, name='StationServiceDelete'),
	path('lineservicedelete/', views.LineServiceDelete, name='LineServiceDelete'),
	path('notice/', views.NoticeView.as_view(), name='notice'),
]