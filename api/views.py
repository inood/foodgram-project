from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import (BaseIngredient, Cart, Favorite, Recipe, Subscription,
                         get_user_model)

User = get_user_model()


def ingredients(request):
    query_text = request.GET['query']
    ingredients_items = BaseIngredient.objects.filter(
        title__istartswith=query_text.lower())

    response_data = []

    for x in ingredients_items:
        block_item = {}
        block_item['title'] = x.title
        block_item['unit'] = x.unit
        response_data.append(block_item)

    return JsonResponse(response_data, safe=False)


class SubscriptionView(APIView):
    def post(self, request):
        following = get_object_or_404(User, id=request.data.get('id'))
        obj, created = Subscription.objects.get_or_create(user=request.user,
                                                       author=following)
        if created:
            return Response({'status': '201'})
        return Response({"status": '302'})

    def delete(self, request, pk):
        following = get_object_or_404(User, id=pk)
        subscribe = get_object_or_404(Subscription, user=request.user,
                                          author=following)
        subscribe.delete()
        return Response({"status": '204'})


class FavoriteView(APIView):
    def post(self, request):
        recipe = get_object_or_404(Recipe, id=request.data.get('id'))
        obj, created = Favorite.objects.get_or_create(user=request.user,
                                                      recipe=recipe)
        if created:
            return Response({'status': '201'})
        return Response({"status": '302'})

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        favorite = get_object_or_404(Favorite, user=request.user,
                                         recipe=recipe)
        favorite.delete()
        return Response({"status": '204'})


class PurchaseView(APIView):
    def post(self, request):
        recipe = get_object_or_404(Recipe, id=request.data.get('id'))
        obj, created = Cart.objects.get_or_create(user=request.user,
                                                      recipe=recipe)
        if created:
            return Response({'status': '201'})
        return Response({"status": '302'})

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        purchase = get_object_or_404(Cart, user=request.user,
                                         recipe=recipe)
        purchase.delete()
        return Response({"status": '204'})
