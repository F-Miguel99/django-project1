from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
from django.urls import path
from utils.recipes.factory import make_recipe

# Create your views here.


def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'recipes/pages/home.html', context ={
        # 'name': 'Filipe Miguel',
        'recipes': [make_recipe() for _ in range(10)],
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        # 'name': 'Filipe Miguel',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })

