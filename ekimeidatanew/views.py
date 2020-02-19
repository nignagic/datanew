from django.shortcuts import render
from django.views import generic
from .models import Railway_type, Company, Line, Station, LineService, StationService
import csv
from io import TextIOWrapper

# Create your views here.
def uploadStation(request):
	if 'csv' in request.FILES:
		stations = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				station_code = line[0]
				station_group_code = line[1]
				station_name = line[2]
				station_name_kana = line[3]
				station_name_en = line[4]
				railway_type = line[5]
				line_name = line[6]
				line_code = Line.objects.get(line_code=line[7])
				if line[8] != '':
					sort_by_line = line[8]
				else:
					sort_by_line = None;
				if line[9] != '':
					pref_cd_old = line[9]
				else:
					pref_cd_old = None;
				post_old = line[10]
				add_old = line[11]
				lon_old = line[12]
				lat_old = line[13]
				if line[14] != '':
					open_ymd_old = line[14]
				else:
					open_ymd_old = None;
				if line[15] != '':
					close_ymd_old = line[15]
				else:
					close_ymd_old = None;
				if line[16] != '':
					e_status_old = line[16]
				else:
					e_status_old = None;
				if line[17] != '':
					e_sort_old = line[17]
				else:
					e_sort_old = None;
				if line[18] != '':
					sort = line[18]
				else:
					sort = None;

				station = Station(
					station_code=station_code,
					station_group_code=station_group_code,
					station_name=station_name,
					station_name_kana=station_name_kana,
					station_name_en=station_name_en,
					railway_type=railway_type,
					line_name=line_name, 
					line_code=line_code,
					sort_by_line=sort_by_line,
					pref_cd_old=pref_cd_old,
					post_old=post_old,
					add_old=add_old,
					lon_old=lon_old,
					lat_old=lat_old,
					open_ymd_old=open_ymd_old,
					close_ymd_old=close_ymd_old,
					e_status_old=e_status_old,
					e_sort_old=e_sort_old,
					sort=sort)
				stations.append(station)
			else:
				i+=1
		Station.objects.bulk_create(stations)

		return render(request, 'ekimeidatanew/upload.html')

	else:
		return render(request, 'ekimeidatanew/upload.html')

def uploadLine(request):
	if 'csv' in request.FILES:
		lines = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				railway_type_name = line[0]
				line_code = line[1]
				line_group_code = line[2]
				line_name_formal = line[3]
				line_name = line[4]
				line_name_sub = line[5]
				company_code = Company.objects.get(company_code=line[6])
				sort_by_company = line[7]
				start_station = line[8]
				end_station = line[9]
				business_type = line[10]
				is_freight = line[11]
				l = Line(
					railway_type_name=railway_type_name,
					line_code=line_code,
					line_group_code=line_group_code,
					line_name_formal=line_name_formal,
					line_name=line_name,
					line_name_sub=line_name_sub,
					company_code=company_code,
					sort_by_company=sort_by_company,
					start_station=start_station,
					end_station=end_station,
					business_type=business_type,
					is_freight=is_freight)
				lines.append(l)
			else:
				i+=1
		Line.objects.bulk_create(lines)

		return render(request, 'ekimeidatanew/upload.html')

	else:
		return render(request, 'ekimeidatanew/upload.html')

def uploadCompany(request):
	if 'csv' in request.FILES:
		companies = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				railway_type_name = line[0]
				railway_type_code = line[1]
				company_code = line[2]
				company_name = line[3]
				company_name_short = line[4]
				company_name_short_2 = line[5]
				company_name_kana =line[6]
				company = Company(
					railway_type_name=railway_type_name,
					railway_type_code=railway_type_code,
					company_code=company_code,
					company_name=company_name,
					company_name_short=company_name_short,
					company_name_short_2=company_name_short_2,
					company_name_kana=company_name_kana)
				companies.append(company)
			else:
				i+=1
		Company.objects.bulk_create(companies)

		return render(request, 'ekimeidatanew/upload.html')

	else:
		return render(request, 'ekimeidatanew/upload.html')

def uploadStationService(request):
	if 'csv' in request.FILES:
		stationservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				station_service_code = line[0]
				station_code = Station.objects.get(station_code=line[1])
				station_name = line[2]
				line_service_name = line[3]
				line_service_code = LineService.objects.get(line_service_code=line[4])
				numbering_head = line[5]
				numbering_symbol = line[6]
				numbering_middle = line[7]
				numbering_number = line[8]
				sort_by_line_service = line[9]

				stationservice = StationService(
					station_service_code=station_service_code,
					station_code=station_code,
					station_name=station_name,
					line_service_name=line_service_name,
					line_service_code=line_service_code,
					numbering_head=numbering_head,
					numbering_symbol=numbering_symbol,
					numbering_middle=numbering_middle,
					numbering_number=numbering_number,
					sort_by_line_service=sort_by_line_service
					)
				stationservices.append(stationservice)
			else:
				i+=1
		StationService.objects.bulk_create(stationservices)

		return render(request, 'ekimeidatanew/upload.html')

	else:
		return render(request, 'ekimeidatanew/upload.html')

