from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_delete_with_confirmation(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.go_to_cart()

    # Step 3: Trigger DELETE (remove item)
    cart_page = CartPage(driver)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Step 4: Handle confirmation popup
    alert = Alert(driver)
    alert.accept()   # click "OK"
    # alert.dismiss() # click "Cancel" if needed

    # Step 5: Verify deletion
    items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" not in items