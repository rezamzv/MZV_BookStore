from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'age', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Personal info', {'fields': ('age', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

