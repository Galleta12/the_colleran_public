# Generated by Django 4.0.2 on 2022-02-25 13:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sizes_for_clothes_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes_for_clothes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'L'), ('M', 'M'), ('S', 'S'), ('XL', 'XL'), ('XXL', 'XXL'), ('Child 11-13', 'Child 11-13'), ('Child 3-4', 'Child 3-4'), ('Child 5-6', 'Child 5-6'), ('Child 7-8', 'Child 7-8'), ('Child 9-10', 'Child 9-10')], max_length=65),
        ),
    ]
