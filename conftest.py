import pytest,allure
from selenium import webdriver
#import logging
import time



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

