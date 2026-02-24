from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By


def test_negative_checkout_missing_fields(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("", "", "")  # invalid input

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "First Name is required" in error_message
    assert "Sauce Labs Backpack" in driver.page_source