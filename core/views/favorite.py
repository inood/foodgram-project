from django.core.paginator import Paginator
from django.shortcuts import render

from core.models import Recipe, Tag
from foodgram.settings import ITEM_COUNT


def favorite(request):
    tags_from_filter = request.GET.getlist('filters')

    if not tags_from_filter:
        tags_from_filter = Tag.objects.filter(is_basic=True).values_list(
            'value', flat=True)

    all_tags = Tag.objects.filter(is_basic=True)

    recipe_list = Recipe.objects.filter(
        favorite_recipes__user=request.user
    ).filter(
        tags__value__in=tags_from_filter
    ).distinct()

    paginator = Paginator(recipe_list, ITEM_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, "favorites.html",
                  {'paginator': paginator,
                   'page': page,
                   'all_tags': all_tags,
                   'tags_list': tags_from_filter, })
