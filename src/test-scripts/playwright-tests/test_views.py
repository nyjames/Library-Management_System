from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        assert page.title() == "Library Management System"
        browser.close()

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/accounts/login/")
        page.wait_for_selector('text=Login')
        page.fill('[name=username]', 'wsv')
        page.fill('[name=password]', 'CSC256_FA2024')
        page.click("input[type='submit']")
        page.wait_for_load_state("networkidle")
        assert page.url == "http://127.0.0.1:8000/"
        assert page.locator("text=Welcome, wsv").is_visible()
        page.close()


def test_admin_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/admin/")
        page.wait_for_selector('text=Django administration')
        page.fill('[name=username]', 'wsv')
        page.fill('[name=password]', 'CSC256_FA2024')
        page.click('text=Log in')
        page.wait_for_load_state("networkidle")
        assert page.locator("text=WELCOME").is_visible()
        page.close()