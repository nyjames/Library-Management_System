
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_selenium_basics():
    driver = webdriver.Chrome()

    driver.get('https://www.wikipedia.org')
    print(driver.title)

    search_box = driver.find_element(By.ID, 'searchInput')
    search_box.send_keys('Selenium (software)')
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)
    print(driver.title)

    assert 'software' in driver.title
    driver.quit()
