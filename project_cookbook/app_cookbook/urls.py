from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name='main'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('register/', views.register, name='register'),
    # path('register/', views.Register.as_view(), name='register'),
    # path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_edit_recipe/', views.add_edit_recipe, name='add_edit_recipe'),
    path('login/', auth_views.LoginView.as_view (template_name= 'app_cookbook/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]