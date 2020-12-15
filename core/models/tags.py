from django.db import models


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Тэг')
    value = models.CharField(max_length=50)
    view = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
