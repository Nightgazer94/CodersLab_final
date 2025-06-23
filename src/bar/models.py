"""
Models for the bar application.

Includes:
- Category: Represents categories for drinks, food and water pipes.
- CocktailIngredient: Individual ingredients used in cocktails.
- Cocktail: Cocktails with price, description, base alcohol, and ingredients.
- Food: Food items with price and description.
- WaterPipe: Water pipes with flavour and tobacco type.

Also includes:
- Custom model managers and querysets for filtering cheap cocktails and food.
- Choice constants for base alcohol types and tobacco types.
"""


from django.db import models
from django.urls import reverse


CHOICES_COCKTAIL = [
    ("None", "None"),
    ("Gin", "Gin"),
    ("Vodka", "Vodka"),
    ("Rum", "Rum"),
    ("Tequila", "Tequila"),
    ("Whisky", "Whisky"),
]

CHOICES_TOBACCO = [
    ("None", "None"),
    ("Light", "Light"),
    ("Dark", "Dark"),
]


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return f"Category: {self.name}"


class CocktailIngredient(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Cocktail Ingredients"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class CocktailQuerySet(models.QuerySet):
    def cheap(self, max_price):
        return self.filter(price__lte=max_price)


class CocktailManager(models.Manager):
    def get_queryset(self):
        return CocktailQuerySet(self.model, using=self._db)

    def cheap(self, max_price):
        return self.get_queryset().cheap(max_price)


class Cocktail(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    description = models.TextField(null=False)
    ingredients = models.ManyToManyField(CocktailIngredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    base_alcohol = models.CharField(choices=CHOICES_COCKTAIL, max_length=9, null=False)
    image = models.FileField(upload_to="images", null=True, blank=True)

    objects = CocktailManager()

    def get_absolute_url(self):
        return reverse('cocktail-details', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Cocktails"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - Price: {self.price}$ - Base alcohol: {self.base_alcohol}"


class FoodQuerySet(models.QuerySet):
    def cheap(self, max_price):
        return self.filter(price__lte=max_price)


class FoodManager(models.Manager):
    def get_queryset(self):
        return FoodQuerySet(self.model, using=self._db)

    def cheap(self, max_price):
        return self.get_queryset().cheap(max_price)


class Food(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    description = models.TextField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = FoodManager()

    def get_absolute_url(self):
        return reverse('food-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Food"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - Price: {self.price}$"


class WaterPipe(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    flavour = models.CharField(max_length=150, null=False)
    tobacco = models.CharField(choices=CHOICES_TOBACCO, max_length=7, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('water-pipe-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Water Pipes"
        ordering = ['name']

    def __str__(self):
        return (f"{self.name} - Price: {self.price}$ - "
                f"Flavour: {self.flavour} - Tobacco: {self.tobacco}")
