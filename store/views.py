from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.redis import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from store.models import (
    Category,
    Product
)
from store.forms import SortProds

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

SORTBY_QUERYSET = {
    'price-ascending': Product.objects.order_by('-price'),
    'price-descending': Product.objects.order_by('price'),
    'created-descending': Product.objects.order_by('pub_date'),
    'created-ascending': Product.objects.all()
}


class IndexView(ListView):
    model = Category
    template_name = 'store/index.html'

    def get_queryset(self):
        """Чтобы корректно отображалсь мейн страница,
        необходимо брать категории, у которых есть фотография.
        """

        return Category.objects.filter(image__isnull=False)[:3]

    # @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryView(ListView):
    model = Category
    template_name = 'store/products.html'

    def get_queryset(self):
        """Получаем кверисет продуктов по категории."""

        query = self.request.resolver_match.kwargs.get('slug')
        category = get_object_or_404(
            Category,
            slug=query
        )
        return Product.objects.filter(categorys=category)

    # @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SearchResultsView(ListView):
    model = Product
    template_name = 'store/products.html'

    def get_queryset(self):
        """Поиск по названию продукта."""

        query = self.request.GET.get('q')
        return Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            ).all()


class AllProductsView(ListView):
    model = Product
    template_name = 'store/products.html'

    def get_queryset(self):
        """Получаем настройки фильтрации."""

        sort = self.request.GET.get('sortby')
        if not sort:
            sort = 'created-descending'
        return SORTBY_QUERYSET.get(sort)

    def get_context_data(self, **kwargs):
        """Отдаём отсортированные продукты."""

        context = super().get_context_data(**kwargs)
        context['sortby'] = SortProds(self.request.GET)
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'store/one_shot.html'

    def get_context_data(self, **kwargs):
        """Здесь можно настроить какие продукты нужно подсовывать юзеру."""

        context = super().get_context_data(**kwargs)
        context['other_prods'] = Product.objects.all()[:5]
        return context

    # @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
