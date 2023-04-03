import pytest
from django.test import Client

from store.views import SORTBY_QUERYSET


class TestSearchView:

    @pytest.mark.django_db(transaction=True)
    def test_search_view(
        self,
        client: Client,
        category,
        another_category,
        product,
        another_product,
    ):
        """Проверка view "store:search" ."""

        urls = [
            {
                'url': 'search?q=prdct',
                'prods': (product, another_product)
            },
            {
                'url': 'search?q=nthr',
                'prods': (another_product,)
            }
        ]

        for url in urls:

            try:
                response = client.get(f'/{url.get("url")}')
            except Exception as e:
                assert False, e.__repr__()

            assert response.status_code == 200, (
                'Статус по view "search" не тот, что ожидался, '
                f'{response.status_code}'
            )

            objects_search = response.context.get('object_list')

            assert any(
                prods in objects_search for prods in url.get('prods')
            ), (
                'View "search" выдаёт неожиданные продукты'
            )


class TestAllProductsView:

    @pytest.mark.django_db(transaction=True)
    def test_allproducts_view(
        self,
        client: Client,
        category,
        another_category,
        product,
        another_product,
    ):
        """Проверка view "store:all" ."""

        url = 'all/'

        try:
            response = client.get(f'/{url}')
        except Exception as e:
            assert False, e.__repr__()

        assert response.status_code == 200, (
            'Статус по view "all" не тот, что ожидался, '
            f'{response.status_code}'
        )

        objects_all = response.context.get('object_list')

        assert any(
            prod in objects_all for prod in (product, another_product)
        ), (
            'Не все продукты отображаются в view "all"'
        )


    @pytest.mark.django_db(transaction=True)
    def test_allproducts_view_with_data(
        self,
        client: Client,
        category,
        another_category,
        product,
        another_product,
    ):
        """Проверка view "store:all" с SORTBY_QUERYSET."""

        url = 'all/'

        for key, data in SORTBY_QUERYSET.items():

            try:
                response = client.get(
                    f'/{url}',
                    {'sortby': key}
                )
            except Exception as e:
                assert False, e.__repr__()

            assert response.status_code == 200, (
                'Статус по view "all" с сортировкой не тот, что ожидался, '
                f'{response.status_code}'
            )

            objects_sorted = response.context.get('object_list')

            assert objects_sorted == data
    

class TestProductView:

    @pytest.mark.django_db(transaction=True)
    def test_product_view(
        self,
        client: Client,
        category,
        product,
        count
    ):
        url = f'product/{product.id}'

        try:
            response = client.get(f'/{url}')
        except Exception as e:
            assert False, e.__repr__()

        assert response.status_code == 200, (
            'Статус по view "product" не тот, что ожидался, '
            f'{response.status_code}'
        )

        object = response.context.get('object')

        assert object == product, (
            'Ожидаемый объект view "Product" не является им'
        )

        assert object == count.product, (
            'Связанный объект Count в view "Product" не является им'
        )
        
        assert object.count >= count.count, (
            'Параметр count связанного объекта Count в view "Product"',
            ' меньше, чем предполагается'
        )

        assert count.size in object.grid_sizes, (
            'Размерная сетка не включает связанный объект Count '
            'в view "Product"'
        )

        assert count.color in object.grid_colors, (
            'Сетка цветов не включает связанный объект Count '
            'в view "Product"'
        )
