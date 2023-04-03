import pytest
from django.test import Client

from cart.models import Order


class TestCartView:

    @pytest.mark.django_db(transaction=True)
    def test_cart_create(
        self,
        client: Client
    ):
        """Проверка создания кастомной сессии."""

        url = '/'

        try:
            response = client.get(url)
        except Exception as e:
            assert False, e.__repr__()

        assert isinstance(response.client.session.get('cart'), dict), (
            'Проверьте, что в сессии юзера создаётся корзина'
        )

        assert isinstance(response.client.session.get('order_objs'), list), (
            'Проверьте, что в сессии юзера создаётся order_objs'
        )


    @pytest.mark.django_db(transaction=True)
    def test_cartadd_view(
        self,
        client: Client,
        category,
        product,
        count
    ):
        """Проверка view "cart:add" ."""

        url = f'cart/cartadd/{product.id}'

        try:
            response = client.get(f'/{url}')
        except Exception as e:
            assert False, e.__repr__()

        assert response.status_code == 302, (
            'Проверьте, что при добавлении в корзину юзер перенапрявляется'
            ' на страницу со всеми продуктами'
        )

        try:
            cart = client.session.get('cart')
        except Exception as e:
            assert False, e.__repr__()

        assert cart.get(str(product.id)) != None, (
            'Проверьте, что корректно работает добавление в корзину'
        )


    @pytest.mark.django_db(transaction=True)
    def test_cartremove_view(
        self,
        client: Client,
        category,
        product,
        count
    ):
        """Проверка view "cart:remove" ."""

        url = f'cart/cartremove/{product.id}'

        try:
            client.get('/')
        except Exception as e:
            assert False, e.__repr__()

        try:
            cart = client.session.get('cart')
        except Exception as e:
            assert False, e.__repr__()

        cart[str(product.id)] = 'some data'

        try:
            response = client.get(f'/{url}')
        except Exception as e:
            assert False, e.__repr__()

        assert response.status_code == 302, (
            'Проверьте, что при удалении из корзины юзер перенапрявляется'
            ' на страницу со всеми продуктами'
        )

        new_cart = client.session.get('cart')

        assert new_cart.get(str(product.id)) == None, (
            'Проверьте, что корректно работает удаление из корзины'
        )


    @pytest.mark.django_db(transaction=True)
    def test_all_checkout_view(
        self,
        client: Client,
        category,
        product,
        count
    ):
        """Здесь проверяем полную цепочку оформления заказа."""

        url = '/cart/cart/'
        url_checkout = '/cart/checkout/'
        url_add_prod = f'/cart/cartadd/{product.id}'

        try:
            client.get('/')
        except Exception as e:
            assert False, e.__repr__()

        try:
            client.get(url_add_prod)
        except Exception as e:
            assert False, e.__repr__()

        try:
            response = client.post(
                url,
                data={
                    'product_id': count.product.id,
                    'size': 'test_size',
                    'color': 'test_color',
                    'count': 1
                },
                follow=True,
            )
        except Exception as e:
            assert False, e.__repr__()

        assert response.status_code in (200, 301, 302), (
            'Проверьте, что ответ от "/cart/cart/" соответствующий'
        )

        assert len(response.client.session.get('order_objs')) == 1, (
            'Проверьте, что объект сессии из cart перемещается в order_objs'
        )

        assert response.resolver_match.url_name == 'checkout', (
            'Проверьте, что при положительном ответе идёт редирект на '
            '"/cart/checkout/"'
        )

        try:
            response = client.post(
                url_checkout,
                data={
                    'phone': '+71234567890',
                    'adress': 'some adress',
                    'customer_name': 'Фамилия Имя Отчество'
                }
            )
        except Exception as e:
            assert False, e.__repr__()

        last_order = Order.objects.last()

        assert last_order.adress == 'some adress', (
            'Проверьте, что view "/cart/checkout/" добавляет объект в Order'
        )
