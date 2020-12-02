from django.urls import path

from api import views


urlpatterns = [
    path('ingredients/', views.ingredients, name='index'),
    ]

