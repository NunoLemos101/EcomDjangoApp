# Generated by Django 2.2.4 on 2019-12-20 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0008_auto_20191219_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]