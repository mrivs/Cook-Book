## Deploy Info
создание  и активация виртуального окружения

    python -m venv venv
    venv\Scripts\activate.ps1

установка django

    python.exe -m pip install --upgrade pip
    pip install django
    python -m pip install Pillow

создание проекта (myproject) и приложения (myapp) django

    django-admin startproject myproject
    python manage.py startapp myapp

в myprogect\settings.py INSTALLED_APPS добавляется  myapp (созданое приложение)

в файле \project\project\urls.py  в urlpatterns указывается путь для приложения myapp. 
Например: 

    path('', include('myapp.urls')),

в файле \project\project\settings.py добавим локальный хост

    ALLOWED_HOSTS = ["127.0.0.1"]

в myapp создается файл urls.py  где  описываются urlpatterns для  views. Например:

    from django.urls import path
    from .import views

    urlpatterns = [
    path('', views.main, name='main'),
    path('client_form/', views.client_form, name='client_form'),
    ]

в файле \project\myapp\views.py , создаются представления

в папке \project\myapp\management\commands\ создаются команды для консоли (также добавить__init__.py)

в файле \project\myapp\models.py создаются модели

создание миграций

    python manage.py makemigrations
    python manage.py migrate


 в settings.py и пропишем следующие пару констант для хранения изображений:
 
    ...
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'


в \project создаем папку  templates  где будет храниться базовый шаблон base.html
в файле \project\project\settings.py добавим 

    TEMPLATES = [
        {   
            'DIRS': [BASE_DIR / 'templates',],
            ...
        }
    ]

в \project\myapp создаем папки  templates\myapp 
(полный путь \myproject\myapp\templates\myapp) где будут храниться шаблоны .html приложения

в файле \project\myapp\forms.py создаются формы для html шаблонов


Создаем суперюзера

    python manage.py createsuperuser

https://pressanybutton.ru/post/poleznye-instrumenty/razvorachivanie-django-proekta-na-pythonanywhere/