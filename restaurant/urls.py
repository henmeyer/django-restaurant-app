from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # Ingredient Views
    path('ingredients/', views.IngredientListView.as_view(),
         name='ingredients_list'),
    path('ingredients/create/', views.IngredientCreateView.as_view(),
         name='ingredient_create'),
    path(
        'ingredients/<pk>/delete/',
        views.IngredientDeleteView.as_view(),
        name='ingredient_delete'),
    path('ingredients/<pk>/update/',
         views.IngredientUpdateView.as_view(),
         name='ingredient_update'),

    # MenuItem views
    path('menu/', views.MenuItemListView.as_view(),
         name='menuitems_list'),
    path('menu/create', views.MenuItemCreateView.as_view(),
         name='menuitem_create'),
    path('menu/<pk>/delete', views.MenuItemDeleteView.as_view(),
         name='menuitem_delete'),
    path('menu/<pk>/update', views.MenuItemUpdateView.as_view(),
         name='menuitem_update'),

    # RecipeRequirement views
    path('reciperequirement/create', views.RecipeRequirementCreateView.as_view(),
         name='reciperequirement_create'),
    path('reciperequirement/<pk>/delete', views.RecipeRequirementDeleteView.as_view(),
         name='reciperequirement_delete'),

    # Purchase views
     path('purchase/', views.PurchaseListView.as_view(),
         name='purchases_list'),
    path('purchase/create', views.PurchaseCreateView.as_view(),
         name='purchase_create'),
]
