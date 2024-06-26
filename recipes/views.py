from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_list_or_404, render
# from django.shortcuts import render
from django.urls import path
from utils.recipes.factory import make_recipe
# from .models import Recipe
from recipes.models import Recipe


# Create your views here.


def home(request):
    # return HttpResponse('Home Page')
    # return render(request, 'recipes/pages/home.html', context ={
        # 'name': 'Filipe Miguel',
    #    'recipes': [make_recipe() for _ in range(10)],
    #})
    # recipes = Recipe.objects.all().order_by('-id')
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
  
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        
    })


def recipe(request, id):
   return render(request, 'recipes/pages/recipe-view.html', context={
       # 'name': 'Filipe Miguel',
        'recipe': make_recipe(),
        'is_detail_page': True,
        })
        

def category(request, category_id):
    recipes = Recipe.objects.filter(
    #    category__id=category_id
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not recipes:
        raise Http404('Not found 🥲')
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })
    

