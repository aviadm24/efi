# Generated by Django 2.0.3 on 2018-04-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180425_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_list_model',
            name='Total_extra_client',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='main_list_model',
            name='Total_extra_provider',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main_list_model',
            name='Luggage',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
