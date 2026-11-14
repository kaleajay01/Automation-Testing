from playwright.sync_api import expect

def test_successful_signin(shared_page):
    shared_page.get_by_role("link", name="Sign In").click()
    expect(shared_page).to_have_url("http://localhost:8081/models/membership/Login")
    shared_page.locator("#username").fill("7498105029")
    role_dropdown = shared_page.get_by_role("combobox")
    role_dropdown.click()

    shared_page.get_by_role("option",name="Student",exact=True).click()
    shared_page.locator("#password").fill("12345")
    shared_page.get_by_role("button",name="Login",exact=True).click()
    expect(shared_page).to_have_url("http://localhost:8081/models/membership/dashboard",timeout=20000)
    print("Login successful! Dashboard opened.")