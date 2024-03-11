from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name='main'),
    path('recipes/', views.recipes, name='recipes'),
    path('about/', views.about, name='about'),
    
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view (template_name= 'app_cookbook/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe_edit/<int:id>/', views.recipe_edit, name='recipe_edit'),
    path('recipe_add/', views.recipe_add, name='recipe_add'),
    path('user_recipes/', views.user_recipes, name='user_recipes'),
    
    
]