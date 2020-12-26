from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from core.backends import get_ingredients, get_tags
from core.forms import RecipeForm
from core.models import Ingredient, Recipe, Subscription, Tag, BaseIngredient

User = get_user_model()


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(
            request.POST or None,
            files=request.FILES or None
        )

        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()

            ingredients = get_ingredients(request)

            for ingredient, quantity in ingredients.items():
                ing, created = Ingredient.objects.get_or_create(
                    item=ingredient,
                    count=quantity)

                new_recipe.ingredients.add(ing)

            form.save_m2m()
            return redirect(
                'profile',
                username=request.user.username
            )

    form = RecipeForm()
    return render(request, 'recipe_create.html', {
        'form': form,
    })


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if not request.user.is_authenticated:
        return render(
            request,
            'recipe_detail.html',
            {'recipe': recipe}
        )

    recipe_owner = False

    if request.user == recipe.author:
        recipe_owner = True
    context = {
        'recipe': recipe,
        'recipe_owner': recipe_owner,
        'is_subscribed':  Subscription.objects.filter(
                author=recipe.author, user=request.user)
    }

    return render(request, 'recipe_detail.html', context)


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = get_object_or_404(User, id=recipe.author_id)

    if request.user != author:
        return redirect(
            'index',
        )

    recipe.delete()
    return render(request, 'recipe_is_delete.html')


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = get_object_or_404(User, id=recipe.author_id)
    all_tags = Tag.objects.all()
    recipe_tags = recipe.tags.values_list('value', flat=True)

    if request.user != author:
        return redirect(
            'recipe_detail',
            recipe_id=recipe_id
        )

    if request.method == 'POST':
        ingredients = get_ingredients(request)
        form = RecipeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )

        if form.is_valid():

            edit_recipe = form.save(commit=False)
            edit_recipe.author = request.user
            edit_recipe.save()
            edit_recipe.tags.clear()
            edit_recipe.ingredients.clear()
            for ingredient, quantity in ingredients.items():
                ing, created = Ingredient.objects.get_or_create(
                    item=ingredient,
                    count=quantity)
                edit_recipe.ingredients.add(ing)
            form.save()
            return redirect(
                'profile',
                username=request.user.username
            )
        else:
            print(form.errors)

    form = RecipeForm(instance=recipe)
    return render(request, 'recipe_edit.html', {
        'form': form,
        'recipe': recipe,
        'all_tags': all_tags,
        'recipe_tags': recipe_tags,
    })
