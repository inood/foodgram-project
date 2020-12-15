from django.core.paginator import Paginator
from django.shortcuts import render

from core.models import Tag, Recipe


def favorite(request):
    tags_list = request.GET.getlist('filters')

    if not tags_list:
        tags_list = ['breakfast', 'lunch', 'dinner']

    all_tags = Tag.objects.all()

    recipe_list = Recipe.objects.filter(
        favorite_recipes__user=request.user
    ).filter(
        tags__value__in=tags_list
    ).distinct()

    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, "favorites.html", {
        'paginator': paginator,
        'page': page,
        'all_tags': all_tags,
        'tags_list': tags_list,
    }
                  )
