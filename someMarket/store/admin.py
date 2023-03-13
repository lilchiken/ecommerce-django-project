from django.contrib import admin

from store.models import Category, Product, Color, Count, Size


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
    )
    list_editable = ('title',)
    search_fields = ('title', 'slug')
    empty_value_display = '-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        # 'categorys',
        'price'
    )
    list_editable = (
        'name',
        'price',
        # 'categorys'
    )
    search_fields = (
        'name',
        'category'
    )
    empty_value_display = '-'

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
   list_display = ('title',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    list_display = (
        'count',
        'color',
        'size',
        'product'
    )
