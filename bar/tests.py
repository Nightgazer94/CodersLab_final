import tempfile
from django.test import TestCase
from django.urls import reverse

from bar.models import (
    Category,
    CocktailIngredient,
    Cocktail,
    Food,
    WaterPipe,
)

"""
Tests for models in the `bar` application.
Validate __str__ and get_absolute_url methods,
common scenarios, and custom managers (e.g., cheap).
"""

class CategoryModelTest(TestCase):
    """TestCase for the Category model."""

    def setUp(self):
        """Create a category instance for tests."""
        self.category = Category.objects.create(name="TestCategory")

    def test_str(self):
        """Ensure __str__ returns 'Category: <name>'."""
        self.assertEqual(str(self.category), "Category: TestCategory")

    def test_get_absolute_url(self):
        """Ensure get_absolute_url returns the correct detail URL."""
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        self.assertEqual(self.category.get_absolute_url(), url)


class CocktailIngredientModelTest(TestCase):
    """TestCase for the CocktailIngredient model."""

    def setUp(self):
        """Create an ingredient instance for tests."""
        self.ingredient = CocktailIngredient.objects.create(name="Lime")

    def test_str(self):
        """Ensure __str__ returns the ingredient name."""
        self.assertEqual(str(self.ingredient), "Lime")

    def test_get_absolute_url(self):
        """Ensure get_absolute_url returns the correct detail URL."""
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient.pk})
        self.assertEqual(self.ingredient.get_absolute_url(), url)


class CocktailModelTest(TestCase):
    """TestCase for the Cocktail model, including the cheap() manager."""

    def setUp(self):
        """Create categories, ingredients, and cocktails for testing."""
        self.category = Category.objects.create(name="Cat")
        self.ing1 = CocktailIngredient.objects.create(name="Gin")
        self.ing2 = CocktailIngredient.objects.create(name="Vodka")
        self.cocktail1 = Cocktail.objects.create(
            name="CheapCocktail",
            price="5.00",
            description="Cheap",
            category=self.category,
            base_alcohol="Gin",
        )
        self.cocktail1.ingredients.set([self.ing1, self.ing2])
        self.cocktail2 = Cocktail.objects.create(
            name="ExpensiveCocktail",
            price="15.00",
            description="Expensive",
            category=self.category,
            base_alcohol="Vodka",
        )
        self.cocktail2.ingredients.set([self.ing1])

    def test_str(self):
        """Ensure __str__ returns formatted string with price and base alcohol."""
        expected = "CheapCocktail - Price: 5.00$ - Base alcohol: Gin"
        self.assertEqual(str(self.cocktail1), expected)

    def test_get_absolute_url(self):
        """Ensure get_absolute_url returns the correct detail URL."""
        url = reverse('cocktail-details', kwargs={'pk': self.cocktail1.pk})
        self.assertEqual(self.cocktail1.get_absolute_url(), url)

    def test_cheap_manager(self):
        """Ensure cheap() manager filters cocktails by max price."""
        cheap_qs = Cocktail.objects.cheap(10.00)
        self.assertIn(self.cocktail1, cheap_qs)
        self.assertNotIn(self.cocktail2, cheap_qs)


class FoodModelTest(TestCase):
    """TestCase for the Food model, including the cheap() manager."""

    def setUp(self):
        """Create category and food items for testing."""
        self.category = Category.objects.create(name="FoodCat")
        self.food1 = Food.objects.create(
            name="Bread",
            price="2.50",
            description="Tasty",
            category=self.category,
        )
        self.food2 = Food.objects.create(
            name="Steak",
            price="25.00",
            description="Delicious",
            category=self.category,
        )

    def test_str(self):
        """Ensure __str__ returns formatted string with price."""
        expected = "Bread - Price: 2.50$"
        self.assertEqual(str(self.food1), expected)

    def test_get_absolute_url(self):
        """Ensure get_absolute_url returns the correct detail URL."""
        url = reverse('food-detail', kwargs={'pk': self.food1.pk})
        self.assertEqual(self.food1.get_absolute_url(), url)

    def test_cheap_manager(self):
        """Ensure cheap() manager filters foods by max price."""
        qs = Food.objects.cheap(10.00)
        self.assertIn(self.food1, qs)
        self.assertNotIn(self.food2, qs)


class WaterPipeModelTest(TestCase):
    """TestCase for the WaterPipe model."""

    def setUp(self):
        """Create category and water pipe instance for testing."""
        self.category = Category.objects.create(name="PipeCat")
        self.pipe = WaterPipe.objects.create(
            name="Hookah",
            price="50.00",
            flavour="Apple",
            tobacco="Light",
            category=self.category,
        )

    def test_str(self):
        """Ensure __str__ returns formatted string with all properties."""
        expected = "Hookah - Price: 50.00$ - Flavour: Apple - Tobacco: Light"
        self.assertEqual(str(self.pipe), expected)

    def test_get_absolute_url(self):
        """Ensure get_absolute_url returns the correct detail URL."""
        url = reverse('water-pipe-detail', kwargs={'pk': self.pipe.pk})
        self.assertEqual(self.pipe.get_absolute_url(), url)
