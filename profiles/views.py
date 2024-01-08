import logging
from .decorators import unauthenticated_user
from .forms import CreateUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from box.models import Recipes

logger = logging.getLogger('recipe_logger')


@unauthenticated_user
def login_user(request):
    """User authentication"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password do not match')
            logger.info('Username or password do not match')
    return render(request, 'profiles/login.html')


@unauthenticated_user
def register_user(request):
    """Registration function"""
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                if User.objects.filter(username=username).exists():
                    messages.info(request, f"The user with username {username} already exists")
                else:
                    form.save()
                    messages.info(request, f"The user with username {username} has been registered")
                    return redirect("login")
            except User.DoesNotExists as error:
                logger.error(error)
    context = {
        'form': form
    }
    return render(request, 'profiles/register.html', context=context)


def logout_user(request):
    """Unauthenticated"""
    logout(request)
    return redirect('home')


def show_user_page(request):
    profile_ = Profile.objects.filter(user__pk=request.user.pk).first()
    recipes = Recipes.objects.filter()
    context ={
        'profile': profile_,
        'recipes': recipes
    }
    return render(request, 'profiles/profile.html', context=context)

