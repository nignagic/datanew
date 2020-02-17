# Generated by Django 3.0.2 on 2020-02-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeidatanew', '0005_auto_20200212_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_service_code', models.CharField(max_length=10, unique=True, verbose_name='路線コード(運行系統)')),
                ('line_service_name_formal', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名（鉄道要覧）')),
                ('company_name_simple', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名(簡易)')),
                ('line_service_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名')),
                ('line_service_name_sub', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線区別名')),
                ('sort_by_company', models.IntegerField(default=0, verbose_name='事業者ごとの並び順')),
                ('is_formal', models.CharField(blank=True, max_length=200, null=True, verbose_name='正式区間')),
                ('is_service', models.CharField(blank=True, max_length=200, null=True, verbose_name='正式区間')),
                ('company_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeidatanew.Company', to_field='company_code', verbose_name='事業者コード')),
                ('line_code', models.ManyToManyField(blank=True, to='ekimeidatanew.Line', verbose_name='路線コード(正式)')),
            ],
        ),
        migrations.AlterField(
            model_name='station',
            name='station_code',
            field=models.IntegerField(default=0, unique=True, verbose_name='駅コード'),
        ),
        migrations.CreateModel(
            name='StationService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_service_code', models.IntegerField(default=0, unique=True, verbose_name='駅コード(運行系統)')),
                ('station_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名')),
                ('line_service_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名(運行系統)')),
                ('numbering_symbol', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線記号')),
                ('numbering_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅番号')),
                ('sort_by_line_service', models.IntegerField(blank=True, default=0, null=True, verbose_name='路線(運行系統)ごとの並び順')),
                ('line_service_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeidatanew.LineService', to_field='line_service_code', verbose_name='路線コード(運行系統)')),
                ('station_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeidatanew.Station', to_field='station_code', verbose_name='駅コード(正式)')),
            ],
        ),
    ]
