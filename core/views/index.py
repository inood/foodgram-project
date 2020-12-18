from django.core.paginator import Paginator
from django.shortcuts import render

from core.models import Recipe, Tag
from foodgram.settings import ITEM_COUNT


def index(request):
    tags_from_filter = request.GET.getlist('filters')

    if not tags_from_filter:
        tags_from_filter = Tag.objects.filter(is_basic=True).values_list(
            'value', flat=True)

    recipe_list = Recipe.objects.filter(
        tags__value__in=tags_from_filter
    ).select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).distinct()

    all_tags = Tag.objects.filter(is_basic=True)

    paginator = Paginator(recipe_list, ITEM_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page,
               'paginator': paginator,
               'all_tags': all_tags,
               'tags_from_filter': tags_from_filter,
               'title': 'Рецепты'
               }
    return render(request, 'index.html', context)
