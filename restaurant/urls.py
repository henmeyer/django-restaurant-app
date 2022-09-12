from django.urls import path
from . import views


urlpatterns = [
    path('', views.IngredientListView.as_view(), name='ingredients_list')
]
