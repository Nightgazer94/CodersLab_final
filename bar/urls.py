"""
URL configuration for the public-facing bar section of the website.

Includes routes for:
- Main page
- Cocktails (all, detail, and cheap)
- Food (all and cheap)
- Water pipes (all)
- Contact page
"""

from django.urls import path
from bar.views import (MainPageView, CocktailsView,CocktailDetailView, FoodListView, WaterPipeView,
                       ContactView, CheapCocktailListView, CheapFoodListView,)


urlpatterns = [
# BAR Main page path
    path('', MainPageView.as_view(), name='main2'),
# BAR Main page path END

# BAR Cocktails paths
    path('cocktails/', CocktailsView.as_view(), name='cocktails'),
    path('cocktails/<int:pk>/', CocktailDetailView.as_view(), name='cocktail-details'),
    path('cheap_cocktails/', CheapCocktailListView.as_view(), name='cheap-cocktails'),
# BAR Cocktails paths END

# BAR Food paths
    path('food/', FoodListView.as_view(), name='food'),
    path('cheap_food/', CheapFoodListView.as_view(), name='cheap-food'),
# Bar Food paths END

# Bar Water Pipe paths
    path('water_pipe/', WaterPipeView.as_view(), name='water-pipe'),
# BAR Water Pipes paths END

# BAR Contact page path
    path('contact/', ContactView.as_view(), name='contact'),
# BAR Contact page path END
]