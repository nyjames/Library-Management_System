from django.conf import settings
import requests

def search_books(query, max_results=40):
    """
    Search for books using the Google Books API.

    Args:
        query (str): The search query (e.g., title, author, ISBN).
        max_results (int): The maximum number of results to retrieve. Defaults to 40.

    Returns:
        list: A list of books matching the search query.
    """
    # Construct the API URL with the provided query and parameters
    url = f"{settings.GOOGLE_BOOKS_API_URL}?q={query}&maxResults={max_results}&key={settings.GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('items', [])
    return []
