# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from .models import Recipe
from utils.pagination import make_view_pagination


def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_view_pagination(req, recipes)

    return render(req, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range
    })


def category(req, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        )
        .order_by('-id')
    )

    page_obj, pagination_range = make_view_pagination(req, recipes)

    return render(req, 'recipes/pages/category.html', context={
        'recipes': page_obj,  # get all recipes with this category
        'title': recipes[0].category.name,  # get category title
        'pagination_range': pagination_range
    })


def recipe(req, id):
    recipe = get_object_or_404(Recipe.objects, id=id, is_published=True)

    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'detail_page': True
    })


def search(req):
    search_term = req.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        ), is_published=True

    ).order_by('-id')

    page_obj, pagination_range = make_view_pagination(req, recipes)

    return render(req, 'recipes/pages/search.html', context={
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    })
