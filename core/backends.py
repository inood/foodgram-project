from django.shortcuts import get_object_or_404

from core.models import BaseIngredient, Tag


def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            ing_num = key[15:]
            ing_object, create = BaseIngredient.objects.get_or_create(
                title=request.POST[key],
                unit=request.POST['unitsIngredient_'+ing_num])
            ingredients[ing_object] = request.POST[
                                                'valueIngredient_' + ing_num]
    return ingredients


def get_tags(request):
    data = request.POST.copy()
    tags = []
    for value in ['lunch', 'dinner', 'breakfast']:
        if value in data and data.get(value) == 'on':
            tag = get_object_or_404(Tag, value=value)
            tags.append(tag)
    return tags
