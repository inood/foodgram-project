from django import forms

from core.models import Recipe
from foodgram.settings import ITEM_COUNT


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_time', 'tags', 'image')
        widgets = {
            'description': forms.Textarea({'rows': ITEM_COUNT}),
            'tags': forms.CheckboxSelectMultiple()
            }


