# Generated by Django 2.2.4 on 2019-12-24 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0017_auto_20191224_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shipping_time',
            new_name='time_you_will_take_to_send_the_product',
        ),
    ]
