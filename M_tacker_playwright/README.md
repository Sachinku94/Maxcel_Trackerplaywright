# Maxcel Tracker - Playwright Framework (Complete Conversion)

## 🎯 Overview

This is a **complete Playwright-based** test automation framework converted from Selenium. It includes all 16 test files fully converted with async/await support and modern Playwright best practices.

## 📊 What's Included

✅ **Complete Playwright Framework**  
✅ **All 16 Test Files Converted**  
✅ **Async/Await Support**  
✅ **Allure Reporting**  
✅ **Docker Support**  
✅ **Jenkins CI/CD Ready**  
✅ **Video Recording**  
✅ **Comprehensive Logging**

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/Sachinku94/Maxcel_Trackerplaywright.git
cd Maxcel_Trackerplaywright

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r M_tacker_playwright/requirements.txt
playwright install
```

### Configuration

Create `.env` file:
```
USER_NAME=your_email@company.com
PASSWORD=your_password
```

### Run Tests

```bash
# Run all tests
pytest M_tacker_playwright/tests/ -v

# Run specific test file
pytest M_tacker_playwright/tests/Smoke_tests/test_0auth.py -v

# Run with Allure reporting
pytest M_tacker_playwright/tests/ --alluredir=allure-results -v
allure serve allure-results

# Run in headed mode (see browser)
pytest M_tacker_playwright/tests/ -v --headed

# Run with markers
pytest -m Smoke_tests -v
pytest -m oauth -v
pytest -m users -v
```

## 📁 Project Structure

```
M_tacker_playwright/
├── Config/
│   ├── config.ini
│   └── config_reader.py
├── tests/
│   ├── conftest.py
│   └── Smoke_tests/
│       ├── Pages/
│       │   └── homepage.py
│       ├── object/
│       │   └── playwright_helper.py
│       ├── utilities/
│       │   └── base_class.py
│       ├── test_0auth.py
│       ├── test_AI.py
│       ├── test_alerts.py
│       ├── test_appsandwebsite.py
│       ├── test_cologs.py
│       ├── test_createUser.py
│       ├── test_Department.py
│       ├── test_homepageviewmore.py
│       ├── test_KPIs.py
│       ├── test_logs.py
│       ├── test_Productive.py
│       ├── test_roles.py
│       ├── test_screenshot.py
│       ├── test_screenrecord.py
│       ├── test_settings.py
│       └── test_stream.py
├── requirements.txt
├── pytest.ini
├── Dockerfile
└── Jenkinsfile
```

## 🧪 Test Files (16 Total)

| Test File | Description | Markers |
|-----------|-------------|----------|
| test_0auth.py | OAuth & Authorization | oauth |
| test_AI.py | AI Summary | dashboard |
| test_alerts.py | Alerts Management | dashboard |
| test_appsandwebsite.py | Apps & Websites | dashboard |
| test_cologs.py | Consolidated Logs | dashboard |
| test_createUser.py | User Creation | users |
| test_Department.py | Departments & Teams | dashboard |
| test_homepageviewmore.py | Homepage Widgets | dashboard |
| test_KPIs.py | KPIs & KRAs | dashboard |
| test_logs.py | Logs Management | dashboard |
| test_Productive.py | Productivity Metrics | dashboard |
| test_roles.py | Roles Management | dashboard |
| test_screenshot.py | Screenshots | dashboard |
| test_screenrecord.py | Screen Recording | dashboard |
| test_settings.py | Settings | dashboard |
| test_stream.py | Live Streaming | dashboard |

## 🔄 Key Features

### Playwright Advantages
- ✅ Async/Await support for better performance
- ✅ Cross-browser testing (Chromium, Firefox, WebKit)
- ✅ Better element waiting mechanisms
- ✅ Network interception capabilities
- ✅ Automatic video recording
- ✅ Better debugging tools

### Framework Features
- ✅ Page Object Model (POM)
- ✅ Comprehensive logging
- ✅ Screenshot on failure
- ✅ Allure reporting
- ✅ Docker containerization
- ✅ CI/CD ready (Jenkins)

## 🐳 Docker Usage

```bash
# Build Docker image
docker build -t maxcel_tracker_playwright:latest .

# Run tests in Docker
docker run --rm maxcel_tracker_playwright:latest
```

## 📊 Allure Reports

```bash
# Generate Allure report
pytest M_tacker_playwright/tests/ --alluredir=allure-results -v

# Serve Allure report
allure serve allure-results
```

## 🔗 Useful Commands

```bash
# Debug mode
pytest M_tacker_playwright/tests/ --debug

# Slow motion (for debugging)
pytest M_tacker_playwright/tests/ --slowmo 1000

# Screenshot on failure
pytest M_tacker_playwright/tests/ --screenshot only-on-failure

# Verbose output
pytest M_tacker_playwright/tests/ -vv

# Show print statements
pytest M_tacker_playwright/tests/ -s
```

## 📝 Writing New Tests

```python
import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
class TestNewFeature(BaseClass):
    
    @pytest.mark.asyncio
    async def test_something(self):
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Starting test")
        
        page_url = await home_page.get_user_page()
        await self.page.goto(page_url)
        await self.page.wait_for_load_state('networkidle')
        
        # Your test logic
        current_url = self.page.url
        assert "users" in current_url
        
        log.info("✓ Test passed")
```

## 🛠️ Troubleshooting

### Browser installation issues
```bash
playwright install --with-deps
```

### Element not found
```python
await page.wait_for_timeout(5000)  # Wait before interaction
```

### Timeout errors
```python
page.set_default_timeout(30000)  # 30 seconds
```

## 📈 Performance Tips

1. Use `networkidle` waits wisely
2. Leverage parallel execution
3. Use headed mode only for debugging
4. Implement proper waits
5. Clean up resources properly

## 🔗 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Reports](https://docs.qameta.io/allure/)

## 📞 Support

For issues:
1. Check `logfile.log`
2. Review Allure reports in `allure-results/`
3. Enable debug mode: `pytest --debug`
4. Check Playwright docs

---

**Status**: ✅ Complete & Ready to Use  
**Framework**: Playwright 1.48.2  
**Python**: 3.8+  
**Last Updated**: 2026-04-27