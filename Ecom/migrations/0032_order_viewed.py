# Generated by Django 2.2.4 on 2019-12-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0031_auto_20191227_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
