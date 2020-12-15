from django import forms

from core.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_time', 'tags', 'image')
        widgets = {
            'description': forms.Textarea({'rows': 6}),
            'tags': forms.CheckboxSelectMultiple()
            }
