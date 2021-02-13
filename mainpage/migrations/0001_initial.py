# Generated by Django 3.1.2 on 2021-01-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=350)),
                ('background_photo', models.ImageField(upload_to='profile/')),
                ('profile_photo', models.ImageField(upload_to='profile/')),
                ('post', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('skill', models.CharField(max_length=2500)),
                ('about_me', models.TextField()),
                ('services', models.TextField()),
                ('complete_work', models.CharField(max_length=5)),
                ('years_experiance', models.CharField(max_length=2)),
                ('total_clients', models.CharField(max_length=4)),
                ('award_won', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=100)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('github', models.URLField()),
                ('whatsapp', models.URLField()),
            ],
        ),
    ]