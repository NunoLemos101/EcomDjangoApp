# Generated by Django 2.2.4 on 2019-12-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0007_auto_20191219_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='3i1415926543PI.jpg', upload_to='images'),
        ),
    ]