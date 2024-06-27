from django.urls import path
# from recipes.views import home  
from . import views

app_name = 'recipes'

urlpatterns = [
    # path('sobre/', sobre),
    #path('contato/', contato),
    # path('', home),
    # path('', views.home),
    # path('recipes/<int:id>/', views.recipe),
    path('', views.home, name='home'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('category/<int:category_id>/', views.category, name='category'),
    
] 
