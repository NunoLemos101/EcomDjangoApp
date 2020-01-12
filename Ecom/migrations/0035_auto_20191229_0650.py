# Generated by Django 2.2.4 on 2019-12-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0034_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Not shipped', 'Not shipped'), ('Order dispatched', 'Order dispatched')], default='Not shipped', max_length=100),
        ),
    ]
