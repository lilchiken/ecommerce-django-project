# Generated by Django 4.1.7 on 2023-03-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_remove_order_products_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='product',
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product_id',
            field=models.IntegerField(),
        ),
    ]
