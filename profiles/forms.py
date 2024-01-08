from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        """Profile creation form"""
        model = User
        fields = ["username", "email", "password1", "password2"]

