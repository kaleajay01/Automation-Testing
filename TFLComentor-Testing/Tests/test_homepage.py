from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):

    page.goto("http://localhost:8081/")

    expect(page).to_have_url("http://localhost:8081/")

    print("Homepage test completed successfully")