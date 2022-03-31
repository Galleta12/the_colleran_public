# Generated by Django 4.0.2 on 2022-03-02 20:24

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_sizes_for_clothes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo_principal',
            field=sorl.thumbnail.fields.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_principal_2',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_principal_3',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_principal_4',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
