# Generated by Django 2.2.4 on 2019-12-24 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecom', '0015_auto_20191224_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='added_to_cart',
        ),
        migrations.CreateModel(
            name='AddCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecom.Product')),
            ],
        ),
    ]
