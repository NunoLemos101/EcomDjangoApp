# Generated by Django 2.2.4 on 2019-12-20 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_creditcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='CardUser',
        ),
    ]
