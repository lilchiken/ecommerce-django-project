import pathlib

PROJECT_NAME = 'someMarket'
BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent

if not BASE_DIR.joinpath(PROJECT_NAME).is_dir:
    assert False, ('Проекта не найден!!!')

if not BASE_DIR.joinpath(PROJECT_NAME).joinpath('manage.py').is_file():
    assert False, ('manage.py не найден!!!')

from django.utils.version import get_version
from rest_framework import VERSION

assert get_version() > '4.0.0', (
    'Пожалуйста, используйте версию Django 4.0.0 или новее'
)
assert VERSION > '3.0.0', (
    'Пожалуйста, используйте версию DRF 3.0.0 или новее'
)

from someMarket.settings import INSTALLED_APPS

assert any(
    app in INSTALLED_APPS for app in [
        ('api' or 'api.apps.ApiConfig'),
        ('cart' or 'cart.apps.CartConfig'),
        ('core' or 'core.apps.CoreConfig'),
        ('store' or 'store.apps.StoreConfig')
    ]
), ('Пожалуйста зарегиструйте приложения')

pytest_plugins = [
    'tests.fixtures.fixture_data',
]
