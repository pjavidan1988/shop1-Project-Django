# Generated by Django 3.1.7 on 2021-04-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_auto_20210421_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='#', upload_to='product2/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default='#', upload_to='product3/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, default='#', upload_to='product4/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, default='#', upload_to='product5/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, default='#', upload_to='product6/%Y/%m/%d'),
        ),
    ]
