# Generated by Django 3.0.5 on 2020-04-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
