from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Cart, Recipe, Ingredient


@login_required
def cart(request):
    if request.GET:
        recipe_id = request.GET.get('recipe_id')
        Cart.objects.get(
            recipe__id=recipe_id
        ).delete()

    purchases = Recipe.objects.filter(Cart__user=request.user)

    return render(request, "cart.html", {'purchases': purchases, })


@login_required
def cart_list_download(request):
    recipe_cart_list = Recipe.objects.filter(
        Cart__user=request.user).all()
    ingredients_list = Ingredient.objects.filter(
        recipe_ingredient__in=recipe_cart_list)
    summary = {}

    for elem in ingredients_list:
        if (elem.item.title, elem.item.unit) not in summary:
            summary[elem.item.title,
                    elem.item.unit] = elem.count
        else:
            summary[elem.item.title,
                    elem.item.unit] += elem.count
    content = "Список покупок:\n"
    for title, number in summary.items():
        content += (f'- {title[0]} —— {number} {title[1]}\n')
    filename = "to_shoping.txt"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(
        filename)
    return response
