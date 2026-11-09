
import json
from pathlib import Path

from playwright.sync_api import expect

from pages.login_page import LoginPage
from config.settings import DASHBOARD_URL


# Load login test data
DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "test_data"
    / "login_data.json"
)

with open(DATA_PATH, "r", encoding="utf-8") as file:
    test_data = json.load(file)


# TEST 1: Valid Login
def test_valid_login(page):

    login = LoginPage(page)

    login.open_login_page()

    login.verify_login_page()

    user = test_data["valid_user"]

    login.login(
        user["username"],
        user["password"],
        user["role"]
    )

    # Verify dashboard navigation
    expect(page).to_have_url(
        DASHBOARD_URL,
        timeout=15000
    )

    # Capture screenshot
    login.take_screenshot("login_success.png")

