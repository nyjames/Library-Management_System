# fetch_books.py
from django import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from catalog.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch books from the Google Books API and store them in the database'

    def handle(self, *args, **options):
        url = f"{settings.GOOGLE_BOOKS_API_URL}?q=subject:fiction&key={settings.API_KEY}&maxResults=40"
        response = requests.get(url)

        if response.status_code == 200:
            books = response.json().get('items', [])

            for book_data in books:
                volume_info = book_data.get('volumeInfo', {})
                title = volume_info.get('title', 'Unknown Title')
                authors = volume_info.get('authors', ['Unknown Author'])
                isbn_list = volume_info.get('industryIdentifiers', [])
                genre = ', '.join(volume_info.get('categories', ['General']))
                published_date = volume_info.get('publishedDate', None)

                # Extract ISBN-13 if available
                isbn = None
                for identifier in isbn_list:
                    if identifier.get('type') == 'ISBN_13':
                        isbn = identifier.get('identifier')
                        break

                if not isbn:
                    continue  # Skip if no ISBN-13 is available

                # Format the published date if available
                if published_date:
                    try:
                        published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
                    except ValueError:
                        published_date = None

                # Check if the book already exists before adding
                book, created = Book.objects.get_or_create(
                    isbn=isbn,
                    defaults={
                        'title': title,
                        'author': ', '.join(authors),
                        'genre': genre,
                        'published_date': published_date,
                        'available': True,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added book: {title}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Book already exists: {title}'))
        else:
            self.stdout.write(self.style.ERROR("Failed to fetch data from Google Books API"))
