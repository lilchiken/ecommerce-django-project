from django.urls import path

import store.views as views

app_name = 'store'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('all/', views.AllProductsView.as_view(), name='all'),
    path('product/<int:pk>', views.ProductView.as_view(), name='one-shot')
]