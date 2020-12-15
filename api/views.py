from django.http import JsonResponse

from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from api.serializers import SubscribeSerializer, FavoriteSerializer, \
    CartSerializer
from core.models import BaseIngredient, Subscription, get_user_model, Recipe, \
    Favorite, Cart

User = get_user_model()


def ingredients(request):
    query_text = request.GET['query']
    ingredients_items = BaseIngredient.objects.filter(title__istartswith=query_text.lower())

    response_data = []

    for x in ingredients_items:
        block_item = {}
        block_item['title'] = x.title
        block_item['unit'] = x.unit
        response_data.append(block_item)

    return JsonResponse(response_data, safe=False)


class SubscriptionAddAPIView(CreateAPIView):
    serializer_class = SubscribeSerializer


class SubscriptionDeleteAPIView(DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        Subscription.objects.filter(
            user=self.request.user, author=self.get_object()
        ).delete()
        return Response(data={"success": True})


class FavoriteAddAPIView(CreateAPIView):
    serializer_class = FavoriteSerializer


class FavoriteDeleteAPIView(DestroyAPIView):
    serializer_class = FavoriteSerializer
    queryset = Recipe.objects.all()

    def destroy(self, request, *args, **kwargs):
        Favorite.objects.filter(
            user=self.request.user, recipe=self.get_object()
        ).delete()
        return Response(data={"success": True})


class CartAddAPIView(CreateAPIView):
    serializer_class = CartSerializer


class CartDeleteAPIView(DestroyAPIView):
    serializer_class = CartSerializer
    queryset = Recipe.objects.all()

    def destroy(self, request, *args, **kwargs):
        Cart.objects.filter(
            user=self.request.user, recipe=self.get_object()
        ).delete()
        return Response(data={"success": True})
