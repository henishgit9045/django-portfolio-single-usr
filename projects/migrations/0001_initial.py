# Generated by Django 3.1.2 on 2021-01-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='projects/')),
                ('image1', models.ImageField(upload_to='projects/')),
                ('image2', models.ImageField(upload_to='projects/')),
                ('image3', models.ImageField(upload_to='projects/')),
                ('project_name', models.CharField(max_length=100)),
                ('project_detail', models.TextField()),
                ('project_category', models.CharField(max_length=100)),
                ('project_date', models.DateField()),
                ('project_url', models.URLField()),
            ],
        ),
    ]
