# Generated by Django 2.2.4 on 2019-12-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0027_auto_20191226_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
