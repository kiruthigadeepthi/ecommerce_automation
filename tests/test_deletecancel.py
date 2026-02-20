from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage


def test_delete_cancellation(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    items_before = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in items_before

    # Step 3: Trigger delete (confirmation popup appears)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Step 4: Cancel deletion
    alert = Alert(driver)
    alert.dismiss()   # simulate clicking "Cancel"

    # Step 5: Verify item still exists
    items_after = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in items_after