# Generated by Django 2.2.4 on 2019-12-31 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191220_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seller_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
