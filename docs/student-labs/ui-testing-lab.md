# Student Lab #3: UI Testing (Selenium and Playwright)

## Introduction to Selenium and Playwright
Selenium is a popular framework for web application testing. It enables developers to automate web browser actions, simulating user interactions like clicking buttons, filling out forms, and navigating between pages. Selenium WebDriver provides APIs to interact with browsers programmatically.

Playwright is a more modern framework with similar use cases that has become popular in recent years. Playwright is able to interact with multiple browser types (Firefox, WebKit, and Chromium) through a single API.

In these labs, you'll learn the basics of automating web tasks with Selenium and Playwright, including setting up a WebDriver, navigating web pages, and automating simple browser tasks. You'll also learn the fundamentals of **UI testing**.

## Lab 1: Navigating the Web with Selenium and ChromeDriver
### Preparing IDE
1\. Create a virtual environment in VSCode
```bash
python -m venv venv
```

2\. Install selenium by entering the following command:
```bash
pip install selenium
```
3\. Selenium requires a seperate webdriver. We will be using ChromeDriver. Check your Chrome version (Settings -> About) and download the appropriate [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) version. Unzip and move chromedriver.exe to an easy to remember location such as 'C:\chromedriver'

4\. Add ChromeDriver to your PATH. Right click the Start button (Windows) and click 'System'. Click 'Advanced system settings' and then 'Environment Variables'. Find 'Path' in system variables and click edit. Add 'C:\chromedriver' and click 'OK'.

5\. Type chromedriver in terminal/command prompt to verify installation
```bash
chromedriver
```

### Part 1: Setting up Selenium script
Every Selenium script you create will require certain common elements. Create a script called test_selenium_basics.py

1\. Import Selenium webdriver.
```python
from selenium import webdriver
```

2\. Import By. By allows us to select elements on a page by html attributes such as ID.
```python
from selenium.webdriver.common.by import By
```
3\. Import Keys. Keys allows us to simulate keyboard presses.
```python
from selenium.webdriver.common.keys import Keys
```

4\. Import time. Time allows us to have delays in our code.
```python
import time
```

5\. Select your webdriver. We will be using ChromeDriver.
```python
driver = webdriver.Chrome()
```

Issues with ChromeDriver are likely to arise from using the wrong version or from incorrect PATH configuration.

**This is the basic setup required for almost any Selenium script. Additional setup may be required for more complex scripts.**

### Part 2: Wikipedia Search with Selenium
We will perform a Wikipedia search using our Selenium script. Continue working on test_selenium_basics.py

1\. Open a webpage (Wikipedia) and print its title.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_selenium_basics():
    driver = webdriver.Chrome()

    driver.get('https://www.wikipedia.org')
    print(driver.title)
```
Run your script. A Chrome window should briefly open and Wikipedia should be printed in the console.

2\. Now we want to find the search box element. Go to [Wikipedia.org](https://www.wikipedia.org) and use the inspect tool to find the search box's ID. Use find_element() and By.ID to get the search box.
```python
search_box = driver.find_element(By.ID, 'searchInput')
```

3\. Now search something. Use send_keys() to enter a search term in the box. Then send an ENTER key. Use time.sleep() to ensure the page has time to load, then print the page's title. Assert that 'Selenium' is contained in the title. Quit the driver and exit the script.
```python
search_box.send_keys('Selenium')
search_box.send_keys(Keys.ENTER)

time.sleep(3)
print(driver.title)

assert 'software' in driver.title, 'Page title does not contain "software"'
driver.quit()
```

Run the test with Pytest and you should see that the assertion failed. This is because the search brought up a page for the chemical element Selenium. Update your test to specify you want Selenium (software) and run it again.

```python
search_box.send_keys('Selenium (software)')
search_box.send_keys(Keys.ENTER)

time.sleep(3)
print(driver.title)

assert 'software' in driver.title, 'Page title does not contain "software"'
driver.quit()
```

Your test should now pass. Congrats on learning how to automate and test simple web functions with Selenium.

## Lab 2: Navigating the Web with Playwright
### Preparing IDE
1\. Create and select a virtual environment if you haven't already.

2\. Install Playwright.
```bash
pip install playwright
playwright install
```
3\. Verify installation.
```bash
playwright --version
```

### Part 1: Setting up Playwright script
1\. Create a new script test_playwright_basics.py. Import and then initialize Playwright with a context manager. Launch a chromium, firefox, or webkit browser in visible mode with 'headless=False'.
```python
from playwright.sync_api import sync_playwright

