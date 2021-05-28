# Generated by Django 3.1.7 on 2021-05-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_remove_comment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'publish'), ('False', 'unpublished')], default='New', max_length=10),
        ),
    ]