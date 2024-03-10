from django.contrib import admin
from .models import Recipe, Category

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "cooking_time", "category", "pecipe_image",'author']
    # list_filter = ["price", "date_added", "count"]
    
    
    search_fields = ['description','title','ingredients']
    search_help_text = 'Поиск по полю Описание рецепта'
    
    fieldsets = [
        (
            "Основная информация",
            {
                "classes": ["wide"],
                "fields": ["title",'category','author'],
            },
        ),
        (
            "Подробности",
            {
                "description": " Подробное описание рецепта",
                "fields": [ "description",'ingredients','steps','cooking_time'],
            },
        ),
    ]

    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    # readonly_fields = ['description']
    pass
# Register your models here.
