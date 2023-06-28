from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

#On utilise useradmin lorsqu'il s'agit des utilisateurs
@admin.register(User)
class UserAdmin(UserAdmin):
    pass
