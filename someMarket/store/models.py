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
        verbose_name = 'Категории'

    def __str__(self) -> str:
        return self.title
    

class Product(models.Model):
    categorys = models.ManyToManyField(
        Category
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
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=True,
        null=True
    )
    count_stock = models.IntegerField(
        verbose_name='Количество в наличии',
        editable=True
    )

    def __str__(self) -> str:
        return self.name
    
    @property
    def is_active(self):
        return True if self.count_stock > 0 else False
