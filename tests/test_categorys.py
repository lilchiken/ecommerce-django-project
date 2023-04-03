import pytest
from django.test import Client


class TestMainView:

    @pytest.mark.django_db(transaction=True)
    def test_main_view(
        self,
        client: Client,
        category,
        another_category
    ):
        url = ''
        try:
            response = client.get(f'{url}/')
        except Exception as e:
            assert False, e.__repr__()

        assert response.status_code == 200, (
            f'Статус от мэйн страницы не тот, {response.status_code}'
        )

        objects_main = response.context.get('object_list')

        assert len(objects_main) != 0, (
            'Проверьте, что категории передаются на мэйн страницу'
        )

        for obj in objects_main:
            assert getattr(obj, 'image'), (
                'Убедитесь, что на мэйн страницу передаются категории только '
                'с картинкой!'
            )


class TestCategoryView:

    @pytest.mark.django_db(transaction=True)
    def test_category_view(
        self,
        client: Client,
        category,
        another_category,
        product,
        another_product
    ):
        urls = [
            {
                'url': f'category/{category.slug}',
                'prod': product
            },
            {
                'url': f'category/{another_category.slug}',
                'prod': another_product
            }
        ]

        for url in urls:

            try:
                response = client.get(f'/{url.get("url")}/')
            except Exception as e:
                assert False, e.__repr__()

            assert response.status_code == 200, (
                f'Статус "category/<slug:slug>" не тот, {response.status_code}'
            )

            objects_category = response.context.get('object_list')

            assert url.get('prod') in objects_category, (
                f'Не найден продукт на странице категории'
            )

            assert len(objects_category) == 1, (
                f'Проверьте, что отображаются продукты нужной категории'
            )
