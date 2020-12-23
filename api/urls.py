from django.urls import path

from api import views

urlpatterns = [
    path('ingredients/', views.ingredients, name='index'),
    path('subscriptions/', views.SubscriptionView.as_view(),
         name='subscriptions_add'),
    path('subscriptions/<int:pk>/', views.SubscriptionView.as_view(),
         name='subscriptions_remove'),
    path('favorites/', views.FavoriteView.as_view(), name='favorite_add'),
    path('favorites/<int:pk>/', views.FavoriteView.as_view(),
         name='favorite_remove'),
    path('purchases/', views.PurchaseView.as_view(), name='purchase_add'),
    path('purchases/<int:pk>/', views.PurchaseView.as_view(),
         name='purchase_remove'),

]
