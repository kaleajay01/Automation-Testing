
from pathlib import Path
from playwright.sync_api import Page, Locator


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator: Locator, value: str):
        locator.fill(value)

    def get_text(self, locator: Locator):
        return locator.inner_text()

    def is_visible(self, locator: Locator):
        return locator.is_visible()

    def take_screenshot(self, filename: str):

        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        self.page.screenshot(
            path=str(screenshot_dir / filename),
            full_page=True
        )

    def get_current_url(self):
        return self.page.url

    def get_title(self):
        return self.page.title()
