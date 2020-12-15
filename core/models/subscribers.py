from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


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
