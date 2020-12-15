from django import template

from core.models import Favorite, Cart
from core.models.subscribers import Subscription

register = template.Library()


@register.filter(name='is_favorite')
def is_favorite(request, recipe):
    if Favorite.objects.filter(
        user=request.user, recipe=recipe
    ).exists():
        return True
    return False


@register.filter(name='is_follower')
def is_follower(request, profile):
    if Subscription.objects.filter(
        user=request.user, author=profile
    ).exists():
        return True
    return False


@register.filter(name='is_in_purchases')
def is_in_purchases(request, recipe):
    if Cart.objects.filter(
        user=request.user, recipe=recipe
    ).exists():
        return True
    return False
