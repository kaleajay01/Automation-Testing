from playwright.sync_api import expect

def test_successful_logout(shared_page):
    expect(shared_page).to_have_url("http://localhost:8081/models/membership/dashboard")

    print("Dashboard is open")
    shared_page.get_by_role("button",name="Ajay Kale").click()

    print("Profile menu opened")
    logout_button = shared_page.get_by_text("Logout",exact=True)
    expect(logout_button).to_be_visible()
    logout_button.click()
    print("Logout button clicked")
    expect(shared_page).to_have_url("http://localhost:8081/",timeout=15000)

    print("Logout successful!")