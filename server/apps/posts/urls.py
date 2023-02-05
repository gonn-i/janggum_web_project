from django.urls import path, include
from . import views


app_name = "posts"

urlpatterns = [
    path("", views.main, name="main"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path('accounts/', include('allauth.urls')),
    
    path('create/', views.create, name='create'),
    path('all_recipe/', views.all_recipe, name='all_recipe'),
]