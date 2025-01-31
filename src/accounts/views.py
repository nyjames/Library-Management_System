from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileImageForm, CustomUserCreationForm


class SignUpView(CreateView):
    """
    View to handle user sign-up.
    Inherits from CreateView and uses the CustomUserCreationForm.
    Redirects to login page on success.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
class CustomUserProfileView(CreateView):

    ''' 
    View to edit profile

    Inherits from CreateView and uses the CustomUserCreationForm.
    Redirects to my_books page on success.

    '''

    def edit_profile(request):

        user = request.user
        if request.method == 'POST':
            form = ProfileImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success')
        else:
            form = ProfileImageForm()

        return render(request, 'my_books.html', {'form': form})
    
    def get_success_url(self):
        return HttpResponse('Successfully uploaded')
