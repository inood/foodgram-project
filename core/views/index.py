from django.core.paginator import Paginator
from django.shortcuts import render

from core.models.recipes import Recipe


def index(request):
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, 6)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html', {'page': page, 'paginator': paginator}
    )
