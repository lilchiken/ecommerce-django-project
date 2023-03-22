from typing import List

from django.shortcuts import (
    redirect,
    render
)
from django.views.decorators.http import require_POST
from django.http import HttpRequest
from django.db.models import QuerySet

from cart.models import (
    Cart,
    ProductOrder,
    Order
)
from cart.forms import (
    ProductOrderForm,
    OrderForm
)
from store.models import (
    Product,
    Count,
    Color,
    Size
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
    forms = []
    for item in cart:
        forms.append(ProductOrderForm(initial={
            'product': item,
            'product_id': item.id,
            'size': item.grid_sizes,
            'color': item.grid_colors,
            'count': cart.cart[str(item.id)]['quantity']
        }))
    for form in forms:
        print(form.initial)
    # cart.clear()
    return render(
        request,
        'cart/ship.html', 
        {
            'cart': cart,
            'form': forms
        }
    )

@require_POST
def checkout_save(request: HttpRequest):
    request.POST._mutable = False
    if not request.POST.get('products'):
        request.POST._mutable = True
        request.POST.setlistdefault('products')
    for i, val in enumerate(request.POST.getlist('product_id')):
        product = Product.objects.get(id=int(val))
        size = Size.objects.get(title=request.POST.getlist('size')[i])
        color = Color.objects.get(title=request.POST.getlist('color')[i])
        prod_obj = ProductOrder.objects.create(
            product_id=product,
            product=request.POST.getlist('product')[i],
            size=size,
            color=color,
            count=int(request.POST.getlist('count')[i])
        )
        request.POST.appendlist('products', prod_obj.id)
        count_obj = Count.objects.filter(
            product=product,
            size=size,
            color=color
        )
        new_count = count_obj.first().count - int(request.POST.getlist('count')[i])
        # count_obj.update(count=new_count)
    request.POST._mutable = False
    form = OrderForm(
        data=request.POST,
    )
    # objects = request.POST.getlist('products').copy()
    print(request.POST.getlist('products'))
    if form.is_valid():
        print(form.cleaned_data)
        prods = ProductOrder.objects.filter(
            id__in=request.POST.getlist('products')
        )
        print(prods)
        Order.objects.create(
            products=prods,
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            adress=form.cleaned_data['phone'],
            customer_name=form.cleaned_data['customer_name']
        )
        return redirect('store:all')
    print(form.initial)
    return render(request ,'cart/checkout.html', {'form': form})
