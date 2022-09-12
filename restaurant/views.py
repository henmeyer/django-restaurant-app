from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient


class IngredientListView(ListView):
    model = Ingredient
    template_name = "restaurant/ingredients_list.html"
