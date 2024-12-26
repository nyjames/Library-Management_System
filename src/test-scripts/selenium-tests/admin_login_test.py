"""Selenium test for Admin Login"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup webdriver
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/admin/')

# Find elements
username_text = driver.find_element(By.ID, "id_username")
password_text = driver.find_element(By.ID, "id_password")
login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")

# Fill in text fields
username_text.send_keys("wsv")
password_text.send_keys("CSC256_FA2024")

# Click button
login_btn.click()

# Wait for three seconds to confirm login
time.sleep(3)

# Find logout button
logout_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

# Click logout button
logout_btn.click()

# Wait for three seconds to confirm logout
time.sleep(3)

# Close the browser
driver.quit()
