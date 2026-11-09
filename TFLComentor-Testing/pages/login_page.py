
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from config.settings import LOGIN_URL

class LoginPage(BasePage):

    def __init__(self, page: Page):

        super().__init__(page)

        # Contact Number
        self.username_input = page.locator("#username")

        # Password
        self.password_input = page.locator("#password")

        # Role dropdown (Shadcn Select)
        self.role_dropdown = page.get_by_role("combobox")

        # Login button
        self.login_button = page.get_by_role(
            "button",
            name="Login",
            exact=True
        )

        # Remember me checkbox
        self.remember_checkbox = page.locator("#remember")

    def open_login_page(self):
        self.navigate("http://localhost:8081/")
        self.page.get_by_role("link", name="Sign In").click()

    def enter_username(self, username):

        self.fill(self.username_input, username)

    def enter_password(self, password):

        self.fill(self.password_input, password)

    def select_role(self, role):
        self.role_dropdown.click()

        role_option = self.page.get_by_role(
            "option",
            name=role,
            exact=True
        )

        role_option.wait_for(state="visible", timeout=15000)
        role_option.click()
        
    def click_login(self):

        self.click(self.login_button)

    def login(self, username, password, role):

        self.enter_username(username)

        self.select_role(role)

        self.enter_password(password)

        self.click_login()

    def verify_login_page(self):

        expect(self.username_input).to_be_visible()

        expect(self.password_input).to_be_visible()

        expect(self.role_dropdown).to_be_visible()

        expect(self.login_button).to_be_visible()
