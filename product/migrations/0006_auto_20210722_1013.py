# Generated by Django 3.1.7 on 2021-07-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210718_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='مقدار'),
        ),
    ]
