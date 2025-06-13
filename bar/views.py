"""
View definitions for the public-facing bar section of the website.

Includes:
- Main page view
- Cocktail category and detail views
- Filtered views for cheap cocktails and food
- Water pipe selection by tobacco type
- Contact page view
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from bar.models import Category, Cocktail, CocktailIngredient, WaterPipe, Food


class MainPageView(View):
    """
    Displays the main page of the bar.
    """
    def get(self, request):
        """
        Renders the main page template.
        """
        return render(request, 'bar/bar_pages/main_page.html')


class CocktailsView(View):
    """
    Displays cocktails grouped by base alcohol type.
    """
    def get(self, request):
        """
        Renders the cocktails page with cocktails filtered by base alcohol.
        """
        cocktails_gin = Cocktail.objects.filter(base_alcohol="Gin")
        cocktails_rum = Cocktail.objects.filter(base_alcohol="Rum")
        cocktails_vodka = Cocktail.objects.filter(base_alcohol="Vodka")
        cocktails_whisky = Cocktail.objects.filter(base_alcohol="Whisky")
        cocktails_tequila = Cocktail.objects.filter(base_alcohol="Tequila")
        return render(request, 'bar/bar_pages/cocktails_page.html', {
            'cocktails_gin': cocktails_gin,
            'cocktails_rum': cocktails_rum,
            'cocktails_vodka': cocktails_vodka,
            'cocktails_whisky': cocktails_whisky,
            'cocktails_tequila': cocktails_tequila,
        })


class CocktailDetailView(DetailView):
    """
    Displays detailed information about a single cocktail.
    """
    model = Cocktail
    template_name = 'bar/bar_pages/cocktail_details_page.html'
    context_object_name = 'cocktail'


class CheapCocktailListView(ListView):
    """
    Displays a list of cocktails that are cheaper than a specified price.
    """
    model = Cocktail
    template_name = "bar/bar_pages/cocktails_cheap_page.html"
    context_object_name = "cheap_cocktails"

    def get_queryset(self):
        """
        Returns a queryset of cocktails priced under 8.00.
        """
        return Cocktail.objects.cheap(8.00)


class FoodListView(ListView):
    """
    Displays a list of all available food items.
    """
    model = Food
    template_name = 'bar/bar_pages/food_page.html'
    context_object_name = 'foods'


class CheapFoodListView(ListView):
    """
    Displays a list of food items that are cheaper than a specified price.
    """
    model = Food
    template_name = "bar/bar_pages/food_cheap_page.html"
    context_object_name = "cheap_foods"

    def get_queryset(self):
        """
        Returns a queryset of food items priced under 10.00.
        """
        return Food.objects.cheap(10.00)


class WaterPipeView(View):
    """
    Displays water pipes grouped by tobacco type (Light or Dark).
    """
    def get(self, request):
        """
        Renders the water pipes page with pipes grouped by tobacco type.
        """
        water_pipes_light = WaterPipe.objects.filter(tobacco='Light')
        water_pipes_dark = WaterPipe.objects.filter(tobacco='Dark')
        return render(request, 'bar/bar_pages/water_pipes_page.html', {
            'water_pipes_light': water_pipes_light,
            'water_pipes_dark': water_pipes_dark,
        })


class ContactView(View):
    """
    Displays the contact page of the bar.
    """
    def get(self, request):
        """
        Renders the contact page template.
        """
        return render(request, 'bar/bar_pages/contact_page.html')
