from django.shortcuts import (
    redirect,
    render
)
from django.views.decorators.http import require_POST

from cart.models import Cart
from cart.forms import ProductOrderForm
from store.models import Product


def cartadd(request, product_id):
    cart = Cart(request)
    cart.add(product_id, 1)
    return redirect('store:all')


def cartremove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('store:all')


def checkout(request):
    cart = Cart(request)
    forms = []
    for item in cart:
        forms.append(ProductOrderForm(initial={
            'product': item,
            'product_id': item.id,
            'size': item.grid_sizes,
            'color': item.grid_colors,
        }))
    for form in forms:
        print(form.initial)
    return render(
        request,
        'cart/ship.html', 
        {
            'cart': cart,
            'form': forms
        }
    )
