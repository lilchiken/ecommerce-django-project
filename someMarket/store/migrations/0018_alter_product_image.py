# Generated by Django 4.1.7 on 2023-03-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_product_count_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/products/', verbose_name='Основная фотография'),
        ),
    ]
