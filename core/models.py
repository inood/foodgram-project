from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.safestring import mark_safe
from pytils.translit import slugify

from foodgram.settings import BASIC_TAG_COUNT

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Тэг')
    value = models.CharField(max_length=50, verbose_name='SLUG')
    view = models.CharField(max_length=50,
                            verbose_name='Стиль отображения тега')
    is_basic = models.BooleanField(verbose_name='Базовый тег')

    def save(self, *args, **kwargs):
        count_basic_tag = Tag.objects.filter(is_basic=True).count()
        if self.is_basic:
            if count_basic_tag < BASIC_TAG_COUNT:
                print(f'{count_basic_tag} < {BASIC_TAG_COUNT}')
                super().save(*args, **kwargs)
            else:
                raise ValidationError(
                    f'Базовых тегов не может быть больше {BASIC_TAG_COUNT}')
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


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


class Recipe(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование')
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredient',
        verbose_name='Ингредиенты')

    tags = models.ManyToManyField(Tag, verbose_name='тэги')
    cooking_time = models.IntegerField(verbose_name='Время приготовления')
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(
        upload_to='main_image/',
        height_field=None,
        width_field=None,
        verbose_name='Главное изображение')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор')
    create_date = models.DateTimeField(
        auto_now_add=True,
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


class Favorite(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorite_recipes',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.recipe.title} - {self.user}'


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Cart'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='Cart'

    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return self.recipe.title


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
    )

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'

    def clean(self):
        if self.author == self.user:
            raise ValidationError(
                'Пользователь не может подписываться сам на себя'
            )

    def __str__(self):
        return f'{self.user.username} подписался на {self.author.username}'

    def follower(self):
        return self.user.username

    def following(self):
        return self.author.username
