from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from core.backends import get_ingredients
from core.forms import RecipeForm
from core.models import Ingredient, Recipe, Subscription

User = get_user_model()


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, files=request.FILES or None)
        ingredients = request.POST.getlist('nameIngredient_1')
        tags = request.POST.getlist('tag')
        if not ingredients:
            form.add_error(None, "Добавьте ингредиенты")
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

            form.save()
            return redirect('recipe_detail',
                            recipe_id=new_recipe.id)
        return render(request, 'recipe_create.html', {'form': form,
                                                      'tags': tags})
    form = RecipeForm()
    return render(request, 'recipe_create.html', {'form': form})


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
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
    return render(request, 'recipe_is_delete.html')


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author != request.user:
        return redirect("recipe_detail", recipe_id=recipe_id)

    recipe_tags = recipe.tags.values_list('value', flat=True)
    ingredients = recipe.ingredients.all()
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None, instance=recipe)
    if request.method == 'POST':
        # tags = request.POST.getlist('tag')
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
            form.save()
            return redirect("recipe_detail", recipe_id=recipe_id)
        return render(request, 'recipe_edit.html', {
                'form': form,
                'recipe': recipe,
                'ingredients': ingredients,
                'tags': recipe_tags,
            })

    return render(request, 'recipe_edit.html', {
        'form': form,
        'recipe': recipe,
        'ingredients': ingredients,
        'tags': recipe_tags,
    })
