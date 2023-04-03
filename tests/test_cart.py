import pytest
from django.test import Client


class TestCartView:

    @pytest.mark.django_db(transaction=True)
    def test_cartadd_view(
        self,
        client: Client,
        category,
        product,
        count
    ):
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
    def test_checkout_view(
        self,
        client: Client,
        category,
        product,
        count
    ):
        url = '/cart/cart/'
        url_add_prod = f'cart/cartadd/{product.id}'
        main_client = client

        try:
            main_client.get('/')
        except Exception as e:
            assert False, e.__repr__()

        try:
            main_client.get(f'/{url_add_prod}')
        except Exception as e:
            assert False, e.__repr__()

        assert len(main_client.session.get('cart')) == 1

        try:
            response = main_client.post(
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

        assert response.status_code == 200

        assert len(response.client.session.get('order_objs')) == 1

        assert response.resolver_match.url_name == 'checkout'
