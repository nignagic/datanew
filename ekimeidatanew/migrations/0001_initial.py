# Generated by Django 3.0.2 on 2020-02-11 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_name', models.CharField(max_length=100, verbose_name='鉄道種別')),
                ('railway_type_code', models.IntegerField(default=0, verbose_name='鉄道種別コード')),
                ('sort_by_railway_type', models.IntegerField(default=0, verbose_name='鉄道種別ごとの並び順')),
                ('railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2')),
                ('sort_by_railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2ごとの並び順')),
                ('company_code', models.IntegerField(default=0, verbose_name='事業者コード')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名')),
                ('company_name_short', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名（愛称）')),
                ('company_name_kana', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名読み（かな）')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_name', models.CharField(max_length=100, verbose_name='鉄道種別')),
                ('railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2')),
                ('sort_by_railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2ごとの並び順')),
                ('line_code', models.IntegerField(default=0, unique=True, verbose_name='路線コード')),
                ('line_group_code', models.IntegerField(default=0, verbose_name='路線グループコード')),
                ('line_name_formal', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名（鉄道要覧）')),
                ('line_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名')),
                ('sort_by_company', models.IntegerField(default=0, verbose_name='事業者ごとの並び順')),
                ('start_station', models.CharField(blank=True, max_length=200, null=True, verbose_name='始点駅')),
                ('end_station', models.CharField(blank=True, max_length=200, null=True, verbose_name='終点駅')),
                ('business_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='第n種事業者')),
                ('is_freight', models.CharField(blank=True, max_length=200, null=True, verbose_name='貨物輸送')),
                ('company_name_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名2')),
            ],
        ),
        migrations.CreateModel(
            name='Railway_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2コード')),
                ('railway_type_code', models.IntegerField(default=0, verbose_name='鉄道種別コード')),
                ('railway_type_name', models.CharField(max_length=100, verbose_name='鉄道種別')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2')),
                ('sort_by_railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2ごとの並び順')),
                ('station_code', models.IntegerField(default=0, verbose_name='駅コード')),
                ('station_group_code', models.IntegerField(default=0, verbose_name='駅グループコード')),
                ('station_cd_old', models.IntegerField(default=0, verbose_name='駅コード（旧）')),
                ('station_g_cd_old', models.IntegerField(default=0, verbose_name='駅グループコード（旧）')),
                ('station_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名')),
                ('station_name_kana', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名読み（かな）')),
                ('station_name_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名読み（英語）')),
                ('railway_type', models.CharField(max_length=100, verbose_name='鉄道種別')),
                ('line_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名')),
                ('sort_by_line', models.IntegerField(default=0, verbose_name='路線ごとの並び順')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名')),
                ('company_code', models.IntegerField(default=0, verbose_name='事業者コード')),
                ('sort_by_company', models.IntegerField(default=0, verbose_name='事業者ごとの並び順')),
                ('line_cd_old', models.IntegerField(default=0, verbose_name='路線コード（旧）')),
                ('pref_cd_old', models.IntegerField(default=0, verbose_name='都道府県コード（旧）')),
                ('post_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅郵便番号（旧）')),
                ('add_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='住所（旧）')),
                ('lon_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='経度（旧）')),
                ('lat_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='緯度（旧）')),
                ('open_ymd_old', models.DateField(blank=True, max_length=200, null=True, verbose_name='開業年月日（旧）')),
                ('close_ymd_old', models.DateField(blank=True, max_length=200, null=True, verbose_name='廃止年月日（旧）')),
                ('e_status_old', models.IntegerField(choices=[(0, '運用中'), (1, '運用前'), (2, '廃止')], default=0, verbose_name='状態（旧）')),
                ('e_sort_old', models.IntegerField(default=0, verbose_name='並び順（旧）')),
                ('sort', models.IntegerField(default=0, verbose_name='並び順')),
                ('line_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeidatanew.Line', to_field='line_code', verbose_name='路線コード')),
            ],
        ),
    ]
