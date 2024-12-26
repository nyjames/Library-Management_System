import requests

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = "AIzaSyCcl9iI2wh5DSu5HYpK3NO_5O47fdIhnG8"

# Test request to the Google Books API
response = requests.get(f"{GOOGLE_BOOKS_API_URL}?q=subject:fiction&key={API_KEY}&maxResults=5")
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    books = data.get("items", [])
    for i, book in enumerate(books, 1):
        volume_info = book.get("volumeInfo", {})

        # Check all expected fields
        title = volume_info.get("title", "Unknown Title")
        authors = volume_info.get("authors", ["Unknown Author"])
        categories = volume_info.get("categories", ["General"])
        published_date = volume_info.get("publishedDate", "Unknown Date")
        isbn_list = volume_info.get("industryIdentifiers", [])

        # Extract ISBN-13 if available
        isbn = None
        for identifier in isbn_list:
            if identifier.get("type") == "ISBN_13":
                isbn = identifier.get("identifier")
                break

        # Print details to verify
        print(f"Book {i}:")
        print(f"  Title: {title}")
        print(f"  Authors: {', '.join(authors)}")
        print(f"  Genre: {', '.join(categories)}")
        print(f"  Published Date: {published_date}")
        print(f"  ISBN-13: {isbn if isbn else 'Not Available'}")
        print("-----")
else:
    print("Failed to fetch data from Google Books API")
