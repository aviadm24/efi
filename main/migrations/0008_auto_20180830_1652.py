# Generated by Django 2.0.3 on 2018-08-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180725_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_list_model',
            name='shonot_client',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='main_list_model',
            name='shonot_provider',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]