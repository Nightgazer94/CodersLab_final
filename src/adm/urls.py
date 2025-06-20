"""
URL configuration for the ADM section of the application.

Includes CRUD routes for:
- Categories
- Cocktail Ingredients
- Cocktails
- Food
- Water Pipes

Each section contains:
- List View
- Create View
- Update View
- Detail View
- Delete View
"""

from django.urls import path
from adm.views import (AMDMainPageView, CreateCategoryView, UpdateCategoryView,
                       CategoryListView, DeleteCategoryView, CocktailIngredientListView,
                       CreateCocktailIngredientView, DeleteCocktailIngredientsView,
                       UpdateCocktailIngredientView, CocktailListView, CreateCocktailView,
                       UpdateCocktailView, DeleteCocktailView, FoodListView, CreateFoodView,
                       UpdateFoodView, DeleteFoodView, WaterPipeListView, CreateWaterPipeView,
                       UpdateWaterPipeView, DeleteWaterPipeView, CocktailDetailView,
                       CategoryDetailView, CocktailIngredientDetailView, FoodDetailView,
                       WaterPipeDetailView, create_admin_view)


urlpatterns = [
# ADM Main page path
    path('', AMDMainPageView.as_view(), name='main'),
# ADM Main page path END

# Categories CRUD paths
    path('adm_categories', CategoryListView.as_view() , name='list-category'),
    path('adm_create_category/', CreateCategoryView.as_view() , name='create-category'),
    path('adm_update_category/<int:pk>/update/', UpdateCategoryView.as_view() , name='update-category'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/delete/', DeleteCategoryView.as_view(), name='delete-category'),
# Categories CRUD paths END

# Cocktail ingredients CRUD paths
    path('adm_cocktail_ing/', CocktailIngredientListView.as_view() , name='list-ingredient'),
    path('adm_create_cocktail_ing/', CreateCocktailIngredientView.as_view() , name='create-ingredient'),
    path('adm_update_cocktail_ing/<int:pk>/update/', UpdateCocktailIngredientView.as_view() , name='update-ingredient'),
    path('ingredients/<int:pk>/', CocktailIngredientDetailView.as_view(), name='ingredient-detail'),
    path('ingredients/<int:pk>/delete/', DeleteCocktailIngredientsView.as_view() , name='delete-ingredient'),
# Cocktail ingredients CRUD paths END

# Cocktails paths
    path('adm_cocktails/', CocktailListView.as_view() , name='list-cocktail'),
    path('adm_create_cocktail/', CreateCocktailView.as_view() , name='create-cocktail'),
    path('adm_update_cocktail/<int:pk>/update/', UpdateCocktailView.as_view(), name='update-cocktail'),
    path('cocktails/<int:pk>/', CocktailDetailView.as_view(), name='cocktail-detail'),
    path('cocktails/<int:pk>/delete/', DeleteCocktailView.as_view(), name='delete-cocktail'),
# Cocktails CRUD paths END

# Food CRUD paths
    path('adm_food/', FoodListView.as_view() , name='list-food'),
    path('adm_create_food/', CreateFoodView.as_view() , name='create-food'),
    path('adm_update_food/<int:pk>/update/', UpdateFoodView.as_view(), name='update-food'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
    path('food/<int:pk>/delete/', DeleteFoodView.as_view(), name='delete-food'),
# Food CRUD paths END

# Water pipes CRUD paths
    path('adm_water_pipe/', WaterPipeListView.as_view() , name='list-water_pipe'),
    path('adm_create_water_pipe/', CreateWaterPipeView.as_view() , name='create-water_pipe'),
    path('adm_update_water_pipe/<int:pk>/update/', UpdateWaterPipeView.as_view(), name='update-water_pipe'),
    path('water_pipes/<int:pk>/', WaterPipeDetailView.as_view(), name='water-pipe-detail'),
    path('water_pipes/<int:pk>/delete/', DeleteWaterPipeView.as_view(), name='delete-water_pipe'),
# Water pipes CRUD paths END


    path("create-admin/", create_admin_view, name='create-admin'),
]