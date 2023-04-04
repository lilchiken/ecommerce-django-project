from typing import (
    List,
    Dict
)

from django.http import HttpRequest
from django.conf import settings

from store.models import Product


class Cart:
    """Кастомное расширение джанго-сессии.
    cart - корзина сессии.
    order_objs - продукты заказа.
    """

    def __init__(self, request: HttpRequest):
        """Здесь мы создаём упомянутые выше атрибуты,
        если они не созданы.
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        order_objs = self.session.get(settings.ORDER_OBJS_SESSION_ID)
        if (not isinstance(cart, Dict) or not isinstance(order_objs, List)):
            self.session[settings.CART_SESSION_ID] = {}
            self.session[settings.ORDER_OBJS_SESSION_ID] = []
        self.cart: Dict = self.session[settings.CART_SESSION_ID]
        self.order_objs: List[Dict] = self.session[settings.ORDER_OBJS_SESSION_ID]

    def __iter__(self):
        """Здесь мы отображаем корзину именно экземплярами модели Product."""

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
