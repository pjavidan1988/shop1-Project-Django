# Generated by Django 3.2 on 2021-04-27 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_setting_aboutus_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='aboutus_image',
        ),
    ]