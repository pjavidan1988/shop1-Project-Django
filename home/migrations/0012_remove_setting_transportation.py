# Generated by Django 3.1.7 on 2021-05-31 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210531_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='Transportation',
        ),
    ]
