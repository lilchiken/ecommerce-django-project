from django.db import models


class TitleStrModel(models.Model):
    """Абстрактная модель для моделей Color, Size."""

    title = models.CharField(
        max_length=32
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
