from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from box import views as box_views
from profiles import views as profiles_views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', box_views.index, name='home'),
    path('recipe/', include('box.urls')),
    path('profile/', include('profiles.urls')),
    path('login/', profiles_views.login_user, name='login'),
    path('logout/', profiles_views.logout_user, name='logout'),
    path('register/', profiles_views.register_user, name='register')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = box_views.pageNotFound
