from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from core.models import Recipe
from foodgram.settings import ITEM_COUNT

User = get_user_model()


@login_required
def subscribe(request):
    subscribtions = User.objects.filter(
        following__user=request.user)
    recipe: dict = {}
    for sub in subscribtions:
        recipe[sub] = Recipe.objects.filter(
            author=sub
        )

    paginator = Paginator(subscribtions, ITEM_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'subscribe.html', {
        'paginator': paginator,
        'page': page,
        'recipe': recipe,
    }
                  )
