# Generated by Django 3.1.7 on 2021-06-05 10:34

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_product_transportation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]
