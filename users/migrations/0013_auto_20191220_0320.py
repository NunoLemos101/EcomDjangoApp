# Generated by Django 2.2.4 on 2019-12-20 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191220_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='WithdrawAmount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='ValidationYear',
            field=models.IntegerField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026)]),
        ),
    ]
