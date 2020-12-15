import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Cart, Recipe


@login_required
def cart(request):
    if request.GET:
        recipe_id = request.GET.get('recipe_id')
        Cart.objects.get(
            recipe__id=recipe_id
        ).delete()

    purchases = Recipe.objects.filter(Cart__user=request.user)

    return render(request, "cart.html", {'purchases': purchases, })
