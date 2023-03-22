from django.urls import path

from cart import views

app_name = 'cart'


urlpatterns = [
    path('cartadd/<int:product_id>', views.cartadd, name='cart-add'),
    path('cartremove/<int:product_id>', views.cartremove, name='cart-remove'),
    path('cart/', views.checkout, name='checkout-product'),
    path('checkout/', views.checkout_save, name='checkout'),
]
