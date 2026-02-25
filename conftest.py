import pytest,allure
from selenium import webdriver
#import logging
import time
from pytest_html import extras



@pytest.fixture(autouse=True)
def attach_environment():
    allure.attach("Browser: Chrome\nOS: Windows", name="Environment Info")
@pytest.fixture
def driver():
    #options = webdriver.Chrome()
    #options.add_argument("--headless")  # run without opening browser
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only act on test call failures
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            # Attach screenshot to HTML report
            if hasattr(report, "extra"):
                report.extra.append(extras.image(screenshot_path))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Add severity marker info
    severity = None
    for marker in item.iter_markers():
        if marker.name.startswith("severity_"):
            severity = marker.name.replace("severity_", "").capitalize()

    if severity:
        if hasattr(report, "extra"):
            report.extra.append(extras.text(f"Severity: {severity}"))
"""
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
   
    yield driver
    driver.quit()
    """
#logging.basicConfig(
    #level=logging.INFO,
    #format="%(asctime)s [%(levelname)s] %(message)s",
    #handlers=[
        #logging.FileHandler("logs/e2e_test.log"),
        #logging.StreamHandler()
    #]
#)

#logger = logging.getLogger(__name__)

