from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404

from store.models import (
    Category,
    Product
)
from store.forms import SortProds


SORTBY_QUERYSET = {
    'price-ascending': Product.objects.order_by('-price'),
    'price-descending': Product.objects.order_by('price'),
    'created-descending': Product.objects.all(),
    'created-ascending': Product.objects.order_by('pub_date'),
}


class IndexView(ListView):
    model = Category
    template_name = 'store/index.html'

    def get_queryset(self):
        return Category.objects.filter(image__isnull=False)[:3]


class CategoryView(ListView):
    model = Category
    template_name = 'store/products.html'

    def get_queryset(self):
        query = self.request.resolver_match.kwargs.get('slug')
        category = get_object_or_404(
            Category,
            slug=query
        )
        return Product.objects.filter(categorys=category)


class SearchResultsView(ListView):
    model = Product
    template_name = 'store/products.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            ).all()


class AllProductsView(ListView):
    model = Product
    template_name = 'store/products.html'

    def get_queryset(self):
        sort = self.request.GET.get('sortby')
        if not sort:
            sort = 'created-descending'
        return SORTBY_QUERYSET.get(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sortby'] = SortProds(self.request.GET)
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'store/one_shot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_count_products = Product.objects.all()[:5]
        context['other_prods'] = max_count_products
        return context
