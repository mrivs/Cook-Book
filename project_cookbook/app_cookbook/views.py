
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Category
from .forms import RecipeForm


def main(request):
    # clients = Client.objects.all()
    recipes = Recipe.objects.order_by('?')[:5]  # Получаем 5 случайных рецептов
    context = {"title": "main page",'recipes': recipes}
    recipes = Recipe.objects.all()[:5]
    return render(request, "app_cookbook/main.html", context)

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {"title": "recipe_detail",'recipe':recipe}
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

def recipe_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                return redirect('main')
        else:
            form = RecipeForm()
        return render(request, 'app_cookbook/recipe_add.html', {'form': form})
    else:
        return redirect('login')

