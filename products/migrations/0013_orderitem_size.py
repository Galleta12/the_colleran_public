# Generated by Django 4.0.2 on 2022-03-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default='', max_length=255),
        ),
    ]
