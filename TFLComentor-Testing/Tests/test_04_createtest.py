from playwright.sync_api import expect

def test_tests_created_navigation(shared_page):
    current_url = shared_page.url
    tests_created_box = (shared_page.get_by_text("Tests Created", exact=True).locator("xpath=ancestor::div[contains(@class, 'cursor-pointer')][1]"))
    expect(tests_created_box).to_be_visible()
    tests_created_box.click()
    print("Tests Created box clicked")
    
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
    shared_page.get_by_role("option", name="INTERMEDIATE").click()
    dropdowns.nth(2).click()
    shared_page.get_by_role("option", name="Approved").click()
    
    expect(shared_page.get_by_role("button", name="Select Questions")).to_be_visible()
    print("Question filters selected successfully")    
    
    shared_page.get_by_role("button", name="Select Questions").click()
    print("Select Questions button clicked")
    
    checkboxes = shared_page.locator('input[type="checkbox"]')
    expect(checkboxes.first).to_be_visible(timeout=20000)
    question_count = checkboxes.count()
    for i in range(question_count):
        checkboxes.nth(i).check()
    print(f"{question_count} questions selected successfully")
    create_button = shared_page.get_by_role("button", name="Create Test")
    expect(create_button).to_be_enabled()
    print("Create Test button is enabled")
    shared_page.get_by_role("button", name="Create Test").click()
    print("test created successfully")
    
    dashboard_button = shared_page.get_by_role("button",name="Go To Dashboard")
    expect(dashboard_button).to_be_visible(timeout=20000)
    dashboard_button.click()
    expect(shared_page).to_have_url("http://localhost:8081/models/membership/dashboard",timeout=15000)
    print("Returned to Dashboard successfully")