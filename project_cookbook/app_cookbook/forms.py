from django import forms
from django.contrib.auth.models import User
from .models import Category, Recipe

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductRecipe(forms.ModelForm):
    class Meta:
        model = Recipe


