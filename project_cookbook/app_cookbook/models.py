from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
'''
- ### Рецепты:
    - Название
    - Описание
    - Шаги приготовления
    - Время приготовления
    - Изображение
    - Автор
    - *другие поля на ваш выбор, например ингредиенты и т.п.

- ### *Категории рецептов
    - Название
    - *другие поля на ваш выбор

- ### *Связующая таблица для связи Рецептов и Категории
    - *обязательные для связи поля
    - *другие поля на ваш выбор
'''

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    
    def __str__(self):
        return str(self.name)
    
class Recipe(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    ingredients=models.TextField(max_length=2000, default='')
    steps=models.TextField(max_length=2000)
    cooking_time=models.TimeField()
    pecipe_image=models.ImageField(null=True, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    