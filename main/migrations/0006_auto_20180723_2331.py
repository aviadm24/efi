# Generated by Django 2.0.3 on 2018-07-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_from_data_to_data_yeruka2_data_yeruka_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider_data',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='provider_data',
            name='contact',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]