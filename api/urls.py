from django.urls import path

from api import views

urlpatterns = [
    path('ingredients/', views.ingredients, name='index'),
    path('subscriptions/', views.SubscriptionAddAPIView.as_view()),
    path('subscriptions/<int:pk>/', views.SubscriptionDeleteAPIView.as_view()),
    path('favorites/', views.FavoriteAddAPIView.as_view()),
    path('favorites/<int:pk>', views.FavoriteDeleteAPIView.as_view()),
    path('purchases/', views.CartAddAPIView.as_view()),
    path('purchases/<int:pk>', views.CartDeleteAPIView.as_view()),
]
