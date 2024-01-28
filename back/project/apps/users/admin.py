from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'is_superuser', 'is_active', 'last_login']
    search_fields = ['username', 'email']
    list_filter = ['is_superuser', 'is_active']

    fieldsets = [
        (
            'Personal info', {
                'fields': ['username', 'email', 'password']
            }
        ),
        (
            'Permissions', {
                'fields': ['is_superuser', 'is_active']
            }
        ),
        (
            'Important dates', {
                'fields': ['last_login', 'date_joined']
            }
        ),

    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    ]

    model = User
