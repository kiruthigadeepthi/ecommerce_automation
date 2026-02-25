from pages.login_page import LoginPage
import pytest
from pytest_html import extras
#Loginpage

@pytest.mark.severity_critical
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
   # driver.node.extra.append(extras.text("Step 1: Navigated to login page"))

    assert "inventory.html" in driver.current_url
    #Updated login page
    #bugfix
    