from django.db import models


class Category(models.Model):
    title = models.CharField(
        verbose_name='Категория',
        unique=True,
        max_length=64
    )
    slug = models.SlugField(
        unique=True,
        max_length=64,
        auto_created=True
    )
    pub_date = models.DateField(
        verbose_name='Дата создания',
        blank=True,
        auto_now_add=True
    )
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/categorys/',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Категории'

    def __str__(self) -> str:
        return self.title
