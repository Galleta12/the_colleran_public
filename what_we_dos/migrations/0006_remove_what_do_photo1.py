# Generated by Django 4.0.2 on 2022-03-28 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('what_we_dos', '0005_what_do_photo1_what_do_photo2_what_do_photo3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='what_do',
            name='photo1',
        ),
    ]
