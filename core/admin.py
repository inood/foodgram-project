from django.contrib import admin

from core.models import (BaseIngredient, Cart, Favorite, Ingredient, Recipe,
                         Subscription, Tag)


@admin.register(BaseIngredient)
class BaseIngredientAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit']
    list_display_links = ['title']
    search_fields = ['title']


@admin.register(Ingredient)
class IngredientAdmin(BaseIngredientAdmin):
    list_display = ['item', 'count']
    list_display_links = ['item']
    list_filter = ['item']
    autocomplete_fields = ('item',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'title', 'author', 'create_date']
    list_display_links = ['title']
    list_filter = ['author']
    filter_horizontal = ('tags',)
    autocomplete_fields = ('ingredients',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'is_basic']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'author']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
