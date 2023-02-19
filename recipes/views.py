from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from utils import factory

# HTTP REQUEST
def home(req):
    return render(req, 'recipes/pages/home.html', context={
        'recipes': [factory.make_recipe() for _ in range(10)]
    })

def recipe(req, id):
    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': factory.make_recipe(),
        'detail_page': True
    })
