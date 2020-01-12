# Generated by Django 2.2.4 on 2019-12-18 21:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.TextField(default='This Product has no Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
    ]
