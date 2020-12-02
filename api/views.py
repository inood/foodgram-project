from django.http import JsonResponse
from django.shortcuts import render
from core.models import BaseIngredient


def ingredients(request):
    query_text = request.GET['query']
    ingredients_items = BaseIngredient.objects.filter(title__istartswith=query_text.lower())

    response_data = []

    for x in ingredients_items:
        block_item = {}
        block_item['title'] = x.title
        block_item['unit'] = x.unit
        response_data.append(block_item)

    return JsonResponse(response_data, safe=False)

