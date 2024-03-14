
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Category
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


def main(request):
    # clients = Client.objects.all()
    recipes = Recipe.objects.order_by('?')[:5]  # Получаем 5 случайных рецептов
    context = {"title": "main page",'recipes': recipes}
    return render(request, "app_cookbook/main.html", context)

def recipes(request):
    # clients = Client.objects.all()
    recipes = Recipe.objects.all()
    context = {"title": "recipes",'recipes': recipes}
    return render(request, "app_cookbook/recipes.html", context)

def about(request):
    context = {"title": "about"}
    return render(request, "app_cookbook/about.html", context)


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {"title": "recipe_detail",'recipe':recipe}
    return render(request, 'app_cookbook/recipe_detail.html', context)

def logout_user(request):
    logout(request)
    return redirect('main')


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

@login_required
def user_recipes(request):
    user = request.user
    recipes = Recipe.objects.filter(author=user)

    return render(request, 'app_cookbook/user_recipes.html', {'recipes': recipes})

@login_required
def recipe_edit(request, id):
    recipe = Recipe.objects.get(id=id)
    if recipe.author != request.user:
        return redirect('main')
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('user_recipes')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'app_cookbook/recipe_edit.html', {'form': form})