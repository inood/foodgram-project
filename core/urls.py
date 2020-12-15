from django.urls import path

from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:recipe_id>/delete', views.recipe_delete, name='recipe_delete'),
    path('recipe_create/', views.recipe_create, name='recipe_create'),
    path('<str:username>', views.profile, name="profile"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('favorite/', views.favorite, name='favorite'),
    path('cart/', views.cart, name='cart'),
]
