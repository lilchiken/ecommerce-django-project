from django.db import models

from store.models import (
    Category,
    Size,
    Color,
    Count
)


class ImagesProduct(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=True,
        null=True,
        default=None
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='other_images',
        blank=True,
        null=True
    )


class Product(models.Model):
    categorys = models.ManyToManyField(
        Category,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=128
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=256,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='Цена',
        decimal_places=2,
        max_digits=16
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        blank=True
    )
    main_image = models.ImageField(
        verbose_name='Основная фотография',
        upload_to='images/products/',
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Продукты'

    def __str__(self) -> str:
        return self.name

    @property
    def grid_sizes(self):
        return set(
            Size.objects.filter(
                grid__product_id=self.pk,
                grid__count__gt=0
            )
        )

    @property
    def grid_colors(self):
        return set(
            Color.objects.filter(
                grid__product_id=self.pk,
                grid__count__gt=0
            )
        )

    @property
    def count(self):
        return sum(
            Count.objects.filter(
                product_id=self.pk
            ).values_list(
                'count',
                flat=True
            )
        )
