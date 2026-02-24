from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
import time

def test_invalid_update_checkout(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.go_to_cart()
    time.sleep(2)

    # Step 3: Attempt invalid update (checkout with missing data)
    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("", "", "")  # invalid: all fields blank

    # Step 4: Verify error message
    error_message=checkout_page.get_errormessage()
    assert "Error" in error_message or "First Name is required" in error_message