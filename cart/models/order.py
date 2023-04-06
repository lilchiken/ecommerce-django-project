from django.db import models


class ProductOrder(models.Model):
    """Эта модель используется для формы."""

    product_id = models.IntegerField()
    size = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    count = models.IntegerField(default=1)


class Order(models.Model):
    """Модель заказов, используется в API."""

    products = models.JSONField(
        verbose_name='Продукты',
        default=None
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    phone = models.CharField(
        'Телефон',
        blank=False,
        null=False,
        max_length=20
    )
    adress = models.CharField(
        'Адрес',
        blank=False,
        null=False,
        max_length=400
    )
    customer_name = models.CharField(
        verbose_name='Имя Фамилия клиента',
        blank=False,
        null=False,
        max_length=100
    )
    created = models.DateTimeField(
        'Время создания заказа',
        auto_now_add=True
    )
