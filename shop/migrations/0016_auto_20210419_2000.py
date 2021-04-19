# Generated by Django 3.1.7 on 2021-04-19 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210419_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(100000)]),
        ),
    ]
