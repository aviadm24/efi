# Generated by Django 2.0.3 on 2019-04-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_main_list_model_flight_shcedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_list_model',
            name='Customer_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='Customer number'),
        ),
    ]
