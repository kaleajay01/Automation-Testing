
from playwright.sync_api import expect


def test_successful_registration(page):

    # 1. Open Register page
    page.goto("http://localhost:8081/models/membership/Register")

    # 2. Verify Register page is loaded
    expect(page.get_by_text("Register", exact=True).first).to_be_visible()

    # 3. Enter First Name
    page.locator("#firstName").fill("Ajay")

    # 4. Enter Last Name
    page.locator("#lastName").fill("Test")

    # 5. Enter Email
    page.locator("#email").fill("ajay.test2026@example.com")

    # 6. Enter Contact Number
    page.locator("#contact").fill("9876543210")

    # 7. Click Register button
    page.get_by_role(
        "button",
        name="Register",
        exact=True
    ).click()

    # 8. Verify successful registration message
    expect(
        page.get_by_text("Registration successful")
    ).to_be_visible(timeout=15000)

    # 9. Verify redirect to Login page
    expect(page).to_have_url(
        "http://localhost:8081/models/membership/Login",
        timeout=20000
    )

    print("Registration completed successfully!")
