# Generated by Django 2.2.4 on 2020-01-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200102_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='ValidationYear',
            field=models.IntegerField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027)]),
        ),
    ]
