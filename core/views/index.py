from django.core.paginator import Paginator
from django.shortcuts import render

from core.models.recipes import Recipe
from core.models.tags import Tag


def index(request):
    tags_list = request.GET.getlist('filters')

    if not tags_list:
        tags_list = ['breakfast', 'lunch', 'dinner']

    recipe_list = Recipe.objects.filter(
        tags__value__in=tags_list
    ).select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).distinct()

    all_tags = Tag.objects.all()

    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page,
               'paginator': paginator,
               'all_tags': all_tags,
               'tags_list': tags_list,
               'title': 'Рецепты'
               }
    return render(request, 'index.html', context)
