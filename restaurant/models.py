"""Importing models from django.db"""
from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    """ Ingredients """
    UNITY = 'UN'
    KILOGRAM = 'KG'
    POUNDS = 'LB'
    UNITS = [
        (UNITY, "Unity"),
        (KILOGRAM, "Kilogram"),
        (POUNDS, "Pounds"),
    ]
    name = models.CharField(max_length=32)
    stock = models.DecimalField(max_digits=19, decimal_places=3, default=0)
    unit = models.CharField(max_length=2, choices=UNITS, default=UNITY)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name}: quantity = {self.stock}{self.unit}, \
        price per unit = {self.unit_price}"

    def get_absolute_url(self):
        return reverse('ingredients_list')


class MenuItem(models.Model):
    """ MenuItem """
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: price {self.price}"

    def get_absolute_url(self):
        return reverse('menuitems_list')


class RecipeRequirement(models.Model):
    """ RecipeRequirement """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.ingredient.name} from {self.menu_item.name}"

    def get_absolute_url(self):
        return reverse('menuitems_list')

class Purchase(models.Model):
    """ Purchase """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.menu_item.name} at {self.timestamp}"

    def get_absolute_url(self):
        return reverse('purchases_list')
