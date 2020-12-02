from django import forms

from core.models import Recipe


class RecipeForm(forms.Form):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_time', 'tags', 'image')
        labels = {'title': 'Комментарий'}
        widgets = {
            'description': forms.Textarea({'rows': 6}),
            'tags': forms.CheckboxSelectMultiple()
            }
