from django.urls import path
from .views import SignUpView

urlpatterns = [
    # Sign-up view URL
    path('signup/', SignUpView.as_view(), name='signup'),
]
