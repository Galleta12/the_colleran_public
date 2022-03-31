# Generated by Django 4.0.2 on 2022-03-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
