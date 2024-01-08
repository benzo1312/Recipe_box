from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ingredients, Recipes


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    """Registration of the Recipes model in the admin panel"""
    list_display = ("title",)
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.photo.url} wight="100" height="110"')

    get_image.short_description = "Photo"


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    """Registering the Ingredients model in the admin panel"""
    list_display = ("title",)
