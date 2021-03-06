# Generated by Django 4.0.2 on 2022-02-24 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='What_WE_DO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_name', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255)),
                ('decription', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
