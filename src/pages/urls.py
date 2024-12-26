from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.HomePageView.as_view(), name='home'),

    # Book catalog page
    path('catalog/', views.book_catalog, name='book_catalog'),

    # Book detail page (view details and checkout/return actions)
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
