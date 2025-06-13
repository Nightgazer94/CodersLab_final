"""
Administration views for CRUD operations on Category, CocktailIngredient,
Cocktail, Food, and WaterPipe models. All views require user authentication.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from adm.forms import (
    CategoryForm,
    CocktailForm,
    CocktailIngredientForm,
    FoodForm,
    WaterPipeForm,
)
from bar.models import (
    Category,
    Cocktail,
    CocktailIngredient,
    Food,
    WaterPipe,
)


# Admin main page
class AMDMainPageView(LoginRequiredMixin, TemplateView):
    """
    Display the main administration dashboard page. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    template_name = 'adm/adm_main_page.html'


# Category CRUD
class CategoryListView(LoginRequiredMixin, ListView):
    """
    List all categories in the system. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Category
    template_name = 'adm/category/adm_category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display details for a single category. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Category
    template_name = 'adm/category/adm_category_detail.html'
    context_object_name = 'category'


class CreateCategoryView(LoginRequiredMixin, CreateView):
    """
    Provide a form to create a new category. Redirects to category detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Category
    form_class = CategoryForm
    template_name = 'adm/category/adm_category_create.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully creating a category.
        """
        return reverse('category-detail', kwargs={'pk': self.object.pk})


class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    """
    Provide a form to update an existing category. Redirects to category detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Category
    form_class = CategoryForm
    template_name = 'adm/category/adm_category_update.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully updating a category.
        """
        return reverse('category-detail', kwargs={'pk': self.object.pk})


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    """
    Confirm and delete a category. Redirects to category list on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Category
    template_name = 'adm/category/adm_category_delete.html'
    success_url = reverse_lazy('list-category')


# Cocktail ingredients CRUD
class CocktailIngredientListView(LoginRequiredMixin, ListView):
    """
    List all cocktail ingredients. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = CocktailIngredient
    template_name = 'adm/cocktail_ingredient/adm_cocktail_ing_list.html'
    context_object_name = 'cocktail_ingredients'


class CocktailIngredientDetailView(LoginRequiredMixin, DetailView):
    """
    Display details for a single cocktail ingredient. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = CocktailIngredient
    template_name = 'adm/cocktail_ingredient/adm_cocktail_ing_detail.html'
    context_object_name = 'ingredient'


class CreateCocktailIngredientView(LoginRequiredMixin, CreateView):
    """
    Provide a form to create a new cocktail ingredient. Redirects to ingredient detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = CocktailIngredient
    form_class = CocktailIngredientForm
    template_name = 'adm/cocktail_ingredient/adm_cocktail_ing_create.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully creating a cocktail ingredient.
        """
        return reverse('ingredient-detail', kwargs={'pk': self.object.pk})


class UpdateCocktailIngredientView(LoginRequiredMixin, UpdateView):
    """
    Provide a form to update an existing cocktail ingredient. Redirects to ingredient detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = CocktailIngredient
    form_class = CocktailIngredientForm
    template_name = 'adm/cocktail_ingredient/adm_cocktail_ing_update.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully updating a cocktail ingredient.
        """
        return reverse('ingredient-detail', kwargs={'pk': self.object.pk})


class DeleteCocktailIngredientsView(LoginRequiredMixin, DeleteView):
    """
    Confirm and delete a cocktail ingredient. Redirects to ingredients list on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = CocktailIngredient
    template_name = 'adm/cocktail_ingredient/adm_cocktail_ing_delete.html'
    success_url = reverse_lazy('list-ingredient')


# Cocktail CRUD
class CocktailListView(LoginRequiredMixin, ListView):
    """
    List all cocktails. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Cocktail
    template_name = 'adm/cocktail/adm_cocktail_list.html'
    context_object_name = 'cocktails'


