from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
from django.urls import path

# Create your views here.


def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Filipe Miguel',
    })

