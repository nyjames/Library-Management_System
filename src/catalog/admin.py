from django.contrib import admin
from .models import Book, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review

class bookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    
    list_display = ('title', 'author', 'genre', 'available', 'published_date', 'isbn')

admin.site.register(Book, bookAdmin)