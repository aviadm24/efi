# Generated by Django 2.0.3 on 2018-04-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(blank=True, max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer_data',
            name='address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='customer_data',
            name='contact',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customer_data',
            name='email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
        migrations.AddField(
            model_name='customer_data',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='driver_data',
            name='address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='driver_data',
            name='contact',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='driver_data',
            name='email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
        migrations.AddField(
            model_name='driver_data',
            name='id_num',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='driver_data',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='provider_data',
            name='address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='provider_data',
            name='contact',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='provider_data',
            name='email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
        migrations.AddField(
            model_name='provider_data',
            name='id_num',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='provider_data',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]