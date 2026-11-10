from playwright.sync_api import expect

def test_website_load(page):
    page.goto("http://localhost:8081/")
    expect(page).to_have_url("http://localhost:8081/")
    expect(page.locator("body")).to_be_visible()

    print("Website loaded successfully!")