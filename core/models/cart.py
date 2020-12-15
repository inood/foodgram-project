from django.contrib.auth import get_user_model
from django.db import models

from core.models import Recipe

User = get_user_model()


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
