from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from core.models.recipes import Recipe
from core.forms import RecipeForm


@login_required
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

    form = RecipeForm()
    return render(request,
                  "recipe_form.html",
                  {'form': form, }
                  )


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    form = RecipeForm()

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'recipe_form.html', context)
