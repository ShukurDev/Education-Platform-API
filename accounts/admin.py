from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email', 'is_staff']
    list_filter = ['username', 'date_created']


admin.site.register(User, UserAdmin)
