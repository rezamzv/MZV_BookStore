from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.foms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'age', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Personal info', {'fields': ('age', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