def test_playwright_basics():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
```
### Part 2: Wikipedia Search with Playwright
1\. Continue in test_playwright_basics.py. Open Wikipedia.
```python
from playwright.sync_api import sync_playwright

def test_playwright_basics():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto('https://www.wikipedia.org')
```
2\. Locate the search box element. If you don't know the ID attribute, inspect the page in your browser and find it.
```python
search_box = page.locator('#searchInput')
```

3\. Send 'Playwright' and hit Enter. We can then automatically wait for the page to load before testing if the title contains 'software'.
```python
search_box.fill('Playwright')
search_box.press('Enter')

page.wait_for_load_state('domcontentloaded')

print(page.title())

assert 'software' in page.title(), 'Page title does not contain "software"'
browser.close() 
```
Run with Pytest. The assertion should fail. Clarify your search to specify 'Playwright (software)'.
```python
search_box = page.locator('#searchInput')
search_box.fill('Playwright (software)')
search_box.press('Enter')

page.wait_for_load_state('domcontentloaded')

print(page.title())

assert 'software' in page.title(), 'Page title does not contain "software"'
browser.close() 
```
Your test should now pass. Congrats on learning how to automate and test simple web functions with Playwright.

## Lab 3: UI Testing Library Management System with Selenium and Playwright
### Objective
UI testing is conducted to ensure that the User Interface functions as expected, such as initiating the correct actions and displaying feedback and error messages when necesary. Learn how to use Selenium and Playwright to test the login UI functionality of the Library Management System (LBMS). By the end of this lab, you'll be able to:

- Set up Selenium and Playwright in your project.

- Write automated tests to validate the login page's behavior.

- Use Selenium and Playwright's debugging tools for troubleshooting.

### Lab Setup
You'll need access to the Library Management System to complete this lab. Clone the project repository to your machine and complete setup.
```
git clone https://github.com/csc256/fa24project-fa24project_team_4.git

cd fa24project-fa24project

git checkout -b ui-testing-lab

python -m venv venv

source venv/bin/activate  # For macOS/Linux

venv\Scripts\activate     # For Windows

pip install -r requirements.txt
```
You'll also need Selenium, ChromeDriver, and Playwright installed. Refer to IDE Setup for Labs 1 and 2.

### Part 1: Login Test with Selenium
Create a new script called 'test_selenium_login.py'

Write a test using Selenium that attempts to login with a valid account and verify that user is redirected to home page upon successful login. Try it first on your own and check the following solution if you need help.
<details><summary>Solution</summary>

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_selenium_login():
    # Initialize the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()
    
    # Navigate to the login page
    driver.get("http://localhost:8000/accounts/login")
    
    # Fill in the login form
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("testuser")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("testpassword123")

    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()
    
    # Wait for redirection
    time.sleep(2)
    
    # Check that the user is redirected to the home page
    assert driver.current_url == "http://localhost:8000/home", "URL does not match the expected home page"

    print("Test passed: Successful login redirects to the home page")

    # Close the browser
    driver.quit()
```
</details>

Now start the server: 
```
python manage.py runserver
```
And run the test:
```
pytest test_selenium_login.py
```
Good work creating your first UI Test with Selenium!

### Part 2: Test for Incorrect Credentials with Playwright
Write a test using Playwright that attempts to login with a invalid account and verify that error message is shown. Try it first on your own and check the following solution if you need help.
<details><summary>Solution</summary>

```python
from playwright.sync_api import sync_playwright

def test_invalid_login_shows_error_message():
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
```
</details>
Start the server if necesary and run the test. Good work creating your second UI Test with Playwright!

### Challenge: Test for Empty Input Fields
Can you write a test to verify that validation messages for empty fields are displayed? Try it using either Selenium or Playwright. 

## Conclusion
In this lab you learned how to use Selenium and Playwright for web automation and testing. You’ve learned the fundamentals of navigating, interacting with, and testing web pages through code, as well as key differences between Selenium and Playwright. You also learned how to use Selenium and Playwright in real-world scenarios by creating and performing UI tests for the Libarary Management System.