def uploadLineService(request):
	if 'csv' in request.FILES:
		lineservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				line_service_code = line[0]
				line_service_name_formal = line[1]
				line_service_name_formal_sub = line[2]

				company_name_simple = line[4]
				is_company_name = line[5]
				line_service_name = line[6]
				line_service_name_sub = line[7]
				company_code = Company.objects.get(company_code=line[8])
				sort_by_company = line[9]
				is_formal = line[10]
				is_service = line[11]
				lineservice = LineService(
					line_service_code=line_service_code,
					line_service_name_formal=line_service_name_formal,
					line_service_name_formal_sub=line_service_name_formal_sub,
					
					company_name_simple=company_name_simple,
					is_company_name=is_company_name,
					line_service_name=line_service_name,
					line_service_name_sub=line_service_name_sub,
					company_code=company_code,
					sort_by_company=sort_by_company,
					is_formal=is_formal,
					is_service=is_service)
				lineservices.append(lineservice)
			else:
				i+=1
		LineService.objects.bulk_create(lineservices)

		return render(request, 'ekimeidatanew/upload.html')

	else:
		return render(request, 'ekimeidatanew/upload.html')

def uploadRailwayType(request):
	if 'csv' in request.FILES:
		railwaytypes = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			railway_type_code_2 = line[0]
			railway_type_code = line[1]
			railway_type_name = line[2]
			railwaytype = Railway_type(railway_type_code_2=railway_type_code_2, railway_type_code=railway_type_code, railway_type_name=railway_type_name)
			railwaytypes.append(railwaytype)
		Railway_type.objects.bulk_create(railwaytypes)

		return render(request, 'ekimeidatanew/upload.html')

	else:
		return render(request, 'ekimeidatanew/upload.html')

def StationDelete(request):
	Station.objects.all().delete()
	return render(request, 'ekimeidatanew/upload.html')

def LineDelete(request):
	Line.objects.all().delete()
	return render(request, 'ekimeidatanew/upload.html')

def CompanyDelete(request):
	Company.objects.all().delete()
	return render(request, 'ekimeidatanew/upload.html')

def StationServiceDelete(request):
	StationService.objects.all().delete()
	return render(request, 'ekimeidatanew/upload.html')

def LineServiceDelete(request):
	LineService.objects.all().delete()
	return render(request, 'ekimeidatanew/upload.html')

class StationListbyLineView(generic.ListView):
	model = Line
	template_name = 'ekimeidatanew/stationlistbyline.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		line = Line.objects.get(line_code=self.kwargs['line_code'])
		stations = Station.objects.filter(line_code=self.kwargs['line_code'])
		transfers = {}
		for station in stations:
			transfers[station] = Station.objects.filter(station_group_code=station.station_group_code).exclude(line_code=line)
		context = {
			'line': line,
			'transfers': transfers
		}
		return context

class StationServiceListbyLineView(generic.ListView):
	model = LineService
	template_name = 'ekimeidatanew/stationservicelistbyline.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		lineservice = LineService.objects.get(line_service_code=self.kwargs['line_service_code'])
		stationservices = StationService.objects.filter(line_service_code=self.kwargs['line_service_code']).order_by('sort_by_line_service').exclude(station_code__e_status_old=2)
		transfers = {}
		stationserviceprev = 0
		for stationservice in stationservices:
			if stationserviceprev != stationservice.station_code.station_group_code:
				transfers[stationservice] = {}
				transferstations = Station.objects.filter(station_group_code=stationservice.station_code.station_group_code)
				for transferstation in transferstations:
					transfers[stationservice][transferstation] = StationService.objects.filter(station_code=transferstation.station_code).exclude(line_service_code=lineservice)
					if transfers[stationservice][transferstation].first() is None:
						del transfers[stationservice][transferstation]
			stationserviceprev = stationservice.station_code.station_group_code
		context = {
			'lineservice': lineservice,
			'transfers': transfers
		}
		return context

class LineServiceListbyCompanyView(generic.ListView):
	model = Company
	template_name = 'ekimeidatanew/company.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		companies = Company.objects.all()
		linebycompany = {}
		for company in companies:
			linebycompany[company] = LineService.objects.filter(company_code=company).order_by('sort_by_company')
			if linebycompany[company].first() is None:
				del linebycompany[company]
		context = {
			'linebycompany': linebycompany
		}
		return context

class StationSearchView(generic.ListView):
	model = StationService
	template_name = 'ekimeidatanew/stationsearch.html'

	def get_context_data(self, **kwargs):
		q_word = self.request.GET.get('q')

		if q_word:
			stations = StationService.objects.filter(station_name__icontains=q_word).order_by('line_service_code').exclude(station_code__e_status_old=2)
		count = stations.count()
		context = {
			'word': q_word,
			'stations': stations,
			'count': count
		}
		return context