from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile
from catalog.models import Review, Book 


# CustomUser admin configuration
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # List fields displayed in the user list view
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]

    # Fieldsets for displaying user details in the form
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)

# Register the CustomUser model with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Registering UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'address')
    search_fields = ('user__username', 'user__email')
