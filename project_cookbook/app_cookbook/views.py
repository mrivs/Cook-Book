
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Category


def main(request):
    # clients = Client.objects.all()
    context = {"title": "main page"}
    recipes = Recipe.objects.all()[:5]
    return render(request, "app_cookbook/main.html", context)

# def register(request):
#     # clients = Client.objects.all()
#     context = {"title": "register"}
#     return render(request, "app_cookbook/register.html", context)

def login(request):
    # clients = Client.objects.all()
    context = {"title": "login"}

    return render(request, "app_cookbook/login.html", context)

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {"title": "recipe_detail"}
    return render(request, 'app_cookbook/recipe_detail.html', context)

def logout(request):
    # Логика выхода пользователя
    return render(request, 'app_cookbook/logout.html')

def add_edit_recipe(request):
    # Логика добавления/редактирования рецепта
    return render(request, 'add_edit_recipe.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    context={'user_form': form}
    return render(request, 'app_cookbook/register.html',context)    