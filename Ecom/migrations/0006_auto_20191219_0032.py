# Generated by Django 2.2.4 on 2019-12-18 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0005_auto_20191218_2340'),
    ]

    operations = [
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
    ]
