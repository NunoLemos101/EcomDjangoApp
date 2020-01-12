# Generated by Django 2.2.4 on 2019-12-24 16:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecom', '0014_product_shipping_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_to_cart',
            field=models.ManyToManyField(related_name='added_to_cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(-0.0)]),
        ),
        migrations.DeleteModel(
            name='AddCard',
        ),
    ]
