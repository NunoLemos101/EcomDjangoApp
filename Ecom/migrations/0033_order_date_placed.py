# Generated by Django 2.2.4 on 2019-12-28 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0032_order_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]