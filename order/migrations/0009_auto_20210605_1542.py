# Generated by Django 3.1.7 on 2021-06-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20210605_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='amount',
            field=models.IntegerField(),
        ),
    ]