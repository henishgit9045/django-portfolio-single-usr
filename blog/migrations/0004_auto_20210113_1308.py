# Generated by Django 3.1.2 on 2021-01-13 07:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210113_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 13, 7, 38, 58, 654768, tzinfo=utc)),
        ),
    ]
