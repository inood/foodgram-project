from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from core.models import Tag, Recipe
from users.forms import User


def profile(request, username):
    follow_button = False

    tags_list = request.GET.getlist('filters')

    if not tags_list:
        tags_list = ['breakfast', 'lunch', 'dinner']

    all_tags = Tag.objects.all()

    profile_user = get_object_or_404(User, username=username)

    recipes_profile = Recipe.objects.filter(
        author=profile_user
    ).filter(
        tags__value__in=tags_list
    ).select_related(
        'author'
    ).distinct()

    if request.user.is_authenticated and request.user != profile:
        follow_button = True

    paginator = Paginator(recipes_profile, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {'paginator': paginator,
               'page': page,
               'profile': profile_user,
               'follow_button': follow_button,
               'all_tags': all_tags,
               'tags_list': tags_list,
               'title': username,
               }
    return render(request, 'profile.html', context)