class CocktailDetailView(LoginRequiredMixin, DetailView):
    """
    Display details for a single cocktail. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Cocktail
    template_name = 'adm/cocktail/adm_cocktail_detail.html'
    context_object_name = 'cocktail'


class CreateCocktailView(LoginRequiredMixin, CreateView):
    """
    Provide a form to create a new cocktail. Redirects to cocktail detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Cocktail
    form_class = CocktailForm
    template_name = 'adm/cocktail/adm_cocktail_create.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully creating a cocktail.
        """
        return reverse('cocktail-detail', kwargs={'pk': self.object.pk})


class UpdateCocktailView(LoginRequiredMixin, UpdateView):
    """
    Provide a form to update an existing cocktail. Redirects to cocktail detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Cocktail
    form_class = CocktailForm
    template_name = 'adm/cocktail/adm_cocktail_update.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully updating a cocktail.
        """
        return reverse('cocktail-detail', kwargs={'pk': self.object.pk})


class DeleteCocktailView(LoginRequiredMixin, DeleteView):
    """
    Confirm and delete a cocktail. Redirects to cocktail list on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Cocktail
    template_name = 'adm/cocktail/adm_cocktail_delete.html'
    success_url = reverse_lazy('list-cocktail')


# Food CRUD
class FoodListView(LoginRequiredMixin, ListView):
    """
    List all food items. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Food
    template_name = 'adm/food/adm_food_list.html'
    context_object_name = 'foods'


class FoodDetailView(LoginRequiredMixin, DetailView):
    """
    Display details for a single food item. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Food
    template_name = 'adm/food/adm_food_detail.html'
    context_object_name = 'food'


class CreateFoodView(LoginRequiredMixin, CreateView):
    """
    Provide a form to create a new food item. Redirects to food detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Food
    form_class = FoodForm
    template_name = 'adm/food/adm_food_create.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully creating a food item.
        """
        return reverse('food-detail', kwargs={'pk': self.object.pk})


class UpdateFoodView(LoginRequiredMixin, UpdateView):
    """
    Provide a form to update an existing food item. Redirects to food detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Food
    form_class = FoodForm
    template_name = 'adm/food/adm_food_update.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully updating a food item.
        """
        return reverse('food-detail', kwargs={'pk': self.object.pk})


class DeleteFoodView(LoginRequiredMixin, DeleteView):
    """
    Confirm and delete a food item. Redirects to food list on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = Food
    template_name = 'adm/food/adm_food_delete.html'
    success_url = reverse_lazy('list-food')


# Water pipe CRUD
class WaterPipeListView(LoginRequiredMixin, ListView):
    """
    List all water pipe products. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = WaterPipe
    template_name = 'adm/water_pipes/adm_water_pipes_list.html'
    context_object_name = 'water_pipes'


class WaterPipeDetailView(LoginRequiredMixin, DetailView):
    """
    Display details for a single water pipe product. Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = WaterPipe
    template_name = 'adm/water_pipes/adm_water_pipes_detail.html'
    context_object_name = 'pipe'


class CreateWaterPipeView(LoginRequiredMixin, CreateView):
    """
    Provide a form to create a new water pipe. Redirects to water pipe detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = WaterPipe
    form_class = WaterPipeForm
    template_name = 'adm/water_pipes/adm_water_pipes_create.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully creating a water pipe.
        """
        return reverse('water-pipe-detail', kwargs={'pk': self.object.pk})


class UpdateWaterPipeView(LoginRequiredMixin, UpdateView):
    """
    Provide a form to update an existing water pipe. Redirects to water pipe detail on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = WaterPipe
    form_class = WaterPipeForm
    template_name = 'adm/water_pipes/adm_water_pipes_update.html'

    def get_success_url(self):
        """
        Return the URL to redirect to after successfully updating a water pipe.
        """
        return reverse('water-pipe-detail', kwargs={'pk': self.object.pk})


class DeleteWaterPipeView(LoginRequiredMixin, DeleteView):
    """
    Confirm and delete a water pipe product. Redirects to water pipe list on success.
    Requires user login.
    """
    login_url = 'login'
    redirect_field_name = 'next'
    model = WaterPipe
    template_name = 'adm/water_pipes/adm_water_pipes_delete.html'
    success_url = reverse_lazy('list-water_pipe')
