from PIL import Image
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredients(models.Model):
    """Model for creating a table of ingredients"""
    title = models.CharField(max_length=50, verbose_name='Ingredient', default=None)
    quantity = models.IntegerField()
    type = models.CharField(max_length=30, verbose_name='Type', default=None)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipes(models.Model):
    """A model for creating tables with recipes"""
    title = models.CharField(max_length=100, verbose_name='Recipe')
    ingredients = models.ManyToManyField(Ingredients, related_name='Ingredients')
    cooking = models.TextField(verbose_name='Cooking method')
    cooking_time = models.FloatField(verbose_name='Cooking time', default=0.0, help_text='hours')
    photo = models.ImageField(verbose_name='Photo', upload_to='photo/', default='default.png')
    slug = models.SlugField(unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Creator', null=True, blank=True)

    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now=True)

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_absolute_url(self):
        return reverse('recipe_list', kwargs={'recipe_slug': self.slug})

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['created_at']
