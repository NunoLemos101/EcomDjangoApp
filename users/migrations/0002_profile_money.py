# Generated by Django 2.2.4 on 2019-12-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
