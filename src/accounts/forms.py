# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username",
                   "email",
                   "avatar",
                   )

class CustomUserChangeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
                   "email",
                   "username",

                   )
        
class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
    
