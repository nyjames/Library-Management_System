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
