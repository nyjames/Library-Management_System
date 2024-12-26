from playwright.sync_api import sync_playwright

def test_playwright_invalid_login():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)  # Set headless=False to see the browser during the test
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the login page
        page.goto("http://localhost:8000/login")

        # Fill in invalid credentials
        page.fill('input[name="username"]', 'invaliduser')
        page.fill('input[name="password"]', 'wrongpassword')

        # Submit the form
        page.click('input[type="submit"]')

        # Check for error message
        error_message = page.text_content('form')
        assert 'Please enter a correct username and password.' in error_message, "Error message not found or incorrect"

        print("Test passed: Invalid login shows error message")

        # Close the browser
        browser.close()