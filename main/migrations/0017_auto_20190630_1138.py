# Generated by Django 2.0.3 on 2019-06-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190611_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fields_to_cancel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Currency_field', models.CharField(blank=True, max_length=256, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='main_list_model',
            name='Client_status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Status Client'),
        ),
        migrations.AlterField(
            model_name='main_list_model',
            name='Customer_num',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Client Reference Number'),
        ),
        migrations.AlterField(
            model_name='main_list_model',
            name='Provider_status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Status Provider'),
        ),
        migrations.AlterField(
            model_name='main_list_model',
            name='Status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Project Status'),
        ),
    ]
