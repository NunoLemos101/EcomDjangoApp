# Generated by Django 2.2.4 on 2019-12-26 17:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0023_auto_20191226_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='clicks',
            field=models.ManyToManyField(blank=True, related_name='clicks', to=settings.AUTH_USER_MODEL),
        ),
    ]
