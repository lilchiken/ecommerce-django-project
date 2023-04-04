from django.db import models

from core.models import TitleStrModel


class Color(TitleStrModel):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Size(TitleStrModel):
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Count(models.Model):
    """Модель определённого вида продукта."""

    count = models.IntegerField(
        verbose_name='Количество продукта',
        editable=True
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='grid'
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name='grid'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='grid'
    )
