# Create your views here.
from django.shortcuts import render
from utils import factory
from .models import Recipe

# HTTP REQUEST
def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def category(req, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes
    })


def recipe(req, id):
    recipe = Recipe.objects.get(id=id)
    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'detail_page': True
    })
