from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.severity_major
def test_checkout_flow(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    assert "Sauce Labs Bolt T-Shirt" in driver.page_source
    inventory_page.go_to_cart()
    
    time.sleep(3)

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("Kiru", "Ajith", "12345")
    driver.find_element(By.ID, "finish").click()

    confirmation = checkout_page.get_confirmation()
    assert "Thank you for your order!" in confirmation

def test_e2e_purchase(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    try:
        assert "inventory.html" in driver.current_url
    except AssertionError:
        driver.save_screenshot("screenshots/login_failure.png")
        raise

