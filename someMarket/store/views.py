from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404

from store.models import Category
from store.models import Product


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
        # print(self.request.GET.get('Sort By'))
        return super().get_queryset()
    


class ProductView(DetailView):
    model = Product
    template_name = 'store/one_shot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_count_products = Product.objects.all()[:5]
        context['other_prods'] = max_count_products
        return context