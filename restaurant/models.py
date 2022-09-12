"""Importing models from django.db"""
from django.db import models


class Ingredients(models.Model):
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


class MenuItem(models.Model):
    """ MenuItem """
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: price {self.price}"


class RecipeRequirement(models.Model):
    """ RecipeRequirement """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
