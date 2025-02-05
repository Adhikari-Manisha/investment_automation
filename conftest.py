import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pytest_html import extras

driver = None  # Global driver instance


# Hook to capture test report information
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # Add URL to report
        extras.append(pytest_html.extras.url("https://ims.mangosoftsolution.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace(" ", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = f'<div><img src="{file_name}" /></div>'
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


# Function to capture screenshots on failure
def _capture_screenshot(name):
    global driver
    if driver:
        driver.get_screenshot_as_file(name)


# Set custom report title
def pytest_html_report_title(report):
    report.title = "Automation Report"


# Browser fixture to initialize and provide a WebDriver instance
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    yield driver
    driver.quit()



def driverChrome():
    global driver
    return driver
