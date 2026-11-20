# TFL Comentor – Automation Testing Project

## Project Overview

This repository contains an automation testing framework for the **TFL Comentor Web Application**, developed using **Python, Playwright, and Pytest**.

The purpose of this project is to automate functional testing of the TFL Comentor application, validate important user workflows, identify application defects, and ensure that the application behaves as expected.

The automation framework uses Playwright to interact with web elements, perform user actions, validate page navigation, and verify application functionality using automated test cases.

## About TFL Comentor

**TFL Comentor** is a web-based application designed to support assessment and learning-related activities.

The application provides functionality for managing users, creating assessments, selecting questions, and assigning assessments to students.

The main application modules covered by this automation project include:

- **User Registration:** Register new users in the application.
- **User Login:** Authenticate users using their mobile number, role, and password.
- **Dashboard:** Access application features after successful login.
- **Assessment Creation:** Create tests by providing test details such as name, difficulty level, description, and duration.
- **Question Options:** Filter questions based on question type, skill level, and status.
- **Question Selection:** Select questions to include in a test.
- **Test Creation:** Submit the selected questions and create an assessment.
- **Assign Assessment:** Select a test, choose students, set the assessment status, date, and time, and assign the assessment.
- **Logout:** End the current user session.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Automation programming language |
| Playwright | Browser automation |
| Pytest | Test execution and test management |
| pytest-playwright | Playwright integration with Pytest |
| Chromium | Browser used for automation |
| Visual Studio Code | Development environment |
| Git & GitHub | Version control and repository management |

## Project Structure

```text
TFLComentor-Testing/
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── Tests/
│   ├── conftest.py
│   ├── test_01_register.py
│   ├── test_02_login.py
│   ├── test_03_dashboard.py
│   ├── test_04_create_test.py
│   ├── test_05_question_options.py
│   ├── test_06_select_questions.py
│   ├── test_07_create_assessment.py
│   ├── test_08_assign_assessment.py
│   └── test_09_logout.py
│
├── test_data/
│   └── login_data.json
│
├── screenshots/
│
├── pytest.ini
├── requirements.txt
├── run_tests.py
└── README.md
```

*Note: The test filenames above represent the suggested organization. Update them to match the actual files in your repository.*

## Application Details

**Application Name:** TFL Comentor

**Frontend URL:**
```text
http://localhost:8081/
```

**Backend APIs:**

```text
Node.js Backend:
http://localhost:3000/api

Java Backend:
http://localhost:8080/api

.NET Backend:
http://localhost:5201/api
```

**Important Application Pages:**

| Module | URL |
|---|---|
| Login | `/models/membership/Login` |
| Register | `/models/membership/Register` |
| Dashboard | `/models/membership/dashboard` |
| Question Options | `/models/question-options` |
| Assign Assessment | `/models/assign-assessment` |

## Automation Test Coverage

The following application workflows are covered by the automation framework:

### 1. Registration Testing
- Verify the registration page.
- Enter first name and last name.
- Enter email address and contact number.
- Submit the registration form.
- Verify the registration result.

### 2. Login Testing
- Verify the login page.
- Enter mobile number.
- Select user role.
- Enter password.
- Click the Login button.
- Verify successful login.
- Verify navigation to the dashboard.

### 3. Dashboard Testing
- Verify dashboard visibility after login.
- Validate the availability of application modules.
- Navigate to different application features.

### 4. Assessment Creation
- Enter test name.
- Select difficulty level.
- Enter test description.
- Enter test duration.
- Submit the test creation form.

### 5. Question Options Testing
- Select question type.
- Select skill level.
- Select question status.
- Verify selected filter values.
- Display matching questions.

### 6. Question Selection
- Display available questions.
- Select required questions using checkboxes.
- Verify question selection.
- Submit the selected questions.

### 7. Test Creation
- Submit the assessment with selected questions.
- Handle application alerts.
- Verify successful test creation.
- Navigate back to the dashboard.

### 8. Assign Assessment Testing
- Open the Assign Assessment page.
- Select an available test.
- Search and select a student.
- Select assessment status.
- Set assessment date.
- Set assessment time.
- Submit the assignment form.

### 9. Logout Testing
- Open the user profile menu.
- Click the Logout option.
- Verify successful logout.

## Installation and Setup

### Prerequisites

Make sure the following tools are installed:

- Python 3.x
- Visual Studio Code
- Git
- Node.js (for running the application, if required)
- TFL Comentor application running locally

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Open the Project

```bash
cd TFLComentor-Testing
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Install Playwright Chromium Browser

```bash
playwright install chromium
```

## Running Automation Tests

### Run a Specific Test File

```bash
python -m pytest Tests/test_login.py --headed -v -s
```

### Run All Tests

```bash
python -m pytest Tests/ --headed -v -s
```

### Run Tests with Slow Motion

```bash
python -m pytest Tests/ --headed -v -s --slowmo=1000
```

### Run the Complete Test Workflow

If `run_tests.py` is configured to execute the test suite:

```bash
python run_tests.py
```

**Command Options:**

| Option | Description |
|---|---|
| `-v` | Displays detailed test execution results |
| `-s` | Displays print statements in the terminal |
| `--headed` | Runs tests with the browser visible |
| `--slowmo=1000` | Adds a 1-second delay between browser actions |

## Test Execution Workflow

The main automation workflow follows the application user journey:

```text
Start
  |
  v
Open TFL Comentor
  |
  v
User Registration
  |
  v
User Login
  |
  v
Dashboard
  |
  v
Create Assessment
  |
  v
Question Options
  |
  v
Select Questions
  |
  v
Create Test
  |
  v
Return to Dashboard
  |
  v
Assign Assessment
  |
  v
Logout
  |
  v
End
```

## Test Reports and Screenshots

The `screenshots/` directory is used to store screenshots captured during automation testing.

Screenshots can help with:

- Debugging failed test cases.
- Identifying UI issues.
- Verifying application behavior.
- Maintaining test execution evidence.

Pytest displays the test execution results in the terminal, including passed and failed test cases.

## Important Notes

- Ensure that the TFL Comentor frontend and required backend services are running before executing tests.
- Verify that the application is accessible at `http://localhost:8081/`.
- Use valid test credentials when executing login tests.
- Ensure that suitable test questions are available before running question selection tests.
- Use unique email addresses and contact numbers when testing registration.
- Some tests depend on the successful execution of earlier workflow steps.
- Run the complete workflow in the intended order when using a shared browser session.

## Future Enhancements

The automation framework can be extended with:

- HTML test reports using `pytest-html`.
- Automated screenshot capture on test failures.
- Page Object Model (POM) implementation.
- Data-driven testing using JSON or Excel files.
- Cross-browser testing with Chromium, Firefox, and WebKit.
- CI/CD integration using GitHub Actions.
- Improved test logging and reporting.
- API testing and UI testing integration.

## Author

**TFL Comentor Automation Testing Project**

**Framework:** Python + Playwright + Pytest

**Application:** TFL Comentor
