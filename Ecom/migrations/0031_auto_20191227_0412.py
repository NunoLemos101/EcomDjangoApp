# Generated by Django 2.2.4 on 2019-12-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0030_auto_20191227_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='Error', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(blank=True, default='Not Provided Yet', max_length=20),
        ),
    ]
