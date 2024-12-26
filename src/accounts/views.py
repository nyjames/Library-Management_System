from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    """
    View to handle user sign-up.
    Inherits from CreateView and uses the CustomUserCreationForm.
    Redirects to login page on success.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
