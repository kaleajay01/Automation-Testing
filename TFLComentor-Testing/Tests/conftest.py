import pytest
@pytest.fixture(scope="session")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def shared_page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()