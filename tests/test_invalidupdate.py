from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_invalid_update_checkout(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.go_to_cart()

    # Step 3: Attempt invalid update (checkout with missing data)
    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("", "", "")  # invalid: all fields blank

    # Step 4: Verify error message
    error_message = driver.find_element_by_css_selector("h3[data-test='error']").text
    assert "Error" in error_message or "First Name is required" in error_message