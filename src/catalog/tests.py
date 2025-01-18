import pytest 
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Book, Review


@pytest.fixture
def user():
    User = get_user_model()
    return User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpassword')

@pytest.fixture
def book():
    return Book.objects.create(

        title='Test Book',
        author='Test Author',
        isbn='1234567890',
        genre='Test Genre',
        published_date='2023-01-01',
        available=True,

        )  
@pytest.fixture
def review(user, book):
    return Review.objects.create(
        book=book,
        review='Test Review',
        author=user
    )


# Test that checks whether or not a review has been created
@pytest.mark.django_db
def test_review_creation(review):
    assert review.review == 'Test Review'
    assert review.book.title == 'Test Book'
    assert review.author.username == 'testuser'

    assert "Review successfully created."