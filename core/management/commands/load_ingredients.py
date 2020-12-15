import json
from django.core.management.base import BaseCommand
from core.models.ingredients import BaseIngredient


def load():
    with open('ingredients.json', 'r',
              encoding='utf-8') as file:
        data = json.load(file)
    if data:
        for item in data:
            new_ingregient = BaseIngredient(title=item['title'],
                                            unit=item['dimension'])
            new_ingregient.save()


class Command(BaseCommand):
    help = 'Загрузка ингредиентов',

    def handle(self, *args, **options):
        load()
