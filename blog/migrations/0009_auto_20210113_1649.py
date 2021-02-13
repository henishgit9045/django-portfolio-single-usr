# Generated by Django 3.1.2 on 2021-01-13 11:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210113_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 13, 11, 19, 23, 240079, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpage')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
