# Generated by Django 3.1.7 on 2021-07-07 16:09

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210707_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='create_at',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
    ]
