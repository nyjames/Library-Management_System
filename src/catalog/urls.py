from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # View to display the catalog of books
    path('catalog/', views.book_catalog, name='book_catalog'),

    # View to display books that the user has checked out
    path('my_books/', views.my_books, name='my_books'),

    # View to display the details of a single book
    path('book/<str:book_id>/', views.book_detail, name='book_detail'),
]
