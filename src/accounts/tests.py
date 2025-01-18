"""
" pytest and pytest-django are required packages to run these tests
"""
import pytest
from .models import CustomUser
from django.urls import reverse

"""
" Test User Signup
"""


@pytest.mark.django_db
def test_signup(client):
    # Test with valid data
    response = client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'age': '30',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    })

    # Check if the response redirects to login or home page
    assert response.status_code == 302
    assert CustomUser.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_signup_duplicate_username(client):
    # Test with duplicate data
    client.post(reverse('signup'), {
        'username': 'duplicateusername',
        'email': 'duplicateuser@example.com',
        'age': '30',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    })

    response = client.post(reverse('signup'), {
        'username': 'duplicateusername',
        'email': 'duplicateuser@example.com',
        'age': '30',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    })

    # Check if the form shows errors due to duplicate username
    assert response.status_code == 200
    assert CustomUser.objects.filter(username='duplicateusername').exists()
    assert b'A user with that username already exists.' in response.content


@pytest.mark.django_db
def test_signup_invalid_email(client):
    # Test with duplicate data
    response = client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'testuserexample.com',
        'age': '30',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    })

    # Check if the form shows errors due to duplicate username
    assert response.status_code == 200
    assert b'Enter a valid email address.' in response.content


@pytest.mark.django_db
def test_signup_weak_password(client):
    # Test with weak password
    response = client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'age': '30',
        'password1': '123',
        'password2': '123'
    })

    # Check if the form shows errors due to weak password
    assert response.status_code == 200
    assert b'This password is too short.' in response.content


@pytest.mark.django_db
def test_signup_password_mismatch(client):
    # Test with mismatching passwords
    response = client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'age': '30',
        'password1': 'testpassword123',
        'password2': 'password123'
    })

    # Check if the form shows errors due to password mismatch
    assert response.status_code == 200
    assert b'The two password fields didn\xe2\x80\x99t match.' in response.content


"""
" Test User Login
"""


@pytest.fixture
def create_user(db):
    # Create testuser for all login tests
    return CustomUser.objects.create_user(username='testuser', password='testpassword123')


@pytest.mark.django_db
def test_login(client, create_user):

    # Login with valid data
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'testpassword123'
    })

    # Print the response content
    print(response.content)

    # Check if the response redirects to the home page after login
    assert response.status_code == 302
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_login_invalid_username(client, create_user):
    # Login in with invalid username
    response = client.post(reverse('login'), {
        'username': 'testuser1',
        'password': 'testpassword123'
    })

    # Check if the form shows an error for invalid username
    assert response.status_code == 200
    assert b'Please enter a correct username and password.' in response.content


@pytest.mark.django_db
def test_login_invalid_password(client, create_user):
    # Login in with invalid password
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'testpassword'
    })

    # Check if the form shows an error for invalid password
    assert response.status_code == 200
    assert b'Please enter a correct username and password.' in response.content


@pytest.mark.django_db
def test_login_empty(client, create_user):
    # Login in with empty fields
    response = client.post(reverse('login'), {
        'username': '',
        'password': ''
    })

    # Check if the form shows an error for empty fields
    assert response.status_code == 200
    assert b'This field is required.' in response.content
