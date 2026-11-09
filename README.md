# Automation Testing Project

## Project Overview
This project automates testing of the TFL Comentor web application using **Playwright with Python** and **Pytest**.

## Technologies Used
- Python
- Playwright
- Pytest
- Visual Studio Code
- Chromium Browser

## Project Structure
```text
TFLComentor-Testing/
├── config/
│   └── settings.py
├── pages/
│   ├── base_page.py
│   └── login_page.py
├── Tests/
│   └── test_login.py
├── test_data/
│   └── login_data.json
├── screenshots/
├── pytest.ini
└── requirements.txt
```

## Test Coverage
- Login page verification
- Mobile number entry
- Role selection
- Password entry
- Login button functionality
- Successful login and dashboard navigation

## Installation
```bash
pip install -r requirements.txt
playwright install chromium
```

## Run Tests
```bash
python -m pytest Tests/test_login.py --headed -v -s
```

## Application URL
```text
http://localhost:8081/
```

## Login Page
```text
http://localhost:8081/models/membership/Login
```

## Test Reports
Screenshots are saved in the `screenshots/` folder.

## Author
TFL Comentor Automation Testing Project
