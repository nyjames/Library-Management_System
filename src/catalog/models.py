# catalog/models.py

from django.db import models
from django.conf import settings  
from django.contrib.auth import get_user_model
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)  # Mark book as available by default
    description = models.TextField(null=True, blank=True)
    
    # Track user who checked out the book
    checked_out_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='checked_out_books'
    )

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
        related_name='reviews',
        
        )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review
    
    def get_absolute_url(self):
        return reverse('catalog:book_detail', args=[str(self.book.id)])