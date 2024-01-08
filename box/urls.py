from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_views, name='recipes'),
    path('<slug:recipe_slug>', views.recipe_list, name='recipe_list'),
    path('favourites/', views.favourites_list, name='favourites_list'),
    path('fav/<int:recipe_id>', views.favourites_add, name='favourite'),
    path('add/', views.add_recipe, name='add_recipe'),
]
