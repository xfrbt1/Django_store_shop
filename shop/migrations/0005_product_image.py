# Generated by Django 4.0.6 on 2022-08-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, height_field=100, upload_to='', width_field=100),
            preserve_default=False,
        ),
    ]
