# Generated by Django 3.0.2 on 2020-01-09 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei1', '0009_auto_20191207_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_cd', models.IntegerField(default=0, unique=True, verbose_name='駅コード')),
                ('station_g_cd', models.IntegerField(default=0, verbose_name='駅グループコード')),
                ('station_name', models.CharField(max_length=200, verbose_name='駅名')),
                ('station_name_k', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名(カナ)')),
                ('station_name_r', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名(ローマ字)')),
                ('post', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅郵便番号')),
                ('add', models.CharField(blank=True, max_length=200, null=True, verbose_name='住所')),
                ('lon', models.CharField(blank=True, max_length=200, null=True, verbose_name='経度')),
                ('lat', models.CharField(blank=True, max_length=200, null=True, verbose_name='緯度')),
                ('open_ymd', models.DateField(blank=True, max_length=200, null=True, verbose_name='開業年月日')),
                ('close_ymd', models.DateField(blank=True, max_length=200, null=True, verbose_name='廃止年月日')),
                ('e_status', models.IntegerField(choices=[(0, '運用中'), (1, '運用前'), (2, '廃止')], default=0, verbose_name='状態')),
                ('e_sort', models.IntegerField(default=0, verbose_name='並び順')),
                ('line_cd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimei1.Line', to_field='line_cd', verbose_name='路線')),
                ('pref_cd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimei1.Prefecture', verbose_name='都道府県')),
            ],
        ),
    ]
