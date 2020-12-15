from django.db import models

from core.models import Recipe, get_user_model

User = get_user_model()


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
