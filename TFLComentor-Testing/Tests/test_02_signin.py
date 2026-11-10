from playwright.sync_api import expect

def test_successful_signin(page):
    page.goto("http://localhost:8081/")
    page.get_by_role("link", name="Sign In").click()
    expect(page).to_have_url("http://localhost:8081/models/membership/Login")
    page.locator("#username").fill("7498105029")
    role_dropdown = page.get_by_role("combobox")
    role_dropdown.click()

    page.get_by_role("option",name="Student",exact=True).click()
    page.locator("#password").fill("12345")
    page.get_by_role("button",name="Login",exact=True).click()

    expect(page).to_have_url("http://localhost:8081/models/membership/dashboard",timeout=20000)

    print("Login successful! Dashboard opened.")