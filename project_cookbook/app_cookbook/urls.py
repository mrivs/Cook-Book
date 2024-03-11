from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view (template_name= 'app_cookbook/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('add_edit_recipe/', views.add_edit_recipe, name='add_edit_recipe'),
    path('recipe_add/', views.recipe_add, name='recipe_add'),
    
    
]