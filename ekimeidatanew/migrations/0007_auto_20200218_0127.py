# Generated by Django 3.0.2 on 2020-02-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeidatanew', '0006_auto_20200217_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineservice',
            name='is_company_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='語頭会社名'),
        ),
        migrations.AddField(
            model_name='lineservice',
            name='line_service_name_formal_sub',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='路線区別名（鉄道要覧）'),
        ),
        migrations.AlterField(
            model_name='lineservice',
            name='is_service',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='運行系統'),
        ),
    ]