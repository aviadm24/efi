# Generated by Django 2.0.3 on 2018-04-25 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180425_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_list_model',
            name='DepOrArr',
        ),
    ]