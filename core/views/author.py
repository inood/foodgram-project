from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from core.models import Recipe, Tag
from foodgram.settings import ITEM_COUNT
from users.forms import User


def profile(request, username):
    follow_button = False

    tags_from_filter = request.GET.getlist('filters')

    if not tags_from_filter:
        tags_from_filter = Tag.objects.filter(is_basic=True).values_list(
            'value', flat=True)

    all_tags = Tag.objects.filter(is_basic=True)

    profile_user = get_object_or_404(User, username=username)

    recipes_profile = Recipe.objects.filter(
        author=profile_user
    ).filter(
        tags__value__in=tags_from_filter
    ).select_related(
        'author'
    ).distinct()

    if request.user.is_authenticated and request.user != profile:
        follow_button = True

    paginator = Paginator(recipes_profile, ITEM_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {'paginator': paginator,
               'page': page,
               'profile': profile_user,
               'follow_button': follow_button,
               'all_tags': all_tags,
               'title': username,
               }
    return render(request, 'profile.html', context)
