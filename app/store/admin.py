from django.contrib import admin

from store.models import (
    Category,
    Product,
    Color,
    Count,
    Size,
    ImagesProduct
)


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


class ImageProductInline(admin.StackedInline):
    model = ImagesProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price'
    )
    list_editable = (
        'name',
        'price',
    )
    search_fields = (
        'name',
        'category'
    )
    empty_value_display = '-'
    inlines = (ImageProductInline,)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'color',
        'count',
    )
