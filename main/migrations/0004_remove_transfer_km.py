# Generated by Django 2.0.3 on 2018-03-15 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180315_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='KM',
        ),
    ]
