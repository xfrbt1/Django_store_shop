# Generated by Django 4.0.6 on 2022-08-23 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
