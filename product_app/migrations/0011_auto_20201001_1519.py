# Generated by Django 3.1.2 on 2020-10-01 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0010_auto_20201001_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time_received',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
