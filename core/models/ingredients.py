from django.db import models
from django.utils.text import slugify


class BaseIngredient(models.Model):
    title = models.CharField(max_length=255,
                             unique=True,
                             db_index=True,
                             verbose_name='Наименование')
    unit = models.CharField(max_length=20, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Каталог ингредиентов'
        verbose_name_plural = 'Каталог ингредиентов'

    def __str__(self):
        return f'{self.title} {self.unit}'


class Ingredient(models.Model):
    item = models.ForeignKey(BaseIngredient,
                             verbose_name='Ингредиент',
                             on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.item} - {self.count}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
