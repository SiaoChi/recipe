from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.Recipes, name ='home'),
    path('recipes/<str:pk>', views.singleRecipe, name='single-recipe'),
    path('create-recipe/', views.CreateRecipe, name = 'create-recipe'),
    path('update-recipe/<str:pk>', views.UpdateRecipe, name='update-recipe'),
    path('delete-recipe/<str:pk>', views.DeleteRecipe, name='delete-recipe'),
    path('my-recipe/', views.UserRecipe, name ='my-recipe'),



    # path('htmx/create-sauce/', views.createSauce, name='create-sauce'),
    # path('htmx/create-material/', views.createMaterial, name='create-material'),
]