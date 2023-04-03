import tempfile

import pytest
from mixer.backend.django import mixer as _mixer
from django.db import models

from store.models import (
    Category,
    Product,
    Size,
    Color,
    Count
)


@pytest.fixture()
def mock_media(settings):
    with tempfile.TemporaryDirectory() as temp_dir:
        settings.MEDIA_ROOT = temp_dir
        yield temp_dir


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def category():
    image = tempfile.NamedTemporaryFile(suffix='.jpg').name
    return Category.objects.create(
        title='test_ctgr',
        slug='test',
        image=image
    )


@pytest.fixture
def another_category():
    image = tempfile.NamedTemporaryFile(suffix='.jpg').name
    return Category.objects.create(
        title='test_nthr_ctgr',
        slug='test-nthr',
        image=image
    )


@pytest.fixture
def size():
    return Size.objects.create(title='test_size')


@pytest.fixture
def color():
    return Color.objects.create(title='test_color')


@pytest.fixture
def product():
    image = tempfile.NamedTemporaryFile(suffix='.jpg').name
    prod = Product.objects.create(
        name='test prdct',
        price=100.01,
        main_image=image
    )
    category = Category.objects.get(title='test_ctgr')
    prod.categorys.add(category)
    return prod


@pytest.fixture
def count():
    color = Color.objects.create(title='test_color')
    size = Size.objects.create(title='test_size')
    prod = Product.objects.get(
        name='test prdct',
        price=100.01,
    )
    return Count.objects.create(
        count=10,
        color=color,
        size=size,
        product=prod
    )


@pytest.fixture
def another_product():
    image = tempfile.NamedTemporaryFile(suffix='.jpg').name
    prod = Product.objects.create(
        name='test nthr prdct',
        price=1.01,
        main_image=image
    )
    category = Category.objects.get(title='test_nthr_ctgr')
    prod.categorys.add(category)
    return prod

@pytest.fixture
def another_count():
    return Count.objects.create(
        count=15,
        color=color,
        size=size,
        product=another_product
    )
