# Generated by Django 2.0.3 on 2019-06-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190528_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main_list_model',
            old_name='status_cheshbonit_yeruka1',
            new_name='Provider_status',
        ),
        migrations.RenameField(
            model_name='main_list_model',
            old_name='status_cheshbonit_yeruka2',
            new_name='Client_status',
        ),
    ]
