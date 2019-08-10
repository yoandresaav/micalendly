# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'last_login',
        'is_superuser',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'is_profesor',
        'is_estudiante',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'is_profesor',
        'is_estudiante',
    )
    raw_id_fields = ('groups', 'user_permissions')