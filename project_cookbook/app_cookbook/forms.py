from django import forms
from django.contrib.auth.models import User
from .models import Category, Recipe

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class RecipeForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    steps=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'cooking_time', 'pecipe_image', 'category']
        labels = {
            'title': 'Название рецепта',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps': 'Инструкции по приготовлению',
            'cooking_time': 'Время приготовления',
            'pecipe_image': 'Изображение',
            'category': 'Категория'
        }


