
from playwright.sync_api import sync_playwright

def test_playwright_basics():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto('https://www.wikipedia.org')
        print(page.title())

        search_box = page.locator('#searchInput')
        search_box.fill('Playwright (software)')
        search_box.press('Enter')

        page.wait_for_load_state('domcontentloaded')

        print(page.title())
        
        assert 'software' in page.title()
        browser.close() 
