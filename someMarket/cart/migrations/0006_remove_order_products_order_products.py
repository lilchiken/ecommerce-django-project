# Generated by Django 4.1.7 on 2023-03-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_order_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='cart.productorder'),
        ),
    ]
