from json import dumps

from django.shortcuts import (
    redirect,
    render,
)

from cart.models import Cart
from cart.forms import (
    ProductOrderForm,
    OrderForm
)
from store.models import (
    Product,
    Count,
)


def cartadd(request, product_id):
    if Product.objects.get(id=product_id).count == 0:
        return redirect('store:all')
    cart = Cart(request)
    cart.add(product_id, 1)
    return redirect('store:all')


def cartremove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('store:all')


def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('store:all')
    elif len(cart.order_objs) != 0 and len(cart) == 0:
        return redirect('cart:checkout')
    try:
        id, obj_cart = next(iter(cart.cart.items()))
        product = Product.objects.get(id=id)
    except StopIteration:
        return redirect('cart:checkout')
    form = ProductOrderForm(initial={
        'product_id': id,
        'size': product.grid_sizes,
        'color': product.grid_colors,
        'count': obj_cart['quantity']
    }, data=request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        cart.add_order_objs(data)
        cart.remove(id)
        return redirect('cart:checkout')
    return render(
        request,
        'cart/ship.html',
        {
            'cart': cart,
            'form': form
        }
    )


def checkout_save(request):
    """
    """
    cart = Cart(request)
    if len(cart.order_objs) == 0:
        return redirect('store:all')
    form = OrderForm(data=request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.products = dumps(cart.order_objs)
        order.save()
        for prod in cart.order_objs:
            count_obj = Count.objects.filter(
                product=prod.get('product_id'),
                size__title=prod.get('size'),
                color__title=prod.get('color')
            )
            new_count = count_obj.first().count - prod.get('count')
            count_obj.update(count=new_count)
        cart.clear_order_objs()
        return render(request, 'cart/thanks.html', {'order': order})
    return render(request, 'cart/checkout.html', {'form': form})
