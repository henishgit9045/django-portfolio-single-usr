# Generated by Django 3.1.2 on 2021-01-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20210115_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('issuing_authority', models.CharField(max_length=500)),
                ('certi_id', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='certificates/')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='total_clients',
            new_name='certificates',
        ),
    ]
