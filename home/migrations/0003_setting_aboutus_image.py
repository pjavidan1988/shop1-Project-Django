# Generated by Django 3.2 on 2021-04-27 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_setting_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='aboutus_image',
            field=models.ImageField(blank=True, upload_to='images/aboutus/%Y/%m/%d/'),
        ),
    ]
