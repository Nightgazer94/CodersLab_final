"""
Admin site registrations for bar application models.
Includes Category, Cocktail, CocktailIngredient, WaterPipe, and Food.
"""


from django.contrib import admin
from bar.models import Category, Cocktail, CocktailIngredient, WaterPipe, Food


admin.site.register(Category)
admin.site.register(Cocktail)
admin.site.register(CocktailIngredient)
admin.site.register(WaterPipe)
admin.site.register(Food)
