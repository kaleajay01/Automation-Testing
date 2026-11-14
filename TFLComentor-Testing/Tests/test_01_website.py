from playwright.sync_api import expect

def test_website_load(shared_page):
    shared_page.goto("http://localhost:8081/")

    expect(shared_page.locator("body")).to_be_visible()

    print("Website loaded successfully")