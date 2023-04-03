from typing import (
    List,
    Dict
)

from django.http import HttpRequest
from django.conf import settings
from django.db import models

from store.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        order_objs = self.session.get(settings.ORDER_OBJS_SESSION_ID)
        if (not isinstance(cart, Dict) or not isinstance(order_objs, List)):
            self.session[settings.CART_SESSION_ID] = {}
            self.session[settings.ORDER_OBJS_SESSION_ID] = []
        self.cart: Dict = self.session[settings.CART_SESSION_ID]
        self.order_objs: List[Dict] = self.session[settings.ORDER_OBJS_SESSION_ID]

    def __iter__(self):
        products = Product.objects.filter(
            id__in=self.cart.keys()
        )
        for product in products:
            yield product

    def add(self, product_id: int, quantity: int):
        if not self.cart.get(str(product_id)):
            self.cart[str(product_id)] = {
                'quantity': quantity
            }
        else:
            self.cart[str(product_id)] = {
                'quantity': int(
                    self.cart[str(product_id)]['quantity']
                ) + int(quantity)
            }
        self.save()

    def add_order_objs(self, dict_obj: Dict):
        self.session[settings.ORDER_OBJS_SESSION_ID].append(dict_obj)
        self.save_orders()

    def remove(self, product_id):
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def save_orders(self):
        self.session[settings.ORDER_OBJS_SESSION_ID] = self.order_objs
        self.session.modified = True

    def count_item(self, product_id):
        return self.cart[str(product_id)]['quantity']

    def total_count(self):
        return sum(
            [item['quantity'] for item in self.cart.values()]
        )

    def total_price(self):
        return sum(
            Product.objects.get(
                id=int(id)
            ).price*item['quantity'] for id, item in self.cart.items()
        )

    def clear(self):
        self.cart.clear()

    def clear_order_objs(self):
        self.order_objs.clear()
        self.save_orders()

    def __len__(self):
        return len(self.cart.keys())


class ProductOrder(models.Model):
    """Эта модель используется для формы."""

    product_id = models.IntegerField()
    size = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.product


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
