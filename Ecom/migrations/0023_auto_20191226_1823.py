# Generated by Django 2.2.4 on 2019-12-26 17:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0022_remove_product_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='clicks',
            field=models.ManyToManyField(default=None, related_name='clicks', to=settings.AUTH_USER_MODEL),
        ),
    ]
