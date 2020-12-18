from django import template

from core.models import Cart, Favorite, Subscription

register = template.Library()


@register.filter(name='is_favorite')
def is_favorite(request, recipe):
    return Favorite.objects.filter(
        user=request.user, recipe=recipe
     ).exists()


@register.filter(name='is_follower')
def is_follower(request, profile):
    return Subscription.objects.filter(
        user=request.user, author=profile
    ).exists()


@register.filter(name='is_in_purchases')
def is_in_purchases(request, recipe):
    return Cart.objects.filter(
        user=request.user, recipe=recipe
    ).exists()
