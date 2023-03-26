from ast import literal_eval

from django.shortcuts import (
    redirect,
    render,
)
from django.views.decorators.http import require_POST

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
    if len(cart) == 0:
        return redirect('store:index')
    forms = []
    for item in cart:
        forms.append(ProductOrderForm(initial={
            'product': item,
            'product_id': item.id,
            'size': item.grid_sizes,
            'color': item.grid_colors,
            'count': cart.cart[str(item.id)]['quantity']
        }))
    
    return render(
        request,
        'cart/ship.html',
        {
            'cart': cart,
            'form': forms
        }
    )


@require_POST
def checkout_save(request):
    """
    """
    request.POST._mutable = False
    if not request.POST.getlist('products'):
        request.POST._mutable = True
        request.POST.setlistdefault('products')
        request.POST.appendlist('products', {'ids': []})
        for i, val in enumerate(request.POST.getlist('product_id')):
            product = Product.objects.get(id=int(val))
            size = Size.objects.get(title=request.POST.getlist('size')[i])
            color = Color.objects.get(title=request.POST.getlist('color')[i])
            prod_obj = ProductOrder.objects.create(
                product_id=product,
                product=request.POST.getlist('product')[i],
                size=size.title,
                color=color.title,
                count=int(request.POST.getlist('count')[i])
            )
            request.POST.getlist('products')[0].get('ids').append(
                str(prod_obj.id)
            )
    form = OrderForm(
        data=request.POST,
    )
    if form.is_valid():
        ids = literal_eval(request.POST.getlist('products')[0])['ids']
        prods = ProductOrder.objects.filter(
            id__in=[int(id) for id in ids]
        )
        order = Order.objects.filter(
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            adress=form.cleaned_data['adress'],
            customer_name=form.cleaned_data['customer_name']
        ).last()
        if not order.products.filter(
            id__in=[int(id) for id in ids]
        ):
            order = Order.objects.create(
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                adress=form.cleaned_data['adress'],
                customer_name=form.cleaned_data['customer_name']
            )
            order.products.set(prods)
            cart = Cart(request)
            cart.clear()
            for prod in prods:
                count_obj = Count.objects.filter(
                    product=prod.product_id,
                    size__title=prod.size,
                    color__title=prod.color
                )
                new_count = count_obj.first().count - prod.count
                count_obj.update(count=new_count)
        return render(request, 'cart/thanks.html', {'order': order})
    return render(request, 'cart/checkout.html', {'form': form})
