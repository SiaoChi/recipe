from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('my-recipe/', views.UserRecipe, name ='my-recipe'),
]