from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Book
from django.views.generic import TemplateView

# Home page view using TemplateView (no extra context needed)
class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required
def book_detail(request, book_id):
    """
    View to display details of a book and allow users to check it out or return it.
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Handle checkout or return book
        if not book.checked_out_by:
            # Checkout book
            book.checked_out_by = request.user
            book.available = False
        else:
            # Return book if checked out by the current user
            if book.checked_out_by == request.user:
                book.checked_out_by = None
                book.available = True
        book.save()

        # Redirect to updated book details
        return redirect('book_detail', book_id=book.id)

    return render(request, 'book_detail.html', {'book': book})

def book_catalog(request):
    """
    View to display all books in the catalog.
    Optionally, can be expanded to support search/filtering.
    """
    books = Book.objects.all()  # Fetch all books
    return render(request, 'book_catalog.html', {'books': books})
