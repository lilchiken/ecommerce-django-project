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
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=False,
        null=False,
    )
    image_0 = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=True,
        null=True,
        default=None
    )
    image_1 = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=True,
        null=True,
        default=None
    )
    image_2 = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=True,
        null=True,
        default=None
    )
    image_3 = models.ImageField(
        verbose_name='Фотография',
        upload_to='images/products/',
        blank=True,
        null=True,
        default=None
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
    
    @property
    def images(self):
        list_images = [
            self.image,
            self.image_0,
            self.image_1,
            self.image_2,
            self.image_3
        ]
        for image in list_images:
            if not image:
                list_images.remove(image)
        return list_images
    
    @property
    def images_more_than_one(self):
        return True if self.image_0 else False
    
    @property
    def grid_sizes(self):
        counts = Count.objects.filter(product=self.pk).values_list('id')
        return Size.objects.filter(grid__in=counts)
        list_size = set()
        for x in self.grid:
            list_size.add(x.size)
        return list_size
    
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Продукты'
