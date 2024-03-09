
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Category


def main(request):
    # clients = Client.objects.all()
    context = {"title": "main page"}
    recipes = Recipe.objects.all()[:5]
    return render(request, "app_cookbook/main.html", context)

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {"title": "recipe_detail"}
    return render(request, 'app_cookbook/recipe_detail.html', context)

def logout_user(request):
    logout(request)
    return redirect('main')

def add_edit_recipe(request):
    # Логика добавления/редактирования рецепта
    return render(request, 'app_cookbook/add_edit_recipe.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    context={'user_form': form}
    return render(request, 'app_cookbook/register.html',context)    

