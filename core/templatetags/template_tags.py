from json import loads

from django import template

from store.models import (
    Category,
    Product
)
from cart.models import Cart

register = template.Library()


@register.inclusion_tag(
    'template_tags/draw_categorys.html',
    name='draw_categorys'
)
def draw_categorys():
    return {
            'categorys': Category.objects.all()[:5]
        }


@register.inclusion_tag(
    'template_tags/count_item.html',
    name='count_item'
)
def count_item(request, product_id):
    cart = Cart(request)
    return {'count_item': cart.count_item(product_id)}


@register.inclusion_tag(
    'template_tags/draw_order.html',
    name='draw_order'
)
def draw_order(order):
    objs = loads(order.products)
    for prod in objs:
        prod['name'] = Product.objects.get(
            id=prod.get('product_id')
        ).name
    return {'order': objs}
