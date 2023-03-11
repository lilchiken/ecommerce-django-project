from django.shortcuts import render
from django.shortcuts import get_list_or_404

from store.models import Category
from store.models import Product

def index(request):
    categorys = Category.objects.filter(image__isnull=False).all().order_by('-pub_date')
    return render(
        request,
        'store/index.html',
        {
            'new_cg': categorys
        }
    )
