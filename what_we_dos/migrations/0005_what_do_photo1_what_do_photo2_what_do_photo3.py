# Generated by Django 4.0.2 on 2022-03-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_we_dos', '0004_what_do_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='what_do',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='what_do',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='what_do',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]