from django.db import models


class Color(models.Model):
    title = models.CharField(
        'Название цвета',
        max_length=32
    )

    def __str__(self) -> str:
        return self.title


class Size(models.Model):
    title = models.CharField(
        'Название размера',
        max_length=32
    )

    def __str__(self) -> str:
        return self.title


class Count(models.Model):
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
