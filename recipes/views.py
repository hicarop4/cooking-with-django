# Create your views here.
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe


def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(req, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True
        )
        .order_by('-id')
    )

    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes,  # get all recipes with this category
        'title': recipes[0].category.name  # get category title
    })


def recipe(req, id):
    recipe = get_object_or_404(Recipe.objects, id=id)

    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'detail_page': True
    })
