# Generated by Django 2.0.3 on 2019-04-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_main_list_model_customer_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_list_model',
            name='Customer_num',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer number'),
        ),
    ]
