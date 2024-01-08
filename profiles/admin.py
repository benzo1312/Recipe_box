from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Registering profiles in the administrator panel"""
    list_display = ('id', 'email')
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.avatar.url} wight='100' height='110'")

    get_image.short_description = "Avatar"
