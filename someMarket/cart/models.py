from django.http import HttpRequest
from django.conf import settings

from store.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            self.session[settings.CART_SESSION_ID] = {}
        self.cart: dict = self.session[settings.CART_SESSION_ID]


    def __iter__(self):
        products = Product.objects.filter(
            id__in=self.cart.keys()
        )
        for product in products:
            yield product


    def __len__(self):
        return len(self.cart.keys())
    

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


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product_id):
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
            self.save()


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
