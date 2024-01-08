from django.db import models
from django.contrib.auth.models import User

from box.models import Recipes


class Profile(models.Model):
    """Profile creation"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    nickname = models.CharField(max_length=100, verbose_name='Nickname')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    bio = models.TextField('Biography', max_length=600, null=True, blank=True)
    avatar = models.ImageField(verbose_name="Avatar", upload_to="users/", default='default.png')
    favourites = models.ManyToManyField(Recipes, blank=True, default=None, related_name='favourite_recipes')

    created_at = models.DateTimeField(verbose_name='Creared_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.user.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
