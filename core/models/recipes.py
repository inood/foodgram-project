from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
from pytils.translit import slugify

from core.models.ingredients import Ingredient
from core.models.tags import Tag


class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='recipe_ingredient',
                                         verbose_name='Ингредиенты')
    tags = models.ManyToManyField(Tag, verbose_name='тэги')
    cooking_time = models.IntegerField(verbose_name='Время приготовления')
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='main_image/',
                              height_field=None,
                              width_field=None,
                              verbose_name='Главное изображение')
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата публикации')

    class Meta:
        ordering = ['-create_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width: 60px; height:60px;" /image_tag/>'
                % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def save(self, *args, **kwargs):
        # через pytils импортируется кирилический sluglify
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
