# Generated by Django 3.0.5 on 2020-04-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_auto_20200427_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckrent',
            name='drop_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='truckrent',
            name='pickup_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]