# Generated by Django 4.0.2 on 2022-03-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_we_dos', '0003_rename_created_date_what_do_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='what_do',
            name='icons',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
