import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from catalog.models import Book, Review
from django.conf import settings
import re
import random

# Constants for Google Books API integration
GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = settings.API_KEY  # Use API_KEY from settings for security (ensure this is in settings.py)


class HomePageView(TemplateView):
    """
    Home page view that renders the homepage template.
    """
    template_name = 'home.html'


@login_required
def book_detail(request, book_id):
    """
    View to display the details of a single book and handle checkout/return actions.

    Args:
        request (HttpRequest): The request object.
        book_id (str): The ID of the book to display (string-based, e.g., UUID).

    Returns:
        HttpResponse: The rendered book detail page.
    """
    # Retrieve the book object using the provided book_id
    book = get_object_or_404(Book, id=book_id)

    # Handle checkout/return actions when POST request is made
    if request.method == 'POST':
        if not book.checked_out_by:  # Book is available
            book.checked_out_by = request.user
            book.available = False  # Mark the book as unavailable
            book.save()
        else:
            if book.checked_out_by == request.user:  # User returning the book
                book.checked_out_by = None
                book.available = True  # Mark the book as available
                book.save()

        return redirect('catalog:book_detail', book_id=book.id)  # Refresh page after action

    # Render the book detail page with the book object
    return render(request, 'book_detail.html', {'book': book})


def my_books(request):
    """
    View to display a list of books currently checked out by the user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered my books page.
    """
    # Retrieve all books that are checked out by the current user
    checked_out_books = Book.objects.filter(checked_out_by=request.user)
    return render(request, 'my_books.html', {'books': checked_out_books})


def book_catalog(request):
    """
    View to display the catalog of books and handle search functionality,
    including randomizing the displayed books for each user.
    """
    # Retrieve the search query from the GET request
    search_query = request.GET.get('search', '').strip()
    books = []  # Initialize the list of books to be displayed
    error_message = None  # Initialize an error message variable

    if search_query:
        # Call Google Books API to search for books based on the query
        search_results = search_books(query=search_query)
        if isinstance(search_results, dict) and 'error' in search_results:
            # Handle errors returned by the search_books function
            error_message = search_results['error']
        else:
            books = search_results
    else:
        # Retrieve all books from the database if no search query is provided
        books = list(Book.objects.all())

    # Randomize the books and limit to 25
    if books:
        books = random.sample(books, min(len(books), 25))

    # Render the book catalog page with the books and search query passed to the template
    return render(request, 'book_catalog.html', {
        'books': books,
        'search_query': search_query,
        'error_message': error_message
    })


def search_books(query, max_results=10):
    """
    Function to search for books using the Google Books API.
    Returns a list of books matching the search query or handles invalid searches gracefully.
    """
    # Validate query
    if not query or query.strip() == "":
        return {"error": "Search query cannot be empty."}

    # If the query appears to be an ISBN, validate its format
    if re.match(r"^\d{10}(\d{3})?$", query):  # Matches 10 or 13-digit ISBN
        # Valid ISBN format
        pass
    elif len(query) < 3:
        # If not an ISBN, titles should be longer than 2 characters
        return {"error": "Search query is too short. Please provide a valid title or ISBN."}

    # Construct API URL
    url = f"{GOOGLE_BOOKS_API_URL}?q={query}&maxResults={max_results}&key={API_KEY}"
    response = requests.get(url)

    # Handle API response
    if response.status_code == 200:
        books = []
        items = response.json().get('items', [])
        if not items:
            return {"error": "No books found for the given query."}

        for item in items:
            book_data = item.get('volumeInfo')
            if book_data:
                # Safely extract data, providing defaults where necessary
                title = book_data.get('title', 'Unknown Title')
                authors = book_data.get('authors', ['Unknown Author'])
                industry_ids = book_data.get('industryIdentifiers', [])
                isbn = industry_ids[0]['identifier'] if industry_ids else "Unknown ISBN"
                genre = book_data.get('categories', ['Unknown Genre'])[0]
                description = book_data.get('description', 'No description available')


                if not isbn:
                    continue

                # Create or retrieve the book in the database
                book, created = Book.objects.get_or_create(
                    isbn=isbn,
                    defaults={
                        'title': title,
                        'author': authors[0],
                        'genre': genre,
                        'description': description,
                    }
                )
                books.append(book)
        return books
    # Handle non-200 API responses
    return {"error": f"Error occurred while accessing the Google Books API (status code: {response.status_code})."}
