from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import Subscription, Favorite, Recipe, Cart

User = get_user_model()


class SubscribeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Subscription
        fields = ['id']

    def validate(self, attrs):
        author_id = attrs.get('id')
        author = get_object_or_404(User, id=author_id)
        user = self.context.get('request').user

        if user == author:
            raise ValidationError(
                {'detail': 'Нельзя подписаться на себя'}
            )
        if Subscription.objects.filter(user=user, author=author).exists():
            raise ValidationError(
                {'detail': 'Вы уже подписаны на автора'}
            )

        attrs['user'] = user
        attrs['author'] = author
        return attrs


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Favorite
        fields = ['id']

    def validate(self, attrs):
        recipe_id = attrs.get('id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = self.context.get('request').user

        if Favorite.objects.filter(user=user, recipe=recipe).exists():
            raise ValidationError(
                {'detail': 'Рецепт уже в избраном'}
            )

        attrs['user'] = user
        attrs['recipe'] = recipe
        return attrs


class CartSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['id']

    def validate(self, attrs):
        recipe_id = attrs.get('id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = self.context.get('request').user

        if Cart.objects.filter(user=user, recipe=recipe).exists():
            raise ValidationError(
                {'detail': 'Рецепт уже в корзине'}
            )

        attrs['user'] = user
        attrs['recipe'] = recipe
        return attrs
