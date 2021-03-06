# Generated by Django 3.1.2 on 2021-01-14 03:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210113_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 14, 3, 45, 10, 102656, tzinfo=utc)),
        ),
    ]
