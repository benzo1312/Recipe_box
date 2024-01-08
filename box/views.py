from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Recipes, Ingredients
from .forms import AddRecipe


def index(request):
    """Basic page"""
    return render(request, 'base.html')


def recipes_views(request):
    """Function of presenting all recipes"""
    recipe = Recipes.objects.all()
    context = {'recipe': recipe}

    return render(request, 'box/recipes.html', context=context)


def recipe_list(request, recipe_slug):
    """Views the Recipe list"""
    recipe = Recipes.objects.prefetch_related().get(slug=recipe_slug)
    ingredients = recipe.ingredients.all()
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'box/recipe_list.html', context=context)


def favourites_add(request, recipe_id):
    """Function of adding and removing recipes to favorites"""
    recipe = Recipes.objects.get(id=recipe_id)
    profile = request.user.profile_user
    if profile.favourites.filter(id=recipe_id).exists():
        profile.favourites.remove(recipe)
    else:
        profile.favourites.add(recipe)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourites_list(request):
    """View of selected recipes"""
    fav_recipe = request.user.profile_user.favourites.all()
    context = {'fav_recipe': fav_recipe}
    return render(request, 'box/favourites.html', context=context)


def add_recipe(request):
    """Recipe adding function"""
    form = AddRecipe
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipes.objects.first()
            recipe.title = data['title']
            recipe.cooking = data['cooking']
            recipe.cooking_time = data['cooking_time']
            recipe.creator = request.user
            recipe.slug = {'slug': ('title',)}
            recipe.save()
    context = {'form': form}
    return render(request, 'box/add_recipe.html', context=context)



def pageNotFound(request, exception):
    """Non-existent page error function"""
    return HttpResponseNotFound("<h3>Page not found</h3>")
