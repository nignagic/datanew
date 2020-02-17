from django.db import models

# Create your models here.
class Railway_type(models.Model):
	railway_type_code_2 = models.IntegerField('鉄道種別2コード', default=0)
	railway_type_code = models.IntegerField('鉄道種別コード', default=0)
	railway_type_name = models.CharField('鉄道種別', max_length=100)
	def __str__(self):
		return self.railway_type_name

class Company(models.Model):
	railway_type_name = models.CharField('鉄道種別', max_length=100)
	railway_type_code = models.IntegerField('鉄道種別コード', default=0)
	company_code = models.IntegerField('事業者コード', default=0, unique=True)
	company_name = models.CharField('事業者名', max_length=200, null=True, blank=True)
	company_name_short = models.CharField('事業者名（愛称）', max_length=200, null=True, blank=True)
	company_name_short_2 = models.CharField('事業者名（愛称2）', max_length=200, null=True, blank=True)
	company_name_kana = models.CharField('事業者名読み（かな）', max_length=200, null=True, blank=True)
	def __str__(self):
		return self.company_name

class Line(models.Model):
	railway_type_name = models.CharField('鉄道種別', max_length=100)
	line_code = models.IntegerField('路線コード', default=0, unique=True)
	line_group_code = models.IntegerField('路線グループコード', default=0)
	line_name_formal = models.CharField('路線名（鉄道要覧）', max_length=200, null=True, blank=True)
	line_name = models.CharField('路線名', max_length=200, null=True, blank=True)
	line_name_sub = models.CharField('路線区別名', max_length=200, null=True, blank=True)
	company_code = models.ForeignKey(Company, to_field='company_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='事業者コード')
	sort_by_company = models.IntegerField('事業者ごとの並び順', default=0)
	start_station = models.CharField('始点駅', max_length=200, null=True, blank=True)
	end_station = models.CharField('終点駅', max_length=200, null=True, blank=True)
	business_type = models.CharField('第n種事業者', max_length=200, null=True, blank=True)
	is_freight = models.CharField('貨物輸送', max_length=200, null=True, blank=True)
	company_name_2 = models.CharField('事業者名2', max_length=200, null=True, blank=True)
	def __str__(self):
		if self.line_name_sub:
			return self.company_code.company_name + " " + self.line_name + "(" + self.line_name_sub + ")"
		else:
			return self.company_code.company_name + " " + self.line_name

class Station(models.Model):
	station_code = models.IntegerField('駅コード', default=0, unique=True)
	station_group_code = models.IntegerField('駅グループコード', default=0)
	station_name = models.CharField('駅名', max_length=200, null=True, blank=True)
	station_name_kana = models.CharField('駅名読み（かな）', max_length=200, null=True, blank=True)
	station_name_en = models.CharField('駅名読み（英語）', max_length=200, null=True, blank=True)
	railway_type = models.CharField('鉄道種別', max_length=100)
	line_name = models.CharField('路線名', max_length=200, null=True, blank=True)
	line_code = models.ForeignKey(Line, to_field='line_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='路線コード')
	sort_by_line = models.IntegerField('路線ごとの並び順', null=True, blank=True, default=0)
	pref_cd_old = models.IntegerField('都道府県コード（旧）', null=True, blank=True, default=0)
	post_old = models.CharField('駅郵便番号（旧）', max_length=200, null=True, blank=True)
	add_old = models.CharField('住所（旧）', max_length=200, null=True, blank=True)
	lon_old = models.CharField('経度（旧）', max_length=200, null=True, blank=True)
	lat_old = models.CharField('緯度（旧）', max_length=200, null=True, blank=True)
	open_ymd_old = models.DateField('開業年月日（旧）', max_length=200, null=True, blank=True)
	close_ymd_old = models.DateField('廃止年月日（旧）', max_length=200, null=True, blank=True)

	STATUS = (
		(0, '運用中'),
		(1, '運用前'),
		(2, '廃止')
	)
	e_status_old = models.IntegerField('状態（旧）', null=True, blank=True, choices=STATUS, default=0)
	e_sort_old = models.IntegerField('並び順（旧）', null=True, blank=True, default=0)
	sort = models.IntegerField('並び順', null=True, blank=True, default=0)
	def __str__(self):
		return self.station_name

class LineService(models.Model):
	line_service_code = models.CharField('路線コード(運行系統)', max_length=10, unique=True)
	line_service_name_formal = models.CharField('路線名（鉄道要覧）', max_length=200, null=True, blank=True)
	line_code = models.ManyToManyField(Line, blank=True, verbose_name='路線コード(正式)')
	company_name_simple = models.CharField('事業者名(簡易)', max_length=200, null=True, blank=True)
	line_service_name = models.CharField('路線名', max_length=200, null=True, blank=True)
	line_service_name_sub = models.CharField('路線区別名', max_length=200, null=True, blank=True)
	company_code = models.ForeignKey(Company, to_field='company_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='事業者コード')
	sort_by_company = models.IntegerField('事業者ごとの並び順', default=0)
	is_formal = models.CharField('正式区間', max_length=200, null=True, blank=True)
	is_service = models.CharField('正式区間', max_length=200, null=True, blank=True)
	def __str__(self):
		name = ""
		if self.company_name_simple:
			name += self.company_name_simple + " "
		name += self.line_service_name
		if self.line_service_name_sub:
			name += "(" + self.line_service_name_sub + ")"
		if self.is_formal and (self.is_service==""):
			name += "[正式区間]"
		if (self.is_formal=="") and self.is_service:
			name += "[運行系統]"
		return name

class StationService(models.Model):
	station_service_code = models.IntegerField('駅コード(運行系統)', default=0, unique=True)
	station_code = models.ForeignKey(Station, to_field='station_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='駅コード(正式)')
	station_name = models.CharField('駅名', max_length=200, null=True, blank=True)
	line_service_name = models.CharField('路線名(運行系統)', max_length=200, null=True, blank=True)
	line_service_code = models.ForeignKey(LineService, to_field='line_service_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='路線コード(運行系統)')
	numbering_symbol = models.CharField('路線記号', max_length=200, null=True, blank=True)
	numbering_number = models.CharField('駅番号', max_length=200, null=True, blank=True)
	sort_by_line_service = models.IntegerField('路線(運行系統)ごとの並び順', null=True, blank=True, default=0)
	def __str__(self):
		return self.station_name