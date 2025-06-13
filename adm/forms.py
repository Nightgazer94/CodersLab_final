from django import forms
from django.core.exceptions import ValidationError

from bar.models import (
    Category,
    Cocktail,
    CocktailIngredient,
    Food,
    WaterPipe,
)

"""
Forms for creating and validating Category, CocktailIngredient, Cocktail, Food,
and WaterPipe objects. Includes custom validation rules for names and prices.
"""

class CategoryForm(forms.ModelForm):
    """
    Form for creating or updating a Category.

    Validates that the name is at least 3 characters long.
    """
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        """
        Ensure the category name has at least 3 non-whitespace characters.

        Returns:
            str: The cleaned and stripped name.

        Raises:
            ValidationError: If the name is shorter than 3 characters.
        """
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 3:
            raise ValidationError(
                "The name must have at least 3 characters."
            )
        return name


class CocktailIngredientForm(forms.ModelForm):
    """
    Form for creating or updating a CocktailIngredient.

    Validates that the ingredient name is at least 3 characters long.
    """
    class Meta:
        model = CocktailIngredient
        fields = ['name']

    def clean_name(self):
        """
        Ensure the ingredient name has at least 3 non-whitespace characters.

        Returns:
            str: The cleaned and stripped name.

        Raises:
            ValidationError: If the name is shorter than 3 characters.
        """
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 3:
            raise ValidationError(
                "The name must have at least 3 characters."
            )
        return name


class CocktailForm(forms.ModelForm):
    """
    Form for creating or updating a Cocktail.

    Validates that the name is at least 3 characters long and the price
    is greater than zero. Uses custom widgets for description and ingredients.
    """
    class Meta:
        model = Cocktail
        fields = [
            'name',
            'price',
            'description',
            'ingredients',
            'category',
            'base_alcohol',
            'image',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
            'ingredients': forms.CheckboxSelectMultiple(),
        }

    def clean_name(self):
        """
        Ensure the cocktail name has at least 3 non-whitespace characters.

        Returns:
            str: The cleaned and stripped name.

        Raises:
            ValidationError: If the name is shorter than 3 characters.
        """
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 3:
            raise ValidationError(
                "The name must have at least 3 characters."
            )
        return name

    def clean_price(self):
        """
        Ensure the cocktail price is greater than zero.

        Returns:
            Decimal: The validated price.

        Raises:
            ValidationError: If the price is less than or equal to zero.
        """
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise ValidationError(
                "Price must be greater than 0."
            )
        return price


class FoodForm(forms.ModelForm):
    """
    Form for creating or updating a Food item.

    Validates that the name is at least 3 characters long and the price
    is greater than zero. Uses a custom widget for description.
    """
    class Meta:
        model = Food
        fields = [
            'name',
            'price',
            'description',
            'category',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_name(self):
        """
        Ensure the food name has at least 3 non-whitespace characters.

        Returns:
            str: The cleaned and stripped name.

        Raises:
            ValidationError: If the name is shorter than 3 characters.
        """
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 3:
            raise ValidationError(
                "The name must have at least 3 characters."
            )
        return name

    def clean_price(self):
        """
        Ensure the food price is greater than zero.

        Returns:
            Decimal: The validated price.

        Raises:
            ValidationError: If the price is less than or equal to zero.
        """
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise ValidationError(
                "Price must be greater than 0."
            )
        return price


class WaterPipeForm(forms.ModelForm):
    """
    Form for creating or updating a WaterPipe product.

    Validates that the name is at least 3 characters long and the price
    is greater than zero.
    """
    class Meta:
        model = WaterPipe
        fields = [
            'name',
            'price',
            'flavour',
            'tobacco',
            'category',
        ]

    def clean_name(self):
        """
        Ensure the water pipe name has at least 3 non-whitespace characters.

        Returns:
            str: The cleaned and stripped name.

        Raises:
            ValidationError: If the name is shorter than 3 characters.
        """
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 3:
            raise ValidationError(
                "The name must have at least 3 characters."
            )
        return name

    def clean_price(self):
        """
        Ensure the water pipe price is greater than zero.

        Returns:
            Decimal: The validated price.

        Raises:
            ValidationError: If the price is less than or equal to zero.
        """
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise ValidationError(
                "Price must be greater than 0."
            )
        return price
