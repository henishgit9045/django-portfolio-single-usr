# Generated by Django 3.1.2 on 2021-01-13 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210113_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 13, 9, 23, 14, 561125, tzinfo=utc)),
        ),
    ]