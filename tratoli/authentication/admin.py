from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'username']

admin.site.register(User, UserAdmin)

