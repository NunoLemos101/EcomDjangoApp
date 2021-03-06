# Generated by Django 2.2.4 on 2019-12-24 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0016_auto_20191224_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shipping_time',
            field=models.CharField(choices=[('1 Day', '1 Day'), ('2 Days', '2 Days'), ('3 Days', '3 Days'), ('4 Days', '4 Days'), ('5 Days', '5 Days'), ('6 Days', '6 Days'), ('7 Days', '7 Days')], default='7 Days', max_length=7),
        ),
        migrations.AlterField(
            model_name='addcart',
            name='number',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
