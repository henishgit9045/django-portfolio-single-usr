# Generated by Django 3.1.2 on 2021-01-13 05:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 13, 5, 32, 16, 445835, tzinfo=utc)),
        ),
    ]
