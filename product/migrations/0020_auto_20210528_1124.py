# Generated by Django 3.1.7 on 2021-05-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20210528_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
    ]