# Generated by Django 2.2.4 on 2020-01-02 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0046_auto_20200102_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], validators=[django.core.validators.MinValueValidator(-0.0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]