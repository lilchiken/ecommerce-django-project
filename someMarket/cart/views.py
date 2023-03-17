from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from cart.models import Cart


def cartadd(request, product_id):
    cart = Cart(request)
    cart.add(product_id, 1)
    return redirect('store:all')


def cartremove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('store:all')
