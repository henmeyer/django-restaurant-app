from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


def index(request):
    return render(request, 'restaurant/index.html')

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'restaurant/ingredients_list.html'

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'restaurant/ingredient_create.html'

class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredients_list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'restaurant/ingredient_update.html'

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'restaurant/menuitems_list.html'

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'restaurant/menuitem_create.html'

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menuitems_list')

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'restaurant/menuitem_update.html'

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'restaurant/reciperequirement_create.html'

class RecipeRequirementDeleteView(DeleteView):
    model = RecipeRequirement
    success_url = reverse_lazy('menuitems_list')

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'restaurant/purchases_list.html'

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'restaurant/purchase_create.html'
