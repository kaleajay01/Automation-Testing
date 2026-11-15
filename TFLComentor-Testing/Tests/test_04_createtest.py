from playwright.sync_api import expect

def test_tests_created_navigation(shared_page):
    current_url = shared_page.url
    tests_created_box = (shared_page.get_by_text("Tests Created", exact=True).locator("xpath=ancestor::div[contains(@class, 'cursor-pointer')][1]"))
    expect(tests_created_box).to_be_visible()
    tests_created_box.click()
    print("Tests Created box clicked")
    # shared_page.wait_for_url(lambda url: str(url) != current_url,timeout=10000)
    
def test_test_create_button(shared_page):
    shared_page.get_by_role("button", name="+ Create Test").click()
    expect(shared_page).to_have_url("http://localhost:8081/models/create-test")
    print("Test Create Button Clicked")
    
def test_create_new_test(shared_page):
    expect(shared_page).to_have_url("http://localhost:8081/models/create-test")
    shared_page.get_by_placeholder("Enter test name").fill("Python Automation Test")
    shared_page.locator('select[name="difficultyLevel"]').select_option("INTERMEDIATE")
    shared_page.get_by_placeholder("Enter description").fill("This test is created using Playwright automation.")
    shared_page.get_by_placeholder("Enter duration").fill("30")
    shared_page.get_by_role("button", name="Create New Test").click()
    print("Clicked the Create New Test Button")
    
def test_select_type_level_status(shared_page):
    expect(shared_page).to_have_url("http://localhost:8081/models/question-options")
    
    dropdowns = shared_page.get_by_role("combobox")
    expect(dropdowns).to_have_count(3)
    dropdowns.nth(0).click()
    shared_page.get_by_role("option", name="MCQ").click()
    dropdowns.nth(1).click()
    shared_page.get_by_role("option", name="Beginner").click()
    dropdowns.nth(2).click()
    shared_page.get_by_role("option", name="Approved").click()
    
    expect(shared_page.get_by_role("button", name="Select Questions")).to_be_visible()
    print("All selections completed successfully")
    
    