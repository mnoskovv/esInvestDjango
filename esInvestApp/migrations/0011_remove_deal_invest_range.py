# Generated by Django 3.0.5 on 2020-04-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esInvestApp', '0010_deal_invest_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='invest_range',
        ),
    ]
