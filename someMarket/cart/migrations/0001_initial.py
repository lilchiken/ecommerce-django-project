# Generated by Django 4.1.7 on 2023-04-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.JSONField(default=None, verbose_name='Продукты')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=400)),
                ('customer_name', models.CharField(max_length=100, verbose_name='Имя Фамилия клиента')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('size', models.CharField(max_length=16)),
                ('color', models.CharField(max_length=16)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
