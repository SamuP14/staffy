from django.contrib import admin
from .models import Profile, Role

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id_number',
        'phone',
        'profession',
        'avatar',
    )

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')