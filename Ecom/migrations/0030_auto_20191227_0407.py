# Generated by Django 2.2.4 on 2019-12-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0029_addcart_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='Error', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]