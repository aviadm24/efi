# Generated by Django 2.0.3 on 2018-07-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180723_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='From_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(blank=True, max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='To_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('To', models.CharField(blank=True, max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeruka2_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yeruka2', models.CharField(blank=True, max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeruka_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yeruka', models.CharField(blank=True, max_length=256, unique=True)),
            ],
        ),
    ]
